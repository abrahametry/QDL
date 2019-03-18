# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:12:40 2019

@author: Abrahametry Mii
"""
import pandas as pd 
import matplotlib.pyplot as plt 
import math
import numpy as np
Datafile = "wrd2vecAnimalData.csv"
data = pd.read_csv(Datafile, names = [0, 1, 2, 3], engine='python')
def distance2d(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def distance3d(x1, y1, x2, y2, z1, z2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
# distance3d(int(data.loc[1,1]), int(data.loc[1,2]), int(data.loc[4,1]), int(data.loc[4,2]), int(data.loc[1,3]), int(data.loc[4,3]))
# plotting points as a scatter plot 
#plt.scatter(data[1], data[2], label= "stars", color= "green", marker= "*", s=50)  
#plt.text(data[1]+0.3, data[2]+0.3, type, fontsize=9)
#plt.xlabel('X') 
#plt.ylabel('Y') 
#plt.title('My scatter plot!') 
#plt.legend() 
#plt.show() 