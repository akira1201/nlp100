import re
sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print ([len(re.sub("\W", "", s)) for s in sentence.split(" ")])
