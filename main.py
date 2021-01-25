#! usr/bin/env python3.8
from pyglet.gl import *

from game import Game
from loadSource import *
import os
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def main():

    game = Game(width=WINDOW_WIDTH, height=WINDOW_HEIGHT,caption='builder\'s mine', resizable=True, refreshRate = 100)
    
    game.set_icon(ICON)
    
    pyglet.app.run()

if __name__ == '__main__':
    main()
