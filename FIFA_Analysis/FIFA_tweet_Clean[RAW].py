# -*- coding: utf-8 -*-
import pandas as pd
import re
import glob
#+++++ Tweet Cleaning Function
def tweet_clean(files):
    # remove URL's from train and test
    train['clean_tweet'] = train['tweet'].apply(lambda x: re.sub(r'http\S+', '', x))
    # remove punctuation marks
    punctuation = '!"#$%&()*+-/:;<=>?@[\\]^_`{|}~'
    train['clean_tweet'] = train['clean_tweet'].apply(lambda x: ''.join(ch for ch in x if ch not in set(punctuation)))
    # convert text to lowercase
    train['clean_tweet'] = train['clean_tweet'].str.lower()
    # remove numbers
    train['clean_tweet'] = train['clean_tweet'].str.replace("[0-9]", " ")
    # remove whitespaces
    train['clean_tweet'] = train['clean_tweet'].apply(lambda x:' '.join(x.split()))
    return train['clean_tweet']

#Multiple CSV File Read
#filenames = glob.glob('ARG/*.csv')
filenames = glob.glob('BRA/*.csv')
#filenames = glob.glob('CRO/*.csv')
#filenames = glob.glob('ENG/*.csv')
#filenames = glob.glob('FRA/*.csv')
#filenames = glob.glob('GER/*.csv')
#filenames = glob.glob('POR/*.csv')
i=0
for filename in filenames:
    #print("tweet_clean(\""+filenames[i]+"\")")
    #print(filenames[i][:-3]+"txt")
    train = pd.read_csv(filename)
    with open(filenames[i][:-3]+"txt", 'w') as f:  
        f.writelines(tweet_clean(train))
    i=i+1

