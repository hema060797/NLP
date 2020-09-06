# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:10:30 2020

@author: hemahemu
"""


import nltk
nltk.download()
from nltk.tokenize import sent_tokenize, word_tokenize
 
data = "All work and no play makes jack a dull boy, all work and no play"
print(word_tokenize(data))
#import nltk
#nltk.download()

from nltk.tokenize import sent_tokenize, word_tokenize
 
data = "All work and no play makes jack a dull boy, all work and no play"
print(word_tokenize(data))



from nltk.tokenize import sent_tokenize, word_tokenize
 
data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
print(sent_tokenize(data))


from nltk.tokenize import sent_tokenize, word_tokenize
 
data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
 
phrases = sent_tokenize(data)
words = word_tokenize(data)
 
print(phrases)
print(words)

#stopwords
from nltk.corpus import stopwords
data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
stopwords=set(stopwords.words('english'))
words=word_tokenize(data)
wordsfiltered=[]
for w in words:
    if w not in stopwords:
        wordsfiltered.append(w)
print(wordsfiltered)

print(len(stopwords))
print(stopwords)

#stemming
words=["game","gamed","games"]
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps=PorterStemmer()
for word in words:
    print(ps.stem(word))
    
    
    
pss=PorterStemmer()
sentence="gaming,the gamers play games"
words=word_tokenize(sentence)
for word in words:
    print(word+":"+pss.stem(word))
    