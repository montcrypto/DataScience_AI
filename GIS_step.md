[TOC]

## ６　地理情報データを扱う

<br>

GISについて少し触れてみようと思います。以下国土交通省国土地理院のHPからの引用です。

>　地理情報システム（**GIS：Geographic Information System**）は、地理的位置を手がかりに、**位置に関する情報を持ったデータ（空間データ）**を総合的に管理・加工し、視覚的に表示し、高度な分析や迅速な判断を可能にする技術である。
>　平成7年1月の阪神・淡路大震災の反省等をきっかけに、政府において、GISに関する本格的な取組が始まった。その中核となる取組が、国土空間データ基盤の整備である。
>　ハードウェア、ソフトウェアの低価格化が進み、簡易なGIS導入が可能になる一方で、地図データ等については、電子化されていない、データ仕様が異なり利用できない等の問題があり、GISを導入する主体が、各々整備する必要があり、社会的には二重、三重の投資となる等の問題があった。
>　このため、GISを高度に活用できる社会の実現のためには、地図情報の電子化のみならず、それを活用していく技術、制度、人材等が必要であり、これらの総体を社会的な基盤としてとらえ、その総合的、体系的な整備を図っていく必要性が認識され始めた。
>　このような背景のもと、平成19年５月には、地理空間情報の活用の推進に関する施策を総合的かつ計画的に推進することを目的として、**地理空間情報活用推進基本法**が、国会で制定された。

<br>

この章では、GISデータやそれに付随する統計量の扱い方について初歩的なところを学習します。

<br>

### ６ー１　データの取得

<br>

> GeoPandas is an open source project to make working with geospatial data in python easier. GeoPandas extends the datatypes used by [pandas](http://pandas.pydata.org/) to allow spatial operations on geometric types. Geometric operations are performed by [shapely](https://shapely.readthedocs.io/). Geopandas further depends on [fiona](https://fiona.readthedocs.io/) for file access and [matplotlib](http://matplotlib.org/) for plotting.

<br>

日本地図に関してはGitHubにData of JapanというTeamが取りまとめた使いやすいJSONファイルがあるのでそれをダウンロードします。このデータは**geopanda**（https://geopandas.org/)（GIS用データをpandas形式に拡張したり、matplotlibで可視化できる）で処理します。

<br>

#### ６ー１ー１　文化庁の指定文化財

<br>

文化庁は国指定文化財等データベース（https://kunishitei.bunka.go.jp/bsys/index）を公開しています。「国宝・重要文化財（建造物）」を開いて「都道府県別にみる」から「京都府」を選択すると305件の物件がでてきます。それらをcsv出力してデータとします（Kyoto_Architecture.csv）。まず、csvファイルをpandasのDataFrameとして読み込みますが、名称、国宝か重要文化財か、時代、緯度、経度の５項目のみを読み込みます。最後に各建造物の緯度と経度のデータをつかって横軸緯度、縦軸経度のグラフ上に散布図をつくります。

<br>

```python
import os
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd

df_temple = pd.read_csv('../../GitHubData/DataScience_AI/data/GIS/Kyoto_Architecture.csv',usecols = [2, 5, 8, 16, 17],\
                        dtype  = {'名称': str, '種別1': str, '時代': str, '緯度': float, '経度': float})
df_temple = df_temple.rename(columns = {'名称': 'article', '種別1': 'category',\
                                        '時代': 'period', '緯度': 'latitude','経度': 'longitude'})

df_temple.plot(figsize=(6,6),y='latitude',x='longitude', kind='scatter', grid=True, legend=True)
plt.axis('square')
plt.show()
```

<br>

#### ６－1ー２　地図上に所在地表示

<br>

日本地図府県境界データを使って、京都府を描画し、その上に重ねて文化財の所在地を表示します。その際に国宝指定を赤、重要文化財指定を灰色とします。府県境界データはGitHub上に、Data of Japanさん (https://github.com/dataofjapan/land) が公開しているjapan.geojsonというファイルをGeoPandaに読み込んで作成します。京都には305件の指定文化財がありますが、多くは京都市に集中していますので、京都府全体の図と京都市近傍に拡大した２つの図を作成します。

```python
import geopandas as gpd
df_jap = gpd.read_file('../../GitHubData/DataScience_AI/data/GIS/japan.geojson')


colors=[]
for cat in df_temple.category:
    if cat == '国宝':
        colors.append('red')
    else:
        colors.append('gray')
            
fig, ax = plt.subplots(nrows=1,ncols=2,figsize = (16,16)) 
for i in range(2):
    if i == 1:
        ax[i].set_xlim([135.6,135.9]);ax[i].set_ylim([34.8,35.1])
    df_jap[df_jap['nam_ja'] == '京都府'].plot(ax=ax[i],figsize=(8,8), \
                           edgecolor='#444', facecolor='white', linewidth = 0.5)
    ax[i].scatter(df_temple.longitude,df_temple.latitude,color=colors)
plt.show()
```

<br>

この図に交通網を重ね合わせて、プロットを観光客動員数で表し、月毎に分析すれば、人の流れを予測しながら交通の運行計画もできそうですね。

<br>



#### ６ー３　都道府県の地図を描く

- 「e-stat 統計で見る日本」より、国税調査、小区分、境界データを47都道府県分ダウンロードして、その内Shapeファイルをgeopandaで読み込んで作図する。

```python
%matplotlib inline
import matplotlib.pyplot as plt
import geopandas as gpd

pref_name='宮崎県'
pref_id=df_jap.id[df_jap['nam_ja']=='宮崎県'].values
map_id=pref_id[0]-1

fig, ax = plt.subplots(figsize = (16,16)) 
gdf = gpd.read_file(prefecture_shp[map_id])      #gdf file に変換した。
gdf.plot(ax=ax, facecolor='white', edgecolor='black', linewidth=0.2)
ax.set_axis_off()
plt.show()
```

#### ６ー４　階級区分図（かいきゅうくぶんず、choropleth map）を人口密度と家族構成で作成する

```python
gdf['DENSITY']= gdf['JINKO']/gdf['AREA']*10**6 # 1平方キロメートルあたりの人口
#print(gdf.head())

fig, ax = plt.subplots(figsize = (24,16))
gdf.plot(column = 'DENSITY', edgecolor = "black",scheme='quantiles', linewidth=0.2, cmap='YlOrRd', ax=ax, legend = True)
ax.set_axis_off()
plt.show()

gdf['FAMILY']= gdf['JINKO']/gdf['SETAI']# 1世帯あたりの人数
#print(gdf.info())
#print(gdf.head())
 
fig, ax = plt.subplots(figsize = (24,16))
gdf.plot(column = 'FAMILY', edgecolor = "black",scheme='quantiles', linewidth=0.2, cmap='YlOrRd', ax=ax, legend = True)
ax.set_axis_off()
plt.show()
```

