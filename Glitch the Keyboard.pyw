#!/usr/bin/python
# -*- coding:utf-8 -*-


import os
try:os.system("pip install pynput")
except:print('[*] Py not in Environment variable or OS not Windows.')
try:os.system("py -m pip install pynput")
except:print('[*] OS not Windows or Py in Environment Variable.')
try:os.system("sudo pip install pynput")
except:print('[*] OS not Linux or kill sudo')

from pynput.keyboard import Key, Controller, Listener

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        keyboard.press('K')
        keyboard.release('K')
    elif key == Key.alt:
        keyboard.press('U')
        keyboard.press('U')
    elif key == Key.alt_l:
        keyboard.press('S')
        keyboard.press('S')
    elif key == Key.alt_r:
        keyboard.press('H')
        keyboard.press('H')
    elif key == Key.backspace:
        keyboard.press('A')
        keyboard.press('A')
    elif key == Key.caps_lock:
        keyboard.press('L')
        keyboard.press('L')
    elif key == Key.cmd:
        keyboard.press('k')
        keyboard.press('k')
    elif key == Key.cmd_r:
        keyboard.press('u')
        keyboard.press('u')
    elif key == Key.ctrl:
        keyboard.press('s')
        keyboard.press('s')
    elif key == Key.ctrl_l:
        keyboard.press('h')
        keyboard.press('h')
    elif key == Key.ctrl_r:
        keyboard.press('a')
        keyboard.press('a')
    elif key == Key.delete:
        keyboard.press('l')
        keyboard.press('l')
    elif key == Key.down:
        keyboard.press('H')
        keyboard.press('H')
    elif key == Key.end:
        keyboard.press('A')
        keyboard.press('A')
    elif key == Key.enter:
        keyboard.press('C')
        keyboard.press('C')
    elif key == Key.f1:
        keyboard.press('K')
        keyboard.press('K')
    elif key == Key.f10:
        keyboard.press('E')
        keyboard.press('E')
    elif key == Key.f11:
        keyboard.press('R')
        keyboard.press('R')
    elif key == Key.f12:
        keyboard.press('h')
        keyboard.press('h')
    elif key == Key.f13:
        keyboard.press('a')
        keyboard.press('a')
    elif key == Key.f14:
        keyboard.press('c')
        keyboard.press('c')
    elif key == Key.f15:
        keyboard.press('k')
        keyboard.press('k')
    elif key == Key.f16:
        keyboard.press('e')
        keyboard.press('e')
    elif key == Key.f17:
        keyboard.press('r')
        keyboard.press('r')
    elif key == Key.f18:
        keyboard.press(']')
        keyboard.press(']')
    elif key == Key.f19:
        keyboard.press('{')
        keyboard.press('{')
    elif key == Key.f20:
        keyboard.press('U')
        keyboard.press('U')
    elif key == Key.f2:
        keyboard.press('H')
        keyboard.press('H')
    elif key == Key.f3:
        keyboard.press('A')
        keyboard.press('A')
    elif key == Key.f4:
        keyboard.press('C')
        keyboard.press('C')
    elif key == Key.f5:
        keyboard.press('K')
        keyboard.press('K')
    elif key == Key.f6:
        keyboard.press('E')
        keyboard.press('E')
    elif key == Key.f7:
        keyboard.press('D')
        keyboard.press('D')
    elif key == Key.home:
        keyboard.press('c')
        keyboard.press('c')
    elif key == Key.insert:
        keyboard.press('d')
        keyboard.press('d')
    elif key == Key.left:
        keyboard.press('d')
        keyboard.press('d')
    elif key == Key.pause:
        keyboard.press('f')
        keyboard.press('f')
    elif key == Key.shift:
        keyboard.press(Key.enter)
        keyboard.press(Key.enter)
    elif key == Key.shift_r:
        keyboard.press('y')
        keyboard.press('y')
    elif key == Key.space:
        keyboard.press('x')
        keyboard.press('x')
    elif key == Key.tab:
        keyboard.press('t')
        keyboard.press('t')







keyboard = Controller()


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
