import sys
from Deliverable import DELIVERABLE, pygameWindow, x, y, xMax, xMin, yMax, yMin
from Deliverable import controller



deliv = DELIVERABLE(controller, pygameWindow,
                    x, y, xMin,
                    xMax, yMin, yMax)
deliv.Run_Forever()

