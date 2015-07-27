#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Tue Jul 21 17:10:20 2015
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
expName = 'bp_cv_pretest'  # from the Builder filename that created this script
expInfo = {'participant':'', 'list':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionText = visual.TextStim(win=win, ori=0, name='instructionText',
    text='These are the instructions',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
leftPhoneme = visual.TextStim(win=win, ori=0, name='leftPhoneme',
    text='default text',    font='Arial',
    pos=[-0.5, 0], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
rightPhoneme = visual.TextStim(win=win, ori=0, name='rightPhoneme',
    text='default text',    font='Arial',
    pos=[0.5, 0], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
cvSound = sound.Sound('A', secs=-1)
cvSound.setVolume(1)

# Initialize components for Routine "blockBreak"
blockBreakClock = core.Clock()
isBlock = visual.TextStim(win=win, ori=0, name='isBlock',
    text='This is block:',    font='Arial',
    pos=[0, 0.1], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
blockText = visual.TextStim(win=win, ori=0, name='blockText',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
pressCont = visual.TextStim(win=win, ori=0, name='pressCont',
    text='Press any button to continue',    font='Arial',
    pos=[0, -0.1], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
leftPhoneme = visual.TextStim(win=win, ori=0, name='leftPhoneme',
    text='default text',    font='Arial',
    pos=[-0.5, 0], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
rightPhoneme = visual.TextStim(win=win, ori=0, name='rightPhoneme',
    text='default text',    font='Arial',
    pos=[0.5, 0], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
cvSound = sound.Sound('A', secs=-1)
cvSound.setVolume(1)

# Initialize components for Routine "expEnd"
expEndClock = core.Clock()
endText = visual.TextStim(win=win, ori=0, name='endText',
    text='The experiment is now over.\n\nThank you for your participation.\n\nThe experimentor will be with you soon.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instructionResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instructionResp.status = NOT_STARTED
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(instructionText)
instructionsComponents.append(instructionResp)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionText* updates
    if t >= 0.0 and instructionText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructionText.tStart = t  # underestimates by a little under one frame
        instructionText.frameNStart = frameN  # exact frame index
        instructionText.setAutoDraw(True)
    
    # *instructionResp* updates
    if t >= 0.0 and instructionResp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructionResp.tStart = t  # underestimates by a little under one frame
        instructionResp.frameNStart = frameN  # exact frame index
        instructionResp.status = STARTED
        # keyboard checking is just starting
        instructionResp.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if instructionResp.status == STARTED:
        theseKeys = event.getKeys(keyList=['enter', '1', '2'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instructionResp.keys = theseKeys[-1]  # just the last key pressed
            instructionResp.rt = instructionResp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instructionResp.keys in ['', [], None]:  # No response was made
   instructionResp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('instructionResp.keys',instructionResp.keys)
if instructionResp.keys != None:  # we had a response
    thisExp.addData('instructionResp.rt', instructionResp.rt)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('stimConditions.xlsx'),
    seed=None, name='block1')
thisExp.addLoop(block1)  # add the loop to the experiment
thisBlock1 = block1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock1.rgb)
if thisBlock1 != None:
    for paramName in thisBlock1.keys():
        exec(paramName + '= thisBlock1.' + paramName)

for thisBlock1 in block1:
    currentLoop = block1
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
    if thisBlock1 != None:
        for paramName in thisBlock1.keys():
            exec(paramName + '= thisBlock1.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    leftPhoneme.setText(optionLeft)
    rightPhoneme.setText(optionRight)
    cvSound.setSound(wavFile)
    trialResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    trialResp.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(leftPhoneme)
    trialComponents.append(ISI)
    trialComponents.append(rightPhoneme)
    trialComponents.append(cvSound)
    trialComponents.append(trialResp)
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
        
        # *leftPhoneme* updates
        if t >= 0.5 and leftPhoneme.status == NOT_STARTED:
            # keep track of start time/frame for later
            leftPhoneme.tStart = t  # underestimates by a little under one frame
            leftPhoneme.frameNStart = frameN  # exact frame index
            leftPhoneme.setAutoDraw(True)
        
        # *rightPhoneme* updates
        if t >= 0.5 and rightPhoneme.status == NOT_STARTED:
            # keep track of start time/frame for later
            rightPhoneme.tStart = t  # underestimates by a little under one frame
            rightPhoneme.frameNStart = frameN  # exact frame index
            rightPhoneme.setAutoDraw(True)
        # start/stop cvSound
        if t >= 1 and cvSound.status == NOT_STARTED:
            # keep track of start time/frame for later
            cvSound.tStart = t  # underestimates by a little under one frame
            cvSound.frameNStart = frameN  # exact frame index
            cvSound.play()  # start the sound (it finishes automatically)
        
        # *trialResp* updates
        if t >= 1 and trialResp.status == NOT_STARTED:
            # keep track of start time/frame for later
            trialResp.tStart = t  # underestimates by a little under one frame
            trialResp.frameNStart = frameN  # exact frame index
            trialResp.status = STARTED
            # keyboard checking is just starting
            trialResp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if trialResp.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                trialResp.keys = theseKeys[-1]  # just the last key pressed
                trialResp.rt = trialResp.clock.getTime()
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
    cvSound.stop() #ensure sound has stopped at end of routine
    # check responses
    if trialResp.keys in ['', [], None]:  # No response was made
       trialResp.keys=None
    # store data for block1 (TrialHandler)
    block1.addData('trialResp.keys',trialResp.keys)
    if trialResp.keys != None:  # we had a response
        block1.addData('trialResp.rt', trialResp.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'block1'


#------Prepare to start Routine "blockBreak"-------
t = 0
blockBreakClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
blockResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
blockResp.status = NOT_STARTED
# keep track of which components have finished
blockBreakComponents = []
blockBreakComponents.append(isBlock)
blockBreakComponents.append(blockText)
blockBreakComponents.append(pressCont)
blockBreakComponents.append(blockResp)
for thisComponent in blockBreakComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "blockBreak"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = blockBreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *isBlock* updates
    if t >= 0.0 and isBlock.status == NOT_STARTED:
        # keep track of start time/frame for later
        isBlock.tStart = t  # underestimates by a little under one frame
        isBlock.frameNStart = frameN  # exact frame index
        isBlock.setAutoDraw(True)
    
    # *blockText* updates
    if t >= 0.0 and blockText.status == NOT_STARTED:
        # keep track of start time/frame for later
        blockText.tStart = t  # underestimates by a little under one frame
        blockText.frameNStart = frameN  # exact frame index
        blockText.setAutoDraw(True)
    if blockText.status == STARTED:  # only update if being drawn
        blockText.setText(blockNo, log=False)
    
    # *pressCont* updates
    if t >= 0.0 and pressCont.status == NOT_STARTED:
        # keep track of start time/frame for later
        pressCont.tStart = t  # underestimates by a little under one frame
        pressCont.frameNStart = frameN  # exact frame index
        pressCont.setAutoDraw(True)
    
    # *blockResp* updates
    if t >= 0.0 and blockResp.status == NOT_STARTED:
        # keep track of start time/frame for later
        blockResp.tStart = t  # underestimates by a little under one frame
        blockResp.frameNStart = frameN  # exact frame index
        blockResp.status = STARTED
        # keyboard checking is just starting
        blockResp.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if blockResp.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space', '1', '2'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            blockResp.keys = theseKeys[-1]  # just the last key pressed
            blockResp.rt = blockResp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blockBreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "blockBreak"-------
for thisComponent in blockBreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if blockResp.keys in ['', [], None]:  # No response was made
   blockResp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('blockResp.keys',blockResp.keys)
if blockResp.keys != None:  # we had a response
    thisExp.addData('blockResp.rt', blockResp.rt)
thisExp.nextEntry()
# the Routine "blockBreak" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('stimConditions.xlsx', selection='5'),
    seed=None, name='block2')
thisExp.addLoop(block2)  # add the loop to the experiment
thisBlock2 = block2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock2.rgb)
if thisBlock2 != None:
    for paramName in thisBlock2.keys():
        exec(paramName + '= thisBlock2.' + paramName)

for thisBlock2 in block2:
    currentLoop = block2
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2.rgb)
    if thisBlock2 != None:
        for paramName in thisBlock2.keys():
            exec(paramName + '= thisBlock2.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    leftPhoneme.setText(optionLeft)
    rightPhoneme.setText(optionRight)
    cvSound.setSound(wavFile)
    trialResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    trialResp.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(leftPhoneme)
    trialComponents.append(ISI)
    trialComponents.append(rightPhoneme)
    trialComponents.append(cvSound)
    trialComponents.append(trialResp)
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
        
        # *leftPhoneme* updates
        if t >= 0.5 and leftPhoneme.status == NOT_STARTED:
            # keep track of start time/frame for later
            leftPhoneme.tStart = t  # underestimates by a little under one frame
            leftPhoneme.frameNStart = frameN  # exact frame index
            leftPhoneme.setAutoDraw(True)
        
        # *rightPhoneme* updates
        if t >= 0.5 and rightPhoneme.status == NOT_STARTED:
            # keep track of start time/frame for later
            rightPhoneme.tStart = t  # underestimates by a little under one frame
            rightPhoneme.frameNStart = frameN  # exact frame index
            rightPhoneme.setAutoDraw(True)
        # start/stop cvSound
        if t >= 1 and cvSound.status == NOT_STARTED:
            # keep track of start time/frame for later
            cvSound.tStart = t  # underestimates by a little under one frame
            cvSound.frameNStart = frameN  # exact frame index
            cvSound.play()  # start the sound (it finishes automatically)
        
        # *trialResp* updates
        if t >= 1 and trialResp.status == NOT_STARTED:
            # keep track of start time/frame for later
            trialResp.tStart = t  # underestimates by a little under one frame
            trialResp.frameNStart = frameN  # exact frame index
            trialResp.status = STARTED
            # keyboard checking is just starting
            trialResp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if trialResp.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                trialResp.keys = theseKeys[-1]  # just the last key pressed
                trialResp.rt = trialResp.clock.getTime()
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
    cvSound.stop() #ensure sound has stopped at end of routine
    # check responses
    if trialResp.keys in ['', [], None]:  # No response was made
       trialResp.keys=None
    # store data for block2 (TrialHandler)
    block2.addData('trialResp.keys',trialResp.keys)
    if trialResp.keys != None:  # we had a response
        block2.addData('trialResp.rt', trialResp.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'block2'


#------Prepare to start Routine "expEnd"-------
t = 0
expEndClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
endResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
endResp.status = NOT_STARTED
# keep track of which components have finished
expEndComponents = []
expEndComponents.append(endText)
expEndComponents.append(endResp)
for thisComponent in expEndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "expEnd"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = expEndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if t >= 0.0 and endText.status == NOT_STARTED:
        # keep track of start time/frame for later
        endText.tStart = t  # underestimates by a little under one frame
        endText.frameNStart = frameN  # exact frame index
        endText.setAutoDraw(True)
    
    # *endResp* updates
    if t >= 0.0 and endResp.status == NOT_STARTED:
        # keep track of start time/frame for later
        endResp.tStart = t  # underestimates by a little under one frame
        endResp.frameNStart = frameN  # exact frame index
        endResp.status = STARTED
        # keyboard checking is just starting
        endResp.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if endResp.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            endResp.keys = theseKeys[-1]  # just the last key pressed
            endResp.rt = endResp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in expEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "expEnd"-------
for thisComponent in expEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if endResp.keys in ['', [], None]:  # No response was made
   endResp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('endResp.keys',endResp.keys)
if endResp.keys != None:  # we had a response
    thisExp.addData('endResp.rt', endResp.rt)
thisExp.nextEntry()
# the Routine "expEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
win.close()
core.quit()
