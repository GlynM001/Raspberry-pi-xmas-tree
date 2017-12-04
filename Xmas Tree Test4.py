#!/usr/bin/env python
# Example test program for the Pi Hut Xmas Tree

from gpiozero import LEDBoard
import time
from gpiozero.tools import random_values
from signal import pause

leds = LEDBoard(11,10,1,20,2,19)

while True:
    leds.off()
    time.sleep(1)
    leds.value = (1,0,0,0,0)
    time.sleep(1)
    
    leds.value = (0,1,0,0,0)
    time.sleep(1)
    
    leds.value = (0,0,1,0,0)
    time.sleep(1)
    
    leds.value = (0,0,0,1,0)
    time.sleep(1)
    
    leds.value = (0,0,0,0,1)
    time.sleep(1)



