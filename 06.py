word_1 = "paraparaparadise"
word_2 = "paragraph"
se = "se"

def n_gram(seq, n):
    return set([seq[i:i+n] for i in range(len(seq)-n+1)])

x = n_gram(word_1, 2)
y = n_gram(word_2, 2)

print("1.和集合 : ", x | y)
print("2.積集合 : ", x & y)
print("3-1.xとyの差集合 : ", x - y)
print("3-2.yとxの差集合 : ", y - x)
print("4-1.'se'がxに含まれるか : ", se in x)
print("4-2.'se'がyに含まれるか : ", se in y)
