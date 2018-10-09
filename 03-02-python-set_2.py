# _*_ coding: utf-8 _*_
course_dict = {
    'AIコース': {'Aさん', 'Cさん', 'Dさん'},
    'Railsコース': {'Bさん', 'Cさん', 'Eさん'},
    'Railsチュートリアルコース': {'Gさん', 'Fさん', 'Eさん'},
    'JS': {'Aさん', 'Gさん', 'Hさん'},
}

def find_person(want_to_find_person):
    """
    受講生がどのコースに在籍しているかを出力する。
    まずはフローチャートを書いて、どのようにアルゴリズムを解いていくか考えてみましょう。
    """
    # ここにコードを書いてみる
    # 辞書型から集合型（set）に変換する事により、辞書のキー（コース名）だけ抽出します。
    # 集合型（set）はシーケンスと似たデータ型なので、for文を利用出来ます。
    # for文の中で、今回新たに作成した関数を呼び出して、それぞれのコースの判定を行います。
    course_name = set(course_dict)
    for i in course_name:
        menber_judge_function(i, want_to_find_person)

# 新たに「メンバー判定関数（menber_judge_function）」を作成して、共通化を図りました。
# 引数で受け取ったコース名から、コースメンバーを取得します。
# あとは、「コースメンバー」と「探したい人」との積集合（&）をとります。
# その判定結果がTrueの場合は、複数人在籍か、それとも1人のみ在籍かを判定します。
# Falseの場合は、在籍していない旨を返します。
def menber_judge_function(course_name, want_to_find_person):
    course_menber  = course_dict[course_name]
    if course_menber & want_to_find_person:
        if len(course_menber & want_to_find_person) == 1:
            print('{0}に{1}のみ在籍しています。'.format(course_name, course_menber & want_to_find_person))
        else:
            print('{0}に{1}は在籍しています。'.format(course_name, want_to_find_person))
    else:
        print('{0}に{1}は在籍していません。'.format(course_name, want_to_find_person))

def main():
    want_to_find_person = {'Cさん', 'Aさん'}
    print('探したい人: {}'.format(want_to_find_person))
    find_person(want_to_find_person)

# モジュールとしてimportされた場合、Pythonは「__name__」変数にモジュール名（03-02-python-set.py）を代入します。
# そのため、当該ファイル（モジュール）をimportしても実行されません。
# 当該ファイルを直接実行した場合（Pythonの引数として直接実行）には、
# 「__name__」変数に「__main__」という文字列を代入しますので、main()関数が呼び出されます。
if __name__ == '__main__':
    main()
