
import sys

sys.path.append('/home/pi/GitRepos/BiblioPixel')

import bibliopixel
#causes frame timing information to be output
bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)

from bibliopixel.led import *
from bibliopixel.animation import StripChannelTest
from bibliopixel.drivers.LPD8806 import *

#create driver for a 12 pixels
driver = DriverLPD8806(num = 12, c_order = ChannelOrder.GRB)
led = LEDStrip(driver)

anim = StripChannelTest(led)
anim.run()

