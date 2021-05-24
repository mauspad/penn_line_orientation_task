#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on November 04, 2019, at 15:52
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y
        
Python version of the Penn Line Orientation Test, adapted for fMRI from Adobe Flash version available at https://penncnp.med.upenn.edu/

Citations:

Gur RC, Richard J, Hughett P, Calkins ME, Macy L, Bilker WB, Gur RE. A cognitive neuroscience-based computerized battery for efficient 
    measurement of individual differences: standardization and initial construct validation. Journal of Neuroscience Methods. 
    2010;187(2):254–262. doi:10.1016/j.jneumeth.2009.11.017

Moore TM, Reise SP, Gur RE, Hakonarson H, Gur RC. Psychometric Properties of the Penn Computerized Neurocognitive Battery. 
    Neuropsychology. 2014 doi:10.1037/neu0000093.

Moore, T. M., Scott, J. C., Reise, S. P., Port, A. M., Jackson, C. T., Ruparel, K., . . . Gur, R. C. (2015). Development of an 
    abbreviated form of the Penn Line Orientation Test using large samples and computerized adaptive test simulation. Psychological 
    Assessment, 27(3), 955-964. http://dx.doi.org/10.1037/pas0000102

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'PLOT'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\mauspad\\Desktop\\untitled.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
    
#hide mouse
your_mouse = event.Mouse(visible = False)

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "wait_for_scanner"
wait_for_scannerClock = core.Clock()
scanner_resp = keyboard.Keyboard()
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_01"
trial_01Clock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished = visual.TextStim(win=win, name='finished',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()
responses = visual.ImageStim(
    win=win,
    name='responses', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline = visual.Line(
    win=win, name='blueline',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=90, pos=(-11, 10),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline = visual.Line(
    win=win, name='redline',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=198, pos=(13, -4),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_02"
trial_02Clock = core.Clock()
instructions_2 = visual.TextStim(win=win, name='instructions_2',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_2 = visual.TextStim(win=win, name='finished_2',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()
responses_2 = visual.ImageStim(
    win=win,
    name='responses_2', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_2 = visual.Line(
    win=win, name='blueline_2',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=162, pos=(-14, -4),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_2 = visual.Line(
    win=win, name='redline_2',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=243, pos=(14, -4),
    lineWidth=3, lineColor=[1.000,1,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_03"
trial_03Clock = core.Clock()
instructions_3 = visual.TextStim(win=win, name='instructions_3',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_3 = visual.TextStim(win=win, name='finished_3',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()
responses_3 = visual.ImageStim(
    win=win,
    name='responses_3', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_3 = visual.Line(
    win=win, name='blueline_3',units='cm', 
    start=(-(1, 0)[0]/2.0, 0), end=(+(1, 0)[0]/2.0, 0),
    ori=261, pos=(11, 10),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_3 = visual.Line(
    win=win, name='redline_3',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=153, pos=(-11, -4),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_04"
trial_04Clock = core.Clock()
instructions_4 = visual.TextStim(win=win, name='instructions_4',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_4 = visual.TextStim(win=win, name='finished_4',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_4 = keyboard.Keyboard()
responses_4 = visual.ImageStim(
    win=win,
    name='responses_4', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_4 = visual.Line(
    win=win, name='blueline_4',units='cm', 
    start=(-(1, 0)[0]/2.0, 0), end=(+(1, 0)[0]/2.0, 0),
    ori=144, pos=(14, 10),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_4 = visual.Line(
    win=win, name='redline_4',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=261, pos=(-15, 9),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_05"
trial_05Clock = core.Clock()
instructions_5 = visual.TextStim(win=win, name='instructions_5',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_5 = visual.TextStim(win=win, name='finished_5',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_5 = keyboard.Keyboard()
responses_5 = visual.ImageStim(
    win=win,
    name='responses_5', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_5 = visual.Line(
    win=win, name='blueline_5',units='cm', 
    start=(-(1, 0)[0]/2.0, 0), end=(+(1, 0)[0]/2.0, 0),
    ori=90, pos=(15, -4),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_5 = visual.Line(
    win=win, name='redline_5',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=198, pos=(-15, -4),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_06"
trial_06Clock = core.Clock()
instructions_6 = visual.TextStim(win=win, name='instructions_6',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_6 = visual.TextStim(win=win, name='finished_6',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_6 = keyboard.Keyboard()
responses_6 = visual.ImageStim(
    win=win,
    name='responses_6', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_6 = visual.Line(
    win=win, name='blueline_6',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=228, pos=(-15, 9),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_6 = visual.Line(
    win=win, name='redline_6',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=102, pos=(15, 9),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_07"
trial_07Clock = core.Clock()
instructions_7 = visual.TextStim(win=win, name='instructions_7',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_7 = visual.TextStim(win=win, name='finished_7',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_7 = keyboard.Keyboard()
responses_7 = visual.ImageStim(
    win=win,
    name='responses_7', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_7 = visual.Line(
    win=win, name='blueline_7',units='cm', 
    start=(-(1, 0)[0]/2.0, 0), end=(+(1, 0)[0]/2.0, 0),
    ori=120, pos=(-12, -4),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_7 = visual.Line(
    win=win, name='redline_7',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=168, pos=(12, 10),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_08"
trial_08Clock = core.Clock()
instructions_8 = visual.TextStim(win=win, name='instructions_8',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_8 = visual.TextStim(win=win, name='finished_8',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_8 = keyboard.Keyboard()
responses_8 = visual.ImageStim(
    win=win,
    name='responses_8', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_8 = visual.Line(
    win=win, name='blueline_8',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=108, pos=(11, -4),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_8 = visual.Line(
    win=win, name='redline_8',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=246, pos=(-10, 10),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_09"
trial_09Clock = core.Clock()
instructions_9 = visual.TextStim(win=win, name='instructions_9',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_9 = visual.TextStim(win=win, name='finished_9',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_9 = keyboard.Keyboard()
responses_9 = visual.ImageStim(
    win=win,
    name='responses_9', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_9 = visual.Line(
    win=win, name='blueline_9',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=132, pos=(12, 10),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_9 = visual.Line(
    win=win, name='redline_9',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=162, pos=(-15, -4),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_10"
trial_10Clock = core.Clock()
instructions_10 = visual.TextStim(win=win, name='instructions_10',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_10 = visual.TextStim(win=win, name='finished_10',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_10 = keyboard.Keyboard()
responses_10 = visual.ImageStim(
    win=win,
    name='responses_10', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_10 = visual.Line(
    win=win, name='blueline_10',units='cm', 
    start=(-(1, 0)[0]/2.0, 0), end=(+(1, 0)[0]/2.0, 0),
    ori=237, pos=(14, 10),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_10 = visual.Line(
    win=win, name='redline_10',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=207, pos=(-16, 10),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_11"
trial_11Clock = core.Clock()
instructions_11 = visual.TextStim(win=win, name='instructions_11',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_11 = visual.TextStim(win=win, name='finished_11',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_11 = keyboard.Keyboard()
responses_11 = visual.ImageStim(
    win=win,
    name='responses_11', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_11 = visual.Line(
    win=win, name='blueline_11',units='cm', 
    start=(-(1, 0)[0]/2.0, 0), end=(+(1, 0)[0]/2.0, 0),
    ori=120, pos=(-13, 10),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_11 = visual.Line(
    win=win, name='redline_11',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=261, pos=(13, -4),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_12"
trial_12Clock = core.Clock()
instructions_12 = visual.TextStim(win=win, name='instructions_12',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_12 = visual.TextStim(win=win, name='finished_12',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_12 = keyboard.Keyboard()
responses_12 = visual.ImageStim(
    win=win,
    name='responses_12', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_12 = visual.Line(
    win=win, name='blueline_12',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=267, pos=(-16, -4),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_12 = visual.Line(
    win=win, name='redline_12',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=117, pos=(16, -3),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_13"
trial_13Clock = core.Clock()
instructions_13 = visual.TextStim(win=win, name='instructions_13',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_13 = visual.TextStim(win=win, name='finished_13',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_13 = keyboard.Keyboard()
responses_13 = visual.ImageStim(
    win=win,
    name='responses_13', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_13 = visual.Line(
    win=win, name='blueline_13',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=132, pos=(13, 9),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_13 = visual.Line(
    win=win, name='redline_13',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=159, pos=(-12, -4),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_14"
trial_14Clock = core.Clock()
instructions_14 = visual.TextStim(win=win, name='instructions_14',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_14 = visual.TextStim(win=win, name='finished_14',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_14 = keyboard.Keyboard()
responses_14 = visual.ImageStim(
    win=win,
    name='responses_14', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_14 = visual.Line(
    win=win, name='blueline_14',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=90, pos=(-13, 9),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_14 = visual.Line(
    win=win, name='redline_14',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=198, pos=(14, -4),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_15"
trial_15Clock = core.Clock()
instructions_15 = visual.TextStim(win=win, name='instructions_15',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_15 = visual.TextStim(win=win, name='finished_15',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_15 = keyboard.Keyboard()
responses_15 = visual.ImageStim(
    win=win,
    name='responses_15', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_15 = visual.Line(
    win=win, name='blueline_15',units='cm', 
    start=(-(1, 0)[0]/2.0, 0), end=(+(1, 0)[0]/2.0, 0),
    ori=261, pos=(13, 8),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_15 = visual.Line(
    win=win, name='redline_15',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=153, pos=(-14, -4),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_16"
trial_16Clock = core.Clock()
instructions_16 = visual.TextStim(win=win, name='instructions_16',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_16 = visual.TextStim(win=win, name='finished_16',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_16 = keyboard.Keyboard()
responses_16 = visual.ImageStim(
    win=win,
    name='responses_16', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_16 = visual.Line(
    win=win, name='blueline_16',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=267, pos=(-15, -4),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_16 = visual.Line(
    win=win, name='redline_16',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=117, pos=(16, -3),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_17"
trial_17Clock = core.Clock()
instructions_17 = visual.TextStim(win=win, name='instructions_17',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_17 = visual.TextStim(win=win, name='finished_17',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_17 = keyboard.Keyboard()
responses_17 = visual.ImageStim(
    win=win,
    name='responses_17', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_17 = visual.Line(
    win=win, name='blueline_17',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=108, pos=(13, -3),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_17 = visual.Line(
    win=win, name='redline_17',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=246, pos=(-13, 9),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_18"
trial_18Clock = core.Clock()
instructions_18 = visual.TextStim(win=win, name='instructions_18',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_18 = visual.TextStim(win=win, name='finished_18',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_18 = keyboard.Keyboard()
responses_18 = visual.ImageStim(
    win=win,
    name='responses_18', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_18 = visual.Line(
    win=win, name='blueline_18',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=162, pos=(-13, -4),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_18 = visual.Line(
    win=win, name='redline_18',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=243, pos=(15, -4),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_19"
trial_19Clock = core.Clock()
instructions_19 = visual.TextStim(win=win, name='instructions_19',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_19 = visual.TextStim(win=win, name='finished_19',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_19 = keyboard.Keyboard()
responses_19 = visual.ImageStim(
    win=win,
    name='responses_19', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_19 = visual.Line(
    win=win, name='blueline_19',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=222, pos=(-15, 9),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_19 = visual.Line(
    win=win, name='redline_19',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=102, pos=(15, 9),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_20"
trial_20Clock = core.Clock()
instructions_20 = visual.TextStim(win=win, name='instructions_20',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_20 = visual.TextStim(win=win, name='finished_20',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_20 = keyboard.Keyboard()
responses_20 = visual.ImageStim(
    win=win,
    name='responses_20', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_20 = visual.Line(
    win=win, name='blueline_20',units='cm', 
    start=(-(1, 0)[0]/2.0, 0), end=(+(1, 0)[0]/2.0, 0),
    ori=120, pos=(-12, -3),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_20 = visual.Line(
    win=win, name='redline_20',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=168, pos=(13, 9),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_21"
trial_21Clock = core.Clock()
instructions_21 = visual.TextStim(win=win, name='instructions_21',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_21 = visual.TextStim(win=win, name='finished_21',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_21 = keyboard.Keyboard()
responses_21 = visual.ImageStim(
    win=win,
    name='responses_21', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_21 = visual.Line(
    win=win, name='blueline_21',units='cm', 
    start=(-(1, 0)[0]/2.0, 0), end=(+(1, 0)[0]/2.0, 0),
    ori=144, pos=(14, 9),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_21 = visual.Line(
    win=win, name='redline_21',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=261, pos=(-14, 9),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_22"
trial_22Clock = core.Clock()
instructions_22 = visual.TextStim(win=win, name='instructions_22',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_22 = visual.TextStim(win=win, name='finished_22',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_22 = keyboard.Keyboard()
responses_22 = visual.ImageStim(
    win=win,
    name='responses_22', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_22 = visual.Line(
    win=win, name='blueline_22',units='cm', 
    start=(-(1, 0)[0]/2.0, 0), end=(+(1, 0)[0]/2.0, 0),
    ori=120, pos=(-13, 8),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_22 = visual.Line(
    win=win, name='redline_22',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=261, pos=(12, -4),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_23"
trial_23Clock = core.Clock()
instructions_23 = visual.TextStim(win=win, name='instructions_23',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_23 = visual.TextStim(win=win, name='finished_23',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_23 = keyboard.Keyboard()
responses_23 = visual.ImageStim(
    win=win,
    name='responses_23', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_23 = visual.Line(
    win=win, name='blueline_23',units='cm', 
    start=(-(1, 0)[0]/2.0, 0), end=(+(1, 0)[0]/2.0, 0),
    ori=237, pos=(15, 9),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_23 = visual.Line(
    win=win, name='redline_23',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=207, pos=(-15, 9),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitters = [6, 3, 4, 2, 4, 6, 4, 6, 2, 4, 3, 4, 3, 2, 6, 2, 3, 2, 3, 4, 2, 6, 3, 6]
fixation_2 = visual.ShapeStim(
    win=win, name='fixation_2', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial_24"
trial_24Clock = core.Clock()
instructions_24 = visual.TextStim(win=win, name='instructions_24',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    units='cm', pos=(-13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
finished_24 = visual.TextStim(win=win, name='finished_24',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    units='cm', pos=(13, -10), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_24 = keyboard.Keyboard()
responses_24 = visual.ImageStim(
    win=win,
    name='responses_24', units='cm', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
blueline_24 = visual.Line(
    win=win, name='blueline_24',units='cm', 
    start=(-(1, 0)[0]/2.0, 0), end=(+(1, 0)[0]/2.0, 0),
    ori=90, pos=(14, -4),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-0.325,-0.835,1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
redline_24 = visual.Line(
    win=win, name='redline_24',units='cm', 
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=198, pos=(-14, -4),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1.000,-0.835,-0.780], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "wait_for_scanner"-------
# update component parameters for each repeat
scanner_resp.keys = []
scanner_resp.rt = []
# keep track of which components have finished
wait_for_scannerComponents = [scanner_resp, fixation]
for thisComponent in wait_for_scannerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wait_for_scannerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "wait_for_scanner"-------
while continueRoutine:
    # get current time
    t = wait_for_scannerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wait_for_scannerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *scanner_resp* updates
    waitOnFlip = False
    if scanner_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scanner_resp.frameNStart = frameN  # exact frame index
        scanner_resp.tStart = t  # local t and not account for scr refresh
        scanner_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scanner_resp, 'tStartRefresh')  # time at next scr refresh
        scanner_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(scanner_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(scanner_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if scanner_resp.status == STARTED and not waitOnFlip:
        theseKeys = scanner_resp.getKeys(keyList=['5'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            scanner_resp.keys = theseKeys.name  # just the last key pressed
            scanner_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *fixation* updates
    if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation.frameNStart = frameN  # exact frame index
        fixation.tStart = t  # local t and not account for scr refresh
        fixation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
        fixation.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_for_scannerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait_for_scanner"-------
for thisComponent in wait_for_scannerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if scanner_resp.keys in ['', [], None]:  # No response was made
    scanner_resp.keys = None
thisExp.addData('scanner_resp.keys',scanner_resp.keys)
if scanner_resp.keys != None:  # we had a response
    thisExp.addData('scanner_resp.rt', scanner_resp.rt)
thisExp.addData('scanner_resp.started', scanner_resp.tStartRefresh)
thisExp.addData('scanner_resp.stopped', scanner_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('fixation.started', fixation.tStartRefresh)
thisExp.addData('fixation.stopped', fixation.tStopRefresh)
# the Routine "wait_for_scanner" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_01"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
trial_01Components = [instructions, finished, key_resp, responses, blueline, redline]
for thisComponent in trial_01Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_01Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_01"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_01Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_01Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    if instructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions.tStop = t  # not accounting for scr refresh
            instructions.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions, 'tStopRefresh')  # time at next scr refresh
            instructions.setAutoDraw(False)
    
    # *finished* updates
    if finished.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished.frameNStart = frameN  # exact frame index
        finished.tStart = t  # local t and not account for scr refresh
        finished.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished, 'tStartRefresh')  # time at next scr refresh
        finished.setAutoDraw(True)
    if finished.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished.tStop = t  # not accounting for scr refresh
            finished.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished, 'tStopRefresh')  # time at next scr refresh
            finished.setAutoDraw(False)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp.tStop = t  # not accounting for scr refresh
            key_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
            key_resp.status = FINISHED
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline.setOri(9,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline.setOri(9,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline.setColor('black')
                redline.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp.keys.append(theseKeys.name)  # storing all keys
            key_resp.rt.append(theseKeys.rt)
    
    # *responses* updates
    if responses.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses.frameNStart = frameN  # exact frame index
        responses.tStart = t  # local t and not account for scr refresh
        responses.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses, 'tStartRefresh')  # time at next scr refresh
        responses.setAutoDraw(True)
    if responses.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses.tStop = t  # not accounting for scr refresh
            responses.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses, 'tStopRefresh')  # time at next scr refresh
            responses.setAutoDraw(False)
    
    # *blueline* updates
    if blueline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline.frameNStart = frameN  # exact frame index
        blueline.tStart = t  # local t and not account for scr refresh
        blueline.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline, 'tStartRefresh')  # time at next scr refresh
        blueline.setAutoDraw(True)
    if blueline.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline.tStop = t  # not accounting for scr refresh
            blueline.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline, 'tStopRefresh')  # time at next scr refresh
            blueline.setAutoDraw(False)
    
    # *redline* updates
    if redline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline.frameNStart = frameN  # exact frame index
        redline.tStart = t  # local t and not account for scr refresh
        redline.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline, 'tStartRefresh')  # time at next scr refresh
        redline.setAutoDraw(True)
    if redline.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline.tStop = t  # not accounting for scr refresh
            redline.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline, 'tStopRefresh')  # time at next scr refresh
            redline.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_01Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_01"-------
for thisComponent in trial_01Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
thisExp.addData('finished.started', finished.tStartRefresh)
thisExp.addData('finished.stopped', finished.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses.started', responses.tStartRefresh)
thisExp.addData('responses.stopped', responses.tStopRefresh)
thisExp.addData('blueline.started', blueline.tStartRefresh)
thisExp.addData('blueline.stopped', blueline.tStopRefresh)
thisExp.addData('redline.started', redline.tStartRefresh)
thisExp.addData('redline.stopped', redline.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_02"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
# keep track of which components have finished
trial_02Components = [instructions_2, finished_2, key_resp_2, responses_2, blueline_2, redline_2]
for thisComponent in trial_02Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_02Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_02"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_02Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_02Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_2* updates
    if instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_2.frameNStart = frameN  # exact frame index
        instructions_2.tStart = t  # local t and not account for scr refresh
        instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_2, 'tStartRefresh')  # time at next scr refresh
        instructions_2.setAutoDraw(True)
    if instructions_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_2.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_2.tStop = t  # not accounting for scr refresh
            instructions_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_2, 'tStopRefresh')  # time at next scr refresh
            instructions_2.setAutoDraw(False)
    
    # *finished_2* updates
    if finished_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_2.frameNStart = frameN  # exact frame index
        finished_2.tStart = t  # local t and not account for scr refresh
        finished_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_2, 'tStartRefresh')  # time at next scr refresh
        finished_2.setAutoDraw(True)
    if finished_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_2.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_2.tStop = t  # not accounting for scr refresh
            finished_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_2, 'tStopRefresh')  # time at next scr refresh
            finished_2.setAutoDraw(False)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_2.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_2.tStop = t  # not accounting for scr refresh
            key_resp_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
            key_resp_2.status = FINISHED
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_2.setOri(9,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_2.setOri(9,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_2.setColor('black')
                redline_2.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_2.keys.append(theseKeys.name)  # storing all keys
            key_resp_2.rt.append(theseKeys.rt)
    
    # *responses_2* updates
    if responses_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_2.frameNStart = frameN  # exact frame index
        responses_2.tStart = t  # local t and not account for scr refresh
        responses_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_2, 'tStartRefresh')  # time at next scr refresh
        responses_2.setAutoDraw(True)
    if responses_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_2.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_2.tStop = t  # not accounting for scr refresh
            responses_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_2, 'tStopRefresh')  # time at next scr refresh
            responses_2.setAutoDraw(False)
    
    # *blueline_2* updates
    if blueline_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_2.frameNStart = frameN  # exact frame index
        blueline_2.tStart = t  # local t and not account for scr refresh
        blueline_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_2, 'tStartRefresh')  # time at next scr refresh
        blueline_2.setAutoDraw(True)
    if blueline_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_2.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_2.tStop = t  # not accounting for scr refresh
            blueline_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_2, 'tStopRefresh')  # time at next scr refresh
            blueline_2.setAutoDraw(False)
    
    # *redline_2* updates
    if redline_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_2.frameNStart = frameN  # exact frame index
        redline_2.tStart = t  # local t and not account for scr refresh
        redline_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_2, 'tStartRefresh')  # time at next scr refresh
        redline_2.setAutoDraw(True)
    if redline_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_2.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_2.tStop = t  # not accounting for scr refresh
            redline_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_2, 'tStopRefresh')  # time at next scr refresh
            redline_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_02Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_02"-------
for thisComponent in trial_02Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_2.started', instructions_2.tStartRefresh)
thisExp.addData('instructions_2.stopped', instructions_2.tStopRefresh)
thisExp.addData('finished_2.started', finished_2.tStartRefresh)
thisExp.addData('finished_2.stopped', finished_2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_2.started', responses_2.tStartRefresh)
thisExp.addData('responses_2.stopped', responses_2.tStopRefresh)
thisExp.addData('blueline_2.started', blueline_2.tStartRefresh)
thisExp.addData('blueline_2.stopped', blueline_2.tStopRefresh)
thisExp.addData('redline_2.started', redline_2.tStartRefresh)
thisExp.addData('redline_2.stopped', redline_2.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_03"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
# keep track of which components have finished
trial_03Components = [instructions_3, finished_3, key_resp_3, responses_3, blueline_3, redline_3]
for thisComponent in trial_03Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_03Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_03"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_03Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_03Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_3* updates
    if instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_3.frameNStart = frameN  # exact frame index
        instructions_3.tStart = t  # local t and not account for scr refresh
        instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_3, 'tStartRefresh')  # time at next scr refresh
        instructions_3.setAutoDraw(True)
    if instructions_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_3.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_3.tStop = t  # not accounting for scr refresh
            instructions_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_3, 'tStopRefresh')  # time at next scr refresh
            instructions_3.setAutoDraw(False)
    
    # *finished_3* updates
    if finished_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_3.frameNStart = frameN  # exact frame index
        finished_3.tStart = t  # local t and not account for scr refresh
        finished_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_3, 'tStartRefresh')  # time at next scr refresh
        finished_3.setAutoDraw(True)
    if finished_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_3.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_3.tStop = t  # not accounting for scr refresh
            finished_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_3, 'tStopRefresh')  # time at next scr refresh
            finished_3.setAutoDraw(False)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_3.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_3.tStop = t  # not accounting for scr refresh
            key_resp_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_3, 'tStopRefresh')  # time at next scr refresh
            key_resp_3.status = FINISHED
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_3.setOri(9,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_3.setOri(9,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_3.setColor('black')
                redline_3.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_3.keys.append(theseKeys.name)  # storing all keys
            key_resp_3.rt.append(theseKeys.rt)
    
    # *responses_3* updates
    if responses_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_3.frameNStart = frameN  # exact frame index
        responses_3.tStart = t  # local t and not account for scr refresh
        responses_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_3, 'tStartRefresh')  # time at next scr refresh
        responses_3.setAutoDraw(True)
    if responses_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_3.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_3.tStop = t  # not accounting for scr refresh
            responses_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_3, 'tStopRefresh')  # time at next scr refresh
            responses_3.setAutoDraw(False)
    
    # *blueline_3* updates
    if blueline_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_3.frameNStart = frameN  # exact frame index
        blueline_3.tStart = t  # local t and not account for scr refresh
        blueline_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_3, 'tStartRefresh')  # time at next scr refresh
        blueline_3.setAutoDraw(True)
    if blueline_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_3.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_3.tStop = t  # not accounting for scr refresh
            blueline_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_3, 'tStopRefresh')  # time at next scr refresh
            blueline_3.setAutoDraw(False)
    
    # *redline_3* updates
    if redline_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_3.frameNStart = frameN  # exact frame index
        redline_3.tStart = t  # local t and not account for scr refresh
        redline_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_3, 'tStartRefresh')  # time at next scr refresh
        redline_3.setAutoDraw(True)
    if redline_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_3.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_3.tStop = t  # not accounting for scr refresh
            redline_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_3, 'tStopRefresh')  # time at next scr refresh
            redline_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_03Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_03"-------
for thisComponent in trial_03Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_3.started', instructions_3.tStartRefresh)
thisExp.addData('instructions_3.stopped', instructions_3.tStopRefresh)
thisExp.addData('finished_3.started', finished_3.tStartRefresh)
thisExp.addData('finished_3.stopped', finished_3.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_3.started', responses_3.tStartRefresh)
thisExp.addData('responses_3.stopped', responses_3.tStopRefresh)
thisExp.addData('blueline_3.started', blueline_3.tStartRefresh)
thisExp.addData('blueline_3.stopped', blueline_3.tStopRefresh)
thisExp.addData('redline_3.started', redline_3.tStartRefresh)
thisExp.addData('redline_3.stopped', redline_3.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_04"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
# keep track of which components have finished
trial_04Components = [instructions_4, finished_4, key_resp_4, responses_4, blueline_4, redline_4]
for thisComponent in trial_04Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_04Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_04"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_04Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_04Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_4* updates
    if instructions_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_4.frameNStart = frameN  # exact frame index
        instructions_4.tStart = t  # local t and not account for scr refresh
        instructions_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_4, 'tStartRefresh')  # time at next scr refresh
        instructions_4.setAutoDraw(True)
    if instructions_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_4.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_4.tStop = t  # not accounting for scr refresh
            instructions_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_4, 'tStopRefresh')  # time at next scr refresh
            instructions_4.setAutoDraw(False)
    
    # *finished_4* updates
    if finished_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_4.frameNStart = frameN  # exact frame index
        finished_4.tStart = t  # local t and not account for scr refresh
        finished_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_4, 'tStartRefresh')  # time at next scr refresh
        finished_4.setAutoDraw(True)
    if finished_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_4.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_4.tStop = t  # not accounting for scr refresh
            finished_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_4, 'tStopRefresh')  # time at next scr refresh
            finished_4.setAutoDraw(False)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_4.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_4.tStop = t  # not accounting for scr refresh
            key_resp_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
            key_resp_4.status = FINISHED
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_4.setOri(9,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_4.setOri(9,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_4.setColor('black')
                redline_4.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_4.keys.append(theseKeys.name)  # storing all keys
            key_resp_4.rt.append(theseKeys.rt)
    
    # *responses_4* updates
    if responses_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_4.frameNStart = frameN  # exact frame index
        responses_4.tStart = t  # local t and not account for scr refresh
        responses_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_4, 'tStartRefresh')  # time at next scr refresh
        responses_4.setAutoDraw(True)
    if responses_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_4.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_4.tStop = t  # not accounting for scr refresh
            responses_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_4, 'tStopRefresh')  # time at next scr refresh
            responses_4.setAutoDraw(False)
    
    # *blueline_4* updates
    if blueline_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_4.frameNStart = frameN  # exact frame index
        blueline_4.tStart = t  # local t and not account for scr refresh
        blueline_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_4, 'tStartRefresh')  # time at next scr refresh
        blueline_4.setAutoDraw(True)
    if blueline_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_4.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_4.tStop = t  # not accounting for scr refresh
            blueline_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_4, 'tStopRefresh')  # time at next scr refresh
            blueline_4.setAutoDraw(False)
    
    # *redline_4* updates
    if redline_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_4.frameNStart = frameN  # exact frame index
        redline_4.tStart = t  # local t and not account for scr refresh
        redline_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_4, 'tStartRefresh')  # time at next scr refresh
        redline_4.setAutoDraw(True)
    if redline_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_4.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_4.tStop = t  # not accounting for scr refresh
            redline_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_4, 'tStopRefresh')  # time at next scr refresh
            redline_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_04Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_04"-------
for thisComponent in trial_04Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_4.started', instructions_4.tStartRefresh)
thisExp.addData('instructions_4.stopped', instructions_4.tStopRefresh)
thisExp.addData('finished_4.started', finished_4.tStartRefresh)
thisExp.addData('finished_4.stopped', finished_4.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_4.started', responses_4.tStartRefresh)
thisExp.addData('responses_4.stopped', responses_4.tStopRefresh)
thisExp.addData('blueline_4.started', blueline_4.tStartRefresh)
thisExp.addData('blueline_4.stopped', blueline_4.tStopRefresh)
thisExp.addData('redline_4.started', redline_4.tStartRefresh)
thisExp.addData('redline_4.stopped', redline_4.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_05"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
# keep track of which components have finished
trial_05Components = [instructions_5, finished_5, key_resp_5, responses_5, blueline_5, redline_5]
for thisComponent in trial_05Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_05Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_05"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_05Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_05Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_5* updates
    if instructions_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_5.frameNStart = frameN  # exact frame index
        instructions_5.tStart = t  # local t and not account for scr refresh
        instructions_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_5, 'tStartRefresh')  # time at next scr refresh
        instructions_5.setAutoDraw(True)
    if instructions_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_5.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_5.tStop = t  # not accounting for scr refresh
            instructions_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_5, 'tStopRefresh')  # time at next scr refresh
            instructions_5.setAutoDraw(False)
    
    # *finished_5* updates
    if finished_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_5.frameNStart = frameN  # exact frame index
        finished_5.tStart = t  # local t and not account for scr refresh
        finished_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_5, 'tStartRefresh')  # time at next scr refresh
        finished_5.setAutoDraw(True)
    if finished_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_5.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_5.tStop = t  # not accounting for scr refresh
            finished_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_5, 'tStopRefresh')  # time at next scr refresh
            finished_5.setAutoDraw(False)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_5.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_5.tStop = t  # not accounting for scr refresh
            key_resp_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_5, 'tStopRefresh')  # time at next scr refresh
            key_resp_5.status = FINISHED
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_5.setOri(6,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_5.setOri(6,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_5.setColor('black')
                redline_5.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_5.keys.append(theseKeys.name)  # storing all keys
            key_resp_5.rt.append(theseKeys.rt)
    
    # *responses_5* updates
    if responses_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_5.frameNStart = frameN  # exact frame index
        responses_5.tStart = t  # local t and not account for scr refresh
        responses_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_5, 'tStartRefresh')  # time at next scr refresh
        responses_5.setAutoDraw(True)
    if responses_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_5.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_5.tStop = t  # not accounting for scr refresh
            responses_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_5, 'tStopRefresh')  # time at next scr refresh
            responses_5.setAutoDraw(False)
    
    # *blueline_5* updates
    if blueline_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_5.frameNStart = frameN  # exact frame index
        blueline_5.tStart = t  # local t and not account for scr refresh
        blueline_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_5, 'tStartRefresh')  # time at next scr refresh
        blueline_5.setAutoDraw(True)
    if blueline_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_5.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_5.tStop = t  # not accounting for scr refresh
            blueline_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_5, 'tStopRefresh')  # time at next scr refresh
            blueline_5.setAutoDraw(False)
    
    # *redline_5* updates
    if redline_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_5.frameNStart = frameN  # exact frame index
        redline_5.tStart = t  # local t and not account for scr refresh
        redline_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_5, 'tStartRefresh')  # time at next scr refresh
        redline_5.setAutoDraw(True)
    if redline_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_5.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_5.tStop = t  # not accounting for scr refresh
            redline_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_5, 'tStopRefresh')  # time at next scr refresh
            redline_5.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_05Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_05"-------
for thisComponent in trial_05Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_5.started', instructions_5.tStartRefresh)
thisExp.addData('instructions_5.stopped', instructions_5.tStopRefresh)
thisExp.addData('finished_5.started', finished_5.tStartRefresh)
thisExp.addData('finished_5.stopped', finished_5.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_5.started', responses_5.tStartRefresh)
thisExp.addData('responses_5.stopped', responses_5.tStopRefresh)
thisExp.addData('blueline_5.started', blueline_5.tStartRefresh)
thisExp.addData('blueline_5.stopped', blueline_5.tStopRefresh)
thisExp.addData('redline_5.started', redline_5.tStartRefresh)
thisExp.addData('redline_5.stopped', redline_5.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_06"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
# keep track of which components have finished
trial_06Components = [instructions_6, finished_6, key_resp_6, responses_6, blueline_6, redline_6]
for thisComponent in trial_06Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_06Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_06"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_06Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_06Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_6* updates
    if instructions_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_6.frameNStart = frameN  # exact frame index
        instructions_6.tStart = t  # local t and not account for scr refresh
        instructions_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_6, 'tStartRefresh')  # time at next scr refresh
        instructions_6.setAutoDraw(True)
    if instructions_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_6.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_6.tStop = t  # not accounting for scr refresh
            instructions_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_6, 'tStopRefresh')  # time at next scr refresh
            instructions_6.setAutoDraw(False)
    
    # *finished_6* updates
    if finished_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_6.frameNStart = frameN  # exact frame index
        finished_6.tStart = t  # local t and not account for scr refresh
        finished_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_6, 'tStartRefresh')  # time at next scr refresh
        finished_6.setAutoDraw(True)
    if finished_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_6.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_6.tStop = t  # not accounting for scr refresh
            finished_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_6, 'tStopRefresh')  # time at next scr refresh
            finished_6.setAutoDraw(False)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_6.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_6.tStop = t  # not accounting for scr refresh
            key_resp_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_6, 'tStopRefresh')  # time at next scr refresh
            key_resp_6.status = FINISHED
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_6.setOri(6,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_6.setOri(6,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_6.setColor('black')
                redline_6.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_6.keys.append(theseKeys.name)  # storing all keys
            key_resp_6.rt.append(theseKeys.rt)
    
    # *responses_6* updates
    if responses_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_6.frameNStart = frameN  # exact frame index
        responses_6.tStart = t  # local t and not account for scr refresh
        responses_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_6, 'tStartRefresh')  # time at next scr refresh
        responses_6.setAutoDraw(True)
    if responses_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_6.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_6.tStop = t  # not accounting for scr refresh
            responses_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_6, 'tStopRefresh')  # time at next scr refresh
            responses_6.setAutoDraw(False)
    
    # *blueline_6* updates
    if blueline_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_6.frameNStart = frameN  # exact frame index
        blueline_6.tStart = t  # local t and not account for scr refresh
        blueline_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_6, 'tStartRefresh')  # time at next scr refresh
        blueline_6.setAutoDraw(True)
    if blueline_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_6.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_6.tStop = t  # not accounting for scr refresh
            blueline_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_6, 'tStopRefresh')  # time at next scr refresh
            blueline_6.setAutoDraw(False)
    
    # *redline_6* updates
    if redline_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_6.frameNStart = frameN  # exact frame index
        redline_6.tStart = t  # local t and not account for scr refresh
        redline_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_6, 'tStartRefresh')  # time at next scr refresh
        redline_6.setAutoDraw(True)
    if redline_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_6.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_6.tStop = t  # not accounting for scr refresh
            redline_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_6, 'tStopRefresh')  # time at next scr refresh
            redline_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_06Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_06"-------
for thisComponent in trial_06Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_6.started', instructions_6.tStartRefresh)
thisExp.addData('instructions_6.stopped', instructions_6.tStopRefresh)
thisExp.addData('finished_6.started', finished_6.tStartRefresh)
thisExp.addData('finished_6.stopped', finished_6.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_6.started', responses_6.tStartRefresh)
thisExp.addData('responses_6.stopped', responses_6.tStopRefresh)
thisExp.addData('blueline_6.started', blueline_6.tStartRefresh)
thisExp.addData('blueline_6.stopped', blueline_6.tStopRefresh)
thisExp.addData('redline_6.started', redline_6.tStartRefresh)
thisExp.addData('redline_6.stopped', redline_6.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_07"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
# keep track of which components have finished
trial_07Components = [instructions_7, finished_7, key_resp_7, responses_7, blueline_7, redline_7]
for thisComponent in trial_07Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_07Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_07"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_07Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_07Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_7* updates
    if instructions_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_7.frameNStart = frameN  # exact frame index
        instructions_7.tStart = t  # local t and not account for scr refresh
        instructions_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_7, 'tStartRefresh')  # time at next scr refresh
        instructions_7.setAutoDraw(True)
    if instructions_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_7.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_7.tStop = t  # not accounting for scr refresh
            instructions_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_7, 'tStopRefresh')  # time at next scr refresh
            instructions_7.setAutoDraw(False)
    
    # *finished_7* updates
    if finished_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_7.frameNStart = frameN  # exact frame index
        finished_7.tStart = t  # local t and not account for scr refresh
        finished_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_7, 'tStartRefresh')  # time at next scr refresh
        finished_7.setAutoDraw(True)
    if finished_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_7.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_7.tStop = t  # not accounting for scr refresh
            finished_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_7, 'tStopRefresh')  # time at next scr refresh
            finished_7.setAutoDraw(False)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_7.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_7.tStop = t  # not accounting for scr refresh
            key_resp_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_7, 'tStopRefresh')  # time at next scr refresh
            key_resp_7.status = FINISHED
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_7.setOri(6,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_7.setOri(6,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_7.setColor('black')
                redline_7.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_7.keys.append(theseKeys.name)  # storing all keys
            key_resp_7.rt.append(theseKeys.rt)
    
    # *responses_7* updates
    if responses_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_7.frameNStart = frameN  # exact frame index
        responses_7.tStart = t  # local t and not account for scr refresh
        responses_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_7, 'tStartRefresh')  # time at next scr refresh
        responses_7.setAutoDraw(True)
    if responses_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_7.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_7.tStop = t  # not accounting for scr refresh
            responses_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_7, 'tStopRefresh')  # time at next scr refresh
            responses_7.setAutoDraw(False)
    
    # *blueline_7* updates
    if blueline_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_7.frameNStart = frameN  # exact frame index
        blueline_7.tStart = t  # local t and not account for scr refresh
        blueline_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_7, 'tStartRefresh')  # time at next scr refresh
        blueline_7.setAutoDraw(True)
    if blueline_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_7.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_7.tStop = t  # not accounting for scr refresh
            blueline_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_7, 'tStopRefresh')  # time at next scr refresh
            blueline_7.setAutoDraw(False)
    
    # *redline_7* updates
    if redline_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_7.frameNStart = frameN  # exact frame index
        redline_7.tStart = t  # local t and not account for scr refresh
        redline_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_7, 'tStartRefresh')  # time at next scr refresh
        redline_7.setAutoDraw(True)
    if redline_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_7.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_7.tStop = t  # not accounting for scr refresh
            redline_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_7, 'tStopRefresh')  # time at next scr refresh
            redline_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_07Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_07"-------
for thisComponent in trial_07Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_7.started', instructions_7.tStartRefresh)
thisExp.addData('instructions_7.stopped', instructions_7.tStopRefresh)
thisExp.addData('finished_7.started', finished_7.tStartRefresh)
thisExp.addData('finished_7.stopped', finished_7.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_7.started', responses_7.tStartRefresh)
thisExp.addData('responses_7.stopped', responses_7.tStopRefresh)
thisExp.addData('blueline_7.started', blueline_7.tStartRefresh)
thisExp.addData('blueline_7.stopped', blueline_7.tStopRefresh)
thisExp.addData('redline_7.started', redline_7.tStartRefresh)
thisExp.addData('redline_7.stopped', redline_7.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_08"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
# keep track of which components have finished
trial_08Components = [instructions_8, finished_8, key_resp_8, responses_8, blueline_8, redline_8]
for thisComponent in trial_08Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_08Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_08"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_08Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_08Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_8* updates
    if instructions_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_8.frameNStart = frameN  # exact frame index
        instructions_8.tStart = t  # local t and not account for scr refresh
        instructions_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_8, 'tStartRefresh')  # time at next scr refresh
        instructions_8.setAutoDraw(True)
    if instructions_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_8.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_8.tStop = t  # not accounting for scr refresh
            instructions_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_8, 'tStopRefresh')  # time at next scr refresh
            instructions_8.setAutoDraw(False)
    
    # *finished_8* updates
    if finished_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_8.frameNStart = frameN  # exact frame index
        finished_8.tStart = t  # local t and not account for scr refresh
        finished_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_8, 'tStartRefresh')  # time at next scr refresh
        finished_8.setAutoDraw(True)
    if finished_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_8.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_8.tStop = t  # not accounting for scr refresh
            finished_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_8, 'tStopRefresh')  # time at next scr refresh
            finished_8.setAutoDraw(False)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_8.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_8.tStop = t  # not accounting for scr refresh
            key_resp_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_8, 'tStopRefresh')  # time at next scr refresh
            key_resp_8.status = FINISHED
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_8.setOri(6,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_8.setOri(6,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_8.setColor('black')
                redline_8.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_8.keys.append(theseKeys.name)  # storing all keys
            key_resp_8.rt.append(theseKeys.rt)
    
    # *responses_8* updates
    if responses_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_8.frameNStart = frameN  # exact frame index
        responses_8.tStart = t  # local t and not account for scr refresh
        responses_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_8, 'tStartRefresh')  # time at next scr refresh
        responses_8.setAutoDraw(True)
    if responses_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_8.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_8.tStop = t  # not accounting for scr refresh
            responses_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_8, 'tStopRefresh')  # time at next scr refresh
            responses_8.setAutoDraw(False)
    
    # *blueline_8* updates
    if blueline_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_8.frameNStart = frameN  # exact frame index
        blueline_8.tStart = t  # local t and not account for scr refresh
        blueline_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_8, 'tStartRefresh')  # time at next scr refresh
        blueline_8.setAutoDraw(True)
    if blueline_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_8.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_8.tStop = t  # not accounting for scr refresh
            blueline_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_8, 'tStopRefresh')  # time at next scr refresh
            blueline_8.setAutoDraw(False)
    
    # *redline_8* updates
    if redline_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_8.frameNStart = frameN  # exact frame index
        redline_8.tStart = t  # local t and not account for scr refresh
        redline_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_8, 'tStartRefresh')  # time at next scr refresh
        redline_8.setAutoDraw(True)
    if redline_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_8.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_8.tStop = t  # not accounting for scr refresh
            redline_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_8, 'tStopRefresh')  # time at next scr refresh
            redline_8.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_08Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_08"-------
for thisComponent in trial_08Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_8.started', instructions_8.tStartRefresh)
thisExp.addData('instructions_8.stopped', instructions_8.tStopRefresh)
thisExp.addData('finished_8.started', finished_8.tStartRefresh)
thisExp.addData('finished_8.stopped', finished_8.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_8.started', responses_8.tStartRefresh)
thisExp.addData('responses_8.stopped', responses_8.tStopRefresh)
thisExp.addData('blueline_8.started', blueline_8.tStartRefresh)
thisExp.addData('blueline_8.stopped', blueline_8.tStopRefresh)
thisExp.addData('redline_8.started', redline_8.tStartRefresh)
thisExp.addData('redline_8.stopped', redline_8.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_09"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
# keep track of which components have finished
trial_09Components = [instructions_9, finished_9, key_resp_9, responses_9, blueline_9, redline_9]
for thisComponent in trial_09Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_09Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_09"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_09Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_09Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_9* updates
    if instructions_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_9.frameNStart = frameN  # exact frame index
        instructions_9.tStart = t  # local t and not account for scr refresh
        instructions_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_9, 'tStartRefresh')  # time at next scr refresh
        instructions_9.setAutoDraw(True)
    if instructions_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_9.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_9.tStop = t  # not accounting for scr refresh
            instructions_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_9, 'tStopRefresh')  # time at next scr refresh
            instructions_9.setAutoDraw(False)
    
    # *finished_9* updates
    if finished_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_9.frameNStart = frameN  # exact frame index
        finished_9.tStart = t  # local t and not account for scr refresh
        finished_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_9, 'tStartRefresh')  # time at next scr refresh
        finished_9.setAutoDraw(True)
    if finished_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_9.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_9.tStop = t  # not accounting for scr refresh
            finished_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_9, 'tStopRefresh')  # time at next scr refresh
            finished_9.setAutoDraw(False)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_9.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_9.tStop = t  # not accounting for scr refresh
            key_resp_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_9, 'tStopRefresh')  # time at next scr refresh
            key_resp_9.status = FINISHED
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_9.setOri(3,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_9.setOri(3,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_9.setColor('black')
                redline_9.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_9.keys.append(theseKeys.name)  # storing all keys
            key_resp_9.rt.append(theseKeys.rt)
    
    # *responses_9* updates
    if responses_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_9.frameNStart = frameN  # exact frame index
        responses_9.tStart = t  # local t and not account for scr refresh
        responses_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_9, 'tStartRefresh')  # time at next scr refresh
        responses_9.setAutoDraw(True)
    if responses_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_9.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_9.tStop = t  # not accounting for scr refresh
            responses_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_9, 'tStopRefresh')  # time at next scr refresh
            responses_9.setAutoDraw(False)
    
    # *blueline_9* updates
    if blueline_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_9.frameNStart = frameN  # exact frame index
        blueline_9.tStart = t  # local t and not account for scr refresh
        blueline_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_9, 'tStartRefresh')  # time at next scr refresh
        blueline_9.setAutoDraw(True)
    if blueline_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_9.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_9.tStop = t  # not accounting for scr refresh
            blueline_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_9, 'tStopRefresh')  # time at next scr refresh
            blueline_9.setAutoDraw(False)
    
    # *redline_9* updates
    if redline_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_9.frameNStart = frameN  # exact frame index
        redline_9.tStart = t  # local t and not account for scr refresh
        redline_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_9, 'tStartRefresh')  # time at next scr refresh
        redline_9.setAutoDraw(True)
    if redline_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_9.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_9.tStop = t  # not accounting for scr refresh
            redline_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_9, 'tStopRefresh')  # time at next scr refresh
            redline_9.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_09Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_09"-------
for thisComponent in trial_09Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_9.started', instructions_9.tStartRefresh)
thisExp.addData('instructions_9.stopped', instructions_9.tStopRefresh)
thisExp.addData('finished_9.started', finished_9.tStartRefresh)
thisExp.addData('finished_9.stopped', finished_9.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_9.started', responses_9.tStartRefresh)
thisExp.addData('responses_9.stopped', responses_9.tStopRefresh)
thisExp.addData('blueline_9.started', blueline_9.tStartRefresh)
thisExp.addData('blueline_9.stopped', blueline_9.tStopRefresh)
thisExp.addData('redline_9.started', redline_9.tStartRefresh)
thisExp.addData('redline_9.stopped', redline_9.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_10"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
# keep track of which components have finished
trial_10Components = [instructions_10, finished_10, key_resp_10, responses_10, blueline_10, redline_10]
for thisComponent in trial_10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_10"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_10Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_10Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_10* updates
    if instructions_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_10.frameNStart = frameN  # exact frame index
        instructions_10.tStart = t  # local t and not account for scr refresh
        instructions_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_10, 'tStartRefresh')  # time at next scr refresh
        instructions_10.setAutoDraw(True)
    if instructions_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_10.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_10.tStop = t  # not accounting for scr refresh
            instructions_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_10, 'tStopRefresh')  # time at next scr refresh
            instructions_10.setAutoDraw(False)
    
    # *finished_10* updates
    if finished_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_10.frameNStart = frameN  # exact frame index
        finished_10.tStart = t  # local t and not account for scr refresh
        finished_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_10, 'tStartRefresh')  # time at next scr refresh
        finished_10.setAutoDraw(True)
    if finished_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_10.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_10.tStop = t  # not accounting for scr refresh
            finished_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_10, 'tStopRefresh')  # time at next scr refresh
            finished_10.setAutoDraw(False)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_10.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_10.tStop = t  # not accounting for scr refresh
            key_resp_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_10, 'tStopRefresh')  # time at next scr refresh
            key_resp_10.status = FINISHED
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_10.setOri(3,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_10.setOri(3,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_10.setColor('black')
                redline_10.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_10.keys.append(theseKeys.name)  # storing all keys
            key_resp_10.rt.append(theseKeys.rt)
    
    # *responses_10* updates
    if responses_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_10.frameNStart = frameN  # exact frame index
        responses_10.tStart = t  # local t and not account for scr refresh
        responses_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_10, 'tStartRefresh')  # time at next scr refresh
        responses_10.setAutoDraw(True)
    if responses_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_10.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_10.tStop = t  # not accounting for scr refresh
            responses_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_10, 'tStopRefresh')  # time at next scr refresh
            responses_10.setAutoDraw(False)
    
    # *blueline_10* updates
    if blueline_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_10.frameNStart = frameN  # exact frame index
        blueline_10.tStart = t  # local t and not account for scr refresh
        blueline_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_10, 'tStartRefresh')  # time at next scr refresh
        blueline_10.setAutoDraw(True)
    if blueline_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_10.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_10.tStop = t  # not accounting for scr refresh
            blueline_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_10, 'tStopRefresh')  # time at next scr refresh
            blueline_10.setAutoDraw(False)
    
    # *redline_10* updates
    if redline_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_10.frameNStart = frameN  # exact frame index
        redline_10.tStart = t  # local t and not account for scr refresh
        redline_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_10, 'tStartRefresh')  # time at next scr refresh
        redline_10.setAutoDraw(True)
    if redline_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_10.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_10.tStop = t  # not accounting for scr refresh
            redline_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_10, 'tStopRefresh')  # time at next scr refresh
            redline_10.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_10"-------
for thisComponent in trial_10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_10.started', instructions_10.tStartRefresh)
thisExp.addData('instructions_10.stopped', instructions_10.tStopRefresh)
thisExp.addData('finished_10.started', finished_10.tStartRefresh)
thisExp.addData('finished_10.stopped', finished_10.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_10.started', responses_10.tStartRefresh)
thisExp.addData('responses_10.stopped', responses_10.tStopRefresh)
thisExp.addData('blueline_10.started', blueline_10.tStartRefresh)
thisExp.addData('blueline_10.stopped', blueline_10.tStopRefresh)
thisExp.addData('redline_10.started', redline_10.tStartRefresh)
thisExp.addData('redline_10.stopped', redline_10.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_11"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
# keep track of which components have finished
trial_11Components = [instructions_11, finished_11, key_resp_11, responses_11, blueline_11, redline_11]
for thisComponent in trial_11Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_11Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_11"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_11Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_11Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_11* updates
    if instructions_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_11.frameNStart = frameN  # exact frame index
        instructions_11.tStart = t  # local t and not account for scr refresh
        instructions_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_11, 'tStartRefresh')  # time at next scr refresh
        instructions_11.setAutoDraw(True)
    if instructions_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_11.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_11.tStop = t  # not accounting for scr refresh
            instructions_11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_11, 'tStopRefresh')  # time at next scr refresh
            instructions_11.setAutoDraw(False)
    
    # *finished_11* updates
    if finished_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_11.frameNStart = frameN  # exact frame index
        finished_11.tStart = t  # local t and not account for scr refresh
        finished_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_11, 'tStartRefresh')  # time at next scr refresh
        finished_11.setAutoDraw(True)
    if finished_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_11.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_11.tStop = t  # not accounting for scr refresh
            finished_11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_11, 'tStopRefresh')  # time at next scr refresh
            finished_11.setAutoDraw(False)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_11.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_11.tStop = t  # not accounting for scr refresh
            key_resp_11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_11, 'tStopRefresh')  # time at next scr refresh
            key_resp_11.status = FINISHED
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_11.setOri(3,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_11.setOri(3,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_11.setColor('black')
                redline_11.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_11.keys.append(theseKeys.name)  # storing all keys
            key_resp_11.rt.append(theseKeys.rt)
    
    # *responses_11* updates
    if responses_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_11.frameNStart = frameN  # exact frame index
        responses_11.tStart = t  # local t and not account for scr refresh
        responses_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_11, 'tStartRefresh')  # time at next scr refresh
        responses_11.setAutoDraw(True)
    if responses_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_11.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_11.tStop = t  # not accounting for scr refresh
            responses_11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_11, 'tStopRefresh')  # time at next scr refresh
            responses_11.setAutoDraw(False)
    
    # *blueline_11* updates
    if blueline_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_11.frameNStart = frameN  # exact frame index
        blueline_11.tStart = t  # local t and not account for scr refresh
        blueline_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_11, 'tStartRefresh')  # time at next scr refresh
        blueline_11.setAutoDraw(True)
    if blueline_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_11.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_11.tStop = t  # not accounting for scr refresh
            blueline_11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_11, 'tStopRefresh')  # time at next scr refresh
            blueline_11.setAutoDraw(False)
    
    # *redline_11* updates
    if redline_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_11.frameNStart = frameN  # exact frame index
        redline_11.tStart = t  # local t and not account for scr refresh
        redline_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_11, 'tStartRefresh')  # time at next scr refresh
        redline_11.setAutoDraw(True)
    if redline_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_11.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_11.tStop = t  # not accounting for scr refresh
            redline_11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_11, 'tStopRefresh')  # time at next scr refresh
            redline_11.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_11Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_11"-------
for thisComponent in trial_11Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_11.started', instructions_11.tStartRefresh)
thisExp.addData('instructions_11.stopped', instructions_11.tStopRefresh)
thisExp.addData('finished_11.started', finished_11.tStartRefresh)
thisExp.addData('finished_11.stopped', finished_11.tStopRefresh)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys = None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.addData('key_resp_11.started', key_resp_11.tStartRefresh)
thisExp.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_11.started', responses_11.tStartRefresh)
thisExp.addData('responses_11.stopped', responses_11.tStopRefresh)
thisExp.addData('blueline_11.started', blueline_11.tStartRefresh)
thisExp.addData('blueline_11.stopped', blueline_11.tStopRefresh)
thisExp.addData('redline_11.started', redline_11.tStartRefresh)
thisExp.addData('redline_11.stopped', redline_11.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_12"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
# keep track of which components have finished
trial_12Components = [instructions_12, finished_12, key_resp_12, responses_12, blueline_12, redline_12]
for thisComponent in trial_12Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_12Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_12"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_12Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_12Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_12* updates
    if instructions_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_12.frameNStart = frameN  # exact frame index
        instructions_12.tStart = t  # local t and not account for scr refresh
        instructions_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_12, 'tStartRefresh')  # time at next scr refresh
        instructions_12.setAutoDraw(True)
    if instructions_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_12.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_12.tStop = t  # not accounting for scr refresh
            instructions_12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_12, 'tStopRefresh')  # time at next scr refresh
            instructions_12.setAutoDraw(False)
    
    # *finished_12* updates
    if finished_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_12.frameNStart = frameN  # exact frame index
        finished_12.tStart = t  # local t and not account for scr refresh
        finished_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_12, 'tStartRefresh')  # time at next scr refresh
        finished_12.setAutoDraw(True)
    if finished_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_12.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_12.tStop = t  # not accounting for scr refresh
            finished_12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_12, 'tStopRefresh')  # time at next scr refresh
            finished_12.setAutoDraw(False)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_12.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_12.tStop = t  # not accounting for scr refresh
            key_resp_12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_12, 'tStopRefresh')  # time at next scr refresh
            key_resp_12.status = FINISHED
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_12.setOri(3,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_12.setOri(3,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_12.setColor('black')
                redline_12.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_12.keys.append(theseKeys.name)  # storing all keys
            key_resp_12.rt.append(theseKeys.rt)
    
    # *responses_12* updates
    if responses_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_12.frameNStart = frameN  # exact frame index
        responses_12.tStart = t  # local t and not account for scr refresh
        responses_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_12, 'tStartRefresh')  # time at next scr refresh
        responses_12.setAutoDraw(True)
    if responses_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_12.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_12.tStop = t  # not accounting for scr refresh
            responses_12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_12, 'tStopRefresh')  # time at next scr refresh
            responses_12.setAutoDraw(False)
    
    # *blueline_12* updates
    if blueline_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_12.frameNStart = frameN  # exact frame index
        blueline_12.tStart = t  # local t and not account for scr refresh
        blueline_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_12, 'tStartRefresh')  # time at next scr refresh
        blueline_12.setAutoDraw(True)
    if blueline_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_12.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_12.tStop = t  # not accounting for scr refresh
            blueline_12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_12, 'tStopRefresh')  # time at next scr refresh
            blueline_12.setAutoDraw(False)
    
    # *redline_12* updates
    if redline_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_12.frameNStart = frameN  # exact frame index
        redline_12.tStart = t  # local t and not account for scr refresh
        redline_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_12, 'tStartRefresh')  # time at next scr refresh
        redline_12.setAutoDraw(True)
    if redline_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_12.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_12.tStop = t  # not accounting for scr refresh
            redline_12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_12, 'tStopRefresh')  # time at next scr refresh
            redline_12.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_12Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_12"-------
for thisComponent in trial_12Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_12.started', instructions_12.tStartRefresh)
thisExp.addData('instructions_12.stopped', instructions_12.tStopRefresh)
thisExp.addData('finished_12.started', finished_12.tStartRefresh)
thisExp.addData('finished_12.stopped', finished_12.tStopRefresh)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.addData('key_resp_12.started', key_resp_12.tStartRefresh)
thisExp.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_12.started', responses_12.tStartRefresh)
thisExp.addData('responses_12.stopped', responses_12.tStopRefresh)
thisExp.addData('blueline_12.started', blueline_12.tStartRefresh)
thisExp.addData('blueline_12.stopped', blueline_12.tStopRefresh)
thisExp.addData('redline_12.started', redline_12.tStartRefresh)
thisExp.addData('redline_12.stopped', redline_12.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_13"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_13.keys = []
key_resp_13.rt = []
# keep track of which components have finished
trial_13Components = [instructions_13, finished_13, key_resp_13, responses_13, blueline_13, redline_13]
for thisComponent in trial_13Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_13Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_13"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_13Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_13Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_13* updates
    if instructions_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_13.frameNStart = frameN  # exact frame index
        instructions_13.tStart = t  # local t and not account for scr refresh
        instructions_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_13, 'tStartRefresh')  # time at next scr refresh
        instructions_13.setAutoDraw(True)
    if instructions_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_13.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_13.tStop = t  # not accounting for scr refresh
            instructions_13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_13, 'tStopRefresh')  # time at next scr refresh
            instructions_13.setAutoDraw(False)
    
    # *finished_13* updates
    if finished_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_13.frameNStart = frameN  # exact frame index
        finished_13.tStart = t  # local t and not account for scr refresh
        finished_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_13, 'tStartRefresh')  # time at next scr refresh
        finished_13.setAutoDraw(True)
    if finished_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_13.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_13.tStop = t  # not accounting for scr refresh
            finished_13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_13, 'tStopRefresh')  # time at next scr refresh
            finished_13.setAutoDraw(False)
    
    # *key_resp_13* updates
    waitOnFlip = False
    if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.tStart = t  # local t and not account for scr refresh
        key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_13.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_13.tStop = t  # not accounting for scr refresh
            key_resp_13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_13, 'tStopRefresh')  # time at next scr refresh
            key_resp_13.status = FINISHED
    if key_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_13.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_13.setOri(3,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_13.setOri(3,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_13.setColor('black')
                redline_13.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_13.keys.append(theseKeys.name)  # storing all keys
            key_resp_13.rt.append(theseKeys.rt)
    
    # *responses_13* updates
    if responses_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_13.frameNStart = frameN  # exact frame index
        responses_13.tStart = t  # local t and not account for scr refresh
        responses_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_13, 'tStartRefresh')  # time at next scr refresh
        responses_13.setAutoDraw(True)
    if responses_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_13.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_13.tStop = t  # not accounting for scr refresh
            responses_13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_13, 'tStopRefresh')  # time at next scr refresh
            responses_13.setAutoDraw(False)
    
    # *blueline_13* updates
    if blueline_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_13.frameNStart = frameN  # exact frame index
        blueline_13.tStart = t  # local t and not account for scr refresh
        blueline_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_13, 'tStartRefresh')  # time at next scr refresh
        blueline_13.setAutoDraw(True)
    if blueline_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_13.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_13.tStop = t  # not accounting for scr refresh
            blueline_13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_13, 'tStopRefresh')  # time at next scr refresh
            blueline_13.setAutoDraw(False)
    
    # *redline_13* updates
    if redline_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_13.frameNStart = frameN  # exact frame index
        redline_13.tStart = t  # local t and not account for scr refresh
        redline_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_13, 'tStartRefresh')  # time at next scr refresh
        redline_13.setAutoDraw(True)
    if redline_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_13.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_13.tStop = t  # not accounting for scr refresh
            redline_13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_13, 'tStopRefresh')  # time at next scr refresh
            redline_13.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_13Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_13"-------
for thisComponent in trial_13Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_13.started', instructions_13.tStartRefresh)
thisExp.addData('instructions_13.stopped', instructions_13.tStopRefresh)
thisExp.addData('finished_13.started', finished_13.tStartRefresh)
thisExp.addData('finished_13.stopped', finished_13.tStopRefresh)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys = None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.addData('key_resp_13.started', key_resp_13.tStartRefresh)
thisExp.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_13.started', responses_13.tStartRefresh)
thisExp.addData('responses_13.stopped', responses_13.tStopRefresh)
thisExp.addData('blueline_13.started', blueline_13.tStartRefresh)
thisExp.addData('blueline_13.stopped', blueline_13.tStopRefresh)
thisExp.addData('redline_13.started', redline_13.tStartRefresh)
thisExp.addData('redline_13.stopped', redline_13.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_14"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_14.keys = []
key_resp_14.rt = []
# keep track of which components have finished
trial_14Components = [instructions_14, finished_14, key_resp_14, responses_14, blueline_14, redline_14]
for thisComponent in trial_14Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_14Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_14"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_14Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_14Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_14* updates
    if instructions_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_14.frameNStart = frameN  # exact frame index
        instructions_14.tStart = t  # local t and not account for scr refresh
        instructions_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_14, 'tStartRefresh')  # time at next scr refresh
        instructions_14.setAutoDraw(True)
    if instructions_14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_14.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_14.tStop = t  # not accounting for scr refresh
            instructions_14.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_14, 'tStopRefresh')  # time at next scr refresh
            instructions_14.setAutoDraw(False)
    
    # *finished_14* updates
    if finished_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_14.frameNStart = frameN  # exact frame index
        finished_14.tStart = t  # local t and not account for scr refresh
        finished_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_14, 'tStartRefresh')  # time at next scr refresh
        finished_14.setAutoDraw(True)
    if finished_14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_14.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_14.tStop = t  # not accounting for scr refresh
            finished_14.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_14, 'tStopRefresh')  # time at next scr refresh
            finished_14.setAutoDraw(False)
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_14.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_14.tStop = t  # not accounting for scr refresh
            key_resp_14.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_14, 'tStopRefresh')  # time at next scr refresh
            key_resp_14.status = FINISHED
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_14.setOri(9,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_14.setOri(9,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_14.setColor('black')
                redline_14.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_14.keys.append(theseKeys.name)  # storing all keys
            key_resp_14.rt.append(theseKeys.rt)
    
    # *responses_14* updates
    if responses_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_14.frameNStart = frameN  # exact frame index
        responses_14.tStart = t  # local t and not account for scr refresh
        responses_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_14, 'tStartRefresh')  # time at next scr refresh
        responses_14.setAutoDraw(True)
    if responses_14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_14.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_14.tStop = t  # not accounting for scr refresh
            responses_14.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_14, 'tStopRefresh')  # time at next scr refresh
            responses_14.setAutoDraw(False)
    
    # *blueline_14* updates
    if blueline_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_14.frameNStart = frameN  # exact frame index
        blueline_14.tStart = t  # local t and not account for scr refresh
        blueline_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_14, 'tStartRefresh')  # time at next scr refresh
        blueline_14.setAutoDraw(True)
    if blueline_14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_14.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_14.tStop = t  # not accounting for scr refresh
            blueline_14.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_14, 'tStopRefresh')  # time at next scr refresh
            blueline_14.setAutoDraw(False)
    
    # *redline_14* updates
    if redline_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_14.frameNStart = frameN  # exact frame index
        redline_14.tStart = t  # local t and not account for scr refresh
        redline_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_14, 'tStartRefresh')  # time at next scr refresh
        redline_14.setAutoDraw(True)
    if redline_14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_14.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_14.tStop = t  # not accounting for scr refresh
            redline_14.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_14, 'tStopRefresh')  # time at next scr refresh
            redline_14.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_14Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_14"-------
for thisComponent in trial_14Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_14.started', instructions_14.tStartRefresh)
thisExp.addData('instructions_14.stopped', instructions_14.tStopRefresh)
thisExp.addData('finished_14.started', finished_14.tStartRefresh)
thisExp.addData('finished_14.stopped', finished_14.tStopRefresh)
# check responses
if key_resp_14.keys in ['', [], None]:  # No response was made
    key_resp_14.keys = None
thisExp.addData('key_resp_14.keys',key_resp_14.keys)
if key_resp_14.keys != None:  # we had a response
    thisExp.addData('key_resp_14.rt', key_resp_14.rt)
thisExp.addData('key_resp_14.started', key_resp_14.tStartRefresh)
thisExp.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_14.started', responses_14.tStartRefresh)
thisExp.addData('responses_14.stopped', responses_14.tStopRefresh)
thisExp.addData('blueline_14.started', blueline_14.tStartRefresh)
thisExp.addData('blueline_14.stopped', blueline_14.tStopRefresh)
thisExp.addData('redline_14.started', redline_14.tStartRefresh)
thisExp.addData('redline_14.stopped', redline_14.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_15"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_15.keys = []
key_resp_15.rt = []
# keep track of which components have finished
trial_15Components = [instructions_15, finished_15, key_resp_15, responses_15, blueline_15, redline_15]
for thisComponent in trial_15Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_15Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_15"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_15Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_15Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_15* updates
    if instructions_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_15.frameNStart = frameN  # exact frame index
        instructions_15.tStart = t  # local t and not account for scr refresh
        instructions_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_15, 'tStartRefresh')  # time at next scr refresh
        instructions_15.setAutoDraw(True)
    if instructions_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_15.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_15.tStop = t  # not accounting for scr refresh
            instructions_15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_15, 'tStopRefresh')  # time at next scr refresh
            instructions_15.setAutoDraw(False)
    
    # *finished_15* updates
    if finished_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_15.frameNStart = frameN  # exact frame index
        finished_15.tStart = t  # local t and not account for scr refresh
        finished_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_15, 'tStartRefresh')  # time at next scr refresh
        finished_15.setAutoDraw(True)
    if finished_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_15.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_15.tStop = t  # not accounting for scr refresh
            finished_15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_15, 'tStopRefresh')  # time at next scr refresh
            finished_15.setAutoDraw(False)
    
    # *key_resp_15* updates
    waitOnFlip = False
    if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.tStart = t  # local t and not account for scr refresh
        key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_15.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_15.tStop = t  # not accounting for scr refresh
            key_resp_15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_15, 'tStopRefresh')  # time at next scr refresh
            key_resp_15.status = FINISHED
    if key_resp_15.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_15.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_15.setOri(9,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_15.setOri(9,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_15.setColor('black')
                redline_15.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_15.keys.append(theseKeys.name)  # storing all keys
            key_resp_15.rt.append(theseKeys.rt)
    
    # *responses_15* updates
    if responses_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_15.frameNStart = frameN  # exact frame index
        responses_15.tStart = t  # local t and not account for scr refresh
        responses_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_15, 'tStartRefresh')  # time at next scr refresh
        responses_15.setAutoDraw(True)
    if responses_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_15.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_15.tStop = t  # not accounting for scr refresh
            responses_15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_15, 'tStopRefresh')  # time at next scr refresh
            responses_15.setAutoDraw(False)
    
    # *blueline_15* updates
    if blueline_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_15.frameNStart = frameN  # exact frame index
        blueline_15.tStart = t  # local t and not account for scr refresh
        blueline_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_15, 'tStartRefresh')  # time at next scr refresh
        blueline_15.setAutoDraw(True)
    if blueline_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_15.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_15.tStop = t  # not accounting for scr refresh
            blueline_15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_15, 'tStopRefresh')  # time at next scr refresh
            blueline_15.setAutoDraw(False)
    
    # *redline_15* updates
    if redline_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_15.frameNStart = frameN  # exact frame index
        redline_15.tStart = t  # local t and not account for scr refresh
        redline_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_15, 'tStartRefresh')  # time at next scr refresh
        redline_15.setAutoDraw(True)
    if redline_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_15.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_15.tStop = t  # not accounting for scr refresh
            redline_15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_15, 'tStopRefresh')  # time at next scr refresh
            redline_15.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_15Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_15"-------
for thisComponent in trial_15Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_15.started', instructions_15.tStartRefresh)
thisExp.addData('instructions_15.stopped', instructions_15.tStopRefresh)
thisExp.addData('finished_15.started', finished_15.tStartRefresh)
thisExp.addData('finished_15.stopped', finished_15.tStopRefresh)
# check responses
if key_resp_15.keys in ['', [], None]:  # No response was made
    key_resp_15.keys = None
thisExp.addData('key_resp_15.keys',key_resp_15.keys)
if key_resp_15.keys != None:  # we had a response
    thisExp.addData('key_resp_15.rt', key_resp_15.rt)
thisExp.addData('key_resp_15.started', key_resp_15.tStartRefresh)
thisExp.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_15.started', responses_15.tStartRefresh)
thisExp.addData('responses_15.stopped', responses_15.tStopRefresh)
thisExp.addData('blueline_15.started', blueline_15.tStartRefresh)
thisExp.addData('blueline_15.stopped', blueline_15.tStopRefresh)
thisExp.addData('redline_15.started', redline_15.tStartRefresh)
thisExp.addData('redline_15.stopped', redline_15.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_16"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_16.keys = []
key_resp_16.rt = []
# keep track of which components have finished
trial_16Components = [instructions_16, finished_16, key_resp_16, responses_16, blueline_16, redline_16]
for thisComponent in trial_16Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_16Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_16"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_16Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_16Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_16* updates
    if instructions_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_16.frameNStart = frameN  # exact frame index
        instructions_16.tStart = t  # local t and not account for scr refresh
        instructions_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_16, 'tStartRefresh')  # time at next scr refresh
        instructions_16.setAutoDraw(True)
    if instructions_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_16.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_16.tStop = t  # not accounting for scr refresh
            instructions_16.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_16, 'tStopRefresh')  # time at next scr refresh
            instructions_16.setAutoDraw(False)
    
    # *finished_16* updates
    if finished_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_16.frameNStart = frameN  # exact frame index
        finished_16.tStart = t  # local t and not account for scr refresh
        finished_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_16, 'tStartRefresh')  # time at next scr refresh
        finished_16.setAutoDraw(True)
    if finished_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_16.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_16.tStop = t  # not accounting for scr refresh
            finished_16.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_16, 'tStopRefresh')  # time at next scr refresh
            finished_16.setAutoDraw(False)
    
    # *key_resp_16* updates
    waitOnFlip = False
    if key_resp_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_16.frameNStart = frameN  # exact frame index
        key_resp_16.tStart = t  # local t and not account for scr refresh
        key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
        key_resp_16.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_16.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_16.tStop = t  # not accounting for scr refresh
            key_resp_16.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_16, 'tStopRefresh')  # time at next scr refresh
            key_resp_16.status = FINISHED
    if key_resp_16.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_16.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_16.setOri(3,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_16.setOri(3,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_16.setColor('black')
                redline_16.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_16.keys.append(theseKeys.name)  # storing all keys
            key_resp_16.rt.append(theseKeys.rt)
    
    # *responses_16* updates
    if responses_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_16.frameNStart = frameN  # exact frame index
        responses_16.tStart = t  # local t and not account for scr refresh
        responses_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_16, 'tStartRefresh')  # time at next scr refresh
        responses_16.setAutoDraw(True)
    if responses_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_16.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_16.tStop = t  # not accounting for scr refresh
            responses_16.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_16, 'tStopRefresh')  # time at next scr refresh
            responses_16.setAutoDraw(False)
    
    # *blueline_16* updates
    if blueline_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_16.frameNStart = frameN  # exact frame index
        blueline_16.tStart = t  # local t and not account for scr refresh
        blueline_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_16, 'tStartRefresh')  # time at next scr refresh
        blueline_16.setAutoDraw(True)
    if blueline_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_16.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_16.tStop = t  # not accounting for scr refresh
            blueline_16.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_16, 'tStopRefresh')  # time at next scr refresh
            blueline_16.setAutoDraw(False)
    
    # *redline_16* updates
    if redline_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_16.frameNStart = frameN  # exact frame index
        redline_16.tStart = t  # local t and not account for scr refresh
        redline_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_16, 'tStartRefresh')  # time at next scr refresh
        redline_16.setAutoDraw(True)
    if redline_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_16.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_16.tStop = t  # not accounting for scr refresh
            redline_16.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_16, 'tStopRefresh')  # time at next scr refresh
            redline_16.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_16Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_16"-------
for thisComponent in trial_16Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_16.started', instructions_16.tStartRefresh)
thisExp.addData('instructions_16.stopped', instructions_16.tStopRefresh)
thisExp.addData('finished_16.started', finished_16.tStartRefresh)
thisExp.addData('finished_16.stopped', finished_16.tStopRefresh)
# check responses
if key_resp_16.keys in ['', [], None]:  # No response was made
    key_resp_16.keys = None
thisExp.addData('key_resp_16.keys',key_resp_16.keys)
if key_resp_16.keys != None:  # we had a response
    thisExp.addData('key_resp_16.rt', key_resp_16.rt)
thisExp.addData('key_resp_16.started', key_resp_16.tStartRefresh)
thisExp.addData('key_resp_16.stopped', key_resp_16.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_16.started', responses_16.tStartRefresh)
thisExp.addData('responses_16.stopped', responses_16.tStopRefresh)
thisExp.addData('blueline_16.started', blueline_16.tStartRefresh)
thisExp.addData('blueline_16.stopped', blueline_16.tStopRefresh)
thisExp.addData('redline_16.started', redline_16.tStartRefresh)
thisExp.addData('redline_16.stopped', redline_16.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_17"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_17.keys = []
key_resp_17.rt = []
# keep track of which components have finished
trial_17Components = [instructions_17, finished_17, key_resp_17, responses_17, blueline_17, redline_17]
for thisComponent in trial_17Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_17Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_17"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_17Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_17Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_17* updates
    if instructions_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_17.frameNStart = frameN  # exact frame index
        instructions_17.tStart = t  # local t and not account for scr refresh
        instructions_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_17, 'tStartRefresh')  # time at next scr refresh
        instructions_17.setAutoDraw(True)
    if instructions_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_17.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_17.tStop = t  # not accounting for scr refresh
            instructions_17.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_17, 'tStopRefresh')  # time at next scr refresh
            instructions_17.setAutoDraw(False)
    
    # *finished_17* updates
    if finished_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_17.frameNStart = frameN  # exact frame index
        finished_17.tStart = t  # local t and not account for scr refresh
        finished_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_17, 'tStartRefresh')  # time at next scr refresh
        finished_17.setAutoDraw(True)
    if finished_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_17.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_17.tStop = t  # not accounting for scr refresh
            finished_17.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_17, 'tStopRefresh')  # time at next scr refresh
            finished_17.setAutoDraw(False)
    
    # *key_resp_17* updates
    waitOnFlip = False
    if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_17.frameNStart = frameN  # exact frame index
        key_resp_17.tStart = t  # local t and not account for scr refresh
        key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
        key_resp_17.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_17.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_17.tStop = t  # not accounting for scr refresh
            key_resp_17.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_17, 'tStopRefresh')  # time at next scr refresh
            key_resp_17.status = FINISHED
    if key_resp_17.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_17.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_17.setOri(6,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_17.setOri(6,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_17.setColor('black')
                redline_17.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_17.keys.append(theseKeys.name)  # storing all keys
            key_resp_17.rt.append(theseKeys.rt)
    
    # *responses_17* updates
    if responses_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_17.frameNStart = frameN  # exact frame index
        responses_17.tStart = t  # local t and not account for scr refresh
        responses_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_17, 'tStartRefresh')  # time at next scr refresh
        responses_17.setAutoDraw(True)
    if responses_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_17.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_17.tStop = t  # not accounting for scr refresh
            responses_17.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_17, 'tStopRefresh')  # time at next scr refresh
            responses_17.setAutoDraw(False)
    
    # *blueline_17* updates
    if blueline_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_17.frameNStart = frameN  # exact frame index
        blueline_17.tStart = t  # local t and not account for scr refresh
        blueline_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_17, 'tStartRefresh')  # time at next scr refresh
        blueline_17.setAutoDraw(True)
    if blueline_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_17.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_17.tStop = t  # not accounting for scr refresh
            blueline_17.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_17, 'tStopRefresh')  # time at next scr refresh
            blueline_17.setAutoDraw(False)
    
    # *redline_17* updates
    if redline_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_17.frameNStart = frameN  # exact frame index
        redline_17.tStart = t  # local t and not account for scr refresh
        redline_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_17, 'tStartRefresh')  # time at next scr refresh
        redline_17.setAutoDraw(True)
    if redline_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_17.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_17.tStop = t  # not accounting for scr refresh
            redline_17.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_17, 'tStopRefresh')  # time at next scr refresh
            redline_17.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_17Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_17"-------
for thisComponent in trial_17Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_17.started', instructions_17.tStartRefresh)
thisExp.addData('instructions_17.stopped', instructions_17.tStopRefresh)
thisExp.addData('finished_17.started', finished_17.tStartRefresh)
thisExp.addData('finished_17.stopped', finished_17.tStopRefresh)
# check responses
if key_resp_17.keys in ['', [], None]:  # No response was made
    key_resp_17.keys = None
thisExp.addData('key_resp_17.keys',key_resp_17.keys)
if key_resp_17.keys != None:  # we had a response
    thisExp.addData('key_resp_17.rt', key_resp_17.rt)
thisExp.addData('key_resp_17.started', key_resp_17.tStartRefresh)
thisExp.addData('key_resp_17.stopped', key_resp_17.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_17.started', responses_17.tStartRefresh)
thisExp.addData('responses_17.stopped', responses_17.tStopRefresh)
thisExp.addData('blueline_17.started', blueline_17.tStartRefresh)
thisExp.addData('blueline_17.stopped', blueline_17.tStopRefresh)
thisExp.addData('redline_17.started', redline_17.tStartRefresh)
thisExp.addData('redline_17.stopped', redline_17.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_18"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_18.keys = []
key_resp_18.rt = []
# keep track of which components have finished
trial_18Components = [instructions_18, finished_18, key_resp_18, responses_18, blueline_18, redline_18]
for thisComponent in trial_18Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_18Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_18"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_18Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_18Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_18* updates
    if instructions_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_18.frameNStart = frameN  # exact frame index
        instructions_18.tStart = t  # local t and not account for scr refresh
        instructions_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_18, 'tStartRefresh')  # time at next scr refresh
        instructions_18.setAutoDraw(True)
    if instructions_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_18.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_18.tStop = t  # not accounting for scr refresh
            instructions_18.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_18, 'tStopRefresh')  # time at next scr refresh
            instructions_18.setAutoDraw(False)
    
    # *finished_18* updates
    if finished_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_18.frameNStart = frameN  # exact frame index
        finished_18.tStart = t  # local t and not account for scr refresh
        finished_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_18, 'tStartRefresh')  # time at next scr refresh
        finished_18.setAutoDraw(True)
    if finished_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_18.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_18.tStop = t  # not accounting for scr refresh
            finished_18.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_18, 'tStopRefresh')  # time at next scr refresh
            finished_18.setAutoDraw(False)
    
    # *key_resp_18* updates
    waitOnFlip = False
    if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_18.frameNStart = frameN  # exact frame index
        key_resp_18.tStart = t  # local t and not account for scr refresh
        key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_18.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_18.tStop = t  # not accounting for scr refresh
            key_resp_18.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_18, 'tStopRefresh')  # time at next scr refresh
            key_resp_18.status = FINISHED
    if key_resp_18.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_18.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_18.setOri(9,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_18.setOri(9,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_18.setColor('black')
                redline_18.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_18.keys.append(theseKeys.name)  # storing all keys
            key_resp_18.rt.append(theseKeys.rt)
    
    # *responses_18* updates
    if responses_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_18.frameNStart = frameN  # exact frame index
        responses_18.tStart = t  # local t and not account for scr refresh
        responses_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_18, 'tStartRefresh')  # time at next scr refresh
        responses_18.setAutoDraw(True)
    if responses_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_18.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_18.tStop = t  # not accounting for scr refresh
            responses_18.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_18, 'tStopRefresh')  # time at next scr refresh
            responses_18.setAutoDraw(False)
    
    # *blueline_18* updates
    if blueline_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_18.frameNStart = frameN  # exact frame index
        blueline_18.tStart = t  # local t and not account for scr refresh
        blueline_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_18, 'tStartRefresh')  # time at next scr refresh
        blueline_18.setAutoDraw(True)
    if blueline_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_18.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_18.tStop = t  # not accounting for scr refresh
            blueline_18.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_18, 'tStopRefresh')  # time at next scr refresh
            blueline_18.setAutoDraw(False)
    
    # *redline_18* updates
    if redline_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_18.frameNStart = frameN  # exact frame index
        redline_18.tStart = t  # local t and not account for scr refresh
        redline_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_18, 'tStartRefresh')  # time at next scr refresh
        redline_18.setAutoDraw(True)
    if redline_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_18.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_18.tStop = t  # not accounting for scr refresh
            redline_18.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_18, 'tStopRefresh')  # time at next scr refresh
            redline_18.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_18Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_18"-------
for thisComponent in trial_18Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_18.started', instructions_18.tStartRefresh)
thisExp.addData('instructions_18.stopped', instructions_18.tStopRefresh)
thisExp.addData('finished_18.started', finished_18.tStartRefresh)
thisExp.addData('finished_18.stopped', finished_18.tStopRefresh)
# check responses
if key_resp_18.keys in ['', [], None]:  # No response was made
    key_resp_18.keys = None
thisExp.addData('key_resp_18.keys',key_resp_18.keys)
if key_resp_18.keys != None:  # we had a response
    thisExp.addData('key_resp_18.rt', key_resp_18.rt)
thisExp.addData('key_resp_18.started', key_resp_18.tStartRefresh)
thisExp.addData('key_resp_18.stopped', key_resp_18.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_18.started', responses_18.tStartRefresh)
thisExp.addData('responses_18.stopped', responses_18.tStopRefresh)
thisExp.addData('blueline_18.started', blueline_18.tStartRefresh)
thisExp.addData('blueline_18.stopped', blueline_18.tStopRefresh)
thisExp.addData('redline_18.started', redline_18.tStartRefresh)
thisExp.addData('redline_18.stopped', redline_18.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_19"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_19.keys = []
key_resp_19.rt = []
# keep track of which components have finished
trial_19Components = [instructions_19, finished_19, key_resp_19, responses_19, blueline_19, redline_19]
for thisComponent in trial_19Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_19Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_19"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_19Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_19Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_19* updates
    if instructions_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_19.frameNStart = frameN  # exact frame index
        instructions_19.tStart = t  # local t and not account for scr refresh
        instructions_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_19, 'tStartRefresh')  # time at next scr refresh
        instructions_19.setAutoDraw(True)
    if instructions_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_19.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_19.tStop = t  # not accounting for scr refresh
            instructions_19.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_19, 'tStopRefresh')  # time at next scr refresh
            instructions_19.setAutoDraw(False)
    
    # *finished_19* updates
    if finished_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_19.frameNStart = frameN  # exact frame index
        finished_19.tStart = t  # local t and not account for scr refresh
        finished_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_19, 'tStartRefresh')  # time at next scr refresh
        finished_19.setAutoDraw(True)
    if finished_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_19.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_19.tStop = t  # not accounting for scr refresh
            finished_19.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_19, 'tStopRefresh')  # time at next scr refresh
            finished_19.setAutoDraw(False)
    
    # *key_resp_19* updates
    waitOnFlip = False
    if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_19.frameNStart = frameN  # exact frame index
        key_resp_19.tStart = t  # local t and not account for scr refresh
        key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
        key_resp_19.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_19.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_19.tStop = t  # not accounting for scr refresh
            key_resp_19.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_19, 'tStopRefresh')  # time at next scr refresh
            key_resp_19.status = FINISHED
    if key_resp_19.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_19.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_19.setOri(6,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_19.setOri(6,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_19.setColor('black')
                redline_19.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_19.keys.append(theseKeys.name)  # storing all keys
            key_resp_19.rt.append(theseKeys.rt)
    
    # *responses_19* updates
    if responses_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_19.frameNStart = frameN  # exact frame index
        responses_19.tStart = t  # local t and not account for scr refresh
        responses_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_19, 'tStartRefresh')  # time at next scr refresh
        responses_19.setAutoDraw(True)
    if responses_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_19.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_19.tStop = t  # not accounting for scr refresh
            responses_19.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_19, 'tStopRefresh')  # time at next scr refresh
            responses_19.setAutoDraw(False)
    
    # *blueline_19* updates
    if blueline_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_19.frameNStart = frameN  # exact frame index
        blueline_19.tStart = t  # local t and not account for scr refresh
        blueline_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_19, 'tStartRefresh')  # time at next scr refresh
        blueline_19.setAutoDraw(True)
    if blueline_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_19.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_19.tStop = t  # not accounting for scr refresh
            blueline_19.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_19, 'tStopRefresh')  # time at next scr refresh
            blueline_19.setAutoDraw(False)
    
    # *redline_19* updates
    if redline_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_19.frameNStart = frameN  # exact frame index
        redline_19.tStart = t  # local t and not account for scr refresh
        redline_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_19, 'tStartRefresh')  # time at next scr refresh
        redline_19.setAutoDraw(True)
    if redline_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_19.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_19.tStop = t  # not accounting for scr refresh
            redline_19.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_19, 'tStopRefresh')  # time at next scr refresh
            redline_19.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_19Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_19"-------
for thisComponent in trial_19Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_19.started', instructions_19.tStartRefresh)
thisExp.addData('instructions_19.stopped', instructions_19.tStopRefresh)
thisExp.addData('finished_19.started', finished_19.tStartRefresh)
thisExp.addData('finished_19.stopped', finished_19.tStopRefresh)
# check responses
if key_resp_19.keys in ['', [], None]:  # No response was made
    key_resp_19.keys = None
thisExp.addData('key_resp_19.keys',key_resp_19.keys)
if key_resp_19.keys != None:  # we had a response
    thisExp.addData('key_resp_19.rt', key_resp_19.rt)
thisExp.addData('key_resp_19.started', key_resp_19.tStartRefresh)
thisExp.addData('key_resp_19.stopped', key_resp_19.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_19.started', responses_19.tStartRefresh)
thisExp.addData('responses_19.stopped', responses_19.tStopRefresh)
thisExp.addData('blueline_19.started', blueline_19.tStartRefresh)
thisExp.addData('blueline_19.stopped', blueline_19.tStopRefresh)
thisExp.addData('redline_19.started', redline_19.tStartRefresh)
thisExp.addData('redline_19.stopped', redline_19.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_20"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_20.keys = []
key_resp_20.rt = []
# keep track of which components have finished
trial_20Components = [instructions_20, finished_20, key_resp_20, responses_20, blueline_20, redline_20]
for thisComponent in trial_20Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_20Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_20"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_20Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_20Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_20* updates
    if instructions_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_20.frameNStart = frameN  # exact frame index
        instructions_20.tStart = t  # local t and not account for scr refresh
        instructions_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_20, 'tStartRefresh')  # time at next scr refresh
        instructions_20.setAutoDraw(True)
    if instructions_20.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_20.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_20.tStop = t  # not accounting for scr refresh
            instructions_20.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_20, 'tStopRefresh')  # time at next scr refresh
            instructions_20.setAutoDraw(False)
    
    # *finished_20* updates
    if finished_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_20.frameNStart = frameN  # exact frame index
        finished_20.tStart = t  # local t and not account for scr refresh
        finished_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_20, 'tStartRefresh')  # time at next scr refresh
        finished_20.setAutoDraw(True)
    if finished_20.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_20.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_20.tStop = t  # not accounting for scr refresh
            finished_20.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_20, 'tStopRefresh')  # time at next scr refresh
            finished_20.setAutoDraw(False)
    
    # *key_resp_20* updates
    waitOnFlip = False
    if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_20.frameNStart = frameN  # exact frame index
        key_resp_20.tStart = t  # local t and not account for scr refresh
        key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
        key_resp_20.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_20.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_20.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_20.tStop = t  # not accounting for scr refresh
            key_resp_20.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_20, 'tStopRefresh')  # time at next scr refresh
            key_resp_20.status = FINISHED
    if key_resp_20.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_20.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_20.setOri(6,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_20.setOri(6,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_20.setColor('black')
                redline_20.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_20.keys.append(theseKeys.name)  # storing all keys
            key_resp_20.rt.append(theseKeys.rt)
    
    # *responses_20* updates
    if responses_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_20.frameNStart = frameN  # exact frame index
        responses_20.tStart = t  # local t and not account for scr refresh
        responses_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_20, 'tStartRefresh')  # time at next scr refresh
        responses_20.setAutoDraw(True)
    if responses_20.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_20.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_20.tStop = t  # not accounting for scr refresh
            responses_20.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_20, 'tStopRefresh')  # time at next scr refresh
            responses_20.setAutoDraw(False)
    
    # *blueline_20* updates
    if blueline_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_20.frameNStart = frameN  # exact frame index
        blueline_20.tStart = t  # local t and not account for scr refresh
        blueline_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_20, 'tStartRefresh')  # time at next scr refresh
        blueline_20.setAutoDraw(True)
    if blueline_20.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_20.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_20.tStop = t  # not accounting for scr refresh
            blueline_20.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_20, 'tStopRefresh')  # time at next scr refresh
            blueline_20.setAutoDraw(False)
    
    # *redline_20* updates
    if redline_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_20.frameNStart = frameN  # exact frame index
        redline_20.tStart = t  # local t and not account for scr refresh
        redline_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_20, 'tStartRefresh')  # time at next scr refresh
        redline_20.setAutoDraw(True)
    if redline_20.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_20.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_20.tStop = t  # not accounting for scr refresh
            redline_20.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_20, 'tStopRefresh')  # time at next scr refresh
            redline_20.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_20Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_20"-------
for thisComponent in trial_20Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_20.started', instructions_20.tStartRefresh)
thisExp.addData('instructions_20.stopped', instructions_20.tStopRefresh)
thisExp.addData('finished_20.started', finished_20.tStartRefresh)
thisExp.addData('finished_20.stopped', finished_20.tStopRefresh)
# check responses
if key_resp_20.keys in ['', [], None]:  # No response was made
    key_resp_20.keys = None
thisExp.addData('key_resp_20.keys',key_resp_20.keys)
if key_resp_20.keys != None:  # we had a response
    thisExp.addData('key_resp_20.rt', key_resp_20.rt)
thisExp.addData('key_resp_20.started', key_resp_20.tStartRefresh)
thisExp.addData('key_resp_20.stopped', key_resp_20.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_20.started', responses_20.tStartRefresh)
thisExp.addData('responses_20.stopped', responses_20.tStopRefresh)
thisExp.addData('blueline_20.started', blueline_20.tStartRefresh)
thisExp.addData('blueline_20.stopped', blueline_20.tStopRefresh)
thisExp.addData('redline_20.started', redline_20.tStartRefresh)
thisExp.addData('redline_20.stopped', redline_20.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_21"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_21.keys = []
key_resp_21.rt = []
# keep track of which components have finished
trial_21Components = [instructions_21, finished_21, key_resp_21, responses_21, blueline_21, redline_21]
for thisComponent in trial_21Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_21Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_21"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_21Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_21Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_21* updates
    if instructions_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_21.frameNStart = frameN  # exact frame index
        instructions_21.tStart = t  # local t and not account for scr refresh
        instructions_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_21, 'tStartRefresh')  # time at next scr refresh
        instructions_21.setAutoDraw(True)
    if instructions_21.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_21.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_21.tStop = t  # not accounting for scr refresh
            instructions_21.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_21, 'tStopRefresh')  # time at next scr refresh
            instructions_21.setAutoDraw(False)
    
    # *finished_21* updates
    if finished_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_21.frameNStart = frameN  # exact frame index
        finished_21.tStart = t  # local t and not account for scr refresh
        finished_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_21, 'tStartRefresh')  # time at next scr refresh
        finished_21.setAutoDraw(True)
    if finished_21.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_21.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_21.tStop = t  # not accounting for scr refresh
            finished_21.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_21, 'tStopRefresh')  # time at next scr refresh
            finished_21.setAutoDraw(False)
    
    # *key_resp_21* updates
    waitOnFlip = False
    if key_resp_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_21.frameNStart = frameN  # exact frame index
        key_resp_21.tStart = t  # local t and not account for scr refresh
        key_resp_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_21, 'tStartRefresh')  # time at next scr refresh
        key_resp_21.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_21.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_21.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_21.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_21.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_21.tStop = t  # not accounting for scr refresh
            key_resp_21.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_21, 'tStopRefresh')  # time at next scr refresh
            key_resp_21.status = FINISHED
    if key_resp_21.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_21.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_21.setOri(9,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_21.setOri(9,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_21.setColor('black')
                redline_21.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_21.keys.append(theseKeys.name)  # storing all keys
            key_resp_21.rt.append(theseKeys.rt)
    
    # *responses_21* updates
    if responses_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_21.frameNStart = frameN  # exact frame index
        responses_21.tStart = t  # local t and not account for scr refresh
        responses_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_21, 'tStartRefresh')  # time at next scr refresh
        responses_21.setAutoDraw(True)
    if responses_21.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_21.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_21.tStop = t  # not accounting for scr refresh
            responses_21.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_21, 'tStopRefresh')  # time at next scr refresh
            responses_21.setAutoDraw(False)
    
    # *blueline_21* updates
    if blueline_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_21.frameNStart = frameN  # exact frame index
        blueline_21.tStart = t  # local t and not account for scr refresh
        blueline_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_21, 'tStartRefresh')  # time at next scr refresh
        blueline_21.setAutoDraw(True)
    if blueline_21.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_21.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_21.tStop = t  # not accounting for scr refresh
            blueline_21.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_21, 'tStopRefresh')  # time at next scr refresh
            blueline_21.setAutoDraw(False)
    
    # *redline_21* updates
    if redline_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_21.frameNStart = frameN  # exact frame index
        redline_21.tStart = t  # local t and not account for scr refresh
        redline_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_21, 'tStartRefresh')  # time at next scr refresh
        redline_21.setAutoDraw(True)
    if redline_21.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_21.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_21.tStop = t  # not accounting for scr refresh
            redline_21.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_21, 'tStopRefresh')  # time at next scr refresh
            redline_21.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_21Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_21"-------
for thisComponent in trial_21Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_21.started', instructions_21.tStartRefresh)
thisExp.addData('instructions_21.stopped', instructions_21.tStopRefresh)
thisExp.addData('finished_21.started', finished_21.tStartRefresh)
thisExp.addData('finished_21.stopped', finished_21.tStopRefresh)
# check responses
if key_resp_21.keys in ['', [], None]:  # No response was made
    key_resp_21.keys = None
thisExp.addData('key_resp_21.keys',key_resp_21.keys)
if key_resp_21.keys != None:  # we had a response
    thisExp.addData('key_resp_21.rt', key_resp_21.rt)
thisExp.addData('key_resp_21.started', key_resp_21.tStartRefresh)
thisExp.addData('key_resp_21.stopped', key_resp_21.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_21.started', responses_21.tStartRefresh)
thisExp.addData('responses_21.stopped', responses_21.tStopRefresh)
thisExp.addData('blueline_21.started', blueline_21.tStartRefresh)
thisExp.addData('blueline_21.stopped', blueline_21.tStopRefresh)
thisExp.addData('redline_21.started', redline_21.tStartRefresh)
thisExp.addData('redline_21.stopped', redline_21.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_22"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_22.keys = []
key_resp_22.rt = []
# keep track of which components have finished
trial_22Components = [instructions_22, finished_22, key_resp_22, responses_22, blueline_22, redline_22]
for thisComponent in trial_22Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_22Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_22"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_22Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_22Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_22* updates
    if instructions_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_22.frameNStart = frameN  # exact frame index
        instructions_22.tStart = t  # local t and not account for scr refresh
        instructions_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_22, 'tStartRefresh')  # time at next scr refresh
        instructions_22.setAutoDraw(True)
    if instructions_22.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_22.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_22.tStop = t  # not accounting for scr refresh
            instructions_22.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_22, 'tStopRefresh')  # time at next scr refresh
            instructions_22.setAutoDraw(False)
    
    # *finished_22* updates
    if finished_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_22.frameNStart = frameN  # exact frame index
        finished_22.tStart = t  # local t and not account for scr refresh
        finished_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_22, 'tStartRefresh')  # time at next scr refresh
        finished_22.setAutoDraw(True)
    if finished_22.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_22.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_22.tStop = t  # not accounting for scr refresh
            finished_22.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_22, 'tStopRefresh')  # time at next scr refresh
            finished_22.setAutoDraw(False)
    
    # *key_resp_22* updates
    waitOnFlip = False
    if key_resp_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_22.frameNStart = frameN  # exact frame index
        key_resp_22.tStart = t  # local t and not account for scr refresh
        key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
        key_resp_22.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_22.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_22.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_22.tStop = t  # not accounting for scr refresh
            key_resp_22.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_22, 'tStopRefresh')  # time at next scr refresh
            key_resp_22.status = FINISHED
    if key_resp_22.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_22.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_22.setOri(3,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_22.setOri(3,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_22.setColor('black')
                redline_22.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_22.keys.append(theseKeys.name)  # storing all keys
            key_resp_22.rt.append(theseKeys.rt)
    
    # *responses_22* updates
    if responses_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_22.frameNStart = frameN  # exact frame index
        responses_22.tStart = t  # local t and not account for scr refresh
        responses_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_22, 'tStartRefresh')  # time at next scr refresh
        responses_22.setAutoDraw(True)
    if responses_22.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_22.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_22.tStop = t  # not accounting for scr refresh
            responses_22.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_22, 'tStopRefresh')  # time at next scr refresh
            responses_22.setAutoDraw(False)
    
    # *blueline_22* updates
    if blueline_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_22.frameNStart = frameN  # exact frame index
        blueline_22.tStart = t  # local t and not account for scr refresh
        blueline_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_22, 'tStartRefresh')  # time at next scr refresh
        blueline_22.setAutoDraw(True)
    if blueline_22.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_22.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_22.tStop = t  # not accounting for scr refresh
            blueline_22.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_22, 'tStopRefresh')  # time at next scr refresh
            blueline_22.setAutoDraw(False)
    
    # *redline_22* updates
    if redline_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_22.frameNStart = frameN  # exact frame index
        redline_22.tStart = t  # local t and not account for scr refresh
        redline_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_22, 'tStartRefresh')  # time at next scr refresh
        redline_22.setAutoDraw(True)
    if redline_22.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_22.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_22.tStop = t  # not accounting for scr refresh
            redline_22.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_22, 'tStopRefresh')  # time at next scr refresh
            redline_22.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_22Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_22"-------
for thisComponent in trial_22Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_22.started', instructions_22.tStartRefresh)
thisExp.addData('instructions_22.stopped', instructions_22.tStopRefresh)
thisExp.addData('finished_22.started', finished_22.tStartRefresh)
thisExp.addData('finished_22.stopped', finished_22.tStopRefresh)
# check responses
if key_resp_22.keys in ['', [], None]:  # No response was made
    key_resp_22.keys = None
thisExp.addData('key_resp_22.keys',key_resp_22.keys)
if key_resp_22.keys != None:  # we had a response
    thisExp.addData('key_resp_22.rt', key_resp_22.rt)
thisExp.addData('key_resp_22.started', key_resp_22.tStartRefresh)
thisExp.addData('key_resp_22.stopped', key_resp_22.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_22.started', responses_22.tStartRefresh)
thisExp.addData('responses_22.stopped', responses_22.tStopRefresh)
thisExp.addData('blueline_22.started', blueline_22.tStartRefresh)
thisExp.addData('blueline_22.stopped', blueline_22.tStopRefresh)
thisExp.addData('redline_22.started', redline_22.tStartRefresh)
thisExp.addData('redline_22.stopped', redline_22.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_23"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_23.keys = []
key_resp_23.rt = []
# keep track of which components have finished
trial_23Components = [instructions_23, finished_23, key_resp_23, responses_23, blueline_23, redline_23]
for thisComponent in trial_23Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_23Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_23"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_23Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_23Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_23* updates
    if instructions_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_23.frameNStart = frameN  # exact frame index
        instructions_23.tStart = t  # local t and not account for scr refresh
        instructions_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_23, 'tStartRefresh')  # time at next scr refresh
        instructions_23.setAutoDraw(True)
    if instructions_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_23.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_23.tStop = t  # not accounting for scr refresh
            instructions_23.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_23, 'tStopRefresh')  # time at next scr refresh
            instructions_23.setAutoDraw(False)
    
    # *finished_23* updates
    if finished_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_23.frameNStart = frameN  # exact frame index
        finished_23.tStart = t  # local t and not account for scr refresh
        finished_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_23, 'tStartRefresh')  # time at next scr refresh
        finished_23.setAutoDraw(True)
    if finished_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_23.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_23.tStop = t  # not accounting for scr refresh
            finished_23.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_23, 'tStopRefresh')  # time at next scr refresh
            finished_23.setAutoDraw(False)
    
    # *key_resp_23* updates
    waitOnFlip = False
    if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_23.frameNStart = frameN  # exact frame index
        key_resp_23.tStart = t  # local t and not account for scr refresh
        key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
        key_resp_23.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_23.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_23.tStop = t  # not accounting for scr refresh
            key_resp_23.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_23, 'tStopRefresh')  # time at next scr refresh
            key_resp_23.status = FINISHED
    if key_resp_23.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_23.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_23.setOri(3,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_23.setOri(3,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_23.setColor('black')
                redline_23.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_23.keys.append(theseKeys.name)  # storing all keys
            key_resp_23.rt.append(theseKeys.rt)
    
    # *responses_23* updates
    if responses_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_23.frameNStart = frameN  # exact frame index
        responses_23.tStart = t  # local t and not account for scr refresh
        responses_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_23, 'tStartRefresh')  # time at next scr refresh
        responses_23.setAutoDraw(True)
    if responses_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_23.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_23.tStop = t  # not accounting for scr refresh
            responses_23.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_23, 'tStopRefresh')  # time at next scr refresh
            responses_23.setAutoDraw(False)
    
    # *blueline_23* updates
    if blueline_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_23.frameNStart = frameN  # exact frame index
        blueline_23.tStart = t  # local t and not account for scr refresh
        blueline_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_23, 'tStartRefresh')  # time at next scr refresh
        blueline_23.setAutoDraw(True)
    if blueline_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_23.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_23.tStop = t  # not accounting for scr refresh
            blueline_23.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_23, 'tStopRefresh')  # time at next scr refresh
            blueline_23.setAutoDraw(False)
    
    # *redline_23* updates
    if redline_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_23.frameNStart = frameN  # exact frame index
        redline_23.tStart = t  # local t and not account for scr refresh
        redline_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_23, 'tStartRefresh')  # time at next scr refresh
        redline_23.setAutoDraw(True)
    if redline_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_23.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_23.tStop = t  # not accounting for scr refresh
            redline_23.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_23, 'tStopRefresh')  # time at next scr refresh
            redline_23.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_23Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_23"-------
for thisComponent in trial_23Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_23.started', instructions_23.tStartRefresh)
thisExp.addData('instructions_23.stopped', instructions_23.tStopRefresh)
thisExp.addData('finished_23.started', finished_23.tStartRefresh)
thisExp.addData('finished_23.stopped', finished_23.tStopRefresh)
# check responses
if key_resp_23.keys in ['', [], None]:  # No response was made
    key_resp_23.keys = None
thisExp.addData('key_resp_23.keys',key_resp_23.keys)
if key_resp_23.keys != None:  # we had a response
    thisExp.addData('key_resp_23.rt', key_resp_23.rt)
thisExp.addData('key_resp_23.started', key_resp_23.tStartRefresh)
thisExp.addData('key_resp_23.stopped', key_resp_23.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_23.started', responses_23.tStartRefresh)
thisExp.addData('responses_23.stopped', responses_23.tStopRefresh)
thisExp.addData('blueline_23.started', blueline_23.tStartRefresh)
thisExp.addData('blueline_23.stopped', blueline_23.tStopRefresh)
thisExp.addData('redline_23.started', redline_23.tStartRefresh)
thisExp.addData('redline_23.stopped', redline_23.tStopRefresh)

# ------Prepare to start Routine "jitter"-------
# update component parameters for each repeat
current_jitter = jitters.pop()
thisExp.addData('jitter', current_jitter)
# keep track of which components have finished
jitterComponents = [fixation_2]
for thisComponent in jitterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "jitter"-------
while continueRoutine:
    # get current time
    t = jitterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=jitterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + current_jitter-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "jitter"-------
for thisComponent in jitterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
# the Routine "jitter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_24"-------
routineTimer.add(11.000000)
# update component parameters for each repeat
key_resp_24.keys = []
key_resp_24.rt = []
# keep track of which components have finished
trial_24Components = [instructions_24, finished_24, key_resp_24, responses_24, blueline_24, redline_24]
for thisComponent in trial_24Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_24Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_24"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trial_24Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_24Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_24* updates
    if instructions_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_24.frameNStart = frameN  # exact frame index
        instructions_24.tStart = t  # local t and not account for scr refresh
        instructions_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_24, 'tStartRefresh')  # time at next scr refresh
        instructions_24.setAutoDraw(True)
    if instructions_24.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_24.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            instructions_24.tStop = t  # not accounting for scr refresh
            instructions_24.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_24, 'tStopRefresh')  # time at next scr refresh
            instructions_24.setAutoDraw(False)
    
    # *finished_24* updates
    if finished_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_24.frameNStart = frameN  # exact frame index
        finished_24.tStart = t  # local t and not account for scr refresh
        finished_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_24, 'tStartRefresh')  # time at next scr refresh
        finished_24.setAutoDraw(True)
    if finished_24.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finished_24.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            finished_24.tStop = t  # not accounting for scr refresh
            finished_24.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finished_24, 'tStopRefresh')  # time at next scr refresh
            finished_24.setAutoDraw(False)
    
    # *key_resp_24* updates
    waitOnFlip = False
    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.tStart = t  # local t and not account for scr refresh
        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_24.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_24.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_24.tStop = t  # not accounting for scr refresh
            key_resp_24.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_24, 'tStopRefresh')  # time at next scr refresh
            key_resp_24.status = FINISHED
    if key_resp_24.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_24.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_24.setOri(6,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_24.setOri(6,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_24.setColor('black')
                redline_24.setColor('black')
                win.flip()
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
            key_resp_24.keys.append(theseKeys.name)  # storing all keys
            key_resp_24.rt.append(theseKeys.rt)
    
    # *responses_24* updates
    if responses_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responses_24.frameNStart = frameN  # exact frame index
        responses_24.tStart = t  # local t and not account for scr refresh
        responses_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responses_24, 'tStartRefresh')  # time at next scr refresh
        responses_24.setAutoDraw(True)
    if responses_24.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > responses_24.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            responses_24.tStop = t  # not accounting for scr refresh
            responses_24.frameNStop = frameN  # exact frame index
            win.timeOnFlip(responses_24, 'tStopRefresh')  # time at next scr refresh
            responses_24.setAutoDraw(False)
    
    # *blueline_24* updates
    if blueline_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_24.frameNStart = frameN  # exact frame index
        blueline_24.tStart = t  # local t and not account for scr refresh
        blueline_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_24, 'tStartRefresh')  # time at next scr refresh
        blueline_24.setAutoDraw(True)
    if blueline_24.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blueline_24.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            blueline_24.tStop = t  # not accounting for scr refresh
            blueline_24.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blueline_24, 'tStopRefresh')  # time at next scr refresh
            blueline_24.setAutoDraw(False)
    
    # *redline_24* updates
    if redline_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_24.frameNStart = frameN  # exact frame index
        redline_24.tStart = t  # local t and not account for scr refresh
        redline_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_24, 'tStartRefresh')  # time at next scr refresh
        redline_24.setAutoDraw(True)
    if redline_24.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > redline_24.tStartRefresh + 11-frameTolerance:
            # keep track of stop time/frame for later
            redline_24.tStop = t  # not accounting for scr refresh
            redline_24.frameNStop = frameN  # exact frame index
            win.timeOnFlip(redline_24, 'tStopRefresh')  # time at next scr refresh
            redline_24.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_24Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_24"-------
for thisComponent in trial_24Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_24.started', instructions_24.tStartRefresh)
thisExp.addData('instructions_24.stopped', instructions_24.tStopRefresh)
thisExp.addData('finished_24.started', finished_24.tStartRefresh)
thisExp.addData('finished_24.stopped', finished_24.tStopRefresh)
# check responses
if key_resp_24.keys in ['', [], None]:  # No response was made
    key_resp_24.keys = None
thisExp.addData('key_resp_24.keys',key_resp_24.keys)
if key_resp_24.keys != None:  # we had a response
    thisExp.addData('key_resp_24.rt', key_resp_24.rt)
thisExp.addData('key_resp_24.started', key_resp_24.tStartRefresh)
thisExp.addData('key_resp_24.stopped', key_resp_24.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('responses_24.started', responses_24.tStartRefresh)
thisExp.addData('responses_24.stopped', responses_24.tStopRefresh)
thisExp.addData('blueline_24.started', blueline_24.tStartRefresh)
thisExp.addData('blueline_24.stopped', blueline_24.tStopRefresh)
thisExp.addData('redline_24.started', redline_24.tStartRefresh)
thisExp.addData('redline_24.stopped', redline_24.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
