## ７　スペクトルの多変量解析

ここでは、スペクトルデータを使って、多変量解析について学習することを目的とします。

<br>

> No matter who pens them, nor in which language they are penned, mere words fail to convey the sadness that befell us on July 17th, 2019, when **Karl Norris** passed away. He became a legend in his own lifetime, long before its end, a legend that will never be surpassed, and created a new world of rapid, chemical-free analysis, the World of Near-infrared Spectroscopy (NIRS). More than 50 years ago his genius recognized that what he had found in the spectra of soybeans could be metamorphosed into a technique that would revolutionize grain analysis. In the decades immediately following, his vision became reality, and the technique has since then expanded far beyond grain analysis into fields too numerous to document. https://icnirs.org/news/a-tribute-to-a-legend/

<br>

### ７−１　スペクトルデータとは

「非破壊検査」、「品質」でネット検索すると青果物の分析についての論文や装置がヒットします。光を用いる分光法、X線などの放射線を用いる方法、または電磁気的な性質を利用する方法などあるなかで、**近赤外分光法**は 1970 年代から農産物の分析に用いられています。なぜ近赤外を使うのでしょう。

私たちが水中の物体をみることができるのは可視光が水を透過するからです。それでも光が達する深さには限界があり、そこからの散乱光を見ることもできません。このことは経験的に皆知るところであり、青が赤よりも透過率が良いために海が青く見えるのも同じ物理現象です。つまり、可視光は水を透過するが、その程度は波長により異なること、赤すなわち波長の長い光はより吸収されるということです。さらに長い赤外線波長を使うとどうでしょう？　赤外線吸収スペクトル法では分子内の官能基の構造を調べることができますが、測定には水を極力排除します。それはOHやNHなどの重要な官能基の吸収付近に覆い被さる吸収を生じることと、ハード的にも光学素子を痛めやすいためです。

近赤外法はちょうど間の波長帯を利用するで、その見えない光は含水物内を透過し、官能基の情報も与えるという両方の性質を持つと理解できます。具体的には、近赤外分析で用いられる波長は果実の皮を透過して果肉のサンプリングを可能にします。一般には、まず目的の成分が既知のサンプルからスペクトルデータを収集し、次にスペクトルから逆に成分量を予測する校正モデルを作成します。このモデルに未知のサンプルから得た近赤外スペクトルを代入して目的成分の予測値を得ます。操作は簡単で測定も迅速で非破壊的であることが近赤外の魅力といえます。

果実のスペクトルは残念ながら持ち合わせていないので、木材の表面から集めたスペクトルで話を進めましょう。４種類の熱帯産材、市場ではメランチと呼ばれる4種のスペクトルです。

<br>

<img src="./img/nir.png" style="zoom:67%;" />

<br>

スペクトルデータは概ね緩やかな曲線で、とてもよく似ているといことに注目してください。ただし、同じ大きさの領域からサンプリングしても有機物の絶対量に応じて吸光の度合が変わるたバックグラウンドは変化します。その影響を除くため２次微分します。下の図は波数8000cm<sup>-1</sup>から4000cm<sup>-1</sup>の領域を取り出して重ね書きしたものですが、絶対値の大きさに影響されずに変化量としたため、異なる資料を比較できるようになりました。このような処理を**正規化**（normalization）といいます。一般的な正規化については後で説明します。

<br>

![](./img/2nd_dev.png)



データが揃うとますますスペクトルは似てきます。しかし若干の差があります。1960年代にKarl Norrisが行なった大豆の研究から始まり、極めて微妙なスペクトルの変化を捉えてサンプルの特徴を取り出す多変量解析手法、今でいうケモメトリクスという方法はあらゆる分野で発展し、自動化された品質評価の技術として社会実装されています。



### ７ー２　次元の圧縮

さて、スペクトルのデータは、波数8000cm<sup>-1</sup>から4000cm<sup>-1</sup>まで2cm<sup>-1</sup>間隔とすると2000個あります。これらを一つ一つサンプルごとに比べて、クラス分けする手もありますが、ここでは、サンプルを代表するような特徴量を取り出すことを考えます。

話は変わりますが、健康診断でよく耳にするBMI (Body Mass Index) という指標は、体重（kg）を身長<sup>2</sup>（m<sup>2</sup>）で除したものです。重さは体積に比例するので、BMIはもう一辺の長さに相当しますから、「あなたの体積にふさわしい重さを超えています」という基準として提案でき、男性ではその値25だと言うわけです。言い換えれば、体重と身長をいう二つのデータ（２次元のデータ）をBMIという一つの指標（１次元）にまとめたものです。このように多次元データの特徴をうまく引き出す幾つかの変数にまとめることを、**次元の圧縮**（Dimensionality Reduction）といいます。



### ７ー３　主成分分析

一つにまとめた



References:

1) A. Savitzky, M. J. E. Golay, Smoothing and Differentiation of Data by Simplified Least Squares Procedures. Analytical Chemistry, 1964, 36 (8), pp 1627-1639.
2) Numerical Recipes 3rd Edition: The Art of Scientific Computing W.H. Press, S.A. Teukolsky, W.T. Vetterling, B.P. Flannery Cambridge University Press ISBN-13: 9780521880688
