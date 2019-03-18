# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:12:40 2019

@author: Abrahametry Mii
"""
import json
import math
import numpy as np
import spacy
nlp = spacy.load('en')
color_data = json.loads(open("xkcd.json").read())
def hex_to_int(s):
    s = s.lstrip("#")
    return int(s[:2], 16), int(s[2:4], 16), int(s[4:6], 16)
colors = dict()
for item in color_data['colors']:
    colors[item["color"]] = hex_to_int(item["hex"])
#Vector Math
def distance(coord1, coord2):
    return math.sqrt(sum([(i - j)**2 for i, j in zip(coord1, coord2)]))
def subtractv(coord1, coord2):
    return [c1 - c2 for c1, c2 in zip(coord1, coord2)]

def addv(coord1, coord2):
    return [c1 + c2 for c1, c2 in zip(coord1, coord2)]

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

def closest(space, coord, n=8):
    closest = []
    for key in sorted(space.keys(), key=lambda x: distance(coord, space[x]))[:n]:
        closest.append(key)
    return closest
#import random
#red = colors['green']
#blue = colors['red']
#for i in range(14):
#    rednames = closest(colors, red)
#    bluenames = closest(colors, blue)
#    print("Grasss are " + rednames[0] + ", Milk are " + bluenames[0])
#    red = colors[random.choice(rednames[1:])]
#    blue = colors[random.choice(bluenames[1:])]
#+++++++++++++++  DRACULA COLOR CODE ++++++++++++++++
#doc = nlp(open("pg345.txt").read())
#doc = nlp(open("Quran_YusufAli.txt").read())
# use word.lower_ to normalize case
#quran_colors = [colors[word.lower_] for word in doc if word.lower_ in colors]
#avg_color = meanv(quran_colors)
#print (avg_color)
#closest(colors, avg_color)
    



































