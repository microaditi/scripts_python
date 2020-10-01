from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythonio","pythonly"]

##for w in example_words:
##    print(ps.stem(w))

new_text = " hey im aditi, trying to learn ntlk, and im programing in python are trying to become a good programmer / pythoner"
    
words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
