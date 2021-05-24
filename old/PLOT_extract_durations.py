# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:12:49 2019

@author: mauspad

USAGE: Put in same directory as your csv output and change file name at "turn csv into dataframe" line. Prints durations for vector creation
"""

import pandas as pd
import numpy
import ast

# create empty RT list
rt = []

# turn csv into dataframe
df = pd.read_csv("data/2283-2_PLOT_2021_Apr_17_1724.csv")

# pull out response keys and RTs as strings
key_string = df.at[1,"key_resp.keys"]
rt_string = df.at[1,"key_resp.rt"]
key_string2 = df.at[2,"key_resp_2.keys"]
rt_string2 = df.at[2,"key_resp_2.rt"]
key_string3 = df.at[3,"key_resp_3.keys"]
rt_string3 = df.at[3,"key_resp_3.rt"]
key_string4 = df.at[4,"key_resp_4.keys"]
rt_string4 = df.at[4,"key_resp_4.rt"]
key_string5 = df.at[5,"key_resp_5.keys"]
rt_string5 = df.at[5,"key_resp_5.rt"]
key_string6 = df.at[6,"key_resp_6.keys"]
rt_string6 = df.at[6,"key_resp_6.rt"]
key_string7 = df.at[7,"key_resp_7.keys"]
rt_string7 = df.at[7,"key_resp_7.rt"]
key_string8 = df.at[8,"key_resp_8.keys"]
rt_string8 = df.at[8,"key_resp_8.rt"]
key_string9 = df.at[9,"key_resp_9.keys"]
rt_string9 = df.at[9,"key_resp_9.rt"]
key_string10 = df.at[10,"key_resp_10.keys"]
rt_string10 = df.at[10,"key_resp_10.rt"]
key_string11 = df.at[11,"key_resp_11.keys"]
rt_string11 = df.at[11,"key_resp_11.rt"]
key_string12 = df.at[12,"key_resp_12.keys"]
rt_string12 = df.at[12,"key_resp_12.rt"]
key_string13 = df.at[13,"key_resp_13.keys"]
rt_string13 = df.at[13,"key_resp_13.rt"]
key_string14 = df.at[14,"key_resp_14.keys"]
rt_string14 = df.at[14,"key_resp_14.rt"]
key_string15 = df.at[15,"key_resp_15.keys"]
rt_string15 = df.at[15,"key_resp_15.rt"]
key_string16 = df.at[16,"key_resp_16.keys"]
rt_string16 = df.at[16,"key_resp_16.rt"]
key_string17 = df.at[17,"key_resp_17.keys"]
rt_string17 = df.at[17,"key_resp_17.rt"]
key_string18 = df.at[18,"key_resp_18.keys"]
rt_string18 = df.at[18,"key_resp_18.rt"]
key_string19 = df.at[19,"key_resp_19.keys"]
rt_string19 = df.at[19,"key_resp_19.rt"]
key_string20 = df.at[20,"key_resp_20.keys"]
rt_string20 = df.at[20,"key_resp_20.rt"]
key_string21 = df.at[21,"key_resp_21.keys"]
rt_string21 = df.at[21,"key_resp_21.rt"]
key_string22 = df.at[22,"key_resp_22.keys"]
rt_string22 = df.at[22,"key_resp_22.rt"]
key_string23 = df.at[23,"key_resp_23.keys"]
rt_string23 = df.at[23,"key_resp_23.rt"]
key_string24 = df.at[24,"key_resp_24.keys"]
rt_string24 = df.at[24,"key_resp_24.rt"]

#convert strings to lists
rt_list = rt_string.strip('][').split(',')
key_list = ast.literal_eval(key_string)
rt_list2 = rt_string2.strip('][').split(',')
key_list2 = ast.literal_eval(key_string2)
rt_list3 = rt_string3.strip('][').split(',')
key_list3 = ast.literal_eval(key_string3)
rt_list4 = rt_string4.strip('][').split(',')
key_list4 = ast.literal_eval(key_string4)
rt_list5 = rt_string5.strip('][').split(',')
key_list5 = ast.literal_eval(key_string5)
rt_list6 = rt_string6.strip('][').split(',')
key_list6 = ast.literal_eval(key_string6)
rt_list7 = rt_string7.strip('][').split(',')
key_list7 = ast.literal_eval(key_string7)
rt_list8 = rt_string8.strip('][').split(',')
key_list8 = ast.literal_eval(key_string8)
rt_list9 = rt_string9.strip('][').split(',')
key_list9 = ast.literal_eval(key_string9)
rt_list10 = rt_string10.strip('][').split(',')
key_list10 = ast.literal_eval(key_string10)
rt_list11 = rt_string11.strip('][').split(',')
key_list11 = ast.literal_eval(key_string11)
rt_list12 = rt_string12.strip('][').split(',')
key_list12 = ast.literal_eval(key_string12)
rt_list13 = rt_string13.strip('][').split(',')
key_list13 = ast.literal_eval(key_string13)
rt_list14 = rt_string14.strip('][').split(',')
key_list14 = ast.literal_eval(key_string14)
rt_list15 = rt_string15.strip('][').split(',')
key_list15 = ast.literal_eval(key_string15)
rt_list16 = rt_string16.strip('][').split(',')
key_list16 = ast.literal_eval(key_string16)
rt_list17 = rt_string17.strip('][').split(',')
key_list17 = ast.literal_eval(key_string17)
rt_list18 = rt_string18.strip('][').split(',')
key_list18 = ast.literal_eval(key_string18)
rt_list19 = rt_string19.strip('][').split(',')
key_list19 = ast.literal_eval(key_string19)
rt_list20 = rt_string20.strip('][').split(',')
key_list20 = ast.literal_eval(key_string20)
rt_list21 = rt_string21.strip('][').split(',')
key_list21 = ast.literal_eval(key_string21)
rt_list22 = rt_string22.strip('][').split(',')
key_list22 = ast.literal_eval(key_string22)
rt_list23 = rt_string23.strip('][').split(',')
key_list23 = ast.literal_eval(key_string23)
rt_list24 = rt_string24.strip('][').split(',')
key_list24 = ast.literal_eval(key_string24)

#check for 3s, index first press and add to list
if ('3' in key_list):
    rt.append(rt_list[key_list.index('3')])
else: 
    print("No 3 for trial 1")
    rt.append(rt_list[-1])
if ('3' in key_list2):
    rt.append(rt_list2[key_list2.index('3')])
else: 
    print("No 3 for trial 2")
    rt.append(rt_list2[-1])
if ('3' in key_list3):
    rt.append(rt_list3[key_list3.index('3')])
else: 
    print("No 3 for trial 3")
    rt.append(rt_list3[-1])
if ('3' in key_list4):
    rt.append(rt_list4[key_list4.index('3')])
else: 
    print("No 3 for trial 4")
    rt.append(rt_list4[-1])
if ('3' in key_list5):
    rt.append(rt_list5[key_list5.index('3')])
else: 
    print("No 3 for trial 5")
    rt.append(rt_list5[-1])
if ('3' in key_list6):
    rt.append(rt_list6[key_list6.index('3')])
else: 
    print("No 3 for trial 6")
    rt.append(rt_list6[-1])
if ('3' in key_list7):    
    rt.append(rt_list7[key_list7.index('3')])
else: 
    print("No 3 for trial 7")
    rt.append(rt_list7[-1])
if ('3' in key_list8):
    rt.append(rt_list8[key_list8.index('3')])
else: 
    print("No 3 for trial 8")
    rt.append(rt_list8[-1])
if ('3' in key_list9):
    rt.append(rt_list9[key_list9.index('3')])
else: 
    print("No 3 for trial 9")
    rt.append(rt_list9[-1])
if ('3' in key_list10):
    rt.append(rt_list10[key_list10.index('3')])
else: 
    print("No 3 for trial 10")
    rt.append(rt_list10[-1])
if ('3' in key_list11):
    rt.append(rt_list11[key_list11.index('3')])
else: 
    print("No 3 for trial 11")
    rt.append(rt_list11[-1])
if ('3' in key_list12):
    rt.append(rt_list12[key_list12.index('3')])
else: 
    print("No 3 for trial 12")
    rt.append(rt_list12[-1])
if ('3' in key_list13):
    rt.append(rt_list13[key_list13.index('3')])
else: 
    print("No 3 for trial 13")
    rt.append(rt_list13[-1])
if ('3' in key_list14):
    rt.append(rt_list14[key_list14.index('3')])
else: 
    print("No 3 for trial 14")
    rt.append(rt_list14[-1])
if ('3' in key_list15):
    rt.append(rt_list15[key_list15.index('3')])
else: 
    print("No 3 for trial 15")
    rt.append(rt_list15[-1])
if ('3' in key_list16):
    rt.append(rt_list16[key_list16.index('3')])
else: 
    print("No 3 for trial 16")
    rt.append(rt_list16[-1])
if ('3' in key_list17):
    rt.append(rt_list17[key_list17.index('3')])
else: 
    print("No 3 for trial 17")
    rt.append(rt_list17[-1])
if ('3' in key_list18):
    rt.append(rt_list18[key_list18.index('3')])
else: 
    print("No 3 for trial 18")
    rt.append(rt_list18[-1])
if ('3' in key_list19):
    rt.append(rt_list19[key_list19.index('3')])
else: 
    print("No 3 for trial 19")
    rt.append(rt_list19[-1])
if ('3' in key_list20):
    rt.append(rt_list20[key_list20.index('3')])
else: 
    print("No 3 for trial 20")
    rt.append(rt_list20[-1])
if ('3' in key_list21):
    rt.append(rt_list21[key_list21.index('3')])
else: 
    print("No 3 for trial 21")
    rt.append(rt_list21[-1])
if ('3' in key_list22):
    rt.append(rt_list22[key_list22.index('3')])
else: 
    print("No 3 for trial 22")
    rt.append(rt_list22[-1])
if ('3' in key_list23):
    rt.append(rt_list23[key_list23.index('3')])
else: 
    print("No 3 for trial 23")
    rt.append(rt_list23[-1])
if ('3' in key_list24):
    rt.append(rt_list24[key_list24.index('3')])
else: 
    print("No 3 for trial 24")
    rt.append(rt_list24[-1])

#print list
print(''.join(rt))

#set up difficulty list
#difficulty = [1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 1.5, 1.6, 3.6, 2.5, 1.7, 2.6, 2.7, 1.8, 3.7, 3.8, 2.8]

#sort and print
#rt = numpy.array(rt)
#difficulty = numpy.array(difficulty)
#inds = difficulty.argsort()
#sortedRT = rt[inds]
#print(''.join(sortedRT))
