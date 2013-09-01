'''
Created on 21.05.2013

@author: Ralu
'''
from nltk.corpus import wordnet as wn
import nltk
word = "left-handed"
# # print type(word)
syns = wn.synsets(word)
# print syns
# c = wn.synsets('left-handed.')
# print c
# print c[0].lemmas
# # for i in range(0, len(c)):
# # #     for c[i] in 
# #     print c[i].lemmas[0].antonyms()
# syns = wn.synsets('left-handed')
# wo = 'loose'
# # print wo.lemmatize()
# for s in syns:
#     for l in s.lemmas:
#         print s, l, s.definition, l.antonyms(), s.entailments()
#         print l.lemmatize()
#         print l.antonyms()
# sentence = "I am in my innermost circle."
# tokens = nltk.word_tokenize(sentence)
# tagged = nltk.pos_tag(tokens)
# print tagged
# car = wn.synset('car.n.03')
# print car.lemmas
# print car.hypernyms()
# print car.hyponyms()
# light = wn.synset('')
#antonyms
# print car.lemmas[0].antonyms()
#print wn.lemma('car.n.0.stanley_steamer').antonyms()
# print syns.lemmas
w = 'killed'
syn = wn.synsets(w)
print syn
for s in syn:
    for l in s.lemmas:
        print s, l, s.definition, l.antonyms(), s.entailments()