# In First part NLP concepts (tokenization, Stemming, bag of words)

import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

# Sentense tokenization
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

# Sentense Stemming and then convert into lovercase
def stem(word):
    return stemmer.stem(word.lower())

# after Tokenization then convert bag of word
def bag_of_words(tokenized_sentence,words):
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words),dtype = np.float32)
    for idx ,w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1
    return bag

# a = "Is anyone there?"
# print(a)
# a = tokenize(a)
# print(a)


