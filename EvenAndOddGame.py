#ランダムライブラリをインポート
import random

while True:
    #1,2以外の操作をしていないかチェック
    answer = input("奇数なら1、偶数なら2を入力してください！>")
    int_answer = int(answer)
    if int_answer == 1:
        pass
    elif int_answer == 2:
        pass
    else:
        print("1か2を入力してください！")
        continue

    #乱数を設定
    num = random.randint(1,10)

    #奇数/偶数の判定処理
    if num % 2 == 0:
        print("偶数です！")
    else:
        print("奇数です!")
    string = input("続けますか？はいorいいえを入力してください>")
    if string == "いいえ": break
print("遊んでくれてありがとう！")
