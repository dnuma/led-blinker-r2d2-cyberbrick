# blink.py - alternate red and white on a CyberBrick LED channel.
#
# Paste the contents into a Code (BETA) snippet on your receiver in the
# CyberBrick DESKTOP app, then bind it to a switch position with
# Module = CODE. This file is a reference copy; the app cannot import .py.
#
# period=250 is the blink interval in ms. Lower is faster.

from leds import LEDController
from machine import Timer

led = LEDController("LED1")
led.repeat_count = 0          # stop any GUI effect from overwriting us

# Timer(0) is a hardware timer, so this cancels a blink started by any
# other snippet even though snippets don't share globals.
try:
    blink_timer
except:
    blink_timer = Timer(0)
blink_timer.deinit()


def alternate(t):
    if led.np[0] == (255, 0, 0):
        c = (255, 255, 255)
    else:
        c = (255, 0, 0)
    for i in range(4):        # OUT1..OUT4
        led.np[i] = c
    led.np.write()


blink_timer.init(period=250, mode=Timer.PERIODIC, callback=alternate)
