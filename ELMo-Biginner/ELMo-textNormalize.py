# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 11:23:18 2019

@author: Abrahametry Mii
"""
import spacy
# import spaCy's language model
nlp = spacy.load('en', disable=['parser', 'ner'])

# function to lemmatize text
def lemmatization(texts):
    output = []
    for i in texts:
             s = [token.lemma_ for token in nlp(i)]
             output.append(' '.join(s))
    return output

train['clean_tweet'] = lemmatization(train['clean_tweet'])
test['clean_tweet'] = lemmatization(test['clean_tweet'])
