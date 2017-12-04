#!/usr/bin/env python
# Program for the Pi Hut Xmas Tree
# that goes up and down the leds

from gpiozero import LEDBoard
from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import Button
from subprocess import check_call
from gpiozero.tools import random_values
import time
from signal import pause

delay = 0.125
delay2 = 0.05

branch1_leds = LEDBoard(27,17,4,18,15,14)
branch2_leds = LEDBoard(11,5,8,12,6,7)
branch3_leds = LEDBoard(19,16,26,13,20,21)
branch4_leds = LEDBoard(25,9,22,24,23,10)
star = PWMLED(2)
star.source = random_values()

def shutdown():
    star.value = 0 # Indicate start of shutdown
    check_call(['sudo', 'poweroff'])

shutdown_btn = Button(3, hold_time=2)
shutdown_btn.when_held = shutdown

branch1_leds.off()
branch2_leds.off()
branch3_leds.off()
branch4_leds.off()
time.sleep(delay)

while True:
    for point in range(6):
        branch1_leds[point].on()
        time.sleep(delay2)
        branch2_leds[point].on()
        time.sleep(delay2)
        branch3_leds[point].on()
        time.sleep(delay2)
        branch4_leds[point].on()
        time.sleep(delay2)
  
    time.sleep(delay)

    for point in range(5, -1, -1):
        branch1_leds[point].off()
        time.sleep(delay2)
        branch2_leds[point].off()
        time.sleep(delay2)
        branch3_leds[point].off()
        time.sleep(delay2)
        branch4_leds[point].off()
        time.sleep(delay2)
        
    time.sleep(delay)
        
Pause()



