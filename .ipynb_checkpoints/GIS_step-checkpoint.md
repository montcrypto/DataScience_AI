[TOC]

## ６　地理情報データを扱う



### ６ー１　データの取得とpythonへの読み込み

#### ６ー１　文化庁のホームページから指定文化財のデータベースをダウンロードしてグラフ上に表示する。

- 例として京都府の建造物指定文化財：Kyoto_Architecture.csv：
- 日本地図はhttps://github.com/dataofjapan/land からJSONファイルを取得。



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

#### ６－２　地図上に文化財所在地をプロットする

- 日本地図府県境界データをgeopandasに読み込み、京都府のみを描画する。
- そこに、文化財のデータを重ねて表示する。その際に国宝指定を赤、重要文化財指定を灰色とする。

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
    df_jap[df_jap['nam_ja'] == '京都府'].plot(ax=ax[i],figsize=(8,8), edgecolor='#444', facecolor='white', linewidth = 0.5)
    ax[i].scatter(df_temple.longitude,df_temple.latitude,color=colors)
plt.show()
```

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

