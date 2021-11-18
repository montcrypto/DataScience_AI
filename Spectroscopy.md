## ７　スペクトル情報の多変量解析

<br>

> No matter who pens them, nor in which language they are penned, mere words fail to convey the sadness that befell us on July 17th, 2019, when Karl Norris passed away. He became a legend in his own lifetime, long before its end, a legend that will never be surpassed, and created a new world of rapid, chemical-free analysis, the World of Near-infrared Spectroscopy (NIRS). More than 50 years ago his genius recognized that what he had found in the spectra of soybeans could be metamorphosed into a technique that would revolutionize grain analysis. In the decades immediately following, his vision became reality, and the technique has since then expanded far beyond grain analysis into fields too numerous to document. https://icnirs.org/news/a-tribute-to-a-legend/

<br>

非破壊検査、品質で検索すると青果物の分析に関する論文や装置ができます。光を用いる分光法、X線などの放射線を用いる方法、あるいは電磁気的な性質を利用する方法などさまざまあるなかで、近赤外分光分析は 1970 年代から農産物の分析に用いられています。なぜ近赤外なのか。私たちが水の中のものをみることができるのは可視光が水を透過できるからですが、それでも深いところまでは光が達せず、そこからの散乱光を見ることもできません。このことは経験的にみなさんが知っていることで、青が赤よりも透過率が良いために 海が青く見えるのも同じ物理現象です。つまり、可視光は水を透過できるが、その程度は波長によって異なること、赤すなわち波長の長い光はより吸収されるということです。さらに長い赤外線波長を使う赤外線吸収スペクトル法では、分子内の官能基の構造を調べることができますが、測定には水を極力排除します。それはOHやNHなどの重要な吸収付近にかぶさるように大きな吸収を生じることと、ハード的にも光学素子を痛めやすいためです。近赤外法はちょうどその間なので、含水物内を透過し、その官能基の情報を与えるという両方の性質を持つと理解できます。例えば、皮付き果実でも、近赤外分析で用いられる波長はあまり吸収されず、皮を透過して果肉のサンプリングができるといいます。一般に、目的の成分が既知のサンプルから得たスペクトルデータを元に成分量を予測する校正モデルを作成します。このモデルにサンプルから得た近赤外スペクトルを代入して、予測値を得ます。操作は簡単で、測定も迅速で非破壊的であることが近赤外の魅力と言えます。

果実のスペクトルは残念ながら持ち合わせていないので、木材の表面から集めたスペクトルで話を進めましょう。４種類の有用熱帯産材、いわゆるメランチと呼ばれる樹種のスペクトルです。スペクトルは極めて似ているといこと注意してください。多変量解析があります。

<br>

<img src="./img/nir.png" style="zoom:67%;" />

<br>

スペクトルデータは概ね緩やかな曲線であまり見分けがつきませんが、高さが揃っていません。バックグラウンドの影響を取り除くために、曲線の変化量だけに注目した









References:

1) A. Savitzky, M. J. E. Golay, Smoothing and Differentiation of Data by Simplified Least Squares Procedures. Analytical Chemistry, 1964, 36 (8), pp 1627-1639.
2) Numerical Recipes 3rd Edition: The Art of Scientific Computing W.H. Press, S.A. Teukolsky, W.T. Vetterling, B.P. Flannery Cambridge University Press ISBN-13: 9780521880688
