# _*_ coding: utf-8 _*_
def make_bricks(small, big, goal):
    small_bricks = 1    #小ブロックの大きさ
    big_bricks = 5      #大ブロックの大きさ

    #ゴールと各ブロックの大きさの割った余りを取得する
    remainder_small = goal%small_bricks
    remainder_big   = goal%big_bricks

    #余りが0かつ、「個数」×「ブロックの大きさ」がゴール以上であればTrue
    #スモールレンガだけでゴールに到達できる場合
    if (remainder_small==0) and (small*small_bricks>=goal):
        return True

    #ビッグレンガだけでゴールに到達できる場合
    if (remainder_big==0) and (big*big_bricks>=goal):
        return True

    #小ブロック、大ブロック単独では解決できない場合。両方を混ぜないとダメなケース
    #ゴールから、大きいブロックの「個数」×「ブロックの大きさ」を引き算して、その大小で処理を分岐
    temp = goal - big*big_bricks
    #「差」が0以上であれば、小さいブロックの「個数」が差以上であればTrue
    if temp >= 0:
        if small >= temp:
            return True
        else:
            return False
    #「差」が0以下であれば、
    #「差」と「大ブロックの大きさ」の除算結果の余りを取得して、「大ブロックの大きさ」
    #との差を求めて、smallの個数と比較する。
    else :
        if small >= big_bricks - (-1)*temp%big_bricks:
            return True
        else:
            return False
