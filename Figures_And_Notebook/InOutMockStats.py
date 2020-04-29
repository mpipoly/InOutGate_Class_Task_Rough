#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy.stats as stats
from scipy import mean, median
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import os
import sys
import re
import glob
import decimal


# In[2]:


# Subject files name path and identifiers

Import_Path = os.getcwd()+'/Data/' # Path to data hold
Blocks = ['001','002','003','004','005'] # Block numbers
Subjects = ['001','002','003','004','005'] # Subject numbers

get_ipython().system('cd /Users/marco/Desktop/InOutGate/Data # Uses shell tool display directory path')
get_ipython().system('ls /Users/marco/Desktop/InOutGate/Data # Uses Shell tool listing folder content')


# In[3]:


# Function to handle disproportionate arrays

def tolerant_mean(arrs):
    lens = [len(i) for i in arrs] # Creates a list of lengths
    arr = np.ma.empty((np.max(lens),len(arrs))) # Creates a mask of needed vector lengths
    arr.mask = True 
    for idx, l in enumerate(arrs):
        arr[:len(l),idx] = l # Returns indx = array value and l = index of array
    # Below returns the average and stadard deviation of re-structured array
    return arr.mean(axis = -1), arr.std(axis=-1) # returns an array of masked mean values and standard deviations


# In[48]:


# below is for general reaction time

sub = {} # Empty subject dictionary
end = '*.csv' # Path string ending
Accuracy = [] # Empty list for average scores
Numpy_List = [] # Empty list
New_Dictionary = {} # empty dictionary 

for s in Subjects[:1]:
    sub[s] = {} # Subject dictionary
    New_Dictionary[s] = {} # Empty nested dictionary
    for block in Blocks:
        sub[s][block] = {} # nested ditionary with key s and nested key block
        New_Dictionary[s][block] = {} # nested ditionary with key s and nested key block
        path_temp = glob.glob(Import_Path+s+'_'+block+'_InOutGate_2020_Apr_27_'+end) # grabs path
        sub[s][block] = pd.read_csv(path_temp[0]) # read in files and assign to dictionary
        Accuracy.append(sub[s][block]['trial_Corr'][:]) # grab values to calculate total accuracy
        New_Dictionary[s][block] = sub[s][block].loc[sub[s][block]['trial_Corr'] == 1] # isolate only correct trials
        Matrix = New_Dictionary[s][block].iloc[:,4].values # 
        Numpy_List.append(Matrix)

# Below is for general reaction time and accuracy  
Acc = np.mean(Accuracy) # average of values
New_Dictionary[s][block].iloc[:,4].values # Structure values in array
Reaction_Time_Array = np.asarray(Numpy_List) # Assign list and convert to array for later computations

Avg_and_Standard_Dev_rt = tolerant_mean(Reaction_Time_Array) # Create a weighted average and standard deviation
Avg_Rt = Avg_and_Standard_Dev_rt[0][:] # Array of reaction time
Avg_SD_rt = Avg_and_Standard_Dev_rt[1][:] # Array of standard deviation
Median_Acc = np.median(Avg_Rt) # Median of reaction time
avg = np.mean(Avg_Rt) # Average of weighted averages
SD = np.mean(Avg_SD_rt) # Average of weighted standard deviation

print('This is the accuracy of correct trial reaction time:', Acc)
print('This is the weighted average of correct trial reaction time:', avg)
print('This is the median of unweighted reaction times:', Median_Acc)
print('This is the standard deviation of weighted reaction times:', SD)


# In[66]:


#-------- Create a histogram of reaction times in correct trials

Made_array = np.asarray(Avg_Rt) # Switch all reaction time averaged to numpy array
plt.hist(Made_array)  # arguments are passed to np.histogram
plt.title("Histogram of overall Correct Trial Reaction Time") # Histogram Title

blue_patch = mpatches.Patch(color='blue', label='Reaction Time Freq data')
plt.legend(handles=[blue_patch])

plt.xlabel('Time Range in Sec') # Histogram x-label
plt.ylabel('Frequency of Range Captured') # Histogram y-label
plt.show() # reveals plot with above parameters
np.histogram(Made_array) # Output array reflects the frequency 


# In[6]:


# Example of output using the last block from subject 001
New_Dictionary[s]['001']


# In[7]:


# Permutations of 5 blocks to represent 5 subjects
# Will be achieved by multiplying the standard deviation to the average of all blocks permuted five times

permutaion_array_list_rt = [] # Empty list
New_rt_values_X_SD = [] # Empty list
Array_length = [] # Empty list
Subject_Dictionary_Rt = {} # Empty Dictionary
Subject_Dictionary_SD = {} # Empty Dictionary

for sub in Subjects[1:]:
    # This is subject loop
    Subject_Dictionary_Rt[sub] = {}  # Empty Nested Dictionary
    Subject_Dictionary_SD[sub] = {} # Empty Nested Dictionary
    for i in range(5):
        # This is block loop
        permutaion_array_list_rt.append(np.random.permutation(Reaction_Time_Array[i])) # Mix the digits in each array for subject 1
        Array_length.append(len(permutaion_array_list_rt[i])) # Create a list of each array length
        Temp_For_Loop = [Array_length[i]] # reassign singular value in list to temporary
        for number in Temp_For_Loop[:]:
            # This is length value loop
            empty_frame = np.empty([number,1]) # create empty array of permuted values vector length
            empty_frame2 = np.empty([number,1]) # create empty array of permuted values vector length
            # Fill values of permutation changes into new array
            for num_l in range(number): empty_frame2[num_l] = permutaion_array_list_rt[i][num_l] # Change data type
            for numl_1 in range(number): empty_frame[numl_1] = (int(float(Avg_SD_rt[numl_1])))*(int(float(permutaion_array_list_rt[i][numl_1]))) # Create element by element permuted and shifted values
            # Append these values for every loop (once)
            New_rt_values_X_SD.append(empty_frame) # Append permutation values into list
            permutaion_array_list_rt[i] = empty_frame2 # Append permutated reaction time values into nested dictionary
        # Shove newly created values into dictionary to join original below every block loop
        Subject_Dictionary_Rt[sub]=permutaion_array_list_rt[i] # for reaction time
        Subject_Dictionary_SD[sub]=New_rt_values_X_SD[i] # for reaction time X standard deviation computed values


temp = [] # Empty list
Original_rt = [] # Empty list
Original_SD = [] # Empty list
# This for loop adds real subject ones five blocks to the permuted value subjects
for i in range(5):
    # loop for number of blocks
    temp.append(Reaction_Time_Array[i]) # temporary list to extract reaction time
    Array_length.append(len(temp)) # append list by legnth
    Temp_real_data_loop = [Array_length[i]] # reassign singular value in list to temporary
    for num in Temp_real_data_loop[:]:
        empty_frame3 = np.empty([num,1]) # create empty frames
        empty_frame4 = np.empty([num,1]) # create empty frames
        for dip in range(num): empty_frame3[dip] = temp[i][dip] # change values into new frame
        for kip in range(num): empty_frame4[kip] = (int(float(Avg_SD_rt[kip]))) # change values into new rame by standard deviation
        Original_rt.append(empty_frame3) # append new values into list
        Original_SD.append(empty_frame4) # append new values into list

Subject_Dictionary_Rt.update({'001': Original_rt}) # Five Subjects worth of data reaction time
Subject_Dictionary_SD.update({'001': Original_SD}) # Five subjects worth of data standard deviation


# In[8]:


# Below produces values by task type for each block
sub = {} # Empty subject dictionary
end = '*.csv' # Path string ending
Accuracy = [] # Empty list for average scores
Numpy_List = [] # Empty list
Add_Dictionary = {} # empty dictionary 
Values_rt_dic = {} # empty dicionary to shove values in
Values_rt_dic = {} # empty dicionary to shove values in
List_CL = [] # Empty list for cue control last
List_CF = [] # Empty list for cue control first
List_GCL = [] # Empty list for cue global control last
List_GCF = [] # Empty list for cue global control first


# For loop to grab dataframe values by cue type: 
for s in Subjects[:1]:
    Add_Dictionary[s] = {} # Nested dictionary with key subject list value: '001' etc..
    for block in Blocks:
        # For loop of blocks
        Add_Dictionary[s][block] = {}
        path_temp = glob.glob(Import_Path+s+'_'+block+'_InOutGate_2020_Apr_27_'+end)
        Add_Dictionary[s][block] = pd.read_csv(path_temp[0])
        # Below grabs values by trial correct value 1 and cue type
        CL = Add_Dictionary[s][block].loc[(Add_Dictionary[s][block]['trial_Corr'][:]>0) & (Add_Dictionary[s][block]['Cue_Type']=='CL')]
        CF = Add_Dictionary[s][block].loc[(Add_Dictionary[s][block]['trial_Corr'][:]>0) & (Add_Dictionary[s][block]['Cue_Type']=='CF')]
        GCL = Add_Dictionary[s][block].loc[(Add_Dictionary[s][block]['trial_Corr'][:]>0) & (Add_Dictionary[s][block]['Cue_Type']=='Global_CL')]
        GCF = Add_Dictionary[s][block].loc[(Add_Dictionary[s][block]['trial_Corr'][:]>0) & (Add_Dictionary[s][block]['Cue_Type']=='Global_CF')]
        # Grabs only the reaction times from the truncated dataframes above
        # This pandas series then becomes an array
        CL = pd.Series(CL['rt'])
        CL = pd.Series.to_numpy(CL)
        CF = pd.Series(CF['rt'])
        CF = pd.Series.to_numpy(CF)
        GCL = pd.Series(GCL['rt'])
        GCL = pd.Series.to_numpy(GCL)
        GCF = pd.Series(GCF['rt'])
        GCF = pd.Series.to_numpy(GCF)
        # These arrays are then appended
        List_CL.append(CL) # pandas lists appended
        List_CF.append(CF) # pandas lists appended
        List_GCF.append(GCF) # pandas lists appended
        List_GCL.append(GCL) # pandas lists appended

List_Cue_Type_Data=[List_CL,List_CF,List_GCL,List_GCF] # create a list of panda lists lists


# In[9]:


# Here we will extract and permute data to create mirror subject blocks worth of each trial type
# The permuted values are multiplied by the array length from the masked standard deviation calculated above

Values_rt_dic = {} # Empty Dictionary
Values_rt_dic = {} # Empty Dictionary
lis_version = ['List_CL','List_CF','List_GCL','List_GCF'] # List for dictionary fills and calls

# THIS LOOP CREATES PREPPED DICTIONARIES FOR FOLLOWING LOOP
for name in lis_version:
    Values_rt_dic[name] = {}# Empty Dictionary
    Values_rt_dic[name] = {}# Empty Dictionary


# This loop will extract and create a comprehensive by cue typ set of data for each subject simulated and permuted
for lis in range(4):
    # Four lists of five cycled through
    Array_length = [] # Empty list for wiping
    permutaion_array_list_rt = [] # Empty list for wiping
    New_rt_values_X_SD = [] # Empty list for wiping
    for sub in Subjects:
        # Five subjects
        for i in range(5):
            # Five arrays in each list position
            permutaion_array_list_rt.append(np.random.permutation(List_Cue_Type_Data[lis][i])) # Mix the digits in each array for subject 1
            Array_length.append(len(permutaion_array_list_rt[i])) # Create a list of each array length
            Temp_For_Loop = [Array_length[i]] # reassign singular value in list to temporary
            for number in Temp_For_Loop[:]:
                empty_frame = np.empty([number,1]) # Empty array of shape array length, 1
                empty_frame2 = np.empty([number,1]) # Empty array of shape array length, 1
                for snip in range(number): empty_frame2[snip] = int(float(permutaion_array_list_rt[i][snip]))
                for pip in range(number): empty_frame[pip] = int((int(float(Avg_SD_rt[pip])))*(int(float(permutaion_array_list_rt[i][pip]))))
                New_rt_values_X_SD.append(empty_frame)
            if lis == 0:
                # 5 subjects of 5 blocks modeled after my data                    
                Values_rt_dic['List_CL']=np.asarray(New_rt_values_X_SD) 
            elif lis == 1:
                # 5 subjects of 5 blocks modeled after my data
                Values_rt_dic['List_CF']=np.asarray(New_rt_values_X_SD)
            elif lis == 2:
                # 5 subjects of 5 blocks modeled after my data
                Values_rt_dic['List_GCL']=np.asarray(New_rt_values_X_SD)
            elif lis == 3:
                # 5 subjects of 5 blocks modeled after my data
                Values_rt_dic['List_GCF']=np.asarray(New_rt_values_X_SD)
                
# This for loop creates averages for each subjects cue types
for name in lis_version:
    for averages in range(25):
        blk_add=Values_rt_dic[name][averages].sum() # sum values
        blk_add=int(blk_add) # shift values to integer )make sure of this to avoid error
        leng = len(Values_rt_dic[name][averages]) # Take the length original
        blk_avg=blk_add/leng # now calculate the average manually
        Values_rt_dic[name][averages]=blk_avg # Shove this value back into the nested dictionary
        


# In[10]:


#******* Calculating ANOVA scores ************#

df = pd.DataFrame( Values_rt_dic) # convert to a dataframe

# load packages to plot and view anaova results
import scipy.stats as stats
# stats f_oneway functions takes the groups as input and returns F and P-value
fvalue, pvalue = stats.f_oneway(df['List_CL'], df['List_CF'], df['List_GCL'], df['List_GCF'])
print(fvalue, pvalue)

# The p-value here is significat!!!!


# In[64]:


import seaborn as sns;
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import matplotlib.patches as mpatches

#ax = plt.subplots()
x = Values_rt_dic['List_CL'] # label for x - axis
y = Values_rt_dic['List_CF'] # label for y - axis
s = plt.scatter(Values_rt_dic['List_CL'],Values_rt_dic['List_CF']) # correlate these two values
blue_patch = mpatches.Patch(color='blue', label='Corr data') # labels for legend
plt.legend(handles=[blue_patch]) # Legend grabbing labels
plt.xlabel('Reaction Time Control First') # xlabel
plt.ylabel('Reaction Time Control Last') # ylabel
plt.title('Correlation Between Control First and Control Last Reaction Time') # title of graph
plt.show() # to reveal graph

print('Below is the Correlation and p-value') # will print set-up for following value
stats.pearsonr(Values_rt_dic['List_CL'],Values_rt_dic['List_CF']) # provides the correlation values


# In[65]:


# Import relevant packadges
import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression

X_CL = df.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
Y_CF = df.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column

linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X_CL,Y_CF)  # perform linear regression
Y_pred = linear_regressor.predict(X_CL)  # make predictions

blue_patch = mpatches.Patch(color='blue', label='Regression data') # labels for legend
plt.legend(handles=[blue_patch]) # grabs label setup for legend

plt.scatter(X_CL, Y_CF) # Create a scatterplot for regreassion line
plt.title('Control Last Predicts Control First Trials') # title of graph
plt.xlabel('Control Last') # title of x-bar
plt.ylabel('Control First') # title of y-bar
plt.plot(X_CL, Y_pred, color='red') # show line
plt.show() # reveal graph


# import more packadges
from sklearn.metrics import r2_score
r2 = r2_score(X_CL, Y_CF,multioutput='variance_weighted') # Grab this value 
print('This is the R2 Value:', r2) # print below

