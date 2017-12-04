#!/usr/bin/env python
# Program for the Pi Hut Xmas Tree
# that turns on & off random leds

from gpiozero import LEDBoard
from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import Button
from subprocess import check_call
from gpiozero.tools import random_values
from random import *
import time
from signal import pause

on_delay = 0.01

star = PWMLED(2)
star.source = random_values()

def shutdown():
    star.value = 0 # Indicate start of shutdown
    check_call(['sudo', 'poweroff'])

shutdown_btn = Button(3, hold_time=2)
shutdown_btn.when_held = shutdown

tree = LEDBoard(*range(4,28))


while True:
    # Turn on a random led
    on_lamp = randint(0, 23)
    tree[on_lamp].on()
    time.sleep(on_delay)

    # Turn off a random led
    off_lamp = randint(0, 23)
    tree[off_lamp].off()

            
Pause()



