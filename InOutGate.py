"""
Authors: Marco Pipoly
University of Iowa,
Iowa City, IA
Hwang Lab, Dpt. of Psychological and Brain Sciences
As of Mar. 09, 2020:

Office:355N PBSB
Office Phone:319-467-0610
Fax Number:319-335-0191
Lab:355N

Lab Contact:
Web - https://kaihwang.github.io/
Email (Lab Director) - kai-hwang@uiowa.edu

This task is an adaptation of a task first published in:
https://www.sciencedirect.com/science/article/pii/S0896627314000063
Neuron.2014."Corticostriatal Output Gating during Selection from Working Memory"
"""

from psychopy import gui, visual, core, data, event, clock # import these function
from psychopy.hardware import keyboard # import new keyboard for reaction time
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy.info import RunTimeInfo # grab this for a trial tracker

import numpy as np # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import random
from random import choice as randomchoice
import os  # handy for system and file path related functions
import sys  # to get file system encoding
import glob # this pulls files in directories to create Dictionaries/Str
import pandas as pd #Facilitates data structure and analysis tools. prepend 'np.'
import pyglet as pyg
import copy #Incorporated for randomization of stimuli
import csv #for export purposes and analysis

#-----------Notes on Script Initiation----------
#This script calls on the directory it is housed in
#as well as the folder containing the correct outputs
#Ensure this is addressed appropriatley before running the script

#-----------Change Directory------
# Ensure that relative paths start from the same directory as this script

_thisDir = os.path.dirname(os.path.abspath(__file__)) # __file__ = ~/Your_Directory/Task_Folder/InOutGate.py
# __file__ is executed when a module is called within a *.py file
os.chdir(_thisDir) # Make sure we are in the directory the script is housed in


# Store infor about experiment and participant in each session
expName = 'InOutGate' # Will appear in documentation for later input/output
expInfo= {'Block': '001', 'Participant':'000', 'Sex? input (M/F)':'', 'Age':'', 'MRI/Behavior? (M/B)':'B'} # Dicionary keys for dlg input

#----------------setup windows and display objects--------
##### Setup the display Window, make sure the size is functional with your computer specs
win = visual.Window(
    size=([1680, 1050]), pos=[55,55], fullscr=False, screen=0,
    allowGUI=False, allowStencil=False, units='deg',
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)

#-------------------- Add multiple shutdown keys "at once"---------------------#
for key in ['q', 'escape']:
    # This for loop goes through the list=[] strings
    event.globalKeys.add(key, func=core.quit)
    # "key" variable now corresponds to keyboard keys
    # 'q' and 'esc' for task termination at any time

# Make sure to adjust window and monitor parameters per computer used
#not doing this will affect stimulus presentation among other things

# ---------- Calculating Keyboard and Window related Metrics ----------#
kb = keyboard.Keyboard() # Create a Psychtool Box Object
win.recordFrameIntervals=True # To trouble shoot and help record window frames
# store frame rate of monitor, if we can measure it
expInfo['frameRate'] = win.getActualFrameRate() # Add frame rate column
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so default 60 Hz

#----------------Setup While Loop to not allow Coninuation if Sex or Age are Incorrect--------

expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName # Add experiment name slot

# 'Notice' to address glitchy mouse cursor compatibility issues
Notice = visual.TextStim(win=win, name='Notice',
    text=u'Howdy, a dialog box will present shortly.\nIf a mouse cursor issue presents,\n use the "tab" key to change entry boxes',
    font=u'Arial', units='deg',
    pos=(0, 0), height=1, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# This works well on mac laptops of similar shape, set to false for outside users
# The purpose of this was to mitigate issues with some screen setting not
# aligning well with the dialog box with/without full screen set on/off
Notice.draw() # Draw the notice described above
win.flip() # Flip the window to reveal notice
core.wait(5) # Provide adequate time for a person to read the information

win.fullscr=False # Shut down fullscreen to facilitate dialog box use
win.winHandle.minimize() # Now minimize the screen
win.flip() # Flip window


# ----------------- This while loop runs to check two types of input age and sex
v = True # Variable for validation
while v:
    # A note on this: blocks are added each run of the script
    dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    # 'dlg' Gui grabs the dictionary to create a pre-experiment info deposit object
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName # Creating experiment name slot
    #----------------Setup Demographics Input Check--------------#
    age = int(expInfo['Age']) # Flip to integer type
    #Below if checks input for age and sex is valid
    if expInfo['Sex? input (M/F)']=='M':
        print('correct sex input')
        v = False # Flips value to false for validity
    elif expInfo['Sex? input (M/F)']=='F':
        print('correct sex input')
        v = False # Flips value to false for validity
    else:
        v = True # flips value to True, continue loop
        print('invalid sex input')
    # Below checks the correct integer was provided
    # Integer must be between 17 and 101 (so 18-100)
    if age > 17 and (age < 101):
        print('correct age')
        v = False # flips vaue to false
    else:
        print('invalid age, must be two digits between 18-100')
        v = True # Flips value to true

# this resets screen parameters post shut down for gui dialog box use
win.winHandle.maximize() # Resent to fullscreen
win.winHandle.activate() # activate the window again
win.fullscr = False # Officiate fullscreen/or remain off
win.flip() # flip to make it main again

#-------------------- Dependent on if Dialog Box 'M' (MRI) or 'B' (behavioral) was selected ----------------------#
if expInfo['MRI/Behavior? (M/B)']=='M':
    # Below is a function designed to work with pre-written ITIs
    # Located in an MRI folder **** Not included due to current lack of MRI access
    for i in ITI_rand_file:
        t=i.split('\n')
        t=t[0]
        ITI_list.append(float(t))

    def make_ITI(num_trials):
        ITI=ITI_list[num_trials]
        return ITI
    # Below function will be called each Experiment
    # num_trials is assigned value later
    def make_ITI(num_trials):
        if isinstance(num_trials, int) == True:
            ITI=np.random.choice([1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]) # numpy randomly grabs a value
            # ITI refers to a "jitter" to prevent anticipatory effects
            # The random value between 1-2 seconds is returned
            return ITI
        else:
            print('Error: Input of Jitter is not integer')

    mri_key='0' # key for MRI if session could be tested
    real_Total_trials = 32 # Number of trials per experiment block
    left_key='1' # for left response
    right_key='1' # for right response
    Wrong_left = '0' # Key code for wrong presses
    Wrong_right = '0' # key code for wrong presses
    # Rename and create path for behavioral experiment output
    thisDir_save=_thisDir # Readdress path link for later specificity
    filename = (thisDir_save+'/Data/'+'{0}_{1}_{2}_{3}').format(expInfo['Participant'], expInfo['Block'],expName, expInfo['date'])

    num_blocks=int(4) # The number of blocks
    num_trials=int(32) # the number of trials

    Cue_Time = .5 # Cue presentation time suring task trials
    Pic_Time = .5 # duration of task stimuli
    Response_Time = 1.5 # Response time during answer window
    refresh_rate=60 # refresh rate

elif expInfo['MRI/Behavior? (M/B)']=='B':

    # Below function will be called each behavioral only experiment
    # num_trials is assigned value later
    def make_ITI(num_trials):
        # here we check input is an integer
        if isinstance(num_trials, int) == True:
            ITI=np.random.choice([1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]) # numpy randomly grabs a value
            # ITI refers to a "jitter" to prevent anticipatory effects
            # The random value between 1-2 seconds is returned
            return ITI
        else:
            print('Error: Input of Jitter is not integer')

    mri_key='1' # key for mri identitity
    real_Total_trials = 32 # Number of trials per experiment block
    left_key='1' # for left response
    right_key='1' # for right response
    Wrong_left = '0' # Key code for wrong presses
    Wrong_right = '0' # key code for wrong presses
    # Rename and create path for behavioral experiment output
    thisDir_save=_thisDir # Readdress path link for later specificity
    filename = (thisDir_save+'/Data/'+'{0}_{1}_{2}_{3}').format(expInfo['Participant'], expInfo['Block'],expName, expInfo['date'])

    num_blocks=int(4) # number of blocks
    num_trials=int(32) # number of trials

    Cue_Time = .5 # Cue presentation time suring task trials
    Pic_Time = .5 # duration of task stimuli
    Response_Time = 1.5 # Response time during answer window
    refresh_rate=60 # refresh rate

else:
    # Will print if there is an error at this step
    print('ERROR: No Experiment Type Provided in Dialog Box Section MRI/Behavior? (M/B)')
    core.quit()


# ***** This will be for CSV initiation to record task responses
# This will be later appended to trial by trial
def makeCSV(filename, thistrialDict, num_trials):
    with open(filename+'.csv', mode='w') as our_data:
         ExpHead=thistrialDict[i].keys() # grabs column headers
         writer=csv.DictWriter(our_data,fieldnames=ExpHead)
         writer.writeheader() #writes in for csv
         for n in range(i+1):
            writer.writerow(thistrialDict[n]) # writes a new line into dictionary

#-------------------- Initiation of Task Visual Variables ---------------------#

# This is the welcome statement
Welc = visual.TextStim(win=win, name='Welc',
    text=u'Welcome to the working memory gating task!',
    units='deg',
    font=u'Arial',
    pos=(0, 0), height=1, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

##### Appears after satisfactory practice session
# This preps participant for coming task
Ready_Check = visual.TextStim(win=win, name='Ready_Check',
    text=u'You are now about to begin the task. \n\nGet Ready \n\nPress Any Key to Continue',
    font=u'Arial', alignVert='center', units='deg',
    pos=(0, 0), height=1, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

##### Central fixations
# Sets up fixation cross
Fix_Cue = visual.TextStim(win=win, name='Fix_Cue',
    text=u'+', units='deg',
    font=u'Arial',
    pos=(0, 0), height=5, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

##### Initialize stim paths
# Sets up numerical set for each orimary cue

# Control first trials have number 1
CF_Cue = visual.TextStim(win=win, name='CF_Cue',
    text=u'1', units='deg',
    font=u'Arial',
    pos=(0, 0), height=5, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Control last trials have number 2
CL_Cue = visual.TextStim(win=win, name='CL_Cue',
    text=u'2', units='deg',
    font=u'Arial',
    pos=(0, 0), height=5, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Global cue trials have number 3
Global_Cue = visual.TextStim(win=win, name='Global_Cue',
    text=u'3', units='deg',
    font=u'Arial',
    pos=(0, 0), height=5, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Sets up directional idicators the letter L and R for response window
L = visual.TextStim(win=win, name='L',
    text=u'L', units='deg',
    font=u'Arial',
    pos=(0, 0), height=3, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

R = visual.TextStim(win=win, name='R',
    text=u'R', units='deg',
    font=u'Arial',
    pos=(0, 0), height=3, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

#-------------------- The below creates functions and variables for trial number check----------#

#### hiearchical cue trees
#
#			     CF                         CL                      # pre-cue and retro cue
#			/	      \	                /       \
#	   Fractal1      Fractal2      Shapes         Shapes               # stimuli grouping by type
#
#             Global_CF                  Global_CL                  # pre-cue and retro cue
#           /          \                /          \
#   Fractal1,          Fractal2,      Fractal1,      Fractal2,
#      Shapes          Shapes             Shapes        Shapes    # stimuli grouping example

# Trial types may appear as:
# 1 = Respond to fractal position only position
# 2 = Respond to shape position only position
# 3 = Respond to specific shape & fractal pairing position

# function below grabbed and slightly edited from:
# https://thispointer.com/python-find-duplicates-in-a-list-with-frequency-count-index-positions/
def getDuplicatesWithCount(listOfElems=''):
    ''' Get frequency count of duplicate elements in the given list '''
    if isinstance(listOfElems, list) == True:
        dictOfElems = dict() # Create empty dicionary for trial type frequency organization
        # Iterate over each element in list
        for elem in listOfElems:
            # Interates through the list of elements, our case string types
            if elem in dictOfElems:
                # if the given string does exist, it increments the value by 1 (how it counts)
                dictOfElems[elem] += 1
            else:
                # if the given string type does not exist, it inputs with a dictionary key value of 1
                dictOfElems[elem] = 1
        # Filter key-value pairs in dictionary. Keep pairs whose value is greater than 1 i.e. only duplicate elements from list.
        dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}
        # Returns a dict of duplicate elements and their frequency count
        return dictOfElems
    else:
        print('Error: did not feed in a list')

condition_list=[] # Create an empty list to fill dynamically
for n in np.arange(num_trials/4):
    # Here n represents each float number
    for cond_name in ['Global_CF','Global_CL','CL','CF']:
        condition_list.append(cond_name) # Each element is slapped in a list
        condition_list_scrambled=np.random.permutation(condition_list)
        #the list is scrambled to get 4 * 8
        
condition_list_scrambled = list(condition_list_scrambled) # Convert to list for later input
Even_trial_chk = getDuplicatesWithCount(condition_list_scrambled) # Make sure there are 8 per type
Trial_order = list(condition_list_scrambled) # Create mixed trial type list (Double check)
num_trial_types=len(Even_trial_chk.keys()) # Check the number of trial types
Freq_Count=int(num_trials/num_trial_types) # Count the number of trials per trial type

# Following if statement continues if all trial types are even
# The following is necessary for successful executtion of this task
if Even_trial_chk['CF'] == Freq_Count & Even_trial_chk['Global_CL'] == Freq_Count & Even_trial_chk['Global_CL'] == Freq_Count & Even_trial_chk['CL'] == Freq_Count:
    print(True) # if correct
else:
    print('Error: Check whether even number of trials per trial type occurred')
    core.quit() # if incorect

#Dictionaries and the corresponding file paths
direc = os.getcwd()+'/InOutGate_Stim/' #_thisDir #'/Users/mpipoly/Desktop/Psychopy/localizer_stim/' #always setup path on the fly in case you switch computers
Frac_etx = 'Fractal_BW_Duo/*.png' # file location for fractal pictures
CircDia_ext = 'Circle_Diamond_BW_Duo/*.jpeg' # file location for diamond/circle pictures
frac_list = glob.glob(direc + Frac_etx) # slap together *.png before loading
circDi_list = glob.glob(direc + CircDia_ext) # slap together *.png before loading

Img_frac = {} # For loaded Fractal images
Img_circDi = {} # For loaded shape imgs
Pic_order_Loaded = {'Fractal':[],'CircDi':[]} # For ranom path images

num_trial_stim = 34 # create two more for pulling stim in response windows


# The following script loads image stim files int two image stim object lists
for i in range(num_trial_stim):
    Pic_order_Loaded['Fractal'].append(random.choice(frac_list)) # grab image stims in unpredictable order
    Pic_order_Loaded['CircDi'].append(random.choice(circDi_list)) # grab image stims in unpredictable order
    # below loads them in an inpredictable order
    Img_frac[i] = visual.ImageStim(win=win, size=[15,15], image=Pic_order_Loaded['Fractal'][i])
    Img_circDi[i] = visual.ImageStim(win=win, size=[15,15], image=Pic_order_Loaded['CircDi'][i])

#------------------------------------------------------

# Setup Stim Trials ********************************************************

Cue_Types = ['frac','circDi'] # cue types to mix for match
Trial_dict = {} # create empty dictionary for trial handeling

#Create a trial dictionary for comparison to initiate during task
# Finished product will have
for i in range(num_trials):
    Trial_dict[i] = {} # empty dictionary with numerical key
    Trial_dict[i][condition_list_scrambled[i]] = {} # Empty nested dictionary
    Trial_dict[i][condition_list_scrambled[i]]['cue1'] = random.choice(Cue_Types) # Grab randomly from list
    # Create alternatives from random order grabbing
    if Trial_dict[i][condition_list_scrambled[i]]['cue1'] == 'frac':
        Trial_dict[i][condition_list_scrambled[i]]['cue2'] = 'circDi'
    elif Trial_dict[i][condition_list_scrambled[i]]['cue1'] == 'circDi':
        Trial_dict[i][condition_list_scrambled[i]]['cue2'] = 'frac'

# Creat function to ensure stimuli are not repeats in responsw window

# --------- While loop for randomizing stim response types ---------#

#This function requires two seperate image object lists loaded using psychopy.

def CheckImageStim(Frac_Pic,circDi_pic):
    ''' Get a correct compliment of image object from assortment for response
    selection. Take two image stim object lists in order. Frac_Pic = Fractal
    Vistual.Stim Object list, circDi_pic = Shape Vistual.Stim Object list'''
    t = True # Valid
    while t:
        e = True # Valid
        d = True # Valid
        s = random.choice(range(len(circDi_pic)-i)) # Select random image stim
        if circDi_pic[i] == circDi_pic[i+1]:
            while d:
                s = random.choice(range(len(circDi_pic)-i)) # Select random image stim
                try:
                    circDi_pic[i+s] == circDi_pic[i]
                    # If Above is true and the same
                    d = True # Continue while loop
                except circDi_pic[i+s] != circDi_pic[i]:
                    d = False # Kill this while loop
        elif Frac_Pic[i] == Frac_Pic[i+1]:
            while d:
                s = random.choice(range(len(circDi_pic)-i)) # Select random image stim
                try:
                    Frac_Pic[i+s] == Frac_Pic[i]
                    # If Above is true and the same
                    e = True # Continue while loop
                except Frac_Pic[i+s] != Frac_Pic[i]:
                    e = False # Kill this while loop
        elif (circDi_pic[i] != circDi_pic[i+s]) & (Frac_Pic[i] != Frac_Pic[i+s]):
            e = False
            d = False
            if (d == False) & (e == False):
                # If Above is true and the same
                Frac_Pic = Frac_Pic[i+s] # reassign new stim for response
                circDi_pic = circDi_pic[i+s] # reassign new stim for response
                t = False # Kill this while loop
                return Frac_Pic, circDi_pic # Returns these two values
            else:
                t = True # Continue while loop
                print('ValueError: Issue with Input. Check that two seperate visual Stim objects were given')

#### Setting up a global clock to track initiation of experiment to end
Time_Since_Run = core.MonotonicClock()  # to track the time since experiment started, this way it is very flexible compare for whole block responses
##### Welcome and pre-task trial stims
Welc.draw() # Draws wealcome message
win.flip() # Window flips to revieal stimuli
event.waitKeys(maxWait=3) # waits about 3 seconds
Ready_Check.draw() # draws ready check message
win.flip() # Window flips to revieal stimuli
event.waitKeys() # wait for any key press

Output_Dictionary = {} # Create empty dictionary
for i in range(num_trials):
    kb.clearEvents() # Clear Key presses
    kb.clock.reset() # Reset clock for trial time stamp
    Output_Dictionary[i] = {} # add slots for this dictionary
    ITI = make_ITI(num_trials) # run jitter ITI function
    subRespso=[] # create empty list
    Fix_Cue.draw() # Fixation cross draw
    win.flip() # Window flips to revieal stimuli

    #Make sure the stimulus position and size is correct
    Img_circDi[i].size = ([15,15]) # Current stim size corrected
    Img_frac[i].size = ([15,15]) # Current size stim corrected
    Img_circDi[i].pos = (0,0) # Current position stim corrected
    Img_frac[i].pos = (0,0) # Current position stim corrected

    if condition_list_scrambled[i] == 'CL':
        if Trial_dict[i]['CL']['cue1'] == 'frac':
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Stim 1 is drawn below
            Img_frac[i].draw() # Stim 1 Displayed
            Photo_Prez_1=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Stim 2 is drawn below
            Img_circDi[i].draw() # Stim 2 Displayed
            Photo_Prez_2=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Cue is drawn below
            CL_Cue.draw() # Cue Displayed
            Cue_Prez_T=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Cue_Time) # Wait time for cue window
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Answer Options Checked/Adjusted for Displayed
            Frac_Pic, circDi_pic = CheckImageStim(Img_frac,Img_circDi) # Pump main lists of imge objects
            Img_circDi[i].size = ([15/2,15/2]) # Shift size smaller
            Img_frac[i].size = ([15/2,15/2]) # Shift size smaller
            Img_circDi[i].pos = (-20,-5)  # Arrange position left
            Img_frac[i].pos = (12,-5)  # Arrange position left
            # Checked response alternates
            circDi_pic.size = ([15/2,15/2]) # Shift size smaller
            Frac_Pic.size = ([15/2,15/2]) # Shift size smaller
            circDi_pic.pos = (20,-5) # Arrange position left
            Frac_Pic.pos = (-12,-5) # Arrange position right
            L.pos = (-20,3) # Arrange position left
            R.pos = (20,3) # Arrange position right
            #Draw response window options
            L.draw() # Indicates L for left press 1
            R.draw() # Indicates R for right press 0
            Img_frac[i].draw() # draws image stim
            Img_circDi[i].draw() # draws image stim
            circDi_pic.draw() # draws image stim
            Frac_Pic.draw() # draws image stim
            subRespo_win_T=Time_Since_Run.getTime() # Grabs the time response window appeared
            win.flip() # Window flips to revieal stimuli
            core.wait(Response_Time) # Wait time for response
            # Below if statement captures whether the response was correct or not
            if Trial_dict[i]['CL']['cue1'] == 'frac':
                corr_resp=left_key # In this case, it will equal 1
            else:
                corr_resp=Wrong_right # In this case it will equal 0
        elif Trial_dict[i]['CL']['cue1'] == 'circDi':
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Cue 1 is drawn below
            Img_circDi[i].draw() # Stim 1 Displayed
            Photo_Prez_1=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            Img_frac[i].draw() # Stim 2 Displayed
            Photo_Prez_1=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            CL_Cue.draw() # Cue Displayed
            Cue_Prez_T=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Cue_Time) # Wait time for cue window
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Answer Options Checked/Adjusted for Displayed
            Frac_Pic, circDi_pic = CheckImageStim(Img_frac,Img_circDi) # Pump main lists of imge objects
            Img_circDi[i].size = ([15/2,15/2]) # Shift size smaller
            Img_frac[i].size = ([15/2,15/2]) # Shift size smaller
            Img_circDi[i].pos = (-20,-5) # Over left and down left
            Img_frac[i].pos = (12,-5) # over right and down
            circDi_pic.size = ([15/2,15/2]) # Shift size smaller
            Frac_Pic.size = ([15/2,15/2]) # Shift size smaller
            circDi_pic.pos = (20,-5) # over right and down
            Frac_Pic.pos = (-12,-5) # over left and down
            L.pos = (-20,3) # over left and up
            R.pos = (20,3) # over right and up
            #Draw response window options
            L.draw() # draws image stim
            R.draw() # draws image stim
            Img_frac[i].draw() # draws image stim
            Img_circDi[i].draw() # draws image stim
            Frac_Pic.draw() # draws image stim
            circDi_pic.draw() # draws image stim
            subRespo_win_T=Time_Since_Run.getTime() # Grabs the time response window appeared
            win.flip() # Window flips to revieal stimuli
            core.wait(Response_Time) # Wait time for response
            # Below if statement captures whether the response was correct or not
            if Trial_dict[i]['CL']['cue1'] == 'circDi':
                corr_resp=left_key # In this case, it will equal 1
            else:
                corr_resp=Wrong_right # In this case, it will equal 0
    elif condition_list_scrambled[i] == 'CF':
        CF_Cue.draw() # draws image stim
        Cue_Prez_T=Time_Since_Run.getTime() # This grabs the stim presentation time
        win.flip() # Window flips to revieal stimuli
        core.wait(Cue_Time) # Wait time for cue window
        if Trial_dict[i]['CF']['cue1'] == 'frac':
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Stim 1 is drawn below
            Img_frac[i].draw() # Stim 1 Displayed
            Photo_Prez_1=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Stim 2 is drawn below
            Img_circDi[i].draw() # Stime 2 Displayed
            Photo_Prez_2=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Answer Options Checked/Adjusted for Displayed
            Frac_Pic, circDi_pic = CheckImageStim(Img_frac,Img_circDi) # Pump main lists of imge objects
            Img_circDi[i].size = ([15/2,15/2]) # Shift size smaller
            Img_frac[i].size = ([15/2,15/2]) # Shift size smaller
            Img_circDi[i].pos = (20,-5) # over right and down
            Img_frac[i].pos = (12,-5) # over right and down
            circDi_pic.size = ([15/2,15/2]) # Shift size smaller
            Frac_Pic.size = ([15/2,15/2]) # Shift size smaller
            circDi_pic.pos = (-20,-5) # over left and down
            Frac_Pic.pos = (-12,-5) # over right and down
            L.pos = (-20,3) # over left and up
            R.pos = (20,3) # over right and up
            #Draw response window options
            L.draw() # draws image stim
            R.draw() # draws image stim
            Img_frac[i].draw() # draws image stim
            Img_circDi[i].draw() # draws image stim
            Frac_Pic.draw() # draws image stim
            circDi_pic.draw() # draws image stim
            subRespo_win_T=Time_Since_Run.getTime() # Grabs the time response window appeared
            win.flip() # Window flips to revieal stimuli
            core.wait(Response_Time) # Wait time for response
            # Below if statement captures whether the response was correct or not
            if Trial_dict[i]['CF']['cue1'] == 'frac':
                corr_resp=right_key # In this case, it will equal 1
            else:
                corr_resp=Wrong_left # In this case, it will equal 0
        elif Trial_dict[i]['CF']['cue1'] == 'circDi':
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Cue 1 is drawn below
            Img_circDi[i].draw() # Stim 1 Displayed
            Photo_Prez_1=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Cue 2 is drawn below
            Img_frac[i].draw() # Stim 2 Displayed
            Photo_Prez_2=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Answer Options Checked/Adjusted for Displayed
            Frac_Pic, circDi_pic = CheckImageStim(Img_frac,Img_circDi) # Pump main lists of imge objects
            Img_circDi[i].size = ([15/2,15/2]) # Shift size smaller
            Img_frac[i].size = ([15/2,15/2]) # Shift size smaller
            Img_circDi[i].pos = (-20,-5) # left and down
            Img_frac[i].pos = (12,-5) # right and down
            circDi_pic.size = ([15/2,15/2]) # Shift size smaller
            Frac_Pic.size = ([15/2,15/2]) # Shift size smaller
            circDi_pic.pos = (20,-5) # right and down
            Frac_Pic.pos = (-12,-5) # right and down
            L.pos = (-20,3) # left and up
            R.pos = (20,3) # right and up
            #Draw response window options
            L.draw() # draws image stim
            R.draw() # draws image stim
            Img_frac[i].draw() # draws image stim
            Img_circDi[i].draw() # draws image stim
            Frac_Pic.draw() # draws image stim
            circDi_pic.draw() # draws image stim
            subRespo_win_T=Time_Since_Run.getTime() # Grabs the time response window appeared
            win.flip() # Window flips to revieal stimuli
            core.wait(Response_Time) # Wait time for response
            # Below if statement captures whether the response was correct or not
            if Trial_dict[i]['CF']['cue1'] == 'circDi':
                corr_resp=left_key # In this case, it will equal 1
            else:
                corr_resp=Wrong_right # In this case, it will equal 0
    elif condition_list_scrambled[i] == 'Global_CF':
        Global_Cue.draw()
        Cue_Prez_T=Time_Since_Run.getTime() # This grabs the stim presentation time
        win.flip() # Window flips to revieal stimuli
        core.wait(Cue_Time) # Wait time for cue window
        if Trial_dict[i]['Global_CF']['cue1'] == 'frac':
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Stim 1 is drawn below
            Img_frac[i].draw() # Stim 1 Displayed
            Photo_Prez_1=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Stim 2 is drawn below
            Img_circDi[i].draw() # Stime 2 displayed
            Photo_Prez_2=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Answer Options Checked/Adjusted for Displayed
            Frac_Pic, circDi_pic = CheckImageStim(Img_frac,Img_circDi) # Pump main lists of imge objects
            Img_circDi[i].size = ([15/2,15/2]) # Shift size smaller
            Img_frac[i].size = ([15/2,15/2]) # Shift size smaller
            Img_circDi[i].pos = (-20,-5) # left and down
            Img_frac[i].pos = (-12,-5) # left and down
            circDi_pic.size = ([15/2,15/2]) # Shift size smaller
            Frac_Pic.size = ([15/2,15/2]) # Shift size smaller
            circDi_pic.pos = (20,-5) # right and down
            Frac_Pic.pos = (12,-5) # right and down
            L.pos = (-20,3) # right and up
            R.pos = (20,3) # right and up
            #Draw response window options
            L.draw() # draws image stim
            R.draw() # draws image stim
            Img_frac[i].draw() # draws image stim
            Img_circDi[i].draw() # draws image stim
            Frac_Pic.draw() # draws image stim
            circDi_pic.draw() # draws image stim
            subRespo_win_T=Time_Since_Run.getTime() # Grabs the time response window appeared
            win.flip() # Window flips to revieal stimuli
            core.wait(Response_Time) # Wait time for response
            # Below if statement captures whether the response was correct or not
            if Trial_dict[i]['Global_CF']['cue1'] == 'frac':
                corr_resp=left_key # In this case, it will equal 1
            else:
                corr_resp=Wrong_right # In this case, it will equal 0
        elif Trial_dict[i]['Global_CF']['cue1'] == 'circDi':
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Stim 1 is drawn below
            Img_circDi[i].draw() # Stim 1 Displayed
            Photo_Prez_1=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Stim 2 is drawn below
            Img_frac[i].draw() # Stim 2 Displayed
            Photo_Prez_2=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Answer Options Checked/Adjusted for Displayed
            Frac_Pic, circDi_pic = CheckImageStim(Img_frac,Img_circDi) # Pump main lists of imge objects
            Img_circDi[i].size = ([15/2,15/2]) # Shift size smaller
            Img_frac[i].size = ([15/2,15/2]) # Shift size smaller
            Img_circDi[i].pos = (20,-5) # right and down
            Img_frac[i].pos = (12,-5) # right and down
            circDi_pic.size = ([15/2,15/2]) # Shift size smaller
            Frac_Pic.size = ([15/2,15/2]) # Shift size smaller
            circDi_pic.pos = (-20,-5) # left and down
            Frac_Pic.pos = (-12,-5) # left and down
            L.pos = (-20,3) # left and up
            R.pos = (20,3) # right and up
            #Draw response window options
            L.draw() # draws image stim
            R.draw() # draws image stim
            Img_frac[i].draw() # draws image stim
            Img_circDi[i].draw() # draws image stim
            Frac_Pic.draw() # draws image stim
            circDi_pic.draw() # draws image stim
            subRespo_win_T=Time_Since_Run.getTime() # Grabs the time response window appeared
            win.flip() # Window flips to revieal stimuli
            core.wait(Response_Time) # Wait time for response
            # Below if statement captures whether the response was correct or not
            if Trial_dict[i]['Global_CF']['cue1'] == 'circDi':
                corr_resp=right_key # In this case, it will equal 1
            else:
                corr_resp=Wrong_left # In this case, it will equal 0
    elif condition_list_scrambled[i] == 'Global_CL':
        if Trial_dict[i]['Global_CL']['cue1'] == 'frac':
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Stim 1 is drawn below
            Img_frac[i].draw() # Stim 1 Displayed
            Photo_Prez_1=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Stim 2 is drawn below
            Img_circDi[i].draw() # Stime 2 Displayed
            Photo_Prez_2=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Cue is drawn below
            Global_Cue.draw() # cue is drawn
            Cue_Prez_T=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Cue_Time) # Wait time for cue window
            # Answer Options Checked/Adjusted for Displayed
            Frac_Pic, circDi_pic = CheckImageStim(Img_frac,Img_circDi) # Pump main lists of imge objects
            Img_circDi[i].size = ([15/2,15/2]) # Shift size smaller
            Img_frac[i].size = ([15/2,15/2]) # Shift size smaller
            Img_circDi[i].pos = (-20,-5) # left and down
            Img_frac[i].pos = (-12,-5) # left and down
            circDi_pic.size = ([15/2,15/2]) # Shift size smaller
            Frac_Pic.size = ([15/2,15/2]) # Shift size smaller
            circDi_pic.pos = (20,-5) # right and down
            Frac_Pic.pos = (12,-5) # right and down
            L.pos = (-20,3) # left and up
            R.pos = (20,3) # right and up
            #Draw response window options
            L.draw() # draws image stim
            R.draw() # draws image stim
            Img_frac[i].draw() # draws image stim
            Img_circDi[i].draw() # draws image stim
            Frac_Pic.draw() # draws image stim
            circDi_pic.draw() # draws image stim
            subRespo_win_T=Time_Since_Run.getTime() # Grabs the time response window appeared
            win.flip() # Window flips to revieal stimuli
            core.wait(Response_Time) # Wait time for response
            # Below if statement captures whether the response was correct or not
            if Trial_dict[i]['Global_CL']['cue1'] == 'frac':
                corr_resp=left_key # In this case, it will equal 1
            else:
                corr_resp=Wrong_right # In this case, it will equal 0
        elif Trial_dict[i]['Global_CL']['cue1'] == 'circDi':
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Stim 1 is drawn below
            Img_circDi[i].draw()
            Photo_Prez_1=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Stim 2 is drawn below
            Img_frac[i].draw() # Stim 2 Displayed
            Photo_Prez_2=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Pic_Time) # Stimulus presentation time
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Cue is drawn below
            Global_Cue.draw() # Cue is draw
            Cue_Prez_T=Time_Since_Run.getTime() # This grabs the stim presentation time
            win.flip() # Window flips to revieal stimuli
            core.wait(Cue_Time) # Wait time for cue window
            Fix_Cue.draw() # Fixation Cross Displayed
            win.flip() # Window flips to revieal stimuli
            core.wait(ITI) # Jittered time between 1-2 sec
            # Answer Options Checked/Adjusted for Displayed
            Frac_Pic, circDi_pic = CheckImageStim(Img_frac,Img_circDi) # Pump main lists of imge objects
            Img_circDi[i].size = ([15/2,15/2]) # Shift size smaller
            Img_frac[i].size = ([15/2,15/2]) # Shift size smaller
            Img_circDi[i].pos = (20,-5) # Shift location right and down
            Img_frac[i].pos = (12,-5) # Shift location right and down
            circDi_pic.size = ([15/2,15/2]) # Shift size smaller
            Frac_Pic.size = ([15/2,15/2]) # Shift size smaller
            circDi_pic.pos = (-20,-5) # Shift location down and left
            Frac_Pic.pos = (-12,-5)# Shift location down and left
            L.pos = (-20,3)# Shift location left and up
            R.pos = (20,3) # Shift location right and up
            #Draw response window options
            L.draw() # Draws the letter
            R.draw() #  Draws letter
            Img_frac[i].draw() # draws image
            Img_circDi[i].draw() # draws image
            Frac_Pic.draw() # draws image
            circDi_pic.draw() # draws image
            subRespo_win_T=Time_Since_Run.getTime() # Grabs the time response window appeared
            win.flip() # Window flips to revieal stimuli
            core.wait(Response_Time) # Wait time for response
            # Below if statement captures whether the response was correct or not
            if Trial_dict[i]['Global_CL']['cue1'] == 'circDi':
                corr_resp=right_key # In this case, it will equal 1
            else:
                corr_resp=Wrong_left # In this case, it will equal 0

    # This grabs the response
    subRespo=kb.getKeys(keyList=[left_key,right_key,Wrong_left,Wrong_right], waitRelease=True, clear=True)

    # This if statement categorizes and slots the reaction time, whether the response was made
    # and whether the response was correct
    if not subRespo:
        trial_Corr=-1 # -1 represents no subject response
        rt='none' # No reaction time for subject response
        subKEY='none' # No key was pressed
    elif subRespo[0].name == '1':
        trial_Corr=1 # Trial was correct
        rt=subRespo[0].rt # Reaction time
        subKEY=subRespo[0].name # key pressed name
    elif subRespo[0].name == '0':
        trial_Corr=0 # Trial was correct
        rt=subRespo[0].rt # Reaction time
        subKEY=subRespo[0].name # key pressed name
    else:
        print('Something Wrong with Subject Response')
        core.quit() # quits the trial if issue occurs

    # These are the categories and slots for the *.csv that will be produced

    Output_Dictionary[i]['Time_Since_Run_subRespo_Window']=subRespo_win_T # When did the response window appear?
    Output_Dictionary[i]['Time_Since_Run_Photo_Prez']=Photo_Prez_1 # When did the image cue1 stim appear?
    #Output_Dictionary[i]['Time_Since_Run_Photo_Prez']=Photo_Prez_2 # When did the image cue2 stim appear?
    Output_Dictionary[i]['Time_Since_Run_Cue_Prez']=Cue_Prez_T # When did the cue appear?
    Output_Dictionary[i]['trial_Corr']=trial_Corr # This is coded, 1, 0, and -1 where 1 is correct, 2 is wrong, -1 is no response
    Output_Dictionary[i]['rt']=rt # the reaction time since trial began
    Output_Dictionary[i]['What_Is_CorrResp']=corr_resp # Was this a correct response? 1 yes, 2 no
    Output_Dictionary[i]['Subject_Respo']=subKEY # What key was pressed 1 or 0
    Output_Dictionary[i]['num_trials']=i # what trial number is this? 0-31 (or 32 trials)
    Output_Dictionary[i]['block']=expInfo['Block'] # Which block is this?
    Output_Dictionary[i]['sub']=expInfo['Participant'] # Subject ID
    Output_Dictionary[i]['Cue_Type']=condition_list_scrambled[i] # What condition was it? CF, CL, Global_CF, Global_CL
    Output_Dictionary[i]['Stim1']=Trial_dict[i][condition_list_scrambled[i]]['cue1'] # What stim was first?
    Output_Dictionary[i]['Stim2']=Trial_dict[i][condition_list_scrambled[i]]['cue2'] # What stim was second?
    Output_Dictionary[i]['Frame Rate']=expInfo['frameRate'] # Get the screen refresh rate
    Output_Dictionary[i]['Sex']=expInfo['Age'] # Get the subjects age
    Output_Dictionary[i]['Age']=expInfo['Sex? input (M/F)'] # Get the sex of the subject


    win.flip() # Flips for refresh and wait before CSV is made
    core.wait(ITI) # randomly pick one from the range of ITIs
    makeCSV(filename=filename,thistrialDict=Output_Dictionary,num_trials=i) # Creates a new line in the csv
