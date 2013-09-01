import nltk
from nltk.corpus import wordnet as wn

class stru:
    def __init__(self):
            self.word = None
            self.pos = None
            self.colour = -1
s = stru()
sentence1 = []
sentence2 = []

sentences = []
def posTag(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    return tagged

# def coloring(sent1, sent2):
    

f = open('input(3).txt', 'r')
g = open('results.txt', 'w')
sentenceTemp = ''
for line in f:
    if (line[0] == '#'):
        sentences.append(sentenceTemp)
        tagged = posTag(sentenceTemp)
        sentenceTemp = ''
    else: sentenceTemp = sentenceTemp + line


