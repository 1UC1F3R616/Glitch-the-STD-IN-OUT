#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
os.system("pip install pynput")
os.system("py -m pip install pynput")
os.system("sudo pip install pynput")

from time import sleep
import random as rm
from pynput.mouse import Button, Controller, Listener

mouse = Controller()

while True:
    mouse.position = (rm.randint(1, 50), 2)
    sleep(2)
    mouse.move(5, -5)
    mouse.press(Button.right)
    mouse.release(Button.right)
    sleep(3)
    mouse.click(Button.left, 2)
    sleep(2)
    mouse.scroll(0, rm.randint(1, 100))
