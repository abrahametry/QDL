# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:35:29 2019

@author: Abrahametry
"""
from __future__ import unicode_literals
import spacy
import numpy as np
from numpy import dot
from numpy.linalg import norm
#%%
nlp = spacy.load('en_core_web_md')
doc = nlp(open("Quran_YusufAli.txt").read())
#doc = nlp(open("pg345.txt").read())
# all of the words in the text file
#%% 
tokens = list(set([w.text for w in doc if w.is_alpha])) 
#nlp.vocab['cheese'].vector
#%% 
def vec(s):
    return nlp.vocab[s].vector
# cosine similarity
#%% 
def cosine(v1, v2):
    if norm(v1) > 0 and norm(v2) > 0:
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0
#%%
def spacy_closest(token_list, vec_to_check, n=10):
    return sorted(token_list, key=lambda x: cosine(vec_to_check, vec(x)), reverse=True)[:n]
#%%
def meanv(coords):
    # assumes every item in coords has same length as item 0
    sumv = [0] * len(coords[0])
    for item in coords:
        for i in range(len(item)):
            sumv[i] += item[i]
    mean = [0] * len(sumv)
    for i in range(len(sumv)):
        mean[i] = float(sumv[i]) / len(coords)
    return mean
def subtractv(coord1, coord2):
    return [c1 - c2 for c1, c2 in zip(coord1, coord2)]
def addv(coord1, coord2):
    return [c1 + c2 for c1, c2 in zip(coord1, coord2)]
#%%
def sentvec(s):
    sent = nlp(s)
    return meanv([w.vector for w in sent])
#%%
sentences = list(doc.sents)
#%%
def spacy_closest_sent(space, input_str, n=10):
    input_vec = sentvec(input_str)
    return sorted(space,
                  key=lambda x: cosine(np.mean([w.vector for w in x], axis=0), input_vec),
                  reverse=True)[:n]
#%%
#Test an Text to find Closest Sentece
ayat = "Sovereign of the Day of Recompense.";
for sent in spacy_closest_sent(sentences, ayat):
    print(sent.text)
    print("---")




























