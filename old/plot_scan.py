#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on April 20, 2021, at 17:52
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
expName = 'PLOT_scan'  # from the Builder filename that created this script
expInfo = {'participant': '', 'run': ''}
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
    originPath='C:\\Users\\mauspad\\Desktop\\line_orientation_scan\\PLOT_scan\\plot_scan.py',
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

# Initialize components for Routine "wait_for_scanner"
wait_for_scannerClock = core.Clock()
trigger = keyboard.Keyboard()
fixation_wait = visual.ShapeStim(
    win=win, name='fixation_wait', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "jitter_2"
jitter_2Clock = core.Clock()
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',units='cm', 
    size=(2,2),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "plot_trials"
plot_trialsClock = core.Clock()
blueline = visual.Line(
    win=win, name='blueline',
    start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
    ori=1.0, pos=[0,0],
    lineWidth=3, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
redline = visual.Line(
    win=win, name='redline',
    start=(-(3, 0)[0]/2.0, 0), end=(+(3, 0)[0]/2.0, 0),
    ori=1.0, pos=[0,0],
    lineWidth=3, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
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

# Initialize components for Routine "end"
endClock = core.Clock()
bye = visual.TextStim(win=win, name='bye',
    text='You have completed the task :)',
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "wait_for_scanner"-------
# update component parameters for each repeat
trigger.keys = []
trigger.rt = []
# keep track of which components have finished
wait_for_scannerComponents = [trigger, fixation_wait]
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
        waitOnFlip = True
        win.callOnFlip(trigger.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger.status == STARTED and not waitOnFlip:
        theseKeys = trigger.getKeys(keyList=['5'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            trigger.keys = theseKeys.name  # just the last key pressed
            trigger.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *fixation_wait* updates
    if fixation_wait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_wait.frameNStart = frameN  # exact frame index
        fixation_wait.tStart = t  # local t and not account for scr refresh
        fixation_wait.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_wait, 'tStartRefresh')  # time at next scr refresh
        fixation_wait.setAutoDraw(True)
    
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
if trigger.keys in ['', [], None]:  # No response was made
    trigger.keys = None
thisExp.addData('trigger.keys',trigger.keys)
if trigger.keys != None:  # we had a response
    thisExp.addData('trigger.rt', trigger.rt)
thisExp.nextEntry()
thisExp.addData('fixation_wait.started', fixation_wait.tStartRefresh)
thisExp.addData('fixation_wait.stopped', fixation_wait.tStopRefresh)
# the Routine "wait_for_scanner" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trials.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "jitter_2"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    jitter_2Components = [fixation]
    for thisComponent in jitter_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    jitter_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "jitter_2"-------
    while continueRoutine:
        # get current time
        t = jitter_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=jitter_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jitter_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "jitter_2"-------
    for thisComponent in jitter_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fixation.started', fixation.tStartRefresh)
    trials.addData('fixation.stopped', fixation.tStopRefresh)
    # the Routine "jitter_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "plot_trials"-------
    routineTimer.add(11.000000)
    # update component parameters for each repeat
    blueline.setPos((Bluex, Bluey))
    blueline.setSize((BlueLengthx, BlueLengthy))
    blueline.setOri(BlueOri)
    blueline.setFillColor([-1.000, 0.004, 1.000])
    blueline.setLineColor([-1.000, 0.004, 1.000])
    redline.setPos((Redx, Redy))
    redline.setOri(RedOri)
    redline.setFillColor('red')
    redline.setLineColor('red')
    key_resp.keys = []
    key_resp.rt = []
    # keep track of which components have finished
    plot_trialsComponents = [blueline, redline, button_instrL, button_instrR, buttons_trial, key_resp]
    for thisComponent in plot_trialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    plot_trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "plot_trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = plot_trialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=plot_trialsClock)
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
        
        # *button_instrL* updates
        if button_instrL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_instrL.frameNStart = frameN  # exact frame index
            button_instrL.tStart = t  # local t and not account for scr refresh
            button_instrL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_instrL, 'tStartRefresh')  # time at next scr refresh
            button_instrL.setAutoDraw(True)
        if button_instrL.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > button_instrL.tStartRefresh + 11-frameTolerance:
                # keep track of stop time/frame for later
                button_instrL.tStop = t  # not accounting for scr refresh
                button_instrL.frameNStop = frameN  # exact frame index
                win.timeOnFlip(button_instrL, 'tStopRefresh')  # time at next scr refresh
                button_instrL.setAutoDraw(False)
        
        # *button_instrR* updates
        if button_instrR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_instrR.frameNStart = frameN  # exact frame index
            button_instrR.tStart = t  # local t and not account for scr refresh
            button_instrR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_instrR, 'tStartRefresh')  # time at next scr refresh
            button_instrR.setAutoDraw(True)
        if button_instrR.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > button_instrR.tStartRefresh + 11-frameTolerance:
                # keep track of stop time/frame for later
                button_instrR.tStop = t  # not accounting for scr refresh
                button_instrR.frameNStop = frameN  # exact frame index
                win.timeOnFlip(button_instrR, 'tStopRefresh')  # time at next scr refresh
                button_instrR.setAutoDraw(False)
        
        # *buttons_trial* updates
        if buttons_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttons_trial.frameNStart = frameN  # exact frame index
            buttons_trial.tStart = t  # local t and not account for scr refresh
            buttons_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttons_trial, 'tStartRefresh')  # time at next scr refresh
            buttons_trial.setAutoDraw(True)
        if buttons_trial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > buttons_trial.tStartRefresh + 11-frameTolerance:
                # keep track of stop time/frame for later
                buttons_trial.tStop = t  # not accounting for scr refresh
                buttons_trial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(buttons_trial, 'tStopRefresh')  # time at next scr refresh
                buttons_trial.setAutoDraw(False)
        
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
            theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys.append(theseKeys.name)  # storing all keys
                key_resp.rt.append(theseKeys.rt)
        if len(key_resp.keys) > 0:
            
            if key_resp.keys[-1] == '1':
                blueline.setOri(Angle,'-')
                key_resp.keys.append(1)
                win.flip()
        
            elif key_resp.keys[-1] == '2':
                blueline.setOri(Angle,'+')
                key_resp.keys.append(2)
                win.flip()
        
            elif key_resp.keys[-1] == '3':
                blueline.setColor([-1,-1,-1],'rgb')
                redline.setColor([-1,-1,-1],'rgb')
                win.flip()
        
            elif key_resp.keys[-1] == 'escape':
                endExpNow = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in plot_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "plot_trials"-------
    for thisComponent in plot_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [bye]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *bye* updates
    if bye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bye.frameNStart = frameN  # exact frame index
        bye.tStart = t  # local t and not account for scr refresh
        bye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bye, 'tStartRefresh')  # time at next scr refresh
        bye.setAutoDraw(True)
    if bye.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bye.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            bye.tStop = t  # not accounting for scr refresh
            bye.frameNStop = frameN  # exact frame index
            win.timeOnFlip(bye, 'tStopRefresh')  # time at next scr refresh
            bye.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

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
