#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on November 01, 2023, at 18:43
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'plot_practice'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\Silver\\Box\\psychopy_git_masters\\PLOT_scan\\plot_practice.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1536, 864], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1.0000, -1.0000, -1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instructions1" ---
    instr1 = visual.ImageStim(
        win=win,
        name='instr1', 
        image='images/instr1.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    enter = keyboard.Keyboard()
    
    # --- Initialize components for Routine "instructions2" ---
    instr_2 = visual.ImageStim(
        win=win,
        name='instr_2', 
        image='images/instr2.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    enter_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "practice1" ---
    # Run 'Begin Experiment' code from code
    #hide mouse
    mouse = event.Mouse(visible=False)
    blueline = visual.Line(
        win=win, name='blueline',
        start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
        ori=1.0, pos=[0,0], anchor='center',
        lineWidth=3.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 1.0000], fillColor=[-1.0000, -1.0000, 1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    blue_correct = visual.Line(
        win=win, name='blue_correct',
        start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
        ori=1.0, pos=[0,0], anchor='center',
        lineWidth=20.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, -1.0000], fillColor=[1.0000, 1.0000, -1.0000],
        opacity=0.0, depth=-2.0, interpolate=True)
    redline = visual.Line(
        win=win, name='redline',
        start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
        ori=1.0, pos=[0,0], anchor='center',
        lineWidth=3.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    red_correct = visual.Line(
        win=win, name='red_correct',
        start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
        ori=1.0, pos=[0,0], anchor='center',
        lineWidth=20.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, -1.0000], fillColor=[1.0000, 1.0000, -1.0000],
        opacity=0.0, depth=-4.0, interpolate=True)
    button_L = visual.TextStim(win=win, name='button_L',
        text='Press 1 and 2 to\nrotate the BLUE line.',
        font='Open Sans',
        pos=(-0.5, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    button_R = visual.TextStim(win=win, name='button_R',
        text='Press ENTER when\nthe lines look parallel.',
        font='Open Sans',
        pos=(0.5, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    buttons_center = visual.ImageStim(
        win=win,
        name='buttons_center', 
        image='images/practice4.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.4), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    paralleltext = visual.TextStim(win=win, name='paralleltext',
        text='See how the lines are parallel?',
        font='Open Sans',
        pos=(0, 2), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    key_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "feedback" ---
    text = visual.TextStim(win=win, name='text',
        text='GOOD JOB!',
        font='Open Sans',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "practice2" ---
    blueline_2 = visual.Line(
        win=win, name='blueline_2',
        start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
        ori=1.0, pos=[0,0], anchor='center',
        lineWidth=3.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 1.0000], fillColor=[-1.0000, -1.0000, 1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    blue_correct_2 = visual.Line(
        win=win, name='blue_correct_2',
        start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
        ori=1.0, pos=[0,0], anchor='center',
        lineWidth=20.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, -1.0000], fillColor=[1.0000, 1.0000, -1.0000],
        opacity=0.0, depth=-2.0, interpolate=True)
    redline_2 = visual.Line(
        win=win, name='redline_2',
        start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
        ori=1.0, pos=[0,0], anchor='center',
        lineWidth=3.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    red_correct_2 = visual.Line(
        win=win, name='red_correct_2',
        start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
        ori=1.0, pos=[0,0], anchor='center',
        lineWidth=20.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, -1.0000], fillColor=[1.0000, 1.0000, -1.0000],
        opacity=0.0, depth=-4.0, interpolate=True)
    button_L_2 = visual.TextStim(win=win, name='button_L_2',
        text='Press 1 and 2 to\nrotate the BLUE line.',
        font='Open Sans',
        pos=(-0.5, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    button_R_2 = visual.TextStim(win=win, name='button_R_2',
        text='Press ENTER when\nthe lines look parallel.',
        font='Open Sans',
        pos=(0.5, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    buttons_center_2 = visual.ImageStim(
        win=win,
        name='buttons_center_2', 
        image='images/practice4.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.4), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    paralleltext_2 = visual.TextStim(win=win, name='paralleltext_2',
        text='See how the lines are parallel?',
        font='Open Sans',
        pos=(0, 2), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    key_resp_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "feedback" ---
    text = visual.TextStim(win=win, name='text',
        text='GOOD JOB!',
        font='Open Sans',
        pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "practice3" ---
    blueline_3 = visual.Line(
        win=win, name='blueline_3',
        start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
        ori=1.0, pos=[0,0], anchor='center',
        lineWidth=3.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 1.0000], fillColor=[-1.0000, -1.0000, 1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    blue_correct_3 = visual.Line(
        win=win, name='blue_correct_3',
        start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
        ori=1.0, pos=[0,0], anchor='center',
        lineWidth=20.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, -1.0000], fillColor=[1.0000, 1.0000, -1.0000],
        opacity=0.0, depth=-2.0, interpolate=True)
    redline_3 = visual.Line(
        win=win, name='redline_3',
        start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
        ori=1.0, pos=[0,0], anchor='center',
        lineWidth=3.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    red_correct_3 = visual.Line(
        win=win, name='red_correct_3',
        start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
        ori=1.0, pos=[0,0], anchor='center',
        lineWidth=20.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, -1.0000], fillColor=[1.0000, 1.0000, -1.0000],
        opacity=0.0, depth=-4.0, interpolate=True)
    button_L_3 = visual.TextStim(win=win, name='button_L_3',
        text='Press 1 and 2 to\nrotate the BLUE line.',
        font='Open Sans',
        pos=(-0.5, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    button_R_3 = visual.TextStim(win=win, name='button_R_3',
        text='Press ENTER when\nthe lines look parallel.',
        font='Open Sans',
        pos=(0.5, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    buttons_center_3 = visual.ImageStim(
        win=win,
        name='buttons_center_3', 
        image='images/practice4.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.4), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    paralleltext_3 = visual.TextStim(win=win, name='paralleltext_3',
        text='See how the lines are parallel?',
        font='Open Sans',
        pos=(0, 2), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    key_resp_3 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "end_prep" ---
    instr3 = visual.ImageStim(
        win=win,
        name='instr3', 
        image='images/instr3.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    enter_3 = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "instructions1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions1.started', globalClock.getTime())
    enter.keys = []
    enter.rt = []
    _enter_allKeys = []
    # keep track of which components have finished
    instructions1Components = [instr1, enter]
    for thisComponent in instructions1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr1* updates
        
        # if instr1 is starting this frame...
        if instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr1.frameNStart = frameN  # exact frame index
            instr1.tStart = t  # local t and not account for scr refresh
            instr1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr1.status = STARTED
            instr1.setAutoDraw(True)
        
        # if instr1 is active this frame...
        if instr1.status == STARTED:
            # update params
            pass
        
        # *enter* updates
        waitOnFlip = False
        
        # if enter is starting this frame...
        if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enter.frameNStart = frameN  # exact frame index
            enter.tStart = t  # local t and not account for scr refresh
            enter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enter, 'tStartRefresh')  # time at next scr refresh
            # update status
            enter.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(enter.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if enter.status == STARTED and not waitOnFlip:
            theseKeys = enter.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _enter_allKeys.extend(theseKeys)
            if len(_enter_allKeys):
                enter.keys = _enter_allKeys[-1].name  # just the last key pressed
                enter.rt = _enter_allKeys[-1].rt
                enter.duration = _enter_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions1" ---
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions1.stopped', globalClock.getTime())
    # the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions2.started', globalClock.getTime())
    enter_2.keys = []
    enter_2.rt = []
    _enter_2_allKeys = []
    # keep track of which components have finished
    instructions2Components = [instr_2, enter_2]
    for thisComponent in instructions2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_2* updates
        
        # if instr_2 is starting this frame...
        if instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_2.frameNStart = frameN  # exact frame index
            instr_2.tStart = t  # local t and not account for scr refresh
            instr_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr_2.status = STARTED
            instr_2.setAutoDraw(True)
        
        # if instr_2 is active this frame...
        if instr_2.status == STARTED:
            # update params
            pass
        
        # *enter_2* updates
        waitOnFlip = False
        
        # if enter_2 is starting this frame...
        if enter_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enter_2.frameNStart = frameN  # exact frame index
            enter_2.tStart = t  # local t and not account for scr refresh
            enter_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enter_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            enter_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(enter_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(enter_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if enter_2.status == STARTED and not waitOnFlip:
            theseKeys = enter_2.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _enter_2_allKeys.extend(theseKeys)
            if len(_enter_2_allKeys):
                enter_2.keys = _enter_2_allKeys[-1].name  # just the last key pressed
                enter_2.rt = _enter_2_allKeys[-1].rt
                enter_2.duration = _enter_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions2" ---
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions2.stopped', globalClock.getTime())
    # the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('practice1.started', globalClock.getTime())
    # Run 'Begin Routine' code from code
    #no really, hide the mouse
    win.mouseVisible = False
    
    #set corrans
    corrans = [120, -60, -240, 300]
    blueline.setPos((0.4, 0.3))
    blueline.setSize((0.1, 0))
    blueline.setOri(-120.0)
    blue_correct.setPos((0.4, 0.3))
    blue_correct.setSize((0.12, 0))
    blue_correct.setOri(120.0)
    redline.setPos((-0.4, 0.3))
    redline.setSize((0.1, 0))
    redline.setOri(120.0)
    red_correct.setPos((-0.4, 0.3))
    red_correct.setSize((0.12, 0))
    red_correct.setOri(120.0)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    practice1Components = [blueline, blue_correct, redline, red_correct, button_L, button_R, buttons_center, paralleltext, key_resp]
    for thisComponent in practice1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code
        #get current response
        resp = event.getKeys(['1','2'])
        
        if len(resp):
            if resp[0] == '1':
                blueline.setOri(10,'-')
                if blueline.ori in corrans:
                    red_correct.opacity = 0.2
                    blue_correct.opacity = 0.2
                    paralleltext.pos = (0,0)
                else:
                    red_correct.opacity = 0
                    blue_correct.opacity = 0
                    paralleltext.pos = (0,2)
            elif resp[0] == '2':
                blueline.setOri(10,'+')
                if blueline.ori in corrans:
                    red_correct.opacity = 0.2
                    blue_correct.opacity = 0.2
                    paralleltext.pos = (0,0)
                else:
                    red_correct.opacity = 0
                    blue_correct.opacity = 0
                    paralleltext.pos = (0,2)
        
        # *blueline* updates
        
        # if blueline is starting this frame...
        if blueline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blueline.frameNStart = frameN  # exact frame index
            blueline.tStart = t  # local t and not account for scr refresh
            blueline.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blueline, 'tStartRefresh')  # time at next scr refresh
            # update status
            blueline.status = STARTED
            blueline.setAutoDraw(True)
        
        # if blueline is active this frame...
        if blueline.status == STARTED:
            # update params
            pass
        
        # *blue_correct* updates
        
        # if blue_correct is starting this frame...
        if blue_correct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blue_correct.frameNStart = frameN  # exact frame index
            blue_correct.tStart = t  # local t and not account for scr refresh
            blue_correct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blue_correct, 'tStartRefresh')  # time at next scr refresh
            # update status
            blue_correct.status = STARTED
            blue_correct.setAutoDraw(True)
        
        # if blue_correct is active this frame...
        if blue_correct.status == STARTED:
            # update params
            pass
        
        # *redline* updates
        
        # if redline is starting this frame...
        if redline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            redline.frameNStart = frameN  # exact frame index
            redline.tStart = t  # local t and not account for scr refresh
            redline.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(redline, 'tStartRefresh')  # time at next scr refresh
            # update status
            redline.status = STARTED
            redline.setAutoDraw(True)
        
        # if redline is active this frame...
        if redline.status == STARTED:
            # update params
            pass
        
        # *red_correct* updates
        
        # if red_correct is starting this frame...
        if red_correct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_correct.frameNStart = frameN  # exact frame index
            red_correct.tStart = t  # local t and not account for scr refresh
            red_correct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_correct, 'tStartRefresh')  # time at next scr refresh
            # update status
            red_correct.status = STARTED
            red_correct.setAutoDraw(True)
        
        # if red_correct is active this frame...
        if red_correct.status == STARTED:
            # update params
            pass
        
        # *button_L* updates
        
        # if button_L is starting this frame...
        if button_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_L.frameNStart = frameN  # exact frame index
            button_L.tStart = t  # local t and not account for scr refresh
            button_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_L, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_L.status = STARTED
            button_L.setAutoDraw(True)
        
        # if button_L is active this frame...
        if button_L.status == STARTED:
            # update params
            pass
        
        # *button_R* updates
        
        # if button_R is starting this frame...
        if button_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_R.frameNStart = frameN  # exact frame index
            button_R.tStart = t  # local t and not account for scr refresh
            button_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_R, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_R.status = STARTED
            button_R.setAutoDraw(True)
        
        # if button_R is active this frame...
        if button_R.status == STARTED:
            # update params
            pass
        
        # *buttons_center* updates
        
        # if buttons_center is starting this frame...
        if buttons_center.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttons_center.frameNStart = frameN  # exact frame index
            buttons_center.tStart = t  # local t and not account for scr refresh
            buttons_center.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttons_center, 'tStartRefresh')  # time at next scr refresh
            # update status
            buttons_center.status = STARTED
            buttons_center.setAutoDraw(True)
        
        # if buttons_center is active this frame...
        if buttons_center.status == STARTED:
            # update params
            pass
        
        # *paralleltext* updates
        
        # if paralleltext is starting this frame...
        if paralleltext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            paralleltext.frameNStart = frameN  # exact frame index
            paralleltext.tStart = t  # local t and not account for scr refresh
            paralleltext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(paralleltext, 'tStartRefresh')  # time at next scr refresh
            # update status
            paralleltext.status = STARTED
            paralleltext.setAutoDraw(True)
        
        # if paralleltext is active this frame...
        if paralleltext.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice1" ---
    for thisComponent in practice1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('practice1.stopped', globalClock.getTime())
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "practice1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('feedback.started', globalClock.getTime())
    # keep track of which components have finished
    feedbackComponents = [text]
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
    frameN = -1
    
    # --- Run Routine "feedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('feedback.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "practice2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('practice2.started', globalClock.getTime())
    # Run 'Begin Routine' code from code_2
    #no really, hide the mouse
    win.mouseVisible = False
    
    #set corrans
    corrans = [80, 260, -100, -280]
    blueline_2.setPos((0.3, 0.3))
    blueline_2.setSize((0.1, 0))
    blueline_2.setOri(100.0)
    blue_correct_2.setPos((0.3, 0.3))
    blue_correct_2.setSize((0.12, 0))
    blue_correct_2.setOri(80.0)
    redline_2.setPos((-0.2, 0.1))
    redline_2.setSize((0.1, 0))
    redline_2.setOri(80.0)
    red_correct_2.setPos((-0.2, 0.1))
    red_correct_2.setSize((0.12, 0))
    red_correct_2.setOri(80.0)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    practice2Components = [blueline_2, blue_correct_2, redline_2, red_correct_2, button_L_2, button_R_2, buttons_center_2, paralleltext_2, key_resp_2]
    for thisComponent in practice2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_2
        #get current response
        resp = event.getKeys(['1','2'])
        
        if len(resp):
            if resp[0] == '1':
                blueline_2.setOri(5,'-')
                if blueline_2.ori in corrans:
                    red_correct_2.opacity = 0.2
                    blue_correct_2.opacity = 0.2
                    paralleltext_2.pos = (0,0)
                else:
                    red_correct_2.opacity = 0
                    blue_correct_2.opacity = 0
                    paralleltext_2.pos = (0,2)
            elif resp[0] == '2':
                blueline_2.setOri(5,'+')
                if blueline_2.ori in corrans:
                    red_correct_2.opacity = 0.2
                    blue_correct_2.opacity = 0.2
                    paralleltext_2.pos = (0,0)
                else:
                    red_correct_2.opacity = 0
                    blue_correct_2.opacity = 0
                    paralleltext_2.pos = (0,2)
        
        # *blueline_2* updates
        
        # if blueline_2 is starting this frame...
        if blueline_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blueline_2.frameNStart = frameN  # exact frame index
            blueline_2.tStart = t  # local t and not account for scr refresh
            blueline_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blueline_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            blueline_2.status = STARTED
            blueline_2.setAutoDraw(True)
        
        # if blueline_2 is active this frame...
        if blueline_2.status == STARTED:
            # update params
            pass
        
        # *blue_correct_2* updates
        
        # if blue_correct_2 is starting this frame...
        if blue_correct_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blue_correct_2.frameNStart = frameN  # exact frame index
            blue_correct_2.tStart = t  # local t and not account for scr refresh
            blue_correct_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blue_correct_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            blue_correct_2.status = STARTED
            blue_correct_2.setAutoDraw(True)
        
        # if blue_correct_2 is active this frame...
        if blue_correct_2.status == STARTED:
            # update params
            pass
        
        # *redline_2* updates
        
        # if redline_2 is starting this frame...
        if redline_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            redline_2.frameNStart = frameN  # exact frame index
            redline_2.tStart = t  # local t and not account for scr refresh
            redline_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(redline_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            redline_2.status = STARTED
            redline_2.setAutoDraw(True)
        
        # if redline_2 is active this frame...
        if redline_2.status == STARTED:
            # update params
            pass
        
        # *red_correct_2* updates
        
        # if red_correct_2 is starting this frame...
        if red_correct_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_correct_2.frameNStart = frameN  # exact frame index
            red_correct_2.tStart = t  # local t and not account for scr refresh
            red_correct_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_correct_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            red_correct_2.status = STARTED
            red_correct_2.setAutoDraw(True)
        
        # if red_correct_2 is active this frame...
        if red_correct_2.status == STARTED:
            # update params
            pass
        
        # *button_L_2* updates
        
        # if button_L_2 is starting this frame...
        if button_L_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_L_2.frameNStart = frameN  # exact frame index
            button_L_2.tStart = t  # local t and not account for scr refresh
            button_L_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_L_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_L_2.status = STARTED
            button_L_2.setAutoDraw(True)
        
        # if button_L_2 is active this frame...
        if button_L_2.status == STARTED:
            # update params
            pass
        
        # *button_R_2* updates
        
        # if button_R_2 is starting this frame...
        if button_R_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_R_2.frameNStart = frameN  # exact frame index
            button_R_2.tStart = t  # local t and not account for scr refresh
            button_R_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_R_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_R_2.status = STARTED
            button_R_2.setAutoDraw(True)
        
        # if button_R_2 is active this frame...
        if button_R_2.status == STARTED:
            # update params
            pass
        
        # *buttons_center_2* updates
        
        # if buttons_center_2 is starting this frame...
        if buttons_center_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttons_center_2.frameNStart = frameN  # exact frame index
            buttons_center_2.tStart = t  # local t and not account for scr refresh
            buttons_center_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttons_center_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            buttons_center_2.status = STARTED
            buttons_center_2.setAutoDraw(True)
        
        # if buttons_center_2 is active this frame...
        if buttons_center_2.status == STARTED:
            # update params
            pass
        
        # *paralleltext_2* updates
        
        # if paralleltext_2 is starting this frame...
        if paralleltext_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            paralleltext_2.frameNStart = frameN  # exact frame index
            paralleltext_2.tStart = t  # local t and not account for scr refresh
            paralleltext_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(paralleltext_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            paralleltext_2.status = STARTED
            paralleltext_2.setAutoDraw(True)
        
        # if paralleltext_2 is active this frame...
        if paralleltext_2.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice2" ---
    for thisComponent in practice2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('practice2.stopped', globalClock.getTime())
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "practice2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('feedback.started', globalClock.getTime())
    # keep track of which components have finished
    feedbackComponents = [text]
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
    frameN = -1
    
    # --- Run Routine "feedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('feedback.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "practice3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('practice3.started', globalClock.getTime())
    # Run 'Begin Routine' code from code_3
    #no really, hide the mouse
    win.mouseVisible = False
    
    #set corrans
    corrans = [140, -40, -220, 320]
    blueline_3.setPos((-0.35, -0.15))
    blueline_3.setSize((0.1, 0))
    blueline_3.setOri(90.0)
    blue_correct_3.setPos((-0.35, -0.15))
    blue_correct_3.setSize((0.12, 0))
    blue_correct_3.setOri(140.0)
    redline_3.setPos((0.4, -.15))
    redline_3.setSize((0.1, 0))
    redline_3.setOri(140.0)
    red_correct_3.setPos((0.4, -.15))
    red_correct_3.setSize((0.12, 0))
    red_correct_3.setOri(140.0)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    practice3Components = [blueline_3, blue_correct_3, redline_3, red_correct_3, button_L_3, button_R_3, buttons_center_3, paralleltext_3, key_resp_3]
    for thisComponent in practice3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_3
        #get current response
        resp = event.getKeys(['1','2'])
        
        if len(resp):
            if resp[0] == '1':
                blueline_3.setOri(10,'-')
                if blueline_3.ori in corrans:
                    red_correct_3.opacity = 0.2
                    blue_correct_3.opacity = 0.2
                    paralleltext_3.pos = (0,0)
                else:
                    red_correct_3.opacity = 0
                    blue_correct_3.opacity = 0
                    paralleltext_3.pos = (0,2)
            elif resp[0] == '2':
                blueline_3.setOri(10,'+')
                if blueline_3.ori in corrans:
                    red_correct_3.opacity = 0.2
                    blue_correct_3.opacity = 0.2
                    paralleltext_3.pos = (0,0)
                else:
                    red_correct_3.opacity = 0
                    blue_correct_3.opacity = 0
                    paralleltext_3.pos = (0,2)
        
        # *blueline_3* updates
        
        # if blueline_3 is starting this frame...
        if blueline_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blueline_3.frameNStart = frameN  # exact frame index
            blueline_3.tStart = t  # local t and not account for scr refresh
            blueline_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blueline_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            blueline_3.status = STARTED
            blueline_3.setAutoDraw(True)
        
        # if blueline_3 is active this frame...
        if blueline_3.status == STARTED:
            # update params
            pass
        
        # *blue_correct_3* updates
        
        # if blue_correct_3 is starting this frame...
        if blue_correct_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blue_correct_3.frameNStart = frameN  # exact frame index
            blue_correct_3.tStart = t  # local t and not account for scr refresh
            blue_correct_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blue_correct_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            blue_correct_3.status = STARTED
            blue_correct_3.setAutoDraw(True)
        
        # if blue_correct_3 is active this frame...
        if blue_correct_3.status == STARTED:
            # update params
            pass
        
        # *redline_3* updates
        
        # if redline_3 is starting this frame...
        if redline_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            redline_3.frameNStart = frameN  # exact frame index
            redline_3.tStart = t  # local t and not account for scr refresh
            redline_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(redline_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            redline_3.status = STARTED
            redline_3.setAutoDraw(True)
        
        # if redline_3 is active this frame...
        if redline_3.status == STARTED:
            # update params
            pass
        
        # *red_correct_3* updates
        
        # if red_correct_3 is starting this frame...
        if red_correct_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_correct_3.frameNStart = frameN  # exact frame index
            red_correct_3.tStart = t  # local t and not account for scr refresh
            red_correct_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_correct_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            red_correct_3.status = STARTED
            red_correct_3.setAutoDraw(True)
        
        # if red_correct_3 is active this frame...
        if red_correct_3.status == STARTED:
            # update params
            pass
        
        # *button_L_3* updates
        
        # if button_L_3 is starting this frame...
        if button_L_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_L_3.frameNStart = frameN  # exact frame index
            button_L_3.tStart = t  # local t and not account for scr refresh
            button_L_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_L_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_L_3.status = STARTED
            button_L_3.setAutoDraw(True)
        
        # if button_L_3 is active this frame...
        if button_L_3.status == STARTED:
            # update params
            pass
        
        # *button_R_3* updates
        
        # if button_R_3 is starting this frame...
        if button_R_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_R_3.frameNStart = frameN  # exact frame index
            button_R_3.tStart = t  # local t and not account for scr refresh
            button_R_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_R_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_R_3.status = STARTED
            button_R_3.setAutoDraw(True)
        
        # if button_R_3 is active this frame...
        if button_R_3.status == STARTED:
            # update params
            pass
        
        # *buttons_center_3* updates
        
        # if buttons_center_3 is starting this frame...
        if buttons_center_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttons_center_3.frameNStart = frameN  # exact frame index
            buttons_center_3.tStart = t  # local t and not account for scr refresh
            buttons_center_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttons_center_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            buttons_center_3.status = STARTED
            buttons_center_3.setAutoDraw(True)
        
        # if buttons_center_3 is active this frame...
        if buttons_center_3.status == STARTED:
            # update params
            pass
        
        # *paralleltext_3* updates
        
        # if paralleltext_3 is starting this frame...
        if paralleltext_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            paralleltext_3.frameNStart = frameN  # exact frame index
            paralleltext_3.tStart = t  # local t and not account for scr refresh
            paralleltext_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(paralleltext_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            paralleltext_3.status = STARTED
            paralleltext_3.setAutoDraw(True)
        
        # if paralleltext_3 is active this frame...
        if paralleltext_3.status == STARTED:
            # update params
            pass
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice3" ---
    for thisComponent in practice3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('practice3.stopped', globalClock.getTime())
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "practice3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "end_prep" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end_prep.started', globalClock.getTime())
    enter_3.keys = []
    enter_3.rt = []
    _enter_3_allKeys = []
    # keep track of which components have finished
    end_prepComponents = [instr3, enter_3]
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
    frameN = -1
    
    # --- Run Routine "end_prep" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr3* updates
        
        # if instr3 is starting this frame...
        if instr3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr3.frameNStart = frameN  # exact frame index
            instr3.tStart = t  # local t and not account for scr refresh
            instr3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr3, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr3.status = STARTED
            instr3.setAutoDraw(True)
        
        # if instr3 is active this frame...
        if instr3.status == STARTED:
            # update params
            pass
        
        # *enter_3* updates
        waitOnFlip = False
        
        # if enter_3 is starting this frame...
        if enter_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enter_3.frameNStart = frameN  # exact frame index
            enter_3.tStart = t  # local t and not account for scr refresh
            enter_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enter_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            enter_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(enter_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(enter_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if enter_3.status == STARTED and not waitOnFlip:
            theseKeys = enter_3.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _enter_3_allKeys.extend(theseKeys)
            if len(_enter_3_allKeys):
                enter_3.keys = _enter_3_allKeys[-1].name  # just the last key pressed
                enter_3.rt = _enter_3_allKeys[-1].rt
                enter_3.duration = _enter_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_prepComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_prep" ---
    for thisComponent in end_prepComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end_prep.stopped', globalClock.getTime())
    # the Routine "end_prep" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
