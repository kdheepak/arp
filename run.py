
import sys

import bibliopixel
#causes frame timing information to be output
bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)

from bibliopixel.drivers.LPD8806 import *
#set number of pixels & LED type here
driver = DriverLPD8806(num = 32)

#load the LEDStrip class
from bibliopixel.led import *
led = LEDStrip(driver)


