# -*- coding: utf-8 -*-
"""
this is for the version with a CORRECT trial 7

march 6 2023

@author: mauspad
"""
#import packages
import pandas as pd
import numpy
import ast

# turn csv into dataframe
df = pd.read_csv("data/_PLOT_behavioral_2023_Mar_09_1515.csv") #change!

# set up some variables
trialno = list(range(1,25)) # trial number
corr1 = [8, 11, 12, 7, 12, 21, 22, 7, 50, 10, 13, 50, 51, 8, 12, 50, 7, 11, 20, 22, 7, 13, 10, 12] # correct number of 1 presses
corr2 = [12, 9, 8, 13, 18, 9, 8, 23, 10, 50, 47, 10, 9, 12, 8, 10, 23, 9, 10, 8, 13, 47, 50, 18] # correct number of 2 presses
movement = [9, 9, 9, 9, 6, 6, 6, 6, 3, 3, 3, 3, 3, 9, 9, 3, 6, 9, 6, 6, 9, 3, 3, 6] # angle moved with each press
corrans = 0 # total correct counter
deg_off_list = [] # tracks degrees off

# loop!
for a, b, c, d in zip(trialno, corr1, corr2, movement):
    #print("Starting trial " + str(a) + "...")
    #print("Correct 1s is " + str(b))
    #print("Correct 2s is " + str(c))
    #print("Movement per click is " + str(d))
    #print(str(corrans) + " correct so far!")
    key_list = df["key_resp.keys"].iloc[a - 1] # pull out key list
    if ('3' in key_list): # detect 3s, make last element, flag if not present
        target = key_list.index('3')
        key_list = key_list[:target]
    else:
        print("Did not lock in trial " + str(a))
    # scoring section. 1s and 2s are recorded twice and I can't fix it without breaking more shit so those counts are halved
    count_1s = ((key_list.count('1')) // 2) #count 1s
    #print(str(count_1s) + " 1s counted")
    count_2s = ((key_list.count('2')) // 2) #count 2s
    #print(str(count_2s) + " 2s counted")
    if count_1s > count_2s:
        #print("More 1s than 2s")
        trialans = count_1s - count_2s
        #print("Adjusted total " + str(trialans) + " 1s")
        if b == trialans: 
            corrans += 1
            deg_off = 0
            print("Trial " + str(a) + " correct!")
        else: 
            deg_off = abs(b - trialans) * d
            print("Trial " + str(a) + " incorrect; " + str(deg_off) + " degrees off")
            deg_off_list.append(deg_off)
    else:
        #print("More 2s than 1s")
        trialans = count_2s - count_1s
        #print("Adjusted total " + str(trialans) + " 2s")
        if c == trialans:
            corrans += 1
            deg_off = 0
            print("Trial " + str(a) + " correct!")
        else: 
            deg_off = abs(c - trialans) * d
            print("Trial " + str(a) + " incorrect; " + str(deg_off) + " degrees off")
            deg_off_list.append(deg_off)
   
print("Total correct: " + str(corrans) + " out of 24")

avgdeg = round(sum(deg_off_list) / len(deg_off_list), 2)

print("Average degrees off: " + str(avgdeg))