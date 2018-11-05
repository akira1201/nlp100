sentense = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"
num = [1, 5, 6, 7, 8, 9, 15, 16, 19]
print ([s[:1] if i+1 in num else s[:2] for i, s in enumerate(sentense.split(" "))])
