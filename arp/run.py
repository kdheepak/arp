
import sys
import time

sys.path.append('/home/pi/GitRepos/BiblioPixel')
sys.path.append('/home/pi/GitRepos/BiblioPixelAnimations')

import bibliopixel
#causes frame timing information to be output
bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)

from bibliopixel.led import *
from bibliopixel.animation import StripChannelTest
from bibliopixel.drivers.LPD8806 import *

#create driver for a 32 pixels
driver = DriverLPD8806(num = 32, c_order = ChannelOrder.GRB, use_py_spi=True)
led = LEDStrip(driver)

import bibliopixel.colors as colors
rainbow = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Purple]

for color in rainbow:
    time.sleep(.5)
    led.fill(color)
    led.update()

led.all_off()
led.update()

