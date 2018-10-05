# _*_ coding: utf-8 _*_
import csv, operator
'''
・csvファイルを操作するために、標準ライブラリであるcsvモジュールをインポートします。
・with構文を使い、close処理を省略します。csvファイルを組み込み型のopen関数で読み込み、
　ファイルオブジェクトとして作成します。open関数の引数を'r'としました（読み込み専用として開きたいため）。
・ファイルオブジェクトfをcsv.readerに読み込ませています。readerオブジェクトはイテレータプロトコルに対応しているため、
　for文やnextで行データを取得することが可能です。
・ソートするために、１行目のヘッダーはソート対象外にしたいので、next関数を使用して、まず表示させて1行先に進めます。
　データ行の2行目以降をソートするために、組み込み型のsorted関数を使用しています。
　sorted関数はリストの内容を残したままソートすることが出来ます。
・あとは、for文で行データ単位に表示させます。
'''
with open('/Users/tsuneo/dive/sample.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    print(next(reader))
    reader = sorted(reader, key=operator.itemgetter(1))
    for line in reader:
        print(line)
