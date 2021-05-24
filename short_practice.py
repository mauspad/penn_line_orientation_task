#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on November 04, 2019, at 17:08
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
expName = 'practice'  # from the Builder filename that created this script
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
    originPath='practice.py',
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
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='cm')
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

# Initialize components for Routine "manual_trigger"
manual_triggerClock = core.Clock()
trigger = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
practice1 = visual.ImageStim(
    win=win,
    name='practice1', 
    image='images\practice1.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
counter = visual.TextStim(win=win, name='counter',
    text='Press 1 to rotate the blue line COUNTER-CLOCKWISE.',
    font='Arial',
    pos=(0, -4), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
blueline = visual.Line(
    win=win, name='blueline',
    start=(-(4, 4)[0]/2.0, 0), end=(+(4, 4)[0]/2.0, 0),
    ori=90, pos=(0, 5),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial_2"
trial_2Clock = core.Clock()
practice1_2 = visual.ImageStim(
    win=win,
    name='practice1_2', 
    image='images\practice2.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
counter_2 = visual.TextStim(win=win, name='counter_2',
    text='Press 2 to rotate the blue line CLOCKWISE.',
    font='Arial',
    pos=(0, -4), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
blueline_2 = visual.Line(
    win=win, name='blueline_2',
    start=(-(4, 4)[0]/2.0, 0), end=(+(4, 4)[0]/2.0, 0),
    ori=90, pos=(0, 5),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "trial_3"
trial_3Clock = core.Clock()
practice1_3 = visual.ImageStim(
    win=win,
    name='practice1_3', 
    image='images\practice3.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
counter_3 = visual.TextStim(win=win, name='counter_3',
    text='Press 3 to end the trial.',
    font='Arial',
    pos=(0, -4), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
blueline_3 = visual.Line(
    win=win, name='blueline_3',
    start=(-(4, 4)[0]/2.0, 0), end=(+(4, 4)[0]/2.0, 0),
    ori=90, pos=(0, 5),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "trial_4"
trial_4Clock = core.Clock()
practice1_4 = visual.ImageStim(
    win=win,
    name='practice1_4', 
    image='images\practice4.jpg', mask=None,
    ori=0, pos=(0, -10), size=(15, 5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
counter_4 = visual.TextStim(win=win, name='counter_4',
    text='Remember, you must rotate the BLUE line so that it is parallel to the red line.\n\nClick 3 when the lines look parallel.',
    font='Arial',
    pos=(0, -3), height=1.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
blueline_4 = visual.Line(
    win=win, name='blueline_4',
    start=(-(4, 4)[0]/2.0, 0), end=(+(4, 4)[0]/2.0, 0),
    ori=90, pos=(-8, 5),
    lineWidth=3, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
key_resp_4 = keyboard.Keyboard()
redline_4 = visual.Line(
    win=win, name='redline_4',
    start=(-(4, 0)[0]/2.0, 0), end=(+(4, 0)[0]/2.0, 0),
    ori=150, pos=(8, 5),
    lineWidth=3, lineColor=[1.000,1.000,0], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "manual_trigger"-------
# update component parameters for each repeat
trigger.keys = []
trigger.rt = []
# keep track of which components have finished
manual_triggerComponents = [trigger]
for thisComponent in manual_triggerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
manual_triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "manual_trigger"-------
while continueRoutine:
    # get current time
    t = manual_triggerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=manual_triggerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trigger* updates
    waitOnFlip = False
    if trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger.frameNStart = frameN  # exact frame index
        trigger.tStart = t  # local t and not account for scr refresh
        trigger.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger, 'tStartRefresh')  # time at next scr refresh
        trigger.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger.status == STARTED and not waitOnFlip:
        theseKeys = trigger.getKeys(keyList=['5'], waitRelease=False)
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
    for thisComponent in manual_triggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "manual_trigger"-------
for thisComponent in manual_triggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "manual_trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
trialComponents = [practice1, counter, blueline, key_resp]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice1* updates
    if practice1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice1.frameNStart = frameN  # exact frame index
        practice1.tStart = t  # local t and not account for scr refresh
        practice1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice1, 'tStartRefresh')  # time at next scr refresh
        practice1.setAutoDraw(True)
    
    # *counter* updates
    if counter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        counter.frameNStart = frameN  # exact frame index
        counter.tStart = t  # local t and not account for scr refresh
        counter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(counter, 'tStartRefresh')  # time at next scr refresh
        counter.setAutoDraw(True)
    
    # *blueline* updates
    if blueline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline.frameNStart = frameN  # exact frame index
        blueline.tStart = t  # local t and not account for scr refresh
        blueline.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline, 'tStartRefresh')  # time at next scr refresh
        blueline.setAutoDraw(True)
    
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
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['1', '5'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline.setOri(15,'-')
                win.flip()
            elif '5' == theseKeys:
                continueRoutine = False
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice1.started', practice1.tStartRefresh)
thisExp.addData('practice1.stopped', practice1.tStopRefresh)
thisExp.addData('counter.started', counter.tStartRefresh)
thisExp.addData('counter.stopped', counter.tStopRefresh)
thisExp.addData('blueline.started', blueline.tStartRefresh)
thisExp.addData('blueline.stopped', blueline.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_2"-------
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
# keep track of which components have finished
trial_2Components = [practice1_2, counter_2, blueline_2, key_resp_2]
for thisComponent in trial_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_2"-------
while continueRoutine:
    # get current time
    t = trial_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice1_2* updates
    if practice1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice1_2.frameNStart = frameN  # exact frame index
        practice1_2.tStart = t  # local t and not account for scr refresh
        practice1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice1_2, 'tStartRefresh')  # time at next scr refresh
        practice1_2.setAutoDraw(True)
    
    # *counter_2* updates
    if counter_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        counter_2.frameNStart = frameN  # exact frame index
        counter_2.tStart = t  # local t and not account for scr refresh
        counter_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(counter_2, 'tStartRefresh')  # time at next scr refresh
        counter_2.setAutoDraw(True)
    
    # *blueline_2* updates
    if blueline_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_2.frameNStart = frameN  # exact frame index
        blueline_2.tStart = t  # local t and not account for scr refresh
        blueline_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_2, 'tStartRefresh')  # time at next scr refresh
        blueline_2.setAutoDraw(True)
    
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
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['2', '5'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '2' == theseKeys:
                blueline_2.setOri(15,'+')
                win.flip()
            elif '5' == theseKeys:
                continueRoutine = False
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_2"-------
for thisComponent in trial_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice1_2.started', practice1_2.tStartRefresh)
thisExp.addData('practice1_2.stopped', practice1_2.tStopRefresh)
thisExp.addData('counter_2.started', counter_2.tStartRefresh)
thisExp.addData('counter_2.stopped', counter_2.tStopRefresh)
thisExp.addData('blueline_2.started', blueline_2.tStartRefresh)
thisExp.addData('blueline_2.stopped', blueline_2.tStopRefresh)
# the Routine "trial_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_3"-------
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
# keep track of which components have finished
trial_3Components = [practice1_3, counter_3, blueline_3, key_resp_3]
for thisComponent in trial_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_3"-------
while continueRoutine:
    # get current time
    t = trial_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice1_3* updates
    if practice1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice1_3.frameNStart = frameN  # exact frame index
        practice1_3.tStart = t  # local t and not account for scr refresh
        practice1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice1_3, 'tStartRefresh')  # time at next scr refresh
        practice1_3.setAutoDraw(True)
    
    # *counter_3* updates
    if counter_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        counter_3.frameNStart = frameN  # exact frame index
        counter_3.tStart = t  # local t and not account for scr refresh
        counter_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(counter_3, 'tStartRefresh')  # time at next scr refresh
        counter_3.setAutoDraw(True)
    
    # *blueline_3* updates
    if blueline_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_3.frameNStart = frameN  # exact frame index
        blueline_3.tStart = t  # local t and not account for scr refresh
        blueline_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_3, 'tStartRefresh')  # time at next scr refresh
        blueline_3.setAutoDraw(True)
    
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
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['3', '5'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '3' == theseKeys:
                blueline_3.setColor('black')
                win.flip()
            elif '5' == theseKeys:
                continueRoutine = False
            # check for quit:
            elif "escape" == theseKeys:
                endExpNow = True
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_3"-------
for thisComponent in trial_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice1_3.started', practice1_3.tStartRefresh)
thisExp.addData('practice1_3.stopped', practice1_3.tStopRefresh)
thisExp.addData('counter_3.started', counter_3.tStartRefresh)
thisExp.addData('counter_3.stopped', counter_3.tStopRefresh)
thisExp.addData('blueline_3.started', blueline_3.tStartRefresh)
thisExp.addData('blueline_3.stopped', blueline_3.tStopRefresh)
# the Routine "trial_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_4"-------
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
# keep track of which components have finished
trial_4Components = [practice1_4, counter_4, blueline_4, key_resp_4, redline_4]
for thisComponent in trial_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_4"-------
while continueRoutine:
    # get current time
    t = trial_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice1_4* updates
    if practice1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice1_4.frameNStart = frameN  # exact frame index
        practice1_4.tStart = t  # local t and not account for scr refresh
        practice1_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice1_4, 'tStartRefresh')  # time at next scr refresh
        practice1_4.setAutoDraw(True)
    
    # *counter_4* updates
    if counter_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        counter_4.frameNStart = frameN  # exact frame index
        counter_4.tStart = t  # local t and not account for scr refresh
        counter_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(counter_4, 'tStartRefresh')  # time at next scr refresh
        counter_4.setAutoDraw(True)
    
    # *blueline_4* updates
    if blueline_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blueline_4.frameNStart = frameN  # exact frame index
        blueline_4.tStart = t  # local t and not account for scr refresh
        blueline_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blueline_4, 'tStartRefresh')  # time at next scr refresh
        blueline_4.setAutoDraw(True)
    
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
        theseKeys = key_resp_4.getKeys(keyList=['1', '2', '3', '5'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            if '1' == theseKeys:
                blueline_4.setOri(15,'-')
                win.flip()
            elif '2' == theseKeys:
                blueline_4.setOri(15,'+')
                win.flip()
            elif '3' == theseKeys:
                blueline_4.setColor('black')
                redline_4.setColor('black')
                win.flip()
            elif '5' == theseKeys:
                continueRoutine = False
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
    
    # *redline_4* updates
    if redline_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        redline_4.frameNStart = frameN  # exact frame index
        redline_4.tStart = t  # local t and not account for scr refresh
        redline_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(redline_4, 'tStartRefresh')  # time at next scr refresh
        redline_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_4"-------
for thisComponent in trial_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice1_4.started', practice1_4.tStartRefresh)
thisExp.addData('practice1_4.stopped', practice1_4.tStopRefresh)
thisExp.addData('counter_4.started', counter_4.tStartRefresh)
thisExp.addData('counter_4.stopped', counter_4.tStopRefresh)
thisExp.addData('blueline_4.started', blueline_4.tStartRefresh)
thisExp.addData('blueline_4.stopped', blueline_4.tStopRefresh)
thisExp.addData('redline_4.started', redline_4.tStartRefresh)
thisExp.addData('redline_4.stopped', redline_4.tStopRefresh)
# the Routine "trial_4" was not non-slip safe, so reset the non-slip timer
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
