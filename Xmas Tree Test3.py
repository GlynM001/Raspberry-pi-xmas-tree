#!/usr/bin/env python
# Example test program for the Pi Hut Xmas Tree

from gpiozero import LEDBoard
from time import sleep
from gpiozero.tools import random_values
from signal import pause

leds = LEDBoard(11,10,1,20,2,19)

for led in leds:
    led.on()
    sleep(1)
    led.off()

