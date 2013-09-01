import nltk
from nltk.corpus import wordnet as wn

class stru:
    def __init__(self):
            self.sentence1 = None
            self.sentence2 = []
            self.words_with_antonyms1 = []
            self.antonyms = []
            self.dependencies = []
            self.affix_part1 = None
            self.affix_part2 = None
s = stru()

sentences = []
nrOfPairs = [0]
test = [0]
antonyms_detected = [0]
parts_of_speech =[
                  'JJ', #adjective
                  'JJR',#adjective, comparative
                  'JJS',#adjective, superlative
                  'NN', #noun, singular
                  'NNS', #noun, plural
                  'RB', #adverb
                  'RBR', #adverb, comparative
                  'RBS', #adverb, superlative
                  'VB', #verb, base form
                  'VBD', #verb, past tense
                  'VBG', #verb, gerund, present simple
                  'VBN', #verb, past participle
                  'VBP', #verb, sing. present
                  'VBZ', #verb, 3rd person, sing-present
                  'IN'
                  ]

     
def traverse(t):
    try:
        t.node    
    except AttributeError:
        print ''
    else:
        if t.node in parts_of_speech:
            if(t.leaves() != []): 
                word = str(t.leaves()[0])
                syns = wn.synsets(word)
                for k in syns:
                    for lemma in k.lemmas:
                        if(lemma.antonyms() != []): 
                            antonymList = lemma.antonyms()
                            for lem in antonymList:
                                antonyms.append(lem)
#                         else:
#                             if ():
                                
        for child in t:
            traverse(child)

def traverse2(t1):
    try:
        t1.node
    except AttributeError:
        print ''
    else:
        if t1.node in parts_of_speech:
            if(t1.leaves() != []): 
                word = str(t1.leaves()[0])
                syns = wn.synsets(word)
                for sy in syns:
                    for lemma in sy.lemmas:
                        if ((lemma.synset.name.split('.')[0] == word) & (lemma in antonyms)):
                            print 'Antonyms Detected!'
                            print lemma,'\n'
                            antonyms_detected[0] = 1
        for child in t1:
            traverse2(child)     
            

def main():
    for i in range(0, len(sentences)-1, 2):
        s.__init__()
        tempTree = nltk.tree.Tree(sentences[i])
        tempTree2 = nltk.tree.Tree(sentences[i+1])
        global antonyms
        antonyms = []
        s.sentence1 = sentences[i]
        s.sentence2 = sentences[i+1]
        traverse(tempTree) 
        antonyms_detected[0] = 0
        traverse2(tempTree2) 
        if(antonyms_detected[0] == 1):
            g.write(sentences[i]+' '+sentences[i+1]+'\n')
            nrOfPairs[0] += 1
#         print nrOfPairs[0]
             
f = open('input(3).txt', 'r')
g = open('results.txt', 'w')
sentenceTemp = ''
for line in f:
    if (line[0] == '#'):
        sentences.append(sentenceTemp)
        sentenceTemp = ''
    else: sentenceTemp = sentenceTemp + line

print len(sentences)    
main()                                               
g.write(nrOfPairs[0].__str__())
g.close()