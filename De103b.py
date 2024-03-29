import sys
from Deliverable import DELIVERABLE, pygameWindow, x, y, xMax, xMin, yMax, yMin
from Deliverable import controller
from Reader import READER, pygameWindow

import numpy as np
import pickle


reader = READER(pygameWindow)
reader.Draw_Gestures()
deliv = DELIVERABLE(controller, pygameWindow,
                    x, y, xMin,
                    xMax, yMin, yMax,
                    DELIVERABLE.previousNumberOfHands,  DELIVERABLE.currentNumberOfHands)

pickle_in = open("userData/gesture1.p", "rb")
gestureData = pickle.load(pickle_in)
print gestureData
# deliv.Run_Forever()
