import random
sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
l = len(sentence)
if l > 4:
    sentence = sentence[0] + "".join(random.sample(sentence[1:l-1], l-2)) + sentence[-1]
print (sentence)
