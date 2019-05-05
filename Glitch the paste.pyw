#!/usr/bin/env
# -*- coding:utf-8 -*-

import os
os.system("py -m pip install pyperclip")
os.system("pip install pyperclip")
os.system("sudo pip install pyperclip")


import pyperclip

while True:
    if pyperclip.copy('OK') != 'NONE':
        pyperclip.copy('ops')
