import sys
from Deliverable import DELIVERABLE, pygameWindow, x, y, xMax, xMin, yMax, yMin
from Deliverable import controller
from Reader import READER
import numpy as np
import pickle


reader = READER()
reader.Print_Gestures()
deliv = DELIVERABLE(controller, pygameWindow,
                    x, y, xMin,
                    xMax, yMin, yMax,
                    DELIVERABLE.previousNumberOfHands,  DELIVERABLE.currentNumberOfHands)


deliv.Run_Forever()
