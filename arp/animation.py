
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

list_colors = [
        colors.Off ,
        colors.Blue,
        colors.Pink ,
        colors.Honeydew,
        colors.Purple,
        colors.Fuchsia,
        colors.LawnGreen,
        colors.AliceBlue,
        colors.Crimson,
        colors.White,
        colors.NavajoWhite,
        colors.Cornsilk,
        colors.Bisque,
        colors.PaleGreen,
        colors.Brown,
        colors.DarkTurquoise,
        colors.DarkGreen,
        colors.MediumOrchid,
        colors.Chocolate,
        colors.PapayaWhip,
        colors.Olive,
        colors.DarkSalmon,
        colors.PeachPuff,
        colors.Plum,
        colors.DarkGoldenrod,
        colors.MintCream,
        colors.CornflowerBlue,
        colors.HotPink,
        colors.DarkBlue,
        colors.LimeGreen,
        colors.DeepSkyBlue,
        colors.DarkKhaki,
        colors.LightGrey,
        colors.Yellow,
        colors.LightSalmon,
        colors.MistyRose,
        colors.SandyBrown,
        colors.DeepPink,
        colors.Magenta,
        colors.Amethyst,
        colors.DarkCyan,
        colors.GreenYellow,
        colors.DarkOrchid,
        colors.OliveDrab,
        colors.Chartreuse,
        colors.Peru,
        colors.Orange,
        colors.Red,
        colors.Wheat,
        colors.LightCyan,
        colors.LightSeaGreen,
        colors.BlueViolet,
        colors.Cyan,
        colors.MediumPurple,
        colors.MidnightBlue,
        colors.Gainsboro,
        colors.PaleTurquoise,
        colors.PaleGoldenrod,
        colors.Gray,
        colors.MediumSeaGreen,
        colors.Moccasin,
        colors.Ivory,
        colors.SlateBlue,
        colors.Green,
        colors.Green_HTML,
        colors.DarkSlateBlue,
        colors.Teal,
        colors.Azure,
        colors.LightSteelBlue,
        colors.Tan,
        colors.AntiqueWhite,
        colors.WhiteSmoke,
        colors.GhostWhite,
        colors.MediumTurquoise,
        colors.FloralWhite,
        colors.LavenderBlush,
        colors.SeaGreen,
        colors.Lavender,
        colors.BlanchedAlmond,
        colors.DarkOliveGreen,
        colors.DarkSeaGreen,
        colors.Violet,
        colors.Navy,
        colors.Beige,
        colors.SaddleBrown,
        colors.IndianRed,
        colors.Snow,
        colors.SteelBlue,
        colors.MediumSlateBlue,
        colors.Black,
        colors.LightBlue,
        colors.Turquoise,
        colors.MediumVioletRed,
        colors.DarkViolet,
        colors.DarkGray,
        colors.Salmon,
        colors.DarkMagenta,
        colors.Tomato,
        colors.SkyBlue,
        colors.Goldenrod,
        colors.MediumSpringGreen,
        colors.DodgerBlue,
        colors.Aqua,
        colors.ForestGreen,
        colors.DarkRed,
        colors.SlateGray,
        colors.Indigo,
        colors.CadetBlue,
        colors.LightYellow,
        colors.DarkOrange,
        colors.PowderBlue,
        colors.RoyalBlue,
        colors.Sienna,
        colors.Thistle,
        colors.Lime,
        colors.Seashell,
        colors.LemonChiffon,
        colors.LightSkyBlue,
        colors.YellowGreen,
        colors.Plaid,
        colors.Aquamarine,
        colors.LightCoral,
        colors.DarkSlateGray,
        colors.Coral,
        colors.Khaki,
        colors.BurlyWood,
        colors.LightGoldenrodYellow,
        colors.MediumBlue,
        colors.LightSlateGray,
        colors.RosyBrown,
        colors.Silver,
        colors.PaleVioletRed,
        colors.FireBrick,
        colors.SpringGreen,
        colors.LightGreen,
        colors.Linen,
        colors.OrangeRed,
        colors.DimGray,
        colors.Maroon,
        colors.LightPink,
        colors.MediumAquamarine,
        colors.Gold,
        colors.Orchid,
        colors.OldLace,]

while True:

    for color in list_colors:

        for i in range(0, 32):
            time.sleep(.075)
            led.set(i, color)
            led.masterBrightness = int(i/32.0 * 255)
            led.update()

        for i in range(0, 32):
            time.sleep(.075)
            led.set(i, color)
            led.masterBrightness = int((32-i)/32.0 * 255)
            led.update()


