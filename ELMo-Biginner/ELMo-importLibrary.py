# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:19:56 2019

@author: Abrahametry Mii
"""
import pandas as pd
import numpy as np
import spacy
from tqdm import tqdm
import re
import time
import pickle
pd.set_option('display.max_colwidth', 200)

# read data
train = pd.read_csv("train_2kmZucJ.csv")
test = pd.read_csv("test_oJQbWVk.csv")

train.shape, test.shape
train['label'].value_counts(normalize = True)