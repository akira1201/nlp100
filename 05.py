sentense = "I am an NLPer"
n = 2
def make_word_n_gram(seq, n):
    words = seq.split(" ")
    return [words[i:i+n] for i in range(len(words)-n+1)]
def make_char_n_gram(seq, n):
    return [seq[i:i+n] for i in range(len(seq)-n+1)]
print ('word-bi-gram:', make_word_n_gram(sentense, n))
print ('character-bi-gram:', make_char_n_gram(sentense, n))
