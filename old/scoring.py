# -*- coding: utf-8 -*-
"""
THIS IS BAD CODE. 
IT WORKS, BUT IT IS VERY VERY BAD. 
DO NOT EMULATE THIS.

Created on Wed Dec 11 15:12:49 2019

@author: mauspad
"""
#import packages
import pandas as pd
import numpy
import ast

# turn csv into dataframe
df = pd.read_csv("data/test_PLOT_2021_Apr_20_1528.csv")

# pull out response keys and RTs as strings
rt = []

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

#detect 3s, flag if not present, make last element and add RT to list if present    
if ('3' in key_list):
    rt.append(rt_list[key_list.index('3')])
    target = key_list.index('3')
    key_list = key_list[:target]
else: 
    print("Did not lock in trial 1")
    rt.append(rt_list[-1])
    
if ('3' in key_list2):
    rt.append(rt_list2[key_list2.index('3')])
    target = key_list2.index('3')
    key_list2 = key_list2[:target]
else: 
    print("Did not lock in trial 2")
    rt.append(rt_list2[-1])
    
if ('3' in key_list3):
    rt.append(rt_list3[key_list3.index('3')])
    target = key_list3.index('3')
    key_list3 = key_list3[:target]
else: 
    print("Did not lock in trial 3")
    rt.append(rt_list3[-1])
    
if ('3' in key_list4):
    rt.append(rt_list4[key_list4.index('3')])
    target = key_list4.index('3')
    key_list4 = key_list4[:target]
else: 
    print("Did not lock in trial 4")
    rt.append(rt_list4[-1])
    
if ('3' in key_list5):
    rt.append(rt_list5[key_list5.index('3')])
    target = key_list5.index('3')
    key_list5 = key_list5[:target]
else: 
    print("Did not lock in trial 5")
    rt.append(rt_list5[-1])
    
if ('3' in key_list6):
    rt.append(rt_list6[key_list6.index('3')])
    target = key_list6.index('3')
    key_list6 = key_list6[:target]
else: 
    print("Did not lock in trial 6")
    rt.append(rt_list6[-1])
    
if ('3' in key_list7):    
    rt.append(rt_list7[key_list7.index('3')])
    target = key_list7.index('3')
    key_list7 = key_list7[:target]
else: 
    print("Did not lock in trial 7")
    rt.append(rt_list7[-1])
    
if ('3' in key_list8):
    rt.append(rt_list8[key_list8.index('3')])
    target = key_list8.index('3')
    key_list8 = key_list8[:target]
else: 
    print("Did not lock in trial 8")
    rt.append(rt_list8[-1])
    
if ('3' in key_list9):
    rt.append(rt_list9[key_list9.index('3')])
    target = key_list9.index('3')
    key_list9 = key_list9[:target]
else: 
    print("Did not lock in trial 9")
    rt.append(rt_list9[-1])
    
if ('3' in key_list10):
    rt.append(rt_list10[key_list10.index('3')])
    target = key_list10.index('3')
    key_list10 = key_list10[:target]
else: 
    print("Did not lock in trial 10")
    rt.append(rt_list10[-1])
    
if ('3' in key_list11):
    rt.append(rt_list11[key_list11.index('3')])
    target = key_list11.index('3')
    key_list11 = key_list11[:target]
else: 
    print("Did not lock in trial 11")
    rt.append(rt_list11[-1])
    
if ('3' in key_list12):
    rt.append(rt_list12[key_list12.index('3')])
    target = key_list12.index('3')
    key_list12 = key_list12[:target]
else: 
    print("Did not lock in trial 12")
    rt.append(rt_list12[-1])
    
if ('3' in key_list13):
    rt.append(rt_list13[key_list13.index('3')])
    target = key_list13.index('3')
    key_list13 = key_list13[:target]
else: 
    print("Did not lock in trial 13")
    rt.append(rt_list13[-1])
    
if ('3' in key_list14):
    rt.append(rt_list14[key_list14.index('3')])
    target = key_list14.index('3')
    key_list14 = key_list14[:target]
else: 
    print("Did not lock in trial 14")
    rt.append(rt_list14[-1])
    
if ('3' in key_list15):
    rt.append(rt_list15[key_list15.index('3')])
    target = key_list15.index('3')
    key_list15 = key_list15[:target]
else: 
    print("Did not lock in trial 15")
    rt.append(rt_list15[-1])
    
if ('3' in key_list16):
    rt.append(rt_list16[key_list16.index('3')])
    target = key_list16.index('3')
    key_list16 = key_list16[:target]
else: 
    print("Did not lock in trial 16")
    rt.append(rt_list16[-1])
    
if ('3' in key_list17):
    rt.append(rt_list17[key_list17.index('3')])
    target = key_list17.index('3')
    key_list17 = key_list17[:target]
else: 
    print("Did not lock in trial 17")
    rt.append(rt_list17[-1])
    
if ('3' in key_list18):
    rt.append(rt_list18[key_list18.index('3')])
    target = key_list18.index('3')
    key_list18 = key_list18[:target]
else: 
    print("Did not lock in trial 18")
    rt.append(rt_list18[-1])
    
if ('3' in key_list19):
    rt.append(rt_list19[key_list19.index('3')])
    target = key_list19.index('3')
    key_list19 = key_list19[:target]
else: 
    print("Did not lock in trial 19")
    rt.append(rt_list19[-1])
    
if ('3' in key_list20):
    rt.append(rt_list20[key_list20.index('3')])
    target = key_list20.index('3')
    key_list20 = key_list20[:target]
else: 
    print("Did not lock in trial 20")
    rt.append(rt_list20[-1])
    
if ('3' in key_list21):
    rt.append(rt_list21[key_list21.index('3')])
    target = key_list21.index('3')
    key_list21 = key_list21[:target]
else: 
    print("Did not lock in trial 21")
    rt.append(rt_list21[-1])
    
if ('3' in key_list22):
    rt.append(rt_list22[key_list22.index('3')])
    target = key_list22.index('3')
    key_list22 = key_list22[:target]
else: 
    print("Did not lock in trial 22")
    rt.append(rt_list22[-1])
    
if ('3' in key_list23):
    rt.append(rt_list23[key_list23.index('3')])
    target = key_list23.index('3')
    key_list23 = key_list23[:target]
else: 
    print("Did not lock in trial 23")
    rt.append(rt_list23[-1])
    
if ('3' in key_list24):
    rt.append(rt_list24[key_list24.index('3')])
    target = key_list24.index('3')
    key_list24 = key_list24[:target]
else: 
    print("Did not lock in trial 24")
    rt.append(rt_list24[-1])

#scoring section
corrans = 0

trial_1_1 = key_list.count('1')
trial_1_2 = key_list.count('2')
trial_1_corr1 = 8
trial_1_corr2 = 12
if trial_1_1 > trial_1_2:
    trial_1_ans = trial_1_1 - trial_1_2
    if trial_1_corr1 == trial_1_ans:
        corrans += 1
        deg_off_1 = 0
        print("Trial 1: Correct")
    else:
        deg_off_1 = abs(trial_1_corr1 - trial_1_ans) * 9
        print("Trial 1: Incorrect. " + str(deg_off_1) + " degrees off")
else:
    trial_1_ans = trial_1_2 - trial_1_1
    if trial_1_corr2 == trial_1_ans:
        corrans += 1
        deg_off_1 = 0
        print("Trial 1: Correct")
    else:
        deg_off_1 = abs(trial_1_corr2 - trial_1_ans) * 9
        print("Trial 1: Incorrect. " + str(deg_off_1) + " degrees off")
        
trial_2_1 = key_list2.count('1')
trial_2_2 = key_list2.count('2')
trial_2_corr1 = 11
trial_2_corr2 = 9
if trial_2_1 > trial_2_2:
    trial_2_ans = trial_2_1 - trial_2_2
    if trial_2_corr1 == trial_2_ans:
        corrans += 1
        deg_off_2 = 0
        print("Trial 2: Correct")
    else:
        deg_off_2 = abs(trial_2_corr1 - trial_2_ans) * 9
        print("Trial 2: Incorrect. " + str(deg_off_2) + " degrees off")
else:
    trial_2_ans = trial_2_2 - trial_2_1
    if trial_2_corr2 == trial_2_ans:
        corrans += 1
        deg_off_2 = 0
        print("Trial 2: Correct")
    else:
        deg_off_2 = abs(trial_2_corr2 - trial_2_ans) * 9
        print("Trial 2: Incorrect. " + str(deg_off_2) + " degrees off")

trial_3_1 = key_list3.count('1')
trial_3_2 = key_list3.count('2')
trial_3_corr1 = 12
trial_3_corr2 = 8
if trial_3_1 > trial_3_2:
    trial_3_ans = trial_3_1 - trial_3_2
    if trial_3_corr1 == trial_3_ans:
        corrans += 1
        deg_off_3 = 0
        print("Trial 3: Correct")
    else:
        deg_off_3 = abs(trial_3_corr1 - trial_3_ans) * 9
        print("Trial 3: Incorrect. " + str(deg_off_3) + " degrees off")
else:
    trial_3_ans = trial_3_2 - trial_3_1
    if trial_3_corr2 == trial_3_ans:
        corrans += 1
        deg_off_3 = 0
        print("Trial 3: Correct")
    else:
        deg_off_3 = abs(trial_3_corr2 - trial_3_ans) * 9
        print("Trial 3: Incorrect. " + str(deg_off_3) + " degrees off")

trial_4_1 = key_list4.count('1')
trial_4_2 = key_list4.count('2')
trial_4_corr1 = 7
trial_4_corr2 = 13
if trial_4_1 > trial_4_2:
    trial_4_ans = trial_4_1 - trial_4_2
    if trial_4_corr1 == trial_4_ans:
        corrans += 1
        deg_off_4 = 0
        print("Trial 4: Correct")
    else:
        deg_off_4 = abs(trial_4_corr1 - trial_4_ans) * 9
        print("Trial 4: Incorrect. " + str(deg_off_4) + " degrees off")
else:
    trial_4_ans = trial_4_2 - trial_4_1
    if trial_4_corr2 == trial_4_ans:
        corrans += 1
        deg_off_4 = 0
        print("Trial 4: Correct")
    else:
        deg_off_4 = abs(trial_4_corr2 - trial_4_ans) * 9
        print("Trial 4: Incorrect. " + str(deg_off_4) + " degrees off")

trial_5_1 = key_list5.count('1')
trial_5_2 = key_list5.count('2')
trial_5_corr1 = 12
trial_5_corr2 = 18
if trial_5_1 > trial_5_2:
    trial_5_ans = trial_5_1 - trial_5_2
    if trial_5_corr1 == trial_5_ans:
        corrans += 1
        deg_off_5 = 0
        print("Trial 5: Correct")
    else:
        deg_off_5 = abs(trial_5_corr1 - trial_5_ans) * 6
        print("Trial 5: Incorrect. " + str(deg_off_5) + " degrees off")
else:
    trial_5_ans = trial_5_2 - trial_5_1
    if trial_5_corr2 == trial_5_ans:
        corrans += 1
        deg_off_5 = 0
        print("Trial 5: Correct")
    else:
        deg_off_5 = abs(trial_5_corr2 - trial_5_ans) * 6
        print("Trial 5: Incorrect. " + str(deg_off_5) + " degrees off")
        
trial_6_1 = key_list6.count('1')
trial_6_2 = key_list6.count('2')
trial_6_corr1 = 21
trial_6_corr2 = 9
if trial_6_1 > trial_6_2:
    trial_6_ans = trial_6_1 - trial_6_2
    if trial_6_corr1 == trial_6_ans:
        corrans += 1
        deg_off_6 = 0
        print("Trial 6: Correct")
    else:
        deg_off_6 = abs(trial_6_corr1 - trial_6_ans) * 6
        print("Trial 6: Incorrect. " + str(deg_off_6) + " degrees off")
else:
    trial_6_ans = trial_6_2 - trial_6_1
    if trial_6_corr2 == trial_6_ans:
        corrans += 1        
        deg_off_6 = 0
        print("Trial 6: Correct")
    else:
        deg_off_6 = abs(trial_6_corr2 - trial_6_ans) * 6   
        print("Trial 6: Incorrect. " + str(deg_off_6) + " degrees off")
            
trial_7_1 = key_list7.count('1')
trial_7_2 = key_list7.count('2')
trial_7_corr1 = 22
trial_7_corr2 = 8
if trial_7_1 > trial_7_2:
    trial_7_ans = trial_7_1 - trial_7_2
    if trial_7_corr1 == trial_7_ans:
        corrans += 1
        deg_off_7 = 0
        print("Trial 7: Correct")
    else:
        deg_off_7 = abs(trial_7_corr1 - trial_7_ans) * 6
        print("Trial 7: Incorrect. " + str(deg_off_7) + " degrees off")
else:
    trial_7_ans = trial_7_2 - trial_7_1
    if trial_7_corr2 == trial_7_ans:
        corrans += 1    
        deg_off_7 = 0
        print("Trial 7: Correct")
    else:
        deg_off_7 = abs(trial_7_corr2 - trial_7_ans) * 6     
        print("Trial 7: Incorrect. " + str(deg_off_7) + " degrees off") 
  
trial_8_1 = key_list8.count('1')
trial_8_2 = key_list8.count('2')
trial_8_corr1 = 7
trial_8_corr2 = 23
if trial_8_1 > trial_8_2:
    trial_8_ans = trial_8_1 - trial_8_2
    if trial_8_corr1 == trial_8_ans:
        corrans += 1
        deg_off_8 = 0
        print("Trial 8: Correct")
    else:
        deg_off_8 = abs(trial_8_corr1 - trial_8_ans) * 6     
        print("Trial 8: Incorrect. " + str(deg_off_8) + " degrees off") 
else:
    trial_8_ans = trial_8_2 - trial_8_1
    if trial_8_corr2 == trial_8_ans:
        corrans += 1  
        deg_off_8 = 0
        print("Trial 8: Correct")
    else:
        deg_off_8 = abs(trial_8_corr2 - trial_8_ans) * 6     
        print("Trial 8: Incorrect. " + str(deg_off_8) + " degrees off") 

trial_9_1 = key_list9.count('1')
trial_9_2 = key_list9.count('2')
trial_9_corr1 = 50
trial_9_corr2 = 10
if trial_9_1 > trial_9_2:
    trial_9_ans = trial_9_1 - trial_9_2
    if trial_9_corr1 == trial_9_ans:
        corrans += 1
        deg_off_9 = 0
        print("Trial 9: Correct")
    else:
        deg_off_9 = abs(trial_9_corr1 - trial_9_ans) * 3     
        print("Trial 9: Incorrect. " + str(deg_off_9) + " degrees off") 
else:
    trial_9_ans = trial_9_2 - trial_9_1
    if trial_9_corr2 == trial_9_ans:
        corrans += 1  
        deg_off_9 = 0
        print("Trial 9: Correct")
    else:
        deg_off_9 = abs(trial_9_corr2 - trial_9_ans) * 3     
        print("Trial 9: Incorrect. " + str(deg_off_9) + " degrees off") 

trial_10_1 = key_list10.count('1')
trial_10_2 = key_list10.count('2')
trial_10_corr1 = 10
trial_10_corr2 = 50
if trial_10_1 > trial_10_2:
    trial_10_ans = trial_10_1 - trial_10_2
    if trial_10_corr1 == trial_10_ans:
        corrans += 1
        deg_off_10 = 0
        print("Trial 10: Correct")
    else:
        deg_off_10 = abs(trial_10_corr1 - trial_10_ans) * 3     
        print("Trial 10: Incorrect. " + str(deg_off_10) + " degrees off") 
else:
    trial_10_ans = trial_10_2 - trial_10_1
    if trial_10_corr2 == trial_10_ans:
        corrans += 1  
        deg_off_10 = 0
        print("Trial 10: Correct")
    else:
        deg_off_10 = abs(trial_10_corr2 - trial_10_ans) * 3     
        print("Trial 10: Incorrect. " + str(deg_off_10) + " degrees off") 

trial_11_1 = key_list11.count('1')
trial_11_2 = key_list11.count('2')
trial_11_corr1 = 13
trial_11_corr2 = 47
if trial_11_1 > trial_11_2:
    trial_11_ans = trial_11_1 - trial_11_2
    if trial_11_corr1 == trial_11_ans:
        corrans += 1
        deg_off_11 = 0
        print("Trial 11: Correct")
    else:
        deg_off_11 = abs(trial_11_corr1 - trial_11_ans) * 3     
        print("Trial 11: Incorrect. " + str(deg_off_11) + " degrees off") 
else:
    trial_11_ans = trial_11_2 - trial_11_1
    if trial_11_corr2 == trial_11_ans:
        corrans += 1  
        deg_off_11 = 0
        print("Trial 11: Correct")
    else:
        deg_off_11 = abs(trial_11_corr2 - trial_11_ans) * 3     
        print("Trial 11: Incorrect. " + str(deg_off_11) + " degrees off") 

trial_12_1 = key_list12.count('1')
trial_12_2 = key_list12.count('2')
trial_12_corr1 = 50
trial_12_corr2 = 10
if trial_12_1 > trial_12_2:
    trial_12_ans = trial_12_1 - trial_12_2
    if trial_12_corr1 == trial_12_ans:
        corrans += 1
        deg_off_12 = 0
        print("Trial 12: Correct")
    else:
        deg_off_12 = abs(trial_12_corr1 - trial_12_ans) * 3     
        print("Trial 12: Incorrect. " + str(deg_off_12) + " degrees off") 
else:
    trial_12_ans = trial_12_2 - trial_12_1
    if trial_12_corr2 == trial_12_ans:
        corrans += 1  
        deg_off_12 = 0
        print("Trial 12: Correct")
    else:
        deg_off_12 = abs(trial_12_corr2 - trial_12_ans) * 3     
        print("Trial 12: Incorrect. " + str(deg_off_12) + " degrees off") 

trial_13_1 = key_list13.count('1')
trial_13_2 = key_list13.count('2')
trial_13_corr1 = 51
trial_13_corr2 = 9
if trial_13_1 > trial_13_2:
    trial_13_ans = trial_13_1 - trial_13_2
    if trial_13_corr1 == trial_13_ans:
        corrans += 1
        deg_off_13 = 0
        print("Trial 13: Correct")
    else:
        deg_off_13 = abs(trial_13_corr1 - trial_13_ans) * 3     
        print("Trial 13: Incorrect. " + str(deg_off_13) + " degrees off") 
else:
    trial_13_ans = trial_13_2 - trial_13_1
    if trial_13_corr2 == trial_13_ans:
        corrans += 1  
        deg_off_13 = 0
        print("Trial 13: Correct")
    else:
        deg_off_13 = abs(trial_13_corr2 - trial_13_ans) * 3     
        print("Trial 13: Incorrect. " + str(deg_off_13) + " degrees off") 

trial_14_1 = key_list14.count('1')
trial_14_2 = key_list14.count('2')
trial_14_corr1 = 8
trial_14_corr2 = 12
if trial_14_1 > trial_14_2:
    trial_14_ans = trial_14_1 - trial_14_2
    if trial_14_corr1 == trial_14_ans:
        corrans += 1
        deg_off_14 = 0
        print("Trial 14: Correct")
    else:
        deg_off_14 = abs(trial_14_corr1 - trial_14_ans) * 9     
        print("Trial 14: Incorrect. " + str(deg_off_14) + " degrees off") 
else:
    trial_14_ans = trial_14_2 - trial_14_1
    if trial_14_corr2 == trial_14_ans:
        corrans += 1  
        deg_off_14 = 0
        print("Trial 14: Correct")
    else:
        deg_off_14 = abs(trial_14_corr2 - trial_14_ans) * 9     
        print("Trial 14: Incorrect. " + str(deg_off_14) + " degrees off") 

trial_15_1 = key_list15.count('1')
trial_15_2 = key_list15.count('2')
trial_15_corr1 = 12
trial_15_corr2 = 8
if trial_15_1 > trial_15_2:
    trial_15_ans = trial_15_1 - trial_15_2
    if trial_15_corr1 == trial_15_ans:
        corrans += 1
        deg_off_15 = 0
        print("Trial 15: Correct")
    else:
        deg_off_15 = abs(trial_15_corr1 - trial_15_ans) * 9     
        print("Trial 15: Incorrect. " + str(deg_off_15) + " degrees off") 
else:
    trial_15_ans = trial_15_2 - trial_15_1
    if trial_15_corr2 == trial_15_ans:
        corrans += 1  
        deg_off_15 = 0
        print("Trial 15: Correct")
    else:
        deg_off_15 = abs(trial_15_corr2 - trial_15_ans) * 9     
        print("Trial 15: Incorrect. " + str(deg_off_15) + " degrees off") 

trial_16_1 = key_list16.count('1')
trial_16_2 = key_list16.count('2')
trial_16_corr1 = 50
trial_16_corr2 = 10
if trial_16_1 > trial_16_2:
    trial_16_ans = trial_16_1 - trial_16_2
    if trial_16_corr1 == trial_16_ans:
        corrans += 1
        deg_off_16 = 0
        print("Trial 16: Correct")
    else:
        deg_off_16 = abs(trial_16_corr1 - trial_16_ans) * 3     
        print("Trial 16: Incorrect. " + str(deg_off_16) + " degrees off") 
else:
    trial_16_ans = trial_16_2 - trial_16_1
    if trial_16_corr2 == trial_16_ans:
        corrans += 1  
        deg_off_16 = 0
        print("Trial 16: Correct")
    else:
        deg_off_16 = abs(trial_16_corr2 - trial_16_ans) * 3     
        print("Trial 16: Incorrect. " + str(deg_off_16) + " degrees off") 
        
trial_17_1 = key_list17.count('1')
trial_17_2 = key_list17.count('2')
trial_17_corr1 = 7
trial_17_corr2 = 23
if trial_17_1 > trial_17_2:
    trial_17_ans = trial_17_1 - trial_17_2
    if trial_17_corr1 == trial_17_ans:
        corrans += 1
        deg_off_17 = 0
        print("Trial 17: Correct")
    else:
        deg_off_17 = abs(trial_17_corr1 - trial_17_ans) * 6     
        print("Trial 17: Incorrect. " + str(deg_off_17) + " degrees off") 
else:
    trial_17_ans = trial_17_2 - trial_17_1
    if trial_17_corr2 == trial_17_ans:
        corrans += 1       
        deg_off_17 = 0
        print("Trial 17: Correct")
    else:
        deg_off_17 = abs(trial_17_corr2 - trial_17_ans) * 6     
        print("Trial 17: Incorrect. " + str(deg_off_17) + " degrees off") 
        
trial_18_1 = key_list18.count('1')
trial_18_2 = key_list18.count('2')
trial_18_corr1 = 11
trial_18_corr2 = 9
if trial_18_1 > trial_18_2:
    trial_18_ans = trial_18_1 - trial_18_2
    if trial_18_corr1 == trial_18_ans:
        corrans += 1
        deg_off_18 = 0
        print("Trial 18: Correct")
    else:
        deg_off_18 = abs(trial_18_corr1 - trial_18_ans) * 9     
        print("Trial 18: Incorrect. " + str(deg_off_18) + " degrees off") 
else:
    trial_18_ans = trial_18_2 - trial_18_1
    if trial_18_corr2 == trial_18_ans:
        corrans += 1     
        deg_off_18 = 0
        print("Trial 18: Correct")
    else:
        deg_off_18 = abs(trial_18_corr2 - trial_18_ans) * 9        
        print("Trial 18: Incorrect. " + str(deg_off_18) + " degrees off")         
        
trial_19_1 = key_list19.count('1')
trial_19_2 = key_list19.count('2')
trial_19_corr1 = 20
trial_19_corr2 = 10
if trial_19_1 > trial_19_2:
    trial_19_ans = trial_19_1 - trial_19_2
    if trial_19_corr1 == trial_19_ans:
        corrans += 1
        deg_off_19 = 0
        print("Trial 19: Correct")
    else:
        deg_off_19 = abs(trial_19_corr1 - trial_19_ans) * 6     
        print("Trial 19: Incorrect. " + str(deg_off_19) + " degrees off") 
else:
    trial_19_ans = trial_19_2 - trial_19_1
    if trial_19_corr2 == trial_19_ans:
        corrans += 1           
        deg_off_19 = 0
        print("Trial 19: Correct")
    else:
        deg_off_19 = abs(trial_19_corr2 - trial_19_ans) * 6              
        print("Trial 19: Incorrect. " + str(deg_off_19) + " degrees off") 

trial_20_1 = key_list20.count('1')
trial_20_2 = key_list20.count('2')
trial_20_corr1 = 22
trial_20_corr2 = 8
if trial_20_1 > trial_20_2:
    trial_20_ans = trial_20_1 - trial_20_2
    if trial_20_corr1 == trial_20_ans:
        corrans += 1
        deg_off_20 = 0
        print("Trial 20: Correct")
    else:
        deg_off_20 = abs(trial_20_corr1 - trial_20_ans) * 6     
        print("Trial 20: Incorrect. " + str(deg_off_20) + " degrees off") 
else:
    trial_20_ans = trial_20_2 - trial_20_1
    if trial_20_corr2 == trial_20_ans:
        corrans += 1         
        deg_off_20 = 0
        print("Trial 20: Correct")
    else:
        deg_off_20 = abs(trial_20_corr2 - trial_20_ans) * 6        
        print("Trial 20: Incorrect. " + str(deg_off_20) + " degrees off")     

trial_21_1 = key_list21.count('1')
trial_21_2 = key_list21.count('2')
trial_21_corr1 = 7
trial_21_corr2 = 13
if trial_21_1 > trial_21_2:
    trial_21_ans = trial_21_1 - trial_21_2
    if trial_21_corr1 == trial_21_ans:
        corrans += 1
        deg_off_21 = 0
        print("Trial 21: Correct")
    else:
        deg_off_21 = abs(trial_21_corr1 - trial_21_ans) * 9     
        print("Trial 21: Incorrect. " + str(deg_off_21) + " degrees off") 
else:
    trial_21_ans = trial_21_2 - trial_21_1
    if trial_21_corr2 == trial_21_ans:
        corrans += 1
        deg_off_21 = 0
        print("Trial 21: Correct")
    else:
        deg_off_21 = abs(trial_21_corr2 - trial_21_ans) * 9      
        print("Trial 21: Incorrect. " + str(deg_off_21) + " degrees off") 

trial_22_1 = key_list22.count('1')
trial_22_2 = key_list22.count('2')
trial_22_corr1 = 13
trial_22_corr2 = 47
if trial_22_1 > trial_22_2:
    trial_22_ans = trial_22_1 - trial_22_2
    if trial_22_corr1 == trial_22_ans:
        corrans += 1
        deg_off_22 = 0
        print("Trial 22: Correct")
    else:
        deg_off_22 = abs(trial_22_corr1 - trial_22_ans) * 3     
        print("Trial 22: Incorrect. " + str(deg_off_22) + " degrees off") 
else:
    trial_22_ans = trial_22_2 - trial_22_1
    if trial_22_corr2 == trial_22_ans:
        corrans += 1 
        deg_off_22 = 0
        print("Trial 22: Correct")
    else:
        deg_off_22 = abs(trial_22_corr2 - trial_22_ans) * 3     
        print("Trial 22: Incorrect. " + str(deg_off_22) + " degrees off") 

trial_23_1 = key_list23.count('1')
trial_23_2 = key_list23.count('2')
trial_23_corr1 = 10
trial_23_corr2 = 50
if trial_23_1 > trial_23_2:
    trial_23_ans = trial_23_1 - trial_23_2
    if trial_23_corr1 == trial_23_ans:
        corrans += 1
        deg_off_23 = 0
        print("Trial 23: Correct")
    else:
        deg_off_23 = abs(trial_23_corr1 - trial_23_ans) * 3     
        print("Trial 23: Incorrect. " + str(deg_off_23) + " degrees off") 
else:
    trial_23_ans = trial_23_2 - trial_23_1
    if trial_23_corr2 == trial_23_ans:
        corrans += 1 
        deg_off_23 = 0
        print("Trial 23: Correct")
    else:
        deg_off_23 = abs(trial_23_corr2 - trial_23_ans) * 3     
        print("Trial 23: Incorrect. " + str(deg_off_23) + " degrees off") 

trial_24_1 = key_list24.count('1')
trial_24_2 = key_list24.count('2')
trial_24_corr1 = 12
trial_24_corr2 = 18
if trial_24_1 > trial_24_2:
    trial_24_ans = trial_24_1 - trial_24_2
    if trial_24_corr1 == trial_24_ans:
        corrans += 1
        deg_off_24 = 0
        print("Trial 24: Correct")
    else:
        deg_off_24 = abs(trial_24_corr1 - trial_24_ans) * 6     
        print("Trial 24: Incorrect. " + str(deg_off_24) + " degrees off") 
else:
    trial_24_ans = trial_24_2 - trial_24_1
    if trial_24_corr2 == trial_24_ans:
        corrans += 1 
        deg_off_24 = 0
        print("Trial 24: Correct")
    else:
        deg_off_24 = abs(trial_24_corr2 - trial_24_ans) * 6     
        print("Trial 24: Incorrect. " + str(deg_off_24) + " degrees off") 
     
print("Total correct: " + str(corrans) + " out of 24")
    
deg_off_list = []
if deg_off_1 > 0:
    deg_off_list.append(deg_off_1)
if deg_off_2 > 0:
    deg_off_list.append(deg_off_2)
if deg_off_3 > 0:
    deg_off_list.append(deg_off_3)
if deg_off_4 > 0:
    deg_off_list.append(deg_off_4)
if deg_off_5 > 0:
    deg_off_list.append(deg_off_5)
if deg_off_6 > 0:
    deg_off_list.append(deg_off_6)
if deg_off_7 > 0:
    deg_off_list.append(deg_off_7)
if deg_off_8 > 0:
    deg_off_list.append(deg_off_8)
if deg_off_9 > 0:
    deg_off_list.append(deg_off_9)
if deg_off_10 > 0:
    deg_off_list.append(deg_off_10)
if deg_off_11 > 0:
    deg_off_list.append(deg_off_11)
if deg_off_12 > 0:
    deg_off_list.append(deg_off_12)
if deg_off_13 > 0:
    deg_off_list.append(deg_off_13)
if deg_off_14 > 0:
    deg_off_list.append(deg_off_14)
if deg_off_15 > 0:
    deg_off_list.append(deg_off_15)
if deg_off_16 > 0:
    deg_off_list.append(deg_off_16)
if deg_off_17 > 0:
    deg_off_list.append(deg_off_17)
if deg_off_18 > 0:
    deg_off_list.append(deg_off_18)
if deg_off_19 > 0:
    deg_off_list.append(deg_off_19)
if deg_off_20 > 0:
    deg_off_list.append(deg_off_20)
if deg_off_21 > 0:
    deg_off_list.append(deg_off_21)
if deg_off_22 > 0:
    deg_off_list.append(deg_off_22)
if deg_off_23 > 0:
    deg_off_list.append(deg_off_23)
if deg_off_24 > 0:
    deg_off_list.append(deg_off_24)    
avgdeg = round(sum(deg_off_list) / len(deg_off_list), 2)
print("Avg degrees off: " + str(avgdeg))

#print list
print("Task durations for vector file:")
newlist = [round(float(i),2) for i in rt]
print(' '.join(str(x) for x in newlist))

#set up difficulty list
#difficulty = [1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 1.5, 1.6, 3.6, 2.5, 1.7, 2.6, 2.7, 1.8, 3.7, 3.8, 2.8]

#sort and print
#rt = numpy.array(rt)
#difficulty = numpy.array(difficulty)
#inds = difficulty.argsort()
#sortedRT = rt[inds]
#print(''.join(sortedRT))
