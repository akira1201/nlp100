sentence = "与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．"
def cipher(s):
    return "".join([chr(219 - ord(x)) if x.islower() else x for x in s])
print(cipher(sentence))
