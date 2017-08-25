# このソフトウェアについて

ファビコン・コレクター。略してファビコレ。

# 概要

* URLを入力してファビコンを取得する
* DBに保存する
* HTMLに出力することで一覧できる
    * クリックするとリンクへ飛ぶ

![example](example.png)

# 用途

* ファビコン一覧して収集欲を満たす
* Webサービスのランチャーとして使う

# 使い方

1. ターミナルを起動する
1. `bash run.sh`コマンドを実行する
1. `http://127.0.0.1:5000/`をブラウザで開く

## URLを追加する

1. `URLを1行ずつ入力してください`とあるテキストエリアにURLを入力する
1. `URLを追加する`ボタンを押下する
1. 画面上にファビコンが表示されたら成功

## URLを参照する

1. ファビコンにマウスカーソルを合わせる
1. クリックするとリンクに飛ぶ

# 開発環境

* インターネット接続環境
* Linux Mint 17.3 MATE
* Python 3.6.1
    * 各種ライブラリ ([ライセンス](#ライセンス)参照)

# 変更履歴

バージョン|リポジトリ名|技術用語
----------|------------|--------
201706021605|FaviconGetter.201706021605|Pythonスクリプト、SQLite3、HTML、CSS
201706051200|FaviconCollector.201706051200|Webサーバ、AJAX、Pythonスクリプト、SQLite

# 課題

* 更新したい
    * リンク切れチェック
    * ファビコン等の一括自動更新
* キーボードで操作したい
    * ファビコンの選択（拡大表示）
    * ファビコンの決定（リンクへ飛ぶ）

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

なお、使用させていただいたライブラリは以下のライセンスである。感謝。

Library|License|Copyright
-------|-------|---------
[requests 2.17.3](http://requests-docs-ja.readthedocs.io/en/latest/)|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)|[Copyright 2012 Kenneth Reitz](http://requests-docs-ja.readthedocs.io/en/latest/user/intro/#requests)
[bs4 0.0.1](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), BeautifulSoup 4.6.0|[MIT](https://opensource.org/licenses/MIT)|[Copyright © 1996-2011 Leonard Richardson](https://pypi.python.org/pypi/beautifulsoup4),[参考](http://tdoc.info/beautifulsoup/)
[dataset 0.8.0](https://dataset.readthedocs.io/en/latest/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2013, Open Knowledge Foundation, Friedrich Lindenberg, Gregor Aisch](https://github.com/pudo/dataset/blob/master/LICENSE.txt)
[Flask 0.12.2](http://flask.pocoo.org/)|[three clause BSD](http://flask.pocoo.org/docs/0.12/license/#flask-license)|[Copyright (c) 2015 by Armin Ronacher and contributors.](http://flask.pocoo.org/docs/0.12/license/)
