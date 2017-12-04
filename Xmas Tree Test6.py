#!/usr/bin/env python
# Example test program for the Pi Hut Xmas Tree

from gpiozero import LEDBoard
from gpiozero import PWMLED
import time
from gpiozero.tools import random_values
from signal import pause

led_number = int(input("Type led number: "))

led = PWMLED(led_number)


while True:
    led.value = 0 # Off
    time.sleep(1)
    led.value = 0.5 # Half Brightnes
    time.sleep(1)
    led.value = 1 # Full brightness
    time.sleep(1)
    
    



