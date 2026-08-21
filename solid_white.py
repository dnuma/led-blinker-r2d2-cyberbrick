# solid_white.py - solid white, and cancels any running blink.
#
# Paste the contents into a Code (BETA) snippet on your receiver in the
# CyberBrick DESKTOP app, then bind it to a switch position with
# Module = CODE. This file is a reference copy; the app cannot import .py.
#
# Every position sharing this LED channel must be a CODE row that calls
# deinit() first - otherwise the blink timer keeps overwriting the colour.

from leds import LEDController
from machine import Timer

try:
    blink_timer
except:
    blink_timer = Timer(0)
blink_timer.deinit()

led = LEDController("LED1")
led.repeat_count = 0
for i in range(4):            # OUT1..OUT4
    led.np[i] = (255, 255, 255)
led.np.write()
