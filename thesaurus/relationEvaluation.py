'''
Created on 28.05.2013

@author: Ralu
'''
import nltk
from nltk.corpus import wordnet as wn
from nltk.parse.dependencygraph import * 
# from nltk.corpus import verbnet as vn
# from nltk.corpus import reuters as reuters_news
# from nltk.corpus import brown as brown
# from nltk.corpus import gutenberg as roget
# from nltk.corpus import semcor as mihalcea
# from nltk.corpus import rte as rte_dragan
# from nltk.corpus import names as names
# from nltk.corpus import stopwords as stopwords
# from nltk.corpus import wordnet_ic as wordlist

from nltk.sem.lfg import *
from nltk.parse.dependencygraph import DependencyGraph

dg = DependencyGraph("""\
Esso       NNP     2       SUB
said       VBD     0       root
the        DT      5       NMOD
Whiting    NNP     5       NMOD
field      NN      6       SUB
started    VBD     2       VMOD
production NN      6       OBJ
Tuesday    NNP     6       VMOD
""")

dg1 = DependencyGraph("""
My PRp 2 poss
dog nn 4 nsubj
also rb 4 advmod
likes vbz 0 root
eating vbg 4 xcomp
sausage nn 5 dobj
""")

#  print(FStructure.read_depgraph(dg))
graph = FStructure.read_depgraph(dg1)
print graph
print 'get ',graph.get('advmod')
for item in graph.iteritems():
    print item[1]
for item in graph.iteritems():
    print item[1][0]
