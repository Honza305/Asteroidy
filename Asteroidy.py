#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:26:13 2018

@author: mah35070
"""

import pyglet
from pyglet.window.key import MOD_CTRL, A


obrazek = pyglet.image.load('zaba.png')
obrazek.anchor_x = obrazek.width // 2
obrazek.anchor_y = obrazek.height // 2

sprite = pyglet.sprite.Sprite(obrazek)



window = pyglet.window.Window()

def tiktak(t):
    print(t)
    sprite.x = sprite.x + 20*t
    sprite.y = sprite.y + 20*t
    


@window.event
def on_draw():
    window.clear()
    sprite.draw()
    
    
    
@window.event
def on_mouse_press(x, y, button, mod):
    if button == 1:
        sprite.x = x
        sprite.y = y
    elif button == 4:
        sprite.rotation += 20

@window.event
def on_key_press(sym, mod):
    if sym != A:
        print (sym, mod)
    
pyglet.clock.schedule_interval(tiktak, 1/10)

pyglet.app.run()
print('Hotovo')