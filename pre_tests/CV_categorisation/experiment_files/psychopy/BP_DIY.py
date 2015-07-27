from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# initialize stimuli
win = visual.Window(fullscr=True, allowGUI=False)
text = visual.TextStim(win)
sounds = load_sounds(SOUNDS)
images = load_images(IM_NAMES, IM_PROPERTIES, win)

