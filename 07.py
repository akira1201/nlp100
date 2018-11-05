x = 12
y = "気温"
z = 22.4

def template(x, y, z):
    return "{time}時の{content}は{temp}".format(time=x, content=y, temp=z)
print(template(x, y, z))
