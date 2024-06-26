# def 関数名():
#     関数で行う処理

def sayhello():
    print("こんにちは")

sayhello()
sayhello()
sayhello()

# 出力結果
# こんにちは
# こんにちは
# こんにちは

# (関数の種類)
# 引数も戻り値もない関数
# 引数も戻り値もある関数
# 引数だけある関数
# 戻り値だけある関数


# (引数と戻り値がある場合)

# def 関数名(引数, 引数2,...):
#    関数で行う処理
#    return 戻り値

def postTaxPrice(price):
    ans = price * 1.1
    return ans

print(postTaxPrice(120),"円")
print(postTaxPrice(128),"円")
print(postTaxPrice(980),"円")

# 出力結果
# 132.0 円
# 140.8 円
# 1078.0 円

# def関数名(引数):と指定
# 関数名をpostTaxPriceとするならdef postTaxPrice(price):と指定。
# 作成した関数はpostTaxPrice(本体価格)で呼び出す。


# 引数だけある関数は値を渡し処理を調整したい時に使用する

def sayhello2(name):
    print("こんにちは、"+ name + "さん。")
sayhello2("フタバ")

# 出力結果
# こんにちは、フタバさん。

# 戻り値だけある関数は処理に変化があるので知りたい時に使用する

import random
def omikuji():
    kuji = ['大吉', '中吉', '小吉', '凶']
    return random.choice(kuji)
kekka = omikuji()
print("結果は",kekka,"です")