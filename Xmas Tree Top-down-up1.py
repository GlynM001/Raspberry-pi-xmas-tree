#!/usr/bin/env python
# Example test program for the Pi Hut Xmas Tree

from gpiozero import LEDBoard
from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import Button
from subprocess import check_call
import time
from signal import pause

delay = 0.125

branch1_leds = LEDBoard(27,17,4,18,15,14)
branch2_leds = LEDBoard(11,5,8,12,6,7)
branch3_leds = LEDBoard(19,16,26,13,20,21)
branch4_leds = LEDBoard(25,9,22,24,23,10)
star = PWMLED(2)
star.pulse()

def shutdown():
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
        branch2_leds[point].on()
        branch3_leds[point].on()
        branch4_leds[point].on()
        time.sleep(delay)
  
    time.sleep(delay)

    for point in range(5, -1, -1):
        branch1_leds[point].off()
        branch2_leds[point].off()
        branch3_leds[point].off()
        branch4_leds[point].off()
        time.sleep(delay)
        
    time.sleep(delay)
        
Pause()



