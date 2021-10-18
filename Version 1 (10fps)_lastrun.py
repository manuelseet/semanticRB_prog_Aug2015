#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), October 28, 2015, at 17:21
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'semantic experiment'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath="C:\\Users\\viscoglab\\Desktop\\Manuel's Experiment\\Other FPS's\\Version 1 (10fps).psyexp",
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 1024), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructions = visual.TextStim(win=win, ori=0, name='instructions',
    text='Welcome to the experiment.\n\nPlease press the spacebar to continue.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instrc_2"
instrc_2Clock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='You will be presented with a series of words or images. Immediately after the end of each trial, please report the words or pictures in the order you saw them.\n\nIf you saw an item twice, you are to report it twice (e.g. key,box, key)\n\nPress the spacebar to begin your practice trials.',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "prac1"
prac1Clock = core.Clock()
text_31 = visual.TextStim(win=win, ori=0, name='text_31',
    text='%%%%%%%',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
dist1a = visual.TextStim(win=win, ori=0, name='dist1a',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
crit1a = visual.TextStim(win=win, ori=0, name='crit1a',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
dist2a = visual.TextStim(win=win, ori=0, name='dist2a',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)
crit2a = visual.TextStim(win=win, ori=0, name='crit2a',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)
dist3a = visual.TextStim(win=win, ori=0, name='dist3a',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0)
endmaska = visual.TextStim(win=win, ori=0, name='endmaska',
    text='%%%%%%%',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)
text_34 = visual.TextStim(win=win, ori=0, name='text_34',
    text='Please report the items in the order you saw them. \n\nSay the item twice if you saw it twice.\n\n\nPress the spacebar to continue after reporting',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "instrc_3"
instrc_3Clock = core.Clock()
text_35 = visual.TextStim(win=win, ori=0, name='text_35',
    text='The stream will now be presented at a faster rate.\n\nPress the spacebar to begin the practice.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "prac2"
prac2Clock = core.Clock()
text_16 = visual.TextStim(win=win, ori=0, name='text_16',
    text='%%%%%%%',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
text_19 = visual.TextStim(win=win, ori=0, name='text_19',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_20 = visual.TextStim(win=win, ori=0, name='text_20',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_21 = visual.TextStim(win=win, ori=0, name='text_21',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)
text_22 = visual.TextStim(win=win, ori=0, name='text_22',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)
text_23 = visual.TextStim(win=win, ori=0, name='text_23',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0)
text_24 = visual.TextStim(win=win, ori=0, name='text_24',
    text='%%%%%%%',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)
text_25 = visual.TextStim(win=win, ori=0, name='text_25',
    text='Please report the items in the order you saw them. \n\nSay the item twice if you saw it twice.\n\n\nPress the spacebar to continue after reporting',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "instrc_4"
instrc_4Clock = core.Clock()
text_36 = visual.TextStim(win=win, ori=0, name='text_36',
    text='The stream will be presented at an even faster rate. This is will be the rate for the entire experiment.\n\nPress the spacebar to begin the practice.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "prac3_2"
prac3_2Clock = core.Clock()
text_26 = visual.TextStim(win=win, ori=0, name='text_26',
    text='%%%%%%%',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
dist1 = visual.TextStim(win=win, ori=0, name='dist1',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
crit1 = visual.TextStim(win=win, ori=0, name='crit1',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
dist2 = visual.TextStim(win=win, ori=0, name='dist2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)
crit2 = visual.TextStim(win=win, ori=0, name='crit2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)
dist3 = visual.TextStim(win=win, ori=0, name='dist3',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0)
text_29 = visual.TextStim(win=win, ori=0, name='text_29',
    text='%%%%%%%',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)
text_30 = visual.TextStim(win=win, ori=0, name='text_30',
    text='Please report the items in the order you saw them. \n\nSay the item twice if you saw it twice.\n\n\nPress the spacebar to continue after reporting',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "instr_real"
instr_realClock = core.Clock()
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text='This marks the end of your practice trials.\n\nPress the spacebar to begin the experiment.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
fixmask1 = visual.TextStim(win=win, ori=0, name='fixmask1',
    text='%%%%%%%%',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
d1 = visual.TextStim(win=win, ori=0, name='d1',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
c1 = visual.TextStim(win=win, ori=0, name='c1',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)
d2 = visual.TextStim(win=win, ori=0, name='d2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)
c2 = visual.TextStim(win=win, ori=0, name='c2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0)
text_9 = visual.TextStim(win=win, ori=0, name='text_9',
    text='%%%%%%%%',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text='Please report the items you saw.\n\nPress the spacebar to continue.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "break_instructions"
break_instructionsClock = core.Clock()
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text='You have come to the end of the first section of the experiment.\n\nYou may take a short break.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "pic_familiar"
pic_familiarClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='The experimenter will now hand you a list of pictures. \nPlease familiarise yourself with the pictures and their names.\n\nPress the spacebar when you are ready to start the second section.\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "pic_trial"
pic_trialClock = core.Clock()
mask1 = visual.ImageStim(win=win, name='mask1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
picC1 = visual.ImageStim(win=win, name='picC1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
picD1 = visual.ImageStim(win=win, name='picD1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
picC2 = visual.ImageStim(win=win, name='picC2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
picD2 = visual.ImageStim(win=win, name='picD2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
mask2 = visual.ImageStim(win=win, name='mask2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
final = visual.TextStim(win=win, ori=0, name='final',
    text='Please report the items you saw.\n\nPress the spacebar to continue after reporting',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "numbers_instructions"
numbers_instructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='This marks the end of the second section.\n\nPress the spacebar when you are ready to commence the final section of this experiment.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
fixmask1 = visual.TextStim(win=win, ori=0, name='fixmask1',
    text='%%%%%%%%',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
d1 = visual.TextStim(win=win, ori=0, name='d1',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
c1 = visual.TextStim(win=win, ori=0, name='c1',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)
d2 = visual.TextStim(win=win, ori=0, name='d2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)
c2 = visual.TextStim(win=win, ori=0, name='c2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0)
text_9 = visual.TextStim(win=win, ori=0, name='text_9',
    text='%%%%%%%%',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text='Please report the items you saw.\n\nPress the spacebar to continue.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='This marks the end of the experiment. \n\nThank you for your participation.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_start = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_start.status = NOT_STARTED
# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(instructions)
InstructionsComponents.append(key_resp_start)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if t >= 0.0 and instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions.tStart = t  # underestimates by a little under one frame
        instructions.frameNStart = frameN  # exact frame index
        instructions.setAutoDraw(True)
    
    # *key_resp_start* updates
    if t >= 1 and key_resp_start.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_start.tStart = t  # underestimates by a little under one frame
        key_resp_start.frameNStart = frameN  # exact frame index
        key_resp_start.status = STARTED
        # keyboard checking is just starting
        key_resp_start.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_start.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_start.keys = theseKeys[-1]  # just the last key pressed
            key_resp_start.rt = key_resp_start.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_start.keys in ['', [], None]:  # No response was made
   key_resp_start.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_start.keys',key_resp_start.keys)
if key_resp_start.keys != None:  # we had a response
    thisExp.addData('key_resp_start.rt', key_resp_start.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instrc_2"-------
t = 0
instrc_2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
instrc_2Components = []
instrc_2Components.append(text_4)
instrc_2Components.append(key_resp_5)
for thisComponent in instrc_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instrc_2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrc_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t  # underestimates by a little under one frame
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 3 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        key_resp_5.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrc_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instrc_2"-------
for thisComponent in instrc_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
   key_resp_5.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "instrc_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath="C:\\Users\\viscoglab\\Desktop\\Manuel's Experiment\\Other FPS's\\Version 1 (10fps).psyexp",
    trialList=data.importConditions('Numbers Expt Prac Stimuli.xlsx'),
    seed=None, name='practice1')
thisExp.addLoop(practice1)  # add the loop to the experiment
thisPractice1 = practice1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPractice1.rgb)
if thisPractice1 != None:
    for paramName in thisPractice1.keys():
        exec(paramName + '= thisPractice1.' + paramName)

for thisPractice1 in practice1:
    currentLoop = practice1
    # abbreviate parameter names if possible (e.g. rgb = thisPractice1.rgb)
    if thisPractice1 != None:
        for paramName in thisPractice1.keys():
            exec(paramName + '= thisPractice1.' + paramName)
    
    #------Prepare to start Routine "prac1"-------
    t = 0
    prac1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    dist1a.setText(D1a)
    crit1a.setText(C1a)
    dist2a.setText(D2a)
    crit2a.setText(C2a)
    dist3a.setText(D3a)
    key_resp_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_10.status = NOT_STARTED
    # keep track of which components have finished
    prac1Components = []
    prac1Components.append(text_31)
    prac1Components.append(dist1a)
    prac1Components.append(crit1a)
    prac1Components.append(dist2a)
    prac1Components.append(crit2a)
    prac1Components.append(dist3a)
    prac1Components.append(endmaska)
    prac1Components.append(text_34)
    prac1Components.append(key_resp_10)
    for thisComponent in prac1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "prac1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = prac1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_31* updates
        if t >= 2 and text_31.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_31.tStart = t  # underestimates by a little under one frame
            text_31.frameNStart = frameN  # exact frame index
            text_31.setAutoDraw(True)
        if text_31.status == STARTED and t >= (2 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_31.setAutoDraw(False)
        
        # *dist1a* updates
        if t >= 3.0 and dist1a.status == NOT_STARTED:
            # keep track of start time/frame for later
            dist1a.tStart = t  # underestimates by a little under one frame
            dist1a.frameNStart = frameN  # exact frame index
            dist1a.setAutoDraw(True)
        if dist1a.status == STARTED and t >= (3.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            dist1a.setAutoDraw(False)
        
        # *crit1a* updates
        if t >= 3.5 and crit1a.status == NOT_STARTED:
            # keep track of start time/frame for later
            crit1a.tStart = t  # underestimates by a little under one frame
            crit1a.frameNStart = frameN  # exact frame index
            crit1a.setAutoDraw(True)
        if crit1a.status == STARTED and t >= (3.5 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            crit1a.setAutoDraw(False)
        
        # *dist2a* updates
        if t >= 4 and dist2a.status == NOT_STARTED:
            # keep track of start time/frame for later
            dist2a.tStart = t  # underestimates by a little under one frame
            dist2a.frameNStart = frameN  # exact frame index
            dist2a.setAutoDraw(True)
        if dist2a.status == STARTED and t >= (4 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            dist2a.setAutoDraw(False)
        
        # *crit2a* updates
        if t >= 4.5 and crit2a.status == NOT_STARTED:
            # keep track of start time/frame for later
            crit2a.tStart = t  # underestimates by a little under one frame
            crit2a.frameNStart = frameN  # exact frame index
            crit2a.setAutoDraw(True)
        if crit2a.status == STARTED and t >= (4.5 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            crit2a.setAutoDraw(False)
        
        # *dist3a* updates
        if t >= 5 and dist3a.status == NOT_STARTED:
            # keep track of start time/frame for later
            dist3a.tStart = t  # underestimates by a little under one frame
            dist3a.frameNStart = frameN  # exact frame index
            dist3a.setAutoDraw(True)
        if dist3a.status == STARTED and t >= (5 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            dist3a.setAutoDraw(False)
        
        # *endmaska* updates
        if t >= 5.5 and endmaska.status == NOT_STARTED:
            # keep track of start time/frame for later
            endmaska.tStart = t  # underestimates by a little under one frame
            endmaska.frameNStart = frameN  # exact frame index
            endmaska.setAutoDraw(True)
        if endmaska.status == STARTED and t >= (5.5 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            endmaska.setAutoDraw(False)
        
        # *text_34* updates
        if t >= 6.5 and text_34.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_34.tStart = t  # underestimates by a little under one frame
            text_34.frameNStart = frameN  # exact frame index
            text_34.setAutoDraw(True)
        
        # *key_resp_10* updates
        if t >= 6.5 and key_resp_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_10.tStart = t  # underestimates by a little under one frame
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            key_resp_10.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_10.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_10.keys = theseKeys[-1]  # just the last key pressed
                key_resp_10.rt = key_resp_10.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "prac1"-------
    for thisComponent in prac1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
       key_resp_10.keys=None
    # store data for practice1 (TrialHandler)
    practice1.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        practice1.addData('key_resp_10.rt', key_resp_10.rt)
    # the Routine "prac1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice1'


#------Prepare to start Routine "instrc_3"-------
t = 0
instrc_3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_11 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_11.status = NOT_STARTED
# keep track of which components have finished
instrc_3Components = []
instrc_3Components.append(text_35)
instrc_3Components.append(key_resp_11)
for thisComponent in instrc_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instrc_3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrc_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_35* updates
    if t >= 0.0 and text_35.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_35.tStart = t  # underestimates by a little under one frame
        text_35.frameNStart = frameN  # exact frame index
        text_35.setAutoDraw(True)
    
    # *key_resp_11* updates
    if t >= 3 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t  # underestimates by a little under one frame
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        key_resp_11.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_11.keys = theseKeys[-1]  # just the last key pressed
            key_resp_11.rt = key_resp_11.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrc_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instrc_3"-------
for thisComponent in instrc_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
   key_resp_11.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.nextEntry()
# the Routine "instrc_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath="C:\\Users\\viscoglab\\Desktop\\Manuel's Experiment\\Other FPS's\\Version 1 (10fps).psyexp",
    trialList=data.importConditions('Numbers Expt Prac Stimuli.xlsx'),
    seed=None, name='practice2')
thisExp.addLoop(practice2)  # add the loop to the experiment
thisPractice2 = practice2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPractice2.rgb)
if thisPractice2 != None:
    for paramName in thisPractice2.keys():
        exec(paramName + '= thisPractice2.' + paramName)

for thisPractice2 in practice2:
    currentLoop = practice2
    # abbreviate parameter names if possible (e.g. rgb = thisPractice2.rgb)
    if thisPractice2 != None:
        for paramName in thisPractice2.keys():
            exec(paramName + '= thisPractice2.' + paramName)
    
    #------Prepare to start Routine "prac2"-------
    t = 0
    prac2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    text_19.setText(D1b)
    text_20.setText(C1b)
    text_21.setText(D2b)
    text_22.setText(C2b)
    text_23.setText(D3b)
    key_resp_8 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_8.status = NOT_STARTED
    # keep track of which components have finished
    prac2Components = []
    prac2Components.append(text_16)
    prac2Components.append(text_19)
    prac2Components.append(text_20)
    prac2Components.append(text_21)
    prac2Components.append(text_22)
    prac2Components.append(text_23)
    prac2Components.append(text_24)
    prac2Components.append(text_25)
    prac2Components.append(key_resp_8)
    for thisComponent in prac2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "prac2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = prac2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_16* updates
        if t >= 1.25 and text_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_16.tStart = t  # underestimates by a little under one frame
            text_16.frameNStart = frameN  # exact frame index
            text_16.setAutoDraw(True)
        if text_16.status == STARTED and t >= (1.25 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_16.setAutoDraw(False)
        
        # *text_19* updates
        if t >= 2.25 and text_19.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_19.tStart = t  # underestimates by a little under one frame
            text_19.frameNStart = frameN  # exact frame index
            text_19.setAutoDraw(True)
        if text_19.status == STARTED and t >= (2.25 + (0.125-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_19.setAutoDraw(False)
        
        # *text_20* updates
        if t >= 2.375 and text_20.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_20.tStart = t  # underestimates by a little under one frame
            text_20.frameNStart = frameN  # exact frame index
            text_20.setAutoDraw(True)
        if text_20.status == STARTED and t >= (2.375 + (0.125-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_20.setAutoDraw(False)
        
        # *text_21* updates
        if t >= 2.50 and text_21.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_21.tStart = t  # underestimates by a little under one frame
            text_21.frameNStart = frameN  # exact frame index
            text_21.setAutoDraw(True)
        if text_21.status == STARTED and t >= (2.50 + (0.125-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_21.setAutoDraw(False)
        
        # *text_22* updates
        if t >= 2.625 and text_22.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_22.tStart = t  # underestimates by a little under one frame
            text_22.frameNStart = frameN  # exact frame index
            text_22.setAutoDraw(True)
        if text_22.status == STARTED and t >= (2.625 + (0.125-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_22.setAutoDraw(False)
        
        # *text_23* updates
        if t >= 2.750 and text_23.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_23.tStart = t  # underestimates by a little under one frame
            text_23.frameNStart = frameN  # exact frame index
            text_23.setAutoDraw(True)
        if text_23.status == STARTED and t >= (2.750 + (0.125-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_23.setAutoDraw(False)
        
        # *text_24* updates
        if t >= 2.875 and text_24.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_24.tStart = t  # underestimates by a little under one frame
            text_24.frameNStart = frameN  # exact frame index
            text_24.setAutoDraw(True)
        if text_24.status == STARTED and t >= (2.875 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_24.setAutoDraw(False)
        
        # *text_25* updates
        if t >= 3.875 and text_25.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_25.tStart = t  # underestimates by a little under one frame
            text_25.frameNStart = frameN  # exact frame index
            text_25.setAutoDraw(True)
        
        # *key_resp_8* updates
        if t >= 3.875 and key_resp_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_8.tStart = t  # underestimates by a little under one frame
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            key_resp_8.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_8.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_8.keys = theseKeys[-1]  # just the last key pressed
                key_resp_8.rt = key_resp_8.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "prac2"-------
    for thisComponent in prac2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
       key_resp_8.keys=None
    # store data for practice2 (TrialHandler)
    practice2.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        practice2.addData('key_resp_8.rt', key_resp_8.rt)
    # the Routine "prac2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice2'


#------Prepare to start Routine "instrc_4"-------
t = 0
instrc_4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_12 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_12.status = NOT_STARTED
# keep track of which components have finished
instrc_4Components = []
instrc_4Components.append(text_36)
instrc_4Components.append(key_resp_12)
for thisComponent in instrc_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instrc_4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrc_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_36* updates
    if t >= 0.0 and text_36.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_36.tStart = t  # underestimates by a little under one frame
        text_36.frameNStart = frameN  # exact frame index
        text_36.setAutoDraw(True)
    
    # *key_resp_12* updates
    if t >= 3 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t  # underestimates by a little under one frame
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        key_resp_12.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_12.keys = theseKeys[-1]  # just the last key pressed
            key_resp_12.rt = key_resp_12.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrc_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instrc_4"-------
for thisComponent in instrc_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
   key_resp_12.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.nextEntry()
# the Routine "instrc_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath="C:\\Users\\viscoglab\\Desktop\\Manuel's Experiment\\Other FPS's\\Version 1 (10fps).psyexp",
    trialList=data.importConditions('Numbers Expt Prac Stimuli.xlsx'),
    seed=None, name='practice3')
thisExp.addLoop(practice3)  # add the loop to the experiment
thisPractice3 = practice3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPractice3.rgb)
if thisPractice3 != None:
    for paramName in thisPractice3.keys():
        exec(paramName + '= thisPractice3.' + paramName)

for thisPractice3 in practice3:
    currentLoop = practice3
    # abbreviate parameter names if possible (e.g. rgb = thisPractice3.rgb)
    if thisPractice3 != None:
        for paramName in thisPractice3.keys():
            exec(paramName + '= thisPractice3.' + paramName)
    
    #------Prepare to start Routine "prac3_2"-------
    t = 0
    prac3_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    dist1.setText(D1c)
    crit1.setText(C1c)
    dist2.setText(D2c)
    crit2.setText(C2c)
    dist3.setText(D3c)
    key_resp_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_9.status = NOT_STARTED
    # keep track of which components have finished
    prac3_2Components = []
    prac3_2Components.append(text_26)
    prac3_2Components.append(dist1)
    prac3_2Components.append(crit1)
    prac3_2Components.append(dist2)
    prac3_2Components.append(crit2)
    prac3_2Components.append(dist3)
    prac3_2Components.append(text_29)
    prac3_2Components.append(text_30)
    prac3_2Components.append(key_resp_9)
    for thisComponent in prac3_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "prac3_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = prac3_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_26* updates
        if t >= 1.2 and text_26.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_26.tStart = t  # underestimates by a little under one frame
            text_26.frameNStart = frameN  # exact frame index
            text_26.setAutoDraw(True)
        if text_26.status == STARTED and t >= (1.2 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_26.setAutoDraw(False)
        
        # *dist1* updates
        if t >= 2.2 and dist1.status == NOT_STARTED:
            # keep track of start time/frame for later
            dist1.tStart = t  # underestimates by a little under one frame
            dist1.frameNStart = frameN  # exact frame index
            dist1.setAutoDraw(True)
        if dist1.status == STARTED and t >= (2.2 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            dist1.setAutoDraw(False)
        
        # *crit1* updates
        if t >= 2.3 and crit1.status == NOT_STARTED:
            # keep track of start time/frame for later
            crit1.tStart = t  # underestimates by a little under one frame
            crit1.frameNStart = frameN  # exact frame index
            crit1.setAutoDraw(True)
        if crit1.status == STARTED and t >= (2.3 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            crit1.setAutoDraw(False)
        
        # *dist2* updates
        if t >= 2.4 and dist2.status == NOT_STARTED:
            # keep track of start time/frame for later
            dist2.tStart = t  # underestimates by a little under one frame
            dist2.frameNStart = frameN  # exact frame index
            dist2.setAutoDraw(True)
        if dist2.status == STARTED and t >= (2.4 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            dist2.setAutoDraw(False)
        
        # *crit2* updates
        if t >= 2.5 and crit2.status == NOT_STARTED:
            # keep track of start time/frame for later
            crit2.tStart = t  # underestimates by a little under one frame
            crit2.frameNStart = frameN  # exact frame index
            crit2.setAutoDraw(True)
        if crit2.status == STARTED and t >= (2.5 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            crit2.setAutoDraw(False)
        
        # *dist3* updates
        if t >= 2.6 and dist3.status == NOT_STARTED:
            # keep track of start time/frame for later
            dist3.tStart = t  # underestimates by a little under one frame
            dist3.frameNStart = frameN  # exact frame index
            dist3.setAutoDraw(True)
        if dist3.status == STARTED and t >= (2.6 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            dist3.setAutoDraw(False)
        
        # *text_29* updates
        if t >= 2.7 and text_29.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_29.tStart = t  # underestimates by a little under one frame
            text_29.frameNStart = frameN  # exact frame index
            text_29.setAutoDraw(True)
        if text_29.status == STARTED and t >= (2.7 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_29.setAutoDraw(False)
        
        # *text_30* updates
        if t >= 3.7 and text_30.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_30.tStart = t  # underestimates by a little under one frame
            text_30.frameNStart = frameN  # exact frame index
            text_30.setAutoDraw(True)
        
        # *key_resp_9* updates
        if t >= 3.7 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t  # underestimates by a little under one frame
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            key_resp_9.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_9.keys = theseKeys[-1]  # just the last key pressed
                key_resp_9.rt = key_resp_9.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac3_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "prac3_2"-------
    for thisComponent in prac3_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
       key_resp_9.keys=None
    # store data for practice3 (TrialHandler)
    practice3.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        practice3.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "prac3_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice3'


#------Prepare to start Routine "instr_real"-------
t = 0
instr_realClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_6.status = NOT_STARTED
# keep track of which components have finished
instr_realComponents = []
instr_realComponents.append(text_6)
instr_realComponents.append(key_resp_6)
for thisComponent in instr_realComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr_real"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr_realClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # underestimates by a little under one frame
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 3 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # underestimates by a little under one frame
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        key_resp_6.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_realComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr_real"-------
for thisComponent in instr_realComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
   key_resp_6.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "instr_real" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
words = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath="C:\\Users\\viscoglab\\Desktop\\Manuel's Experiment\\Other FPS's\\Version 1 (10fps).psyexp",
    trialList=data.importConditions('Word V1.1.xlsx'),
    seed=None, name='words')
thisExp.addLoop(words)  # add the loop to the experiment
thisWord = words.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisWord.rgb)
if thisWord != None:
    for paramName in thisWord.keys():
        exec(paramName + '= thisWord.' + paramName)

for thisWord in words:
    currentLoop = words
    # abbreviate parameter names if possible (e.g. rgb = thisWord.rgb)
    if thisWord != None:
        for paramName in thisWord.keys():
            exec(paramName + '= thisWord.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    d1.setText(C1)
    c1.setText(D1)
    d2.setText(C2)
    c2.setText(D2)
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(fixmask1)
    trialComponents.append(d1)
    trialComponents.append(c1)
    trialComponents.append(d2)
    trialComponents.append(c2)
    trialComponents.append(text_9)
    trialComponents.append(text_10)
    trialComponents.append(key_resp_2)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixmask1* updates
        if frameN >= 100 and fixmask1.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixmask1.tStart = t  # underestimates by a little under one frame
            fixmask1.frameNStart = frameN  # exact frame index
            fixmask1.setAutoDraw(True)
        if fixmask1.status == STARTED and frameN >= (fixmask1.frameNStart + 100):
            fixmask1.setAutoDraw(False)
        
        # *d1* updates
        if frameN >= 200 and d1.status == NOT_STARTED:
            # keep track of start time/frame for later
            d1.tStart = t  # underestimates by a little under one frame
            d1.frameNStart = frameN  # exact frame index
            d1.setAutoDraw(True)
        if d1.status == STARTED and frameN >= (d1.frameNStart + 10):
            d1.setAutoDraw(False)
        
        # *c1* updates
        if frameN >= 210 and c1.status == NOT_STARTED:
            # keep track of start time/frame for later
            c1.tStart = t  # underestimates by a little under one frame
            c1.frameNStart = frameN  # exact frame index
            c1.setAutoDraw(True)
        if c1.status == STARTED and frameN >= (c1.frameNStart + 10):
            c1.setAutoDraw(False)
        
        # *d2* updates
        if frameN >= 220 and d2.status == NOT_STARTED:
            # keep track of start time/frame for later
            d2.tStart = t  # underestimates by a little under one frame
            d2.frameNStart = frameN  # exact frame index
            d2.setAutoDraw(True)
        if d2.status == STARTED and frameN >= (d2.frameNStart + 10):
            d2.setAutoDraw(False)
        
        # *c2* updates
        if frameN >= 230 and c2.status == NOT_STARTED:
            # keep track of start time/frame for later
            c2.tStart = t  # underestimates by a little under one frame
            c2.frameNStart = frameN  # exact frame index
            c2.setAutoDraw(True)
        if c2.status == STARTED and frameN >= (c2.frameNStart + 10):
            c2.setAutoDraw(False)
        
        # *text_9* updates
        if frameN >= 240 and text_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_9.tStart = t  # underestimates by a little under one frame
            text_9.frameNStart = frameN  # exact frame index
            text_9.setAutoDraw(True)
        if text_9.status == STARTED and frameN >= (text_9.frameNStart + 110):
            text_9.setAutoDraw(False)
        
        # *text_10* updates
        if frameN >= 350 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t  # underestimates by a little under one frame
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        
        # *key_resp_2* updates
        if frameN >= 350 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
    # store data for words (TrialHandler)
    words.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        words.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'words'


#------Prepare to start Routine "break_instructions"-------
t = 0
break_instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
break_instructionsComponents = []
break_instructionsComponents.append(text_5)
break_instructionsComponents.append(key_resp_4)
for thisComponent in break_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "break_instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = break_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # underestimates by a little under one frame
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 3 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "break_instructions"-------
for thisComponent in break_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
   key_resp_4.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "break_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "pic_familiar"-------
t = 0
pic_familiarClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_15 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_15.status = NOT_STARTED
# keep track of which components have finished
pic_familiarComponents = []
pic_familiarComponents.append(text_3)
pic_familiarComponents.append(key_resp_15)
for thisComponent in pic_familiarComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "pic_familiar"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = pic_familiarClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # *key_resp_15* updates
    if t >= 2 and key_resp_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_15.tStart = t  # underestimates by a little under one frame
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        key_resp_15.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_15.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_15.keys = theseKeys[-1]  # just the last key pressed
            key_resp_15.rt = key_resp_15.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pic_familiarComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "pic_familiar"-------
for thisComponent in pic_familiarComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_15.keys in ['', [], None]:  # No response was made
   key_resp_15.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_15.keys',key_resp_15.keys)
if key_resp_15.keys != None:  # we had a response
    thisExp.addData('key_resp_15.rt', key_resp_15.rt)
thisExp.nextEntry()
# the Routine "pic_familiar" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pictures = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath="C:\\Users\\viscoglab\\Desktop\\Manuel's Experiment\\Other FPS's\\Version 1 (10fps).psyexp",
    trialList=data.importConditions('Picture V2.1.xlsx'),
    seed=None, name='pictures')
thisExp.addLoop(pictures)  # add the loop to the experiment
thisPicture = pictures.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPicture.rgb)
if thisPicture != None:
    for paramName in thisPicture.keys():
        exec(paramName + '= thisPicture.' + paramName)

for thisPicture in pictures:
    currentLoop = pictures
    # abbreviate parameter names if possible (e.g. rgb = thisPicture.rgb)
    if thisPicture != None:
        for paramName in thisPicture.keys():
            exec(paramName + '= thisPicture.' + paramName)
    
    #------Prepare to start Routine "pic_trial"-------
    t = 0
    pic_trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    mask1.setImage(M1)
    picC1.setImage(C1)
    picD1.setImage(D1)
    picC2.setImage(C2)
    picD2.setImage(D2)
    mask2.setImage(M2)
    key_resp_14 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_14.status = NOT_STARTED
    # keep track of which components have finished
    pic_trialComponents = []
    pic_trialComponents.append(mask1)
    pic_trialComponents.append(picC1)
    pic_trialComponents.append(picD1)
    pic_trialComponents.append(picC2)
    pic_trialComponents.append(picD2)
    pic_trialComponents.append(mask2)
    pic_trialComponents.append(final)
    pic_trialComponents.append(key_resp_14)
    for thisComponent in pic_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pic_trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = pic_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mask1* updates
        if frameN >= 100 and mask1.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask1.tStart = t  # underestimates by a little under one frame
            mask1.frameNStart = frameN  # exact frame index
            mask1.setAutoDraw(True)
        if mask1.status == STARTED and frameN >= (mask1.frameNStart + 100):
            mask1.setAutoDraw(False)
        
        # *picC1* updates
        if frameN >= 200 and picC1.status == NOT_STARTED:
            # keep track of start time/frame for later
            picC1.tStart = t  # underestimates by a little under one frame
            picC1.frameNStart = frameN  # exact frame index
            picC1.setAutoDraw(True)
        if picC1.status == STARTED and frameN >= (picC1.frameNStart + 9):
            picC1.setAutoDraw(False)
        
        # *picD1* updates
        if frameN >= 209 and picD1.status == NOT_STARTED:
            # keep track of start time/frame for later
            picD1.tStart = t  # underestimates by a little under one frame
            picD1.frameNStart = frameN  # exact frame index
            picD1.setAutoDraw(True)
        if picD1.status == STARTED and frameN >= (picD1.frameNStart + 9):
            picD1.setAutoDraw(False)
        
        # *picC2* updates
        if frameN >= 218 and picC2.status == NOT_STARTED:
            # keep track of start time/frame for later
            picC2.tStart = t  # underestimates by a little under one frame
            picC2.frameNStart = frameN  # exact frame index
            picC2.setAutoDraw(True)
        if picC2.status == STARTED and frameN >= (picC2.frameNStart + 9):
            picC2.setAutoDraw(False)
        
        # *picD2* updates
        if frameN >= 227 and picD2.status == NOT_STARTED:
            # keep track of start time/frame for later
            picD2.tStart = t  # underestimates by a little under one frame
            picD2.frameNStart = frameN  # exact frame index
            picD2.setAutoDraw(True)
        if picD2.status == STARTED and frameN >= (picD2.frameNStart + 9):
            picD2.setAutoDraw(False)
        
        # *mask2* updates
        if frameN >= 236 and mask2.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask2.tStart = t  # underestimates by a little under one frame
            mask2.frameNStart = frameN  # exact frame index
            mask2.setAutoDraw(True)
        if mask2.status == STARTED and frameN >= (mask2.frameNStart + 110):
            mask2.setAutoDraw(False)
        
        # *final* updates
        if frameN >= 346 and final.status == NOT_STARTED:
            # keep track of start time/frame for later
            final.tStart = t  # underestimates by a little under one frame
            final.frameNStart = frameN  # exact frame index
            final.setAutoDraw(True)
        
        # *key_resp_14* updates
        if t >= 4.3 and key_resp_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_14.tStart = t  # underestimates by a little under one frame
            key_resp_14.frameNStart = frameN  # exact frame index
            key_resp_14.status = STARTED
            # keyboard checking is just starting
            key_resp_14.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_14.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_14.keys = theseKeys[-1]  # just the last key pressed
                key_resp_14.rt = key_resp_14.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pic_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pic_trial"-------
    for thisComponent in pic_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_14.keys in ['', [], None]:  # No response was made
       key_resp_14.keys=None
    # store data for pictures (TrialHandler)
    pictures.addData('key_resp_14.keys',key_resp_14.keys)
    if key_resp_14.keys != None:  # we had a response
        pictures.addData('key_resp_14.rt', key_resp_14.rt)
    # the Routine "pic_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'pictures'


#------Prepare to start Routine "numbers_instructions"-------
t = 0
numbers_instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_13 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_13.status = NOT_STARTED
# keep track of which components have finished
numbers_instructionsComponents = []
numbers_instructionsComponents.append(text_2)
numbers_instructionsComponents.append(key_resp_13)
for thisComponent in numbers_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "numbers_instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = numbers_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_13* updates
    if t >= 5 and key_resp_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_13.tStart = t  # underestimates by a little under one frame
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        key_resp_13.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_13.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_13.keys = theseKeys[-1]  # just the last key pressed
            key_resp_13.rt = key_resp_13.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in numbers_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "numbers_instructions"-------
for thisComponent in numbers_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
   key_resp_13.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.nextEntry()
# the Routine "numbers_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
numbers = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath="C:\\Users\\viscoglab\\Desktop\\Manuel's Experiment\\Other FPS's\\Version 1 (10fps).psyexp",
    trialList=data.importConditions('v1.xlsx'),
    seed=None, name='numbers')
thisExp.addLoop(numbers)  # add the loop to the experiment
thisNumber = numbers.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisNumber.rgb)
if thisNumber != None:
    for paramName in thisNumber.keys():
        exec(paramName + '= thisNumber.' + paramName)

for thisNumber in numbers:
    currentLoop = numbers
    # abbreviate parameter names if possible (e.g. rgb = thisNumber.rgb)
    if thisNumber != None:
        for paramName in thisNumber.keys():
            exec(paramName + '= thisNumber.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    d1.setText(C1)
    c1.setText(D1)
    d2.setText(C2)
    c2.setText(D2)
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(fixmask1)
    trialComponents.append(d1)
    trialComponents.append(c1)
    trialComponents.append(d2)
    trialComponents.append(c2)
    trialComponents.append(text_9)
    trialComponents.append(text_10)
    trialComponents.append(key_resp_2)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixmask1* updates
        if frameN >= 100 and fixmask1.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixmask1.tStart = t  # underestimates by a little under one frame
            fixmask1.frameNStart = frameN  # exact frame index
            fixmask1.setAutoDraw(True)
        if fixmask1.status == STARTED and frameN >= (fixmask1.frameNStart + 100):
            fixmask1.setAutoDraw(False)
        
        # *d1* updates
        if frameN >= 200 and d1.status == NOT_STARTED:
            # keep track of start time/frame for later
            d1.tStart = t  # underestimates by a little under one frame
            d1.frameNStart = frameN  # exact frame index
            d1.setAutoDraw(True)
        if d1.status == STARTED and frameN >= (d1.frameNStart + 10):
            d1.setAutoDraw(False)
        
        # *c1* updates
        if frameN >= 210 and c1.status == NOT_STARTED:
            # keep track of start time/frame for later
            c1.tStart = t  # underestimates by a little under one frame
            c1.frameNStart = frameN  # exact frame index
            c1.setAutoDraw(True)
        if c1.status == STARTED and frameN >= (c1.frameNStart + 10):
            c1.setAutoDraw(False)
        
        # *d2* updates
        if frameN >= 220 and d2.status == NOT_STARTED:
            # keep track of start time/frame for later
            d2.tStart = t  # underestimates by a little under one frame
            d2.frameNStart = frameN  # exact frame index
            d2.setAutoDraw(True)
        if d2.status == STARTED and frameN >= (d2.frameNStart + 10):
            d2.setAutoDraw(False)
        
        # *c2* updates
        if frameN >= 230 and c2.status == NOT_STARTED:
            # keep track of start time/frame for later
            c2.tStart = t  # underestimates by a little under one frame
            c2.frameNStart = frameN  # exact frame index
            c2.setAutoDraw(True)
        if c2.status == STARTED and frameN >= (c2.frameNStart + 10):
            c2.setAutoDraw(False)
        
        # *text_9* updates
        if frameN >= 240 and text_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_9.tStart = t  # underestimates by a little under one frame
            text_9.frameNStart = frameN  # exact frame index
            text_9.setAutoDraw(True)
        if text_9.status == STARTED and frameN >= (text_9.frameNStart + 110):
            text_9.setAutoDraw(False)
        
        # *text_10* updates
        if frameN >= 350 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t  # underestimates by a little under one frame
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        
        # *key_resp_2* updates
        if frameN >= 350 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
    # store data for numbers (TrialHandler)
    numbers.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        numbers.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'numbers'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
endComponents = []
endComponents.append(text)
endComponents.append(key_resp_3)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 5 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
   key_resp_3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
win.close()
core.quit()
