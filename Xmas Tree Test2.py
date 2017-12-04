#!/usr/bin/env python
# Test to deternin actual tree led numbers

from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause

led2 = LEDBoard(2)
for led in tree:
    led.source_delay = 0.2
    led.source = random_values()
pause()
