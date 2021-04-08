import os
from sense_hat import SenseHat
from time import sleep

red   = [255,   0,  0]
green = [  0, 255,  0]
blue  = [  0,   0,255]

class Timer:
    def __init__(self):
        self._running  = True
    
    def terminate(self):
        self._running = False
    
    def run(self, s, sense):
        while self._running:
            timer(s, sense)

def timer(s, sense):
    display = [blue for i in range(64)]
    sense.set_pixels(display)
    
    for i in range(0, 64):
        sleep(s/64)
        display[i] = green
        sense.set_pixels(display)
    
    sense.clear(red)
    sleep(0.1)
    sense.clear()

