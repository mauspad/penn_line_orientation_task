#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on May 12, 2021, at 10:53
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

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
expName = 'PLOT behavioral full practice'  # from the Builder filename that created this script
expInfo = {'participant': ''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\mauspad\\Desktop\\line_orientation_scan\\PLOT_behavioral\\full_practice.py',
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
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='cm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instr1 = visual.ImageStim(
    win=win,
    name='instr1', units='pix', 
    image='images/instr1.png', mask=None,
    ori=0, pos=(0, 0), size=(1101, 690),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
enter = keyboard.Keyboard()

# Initialize components for Routine "instructions_2"
instructions_2Clock = core.Clock()
instr2 = visual.ImageStim(
    win=win,
    name='instr2', units='pix', 
    image='images/instr2.png', mask=None,
    ori=0, pos=(0, 0), size=(1101, 690),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
enter2 = keyboard.Keyboard()

# Initialize components for Routine "practice_1"
practice_1Clock = core.Clock()
blueline = visual.Line(
    win=win, name='blueline',
    start=(-[2, 1][0]/2.0, 0), end=(+[2, 1][0]/2.0, 0),
    ori=-120, pos=(12, 9),
    lineWidth=3, lineColor='blue', lineColorSpace='rgb',
    fillColor='blue', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
redline = visual.Line(
    win=win, name='redline',
    start=(-[2, 1][0]/2.0, 0), end=(+[2, 1][0]/2.0, 0),
    ori=120, pos=(-12, 9),
    lineWidth=3, lineColor='red', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
button_instrL = visual.TextStim(win=win, name='button_instrL',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    pos=(-13, -9), height=0.8, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
button_instrR = visual.TextStim(win=win, name='button_instrR',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    pos=(13, -9), height=0.8, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
buttons_trial = visual.ImageStim(
    win=win,
    name='buttons_trial', 
    image='images/practice4.jpg', mask=None,
    ori=0, pos=(0, -9), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
key_resp = keyboard.Keyboard()
your_mouse = event.Mouse(visible = False)
blue_correct = visual.Line(
    win=win, name='blue_correct',
    start=(-[4, 1][0]/2.0, 0), end=(+[4, 1][0]/2.0, 0),
    ori=120, pos=(12, 9),
    lineWidth=9, lineColor='yellow', lineColorSpace='rgb',
    fillColor='yellow', fillColorSpace='rgb',
    opacity=0, depth=-7.0, interpolate=True)
red_correct = visual.Line(
    win=win, name='red_correct',
    start=(-[4, 1][0]/2.0, 0), end=(+[4, 1][0]/2.0, 0),
    ori=120, pos=(-12, 9),
    lineWidth=9, lineColor='yellow', lineColorSpace='rgb',
    fillColor='yellow', fillColorSpace='rgb',
    opacity=0, depth=-8.0, interpolate=True)
paralleltext = visual.TextStim(win=win, name='paralleltext',
    text='See how the lines are parallel?',
    font='Arial',
    pos=(0, 20), height=0.8, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
goodjob = visual.TextStim(win=win, name='goodjob',
    text='GOOD JOB!',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practice_2"
practice_2Clock = core.Clock()
blueline_2 = visual.Line(
    win=win, name='blueline_2',
    start=(-[2, 1][0]/2.0, 0), end=(+[2, 1][0]/2.0, 0),
    ori=100, pos=(9, 9),
    lineWidth=3, lineColor='blue', lineColorSpace='rgb',
    fillColor='blue', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
redline_2 = visual.Line(
    win=win, name='redline_2',
    start=(-[2, 1][0]/2.0, 0), end=(+[2, 1][0]/2.0, 0),
    ori=80, pos=(-7, -2),
    lineWidth=3, lineColor='red', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
button_instrL_2 = visual.TextStim(win=win, name='button_instrL_2',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    pos=(-13, -9), height=0.8, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
button_instrR_2 = visual.TextStim(win=win, name='button_instrR_2',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    pos=(13, -9), height=0.8, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
buttons_trial_2 = visual.ImageStim(
    win=win,
    name='buttons_trial_2', 
    image='images/practice4.jpg', mask=None,
    ori=0, pos=(0, -9), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
key_resp_2 = keyboard.Keyboard()
your_mouse = event.Mouse(visible = False)
blue_correct_2 = visual.Line(
    win=win, name='blue_correct_2',
    start=(-[4, 1][0]/2.0, 0), end=(+[4, 1][0]/2.0, 0),
    ori=80, pos=(9, 9),
    lineWidth=9, lineColor='yellow', lineColorSpace='rgb',
    fillColor='yellow', fillColorSpace='rgb',
    opacity=0, depth=-7.0, interpolate=True)
red_correct_2 = visual.Line(
    win=win, name='red_correct_2',
    start=(-[4, 1][0]/2.0, 0), end=(+[4, 1][0]/2.0, 0),
    ori=80, pos=(-7, -2),
    lineWidth=9, lineColor='yellow', lineColorSpace='rgb',
    fillColor='yellow', fillColorSpace='rgb',
    opacity=0, depth=-8.0, interpolate=True)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
goodjob = visual.TextStim(win=win, name='goodjob',
    text='GOOD JOB!',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practice_3"
practice_3Clock = core.Clock()
blueline_3 = visual.Line(
    win=win, name='blueline_3',
    start=(-[1, 1][0]/2.0, 0), end=(+[1, 1][0]/2.0, 0),
    ori=90, pos=(-11, -4),
    lineWidth=3, lineColor='blue', lineColorSpace='rgb',
    fillColor='blue', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
redline_3 = visual.Line(
    win=win, name='redline_3',
    start=(-[2, 1][0]/2.0, 0), end=(+[2, 1][0]/2.0, 0),
    ori=140, pos=(12, -4),
    lineWidth=3, lineColor='red', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
button_instrL_3 = visual.TextStim(win=win, name='button_instrL_3',
    text='Click buttons 1 and 2 to\nrotate the BLUE line.',
    font='Arial',
    pos=(-13, -9), height=0.8, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
button_instrR_3 = visual.TextStim(win=win, name='button_instrR_3',
    text='Click button 3 when\nthe lines look parallel.',
    font='Arial',
    pos=(13, -9), height=0.8, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
buttons_trial_3 = visual.ImageStim(
    win=win,
    name='buttons_trial_3', 
    image='images/practice4.jpg', mask=None,
    ori=0, pos=(0, -9), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
key_resp_3 = keyboard.Keyboard()
your_mouse = event.Mouse(visible = False)
blue_correct_3 = visual.Line(
    win=win, name='blue_correct_3',
    start=(-[4, 1][0]/2.0, 0), end=(+[4, 1][0]/2.0, 0),
    ori=140, pos=(-11, -4),
    lineWidth=9, lineColor='yellow', lineColorSpace='rgb',
    fillColor='yellow', fillColorSpace='rgb',
    opacity=0, depth=-7.0, interpolate=True)
red_correct_3 = visual.Line(
    win=win, name='red_correct_3',
    start=(-[4, 1][0]/2.0, 0), end=(+[4, 1][0]/2.0, 0),
    ori=140, pos=(12, -4),
    lineWidth=9, lineColor='yellow', lineColorSpace='rgb',
    fillColor='yellow', fillColorSpace='rgb',
    opacity=0, depth=-8.0, interpolate=True)

# Initialize components for Routine "end_prep"
end_prepClock = core.Clock()
instructions3 = visual.ImageStim(
    win=win,
    name='instructions3', units='pix', 
    image='images/instr3.png', mask=None,
    ori=0, pos=(0, 0), size=(1101, 690),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
# update component parameters for each repeat
enter.keys = []
enter.rt = []
# keep track of which components have finished
instructionsComponents = [instr1, enter]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1.frameNStart = frameN  # exact frame index
        instr1.tStart = t  # local t and not account for scr refresh
        instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
        instr1.setAutoDraw(True)
    
    # *enter* updates
    waitOnFlip = False
    if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter.frameNStart = frameN  # exact frame index
        enter.tStart = t  # local t and not account for scr refresh
        enter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter, 'tStartRefresh')  # time at next scr refresh
        enter.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter.status == STARTED and not waitOnFlip:
        theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions_2"-------
# update component parameters for each repeat
enter2.keys = []
enter2.rt = []
# keep track of which components have finished
instructions_2Components = [instr2, enter2]
for thisComponent in instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instructions_2"-------
while continueRoutine:
    # get current time
    t = instructions_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr2* updates
    if instr2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr2.frameNStart = frameN  # exact frame index
        instr2.tStart = t  # local t and not account for scr refresh
        instr2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr2, 'tStartRefresh')  # time at next scr refresh
        instr2.setAutoDraw(True)
    
    # *enter2* updates
    waitOnFlip = False
    if enter2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter2.frameNStart = frameN  # exact frame index
        enter2.tStart = t  # local t and not account for scr refresh
        enter2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter2, 'tStartRefresh')  # time at next scr refresh
        enter2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(enter2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter2.status == STARTED and not waitOnFlip:
        theseKeys = enter2.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_2"-------
for thisComponent in instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_1"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
practice_1Components = [blueline, redline, button_instrL, button_instrR, buttons_trial, key_resp, blue_correct, red_correct, paralleltext]
for thisComponent in practice_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "practice_1"-------
while continueRoutine:
    # get current time
    t = practice_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blueline* updates
    if blueline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline.frameNStart = frameN  # exact frame index
        blueline.tStart = t  # local t and not account for scr refresh
        blueline.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline, 'tStartRefresh')  # time at next scr refresh
        blueline.setAutoDraw(True)
    
    # *redline* updates
    if redline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline.frameNStart = frameN  # exact frame index
        redline.tStart = t  # local t and not account for scr refresh
        redline.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline, 'tStartRefresh')  # time at next scr refresh
        redline.setAutoDraw(True)
    
    # *button_instrL* updates
    if button_instrL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_instrL.frameNStart = frameN  # exact frame index
        button_instrL.tStart = t  # local t and not account for scr refresh
        button_instrL.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_instrL, 'tStartRefresh')  # time at next scr refresh
        button_instrL.setAutoDraw(True)
    
    # *button_instrR* updates
    if button_instrR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_instrR.frameNStart = frameN  # exact frame index
        button_instrR.tStart = t  # local t and not account for scr refresh
        button_instrR.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_instrR, 'tStartRefresh')  # time at next scr refresh
        button_instrR.setAutoDraw(True)
    
    # *buttons_trial* updates
    if buttons_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttons_trial.frameNStart = frameN  # exact frame index
        buttons_trial.tStart = t  # local t and not account for scr refresh
        buttons_trial.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttons_trial, 'tStartRefresh')  # time at next scr refresh
        buttons_trial.setAutoDraw(True)
    
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
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys.append(theseKeys.name)  # storing all keys
            key_resp.rt.append(theseKeys.rt)
    corrans = [120, -60, -240, 300]
    
    if len(key_resp.keys) > 0:
        
        if key_resp.keys[-1] == '1':
            blueline.setOri(10,'-')
            key_resp.keys.append(1)
            win.flip()
            if blueline.ori in corrans:
                red_correct.opacity = 0.5
                blue_correct.opacity = 0.5
                paralleltext.pos = (0,0)
            else:
                red_correct.opacity = 0
                blue_correct.opacity = 0
                paralleltext.pos = (0,20)
                
        elif key_resp.keys[-1] == '2':
            blueline.setOri(10,'+')
            key_resp.keys.append(2)
            win.flip()
            if blueline.ori in corrans:
                red_correct.opacity = 0.5
                blue_correct.opacity = 0.5
                paralleltext.pos = (0,0)
            else:
                red_correct.opacity = 0
                blue_correct.opacity = 0
                paralleltext.pos = (0,20)
    
                
        elif key_resp.keys[-1] == '3':
            continueRoutine = False
            
        elif key_resp.keys[-1] == 'escape':
            endExpNow = True
            
    
    # *blue_correct* updates
    if blue_correct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blue_correct.frameNStart = frameN  # exact frame index
        blue_correct.tStart = t  # local t and not account for scr refresh
        blue_correct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blue_correct, 'tStartRefresh')  # time at next scr refresh
        blue_correct.setAutoDraw(True)
    
    # *red_correct* updates
    if red_correct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        red_correct.frameNStart = frameN  # exact frame index
        red_correct.tStart = t  # local t and not account for scr refresh
        red_correct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(red_correct, 'tStartRefresh')  # time at next scr refresh
        red_correct.setAutoDraw(True)
    
    # *paralleltext* updates
    if paralleltext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        paralleltext.frameNStart = frameN  # exact frame index
        paralleltext.tStart = t  # local t and not account for scr refresh
        paralleltext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(paralleltext, 'tStartRefresh')  # time at next scr refresh
        paralleltext.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_1"-------
for thisComponent in practice_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "practice_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "feedback"-------
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
feedbackComponents = [goodjob]
for thisComponent in feedbackComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "feedback"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = feedbackClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *goodjob* updates
    if goodjob.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goodjob.frameNStart = frameN  # exact frame index
        goodjob.tStart = t  # local t and not account for scr refresh
        goodjob.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goodjob, 'tStartRefresh')  # time at next scr refresh
        goodjob.setAutoDraw(True)
    if goodjob.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > goodjob.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            goodjob.tStop = t  # not accounting for scr refresh
            goodjob.frameNStop = frameN  # exact frame index
            win.timeOnFlip(goodjob, 'tStopRefresh')  # time at next scr refresh
            goodjob.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback"-------
for thisComponent in feedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "practice_2"-------
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
# keep track of which components have finished
practice_2Components = [blueline_2, redline_2, button_instrL_2, button_instrR_2, buttons_trial_2, key_resp_2, blue_correct_2, red_correct_2]
for thisComponent in practice_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "practice_2"-------
while continueRoutine:
    # get current time
    t = practice_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blueline_2* updates
    if blueline_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_2.frameNStart = frameN  # exact frame index
        blueline_2.tStart = t  # local t and not account for scr refresh
        blueline_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_2, 'tStartRefresh')  # time at next scr refresh
        blueline_2.setAutoDraw(True)
    
    # *redline_2* updates
    if redline_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_2.frameNStart = frameN  # exact frame index
        redline_2.tStart = t  # local t and not account for scr refresh
        redline_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_2, 'tStartRefresh')  # time at next scr refresh
        redline_2.setAutoDraw(True)
    
    # *button_instrL_2* updates
    if button_instrL_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_instrL_2.frameNStart = frameN  # exact frame index
        button_instrL_2.tStart = t  # local t and not account for scr refresh
        button_instrL_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_instrL_2, 'tStartRefresh')  # time at next scr refresh
        button_instrL_2.setAutoDraw(True)
    
    # *button_instrR_2* updates
    if button_instrR_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_instrR_2.frameNStart = frameN  # exact frame index
        button_instrR_2.tStart = t  # local t and not account for scr refresh
        button_instrR_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_instrR_2, 'tStartRefresh')  # time at next scr refresh
        button_instrR_2.setAutoDraw(True)
    
    # *buttons_trial_2* updates
    if buttons_trial_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttons_trial_2.frameNStart = frameN  # exact frame index
        buttons_trial_2.tStart = t  # local t and not account for scr refresh
        buttons_trial_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttons_trial_2, 'tStartRefresh')  # time at next scr refresh
        buttons_trial_2.setAutoDraw(True)
    
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
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_2.keys.append(theseKeys.name)  # storing all keys
            key_resp_2.rt.append(theseKeys.rt)
    corrans = [80, 260, -100, -280]
    
    if len(key_resp_2.keys) > 0:
        
        if key_resp_2.keys[-1] == '1':
            blueline_2.setOri(5,'-')
            key_resp_2.keys.append(1)
            win.flip()
            if blueline_2.ori in corrans:
                red_correct_2.opacity = 0.5
                blue_correct_2.opacity = 0.5
            else:
                red_correct_2.opacity = 0
                blue_correct_2.opacity = 0
                
        elif key_resp_2.keys[-1] == '2':
            blueline_2.setOri(5,'+')
            key_resp_2.keys.append(2)
            win.flip()
            if blueline_2.ori in corrans:
                red_correct_2.opacity = 0.5
                blue_correct_2.opacity = 0.5
            else:
                red_correct_2.opacity = 0
                blue_correct_2.opacity = 0
                
        elif key_resp_2.keys[-1] == '3':
            continueRoutine = False
            
        elif key_resp_2.keys[-1] == 'escape':
            endExpNow = True
            
    
    # *blue_correct_2* updates
    if blue_correct_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blue_correct_2.frameNStart = frameN  # exact frame index
        blue_correct_2.tStart = t  # local t and not account for scr refresh
        blue_correct_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blue_correct_2, 'tStartRefresh')  # time at next scr refresh
        blue_correct_2.setAutoDraw(True)
    
    # *red_correct_2* updates
    if red_correct_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        red_correct_2.frameNStart = frameN  # exact frame index
        red_correct_2.tStart = t  # local t and not account for scr refresh
        red_correct_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(red_correct_2, 'tStartRefresh')  # time at next scr refresh
        red_correct_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_2"-------
for thisComponent in practice_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "practice_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "feedback"-------
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
feedbackComponents = [goodjob]
for thisComponent in feedbackComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "feedback"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = feedbackClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *goodjob* updates
    if goodjob.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goodjob.frameNStart = frameN  # exact frame index
        goodjob.tStart = t  # local t and not account for scr refresh
        goodjob.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goodjob, 'tStartRefresh')  # time at next scr refresh
        goodjob.setAutoDraw(True)
    if goodjob.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > goodjob.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            goodjob.tStop = t  # not accounting for scr refresh
            goodjob.frameNStop = frameN  # exact frame index
            win.timeOnFlip(goodjob, 'tStopRefresh')  # time at next scr refresh
            goodjob.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback"-------
for thisComponent in feedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "practice_3"-------
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
# keep track of which components have finished
practice_3Components = [blueline_3, redline_3, button_instrL_3, button_instrR_3, buttons_trial_3, key_resp_3, blue_correct_3, red_correct_3]
for thisComponent in practice_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "practice_3"-------
while continueRoutine:
    # get current time
    t = practice_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blueline_3* updates
    if blueline_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_3.frameNStart = frameN  # exact frame index
        blueline_3.tStart = t  # local t and not account for scr refresh
        blueline_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_3, 'tStartRefresh')  # time at next scr refresh
        blueline_3.setAutoDraw(True)
    
    # *redline_3* updates
    if redline_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_3.frameNStart = frameN  # exact frame index
        redline_3.tStart = t  # local t and not account for scr refresh
        redline_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_3, 'tStartRefresh')  # time at next scr refresh
        redline_3.setAutoDraw(True)
    
    # *button_instrL_3* updates
    if button_instrL_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_instrL_3.frameNStart = frameN  # exact frame index
        button_instrL_3.tStart = t  # local t and not account for scr refresh
        button_instrL_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_instrL_3, 'tStartRefresh')  # time at next scr refresh
        button_instrL_3.setAutoDraw(True)
    
    # *button_instrR_3* updates
    if button_instrR_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_instrR_3.frameNStart = frameN  # exact frame index
        button_instrR_3.tStart = t  # local t and not account for scr refresh
        button_instrR_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_instrR_3, 'tStartRefresh')  # time at next scr refresh
        button_instrR_3.setAutoDraw(True)
    
    # *buttons_trial_3* updates
    if buttons_trial_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buttons_trial_3.frameNStart = frameN  # exact frame index
        buttons_trial_3.tStart = t  # local t and not account for scr refresh
        buttons_trial_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buttons_trial_3, 'tStartRefresh')  # time at next scr refresh
        buttons_trial_3.setAutoDraw(True)
    
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
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_3.keys.append(theseKeys.name)  # storing all keys
            key_resp_3.rt.append(theseKeys.rt)
    corrans = [140, -40, -220, 320]
    
    if len(key_resp_3.keys) > 0:
        
        if key_resp_3.keys[-1] == '1':
            blueline_3.setOri(10,'-')
            key_resp_3.keys.append(1)
            win.flip()
            if blueline_3.ori in corrans:
                red_correct_3.opacity = 0.5
                blue_correct_3.opacity = 0.5
            else:
                red_correct_3.opacity = 0
                blue_correct_3.opacity = 0
                
        elif key_resp_3.keys[-1] == '2':
            blueline_3.setOri(10,'+')
            key_resp_3.keys.append(2)
            win.flip()
            if blueline_3.ori in corrans:
                red_correct_3.opacity = 0.5
                blue_correct_3.opacity = 0.5
            else:
                red_correct_3.opacity = 0
                blue_correct_3.opacity = 0
                
        elif key_resp_3.keys[-1] == '3':
            continueRoutine = False
            
        elif key_resp_3.keys[-1] == 'escape':
            endExpNow = True
            
    
    # *blue_correct_3* updates
    if blue_correct_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blue_correct_3.frameNStart = frameN  # exact frame index
        blue_correct_3.tStart = t  # local t and not account for scr refresh
        blue_correct_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blue_correct_3, 'tStartRefresh')  # time at next scr refresh
        blue_correct_3.setAutoDraw(True)
    
    # *red_correct_3* updates
    if red_correct_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        red_correct_3.frameNStart = frameN  # exact frame index
        red_correct_3.tStart = t  # local t and not account for scr refresh
        red_correct_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(red_correct_3, 'tStartRefresh')  # time at next scr refresh
        red_correct_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_3"-------
for thisComponent in practice_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "practice_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "end_prep"-------
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
# keep track of which components have finished
end_prepComponents = [instructions3, key_resp_4]
for thisComponent in end_prepComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_prepClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end_prep"-------
while continueRoutine:
    # get current time
    t = end_prepClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_prepClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions3* updates
    if instructions3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions3.frameNStart = frameN  # exact frame index
        instructions3.tStart = t  # local t and not account for scr refresh
        instructions3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions3, 'tStartRefresh')  # time at next scr refresh
        instructions3.setAutoDraw(True)
    
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
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_prepComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_prep"-------
for thisComponent in end_prepComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions3.started', instructions3.tStartRefresh)
thisExp.addData('instructions3.stopped', instructions3.tStopRefresh)
# the Routine "end_prep" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
