import os
from sense_hat import SenseHat
from time import sleep

class Cam:
    def __init__(self):
        self._running  = True
    
    def terminate(self):
        self._running = False
    
    def run(self, s):
        while self._running:
            os.system("./cam-trigger.sh " +str(s))
