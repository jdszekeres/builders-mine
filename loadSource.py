import os,math

from block import Block
from pyglet.gl import *

# the icon of the window
ICON = pyglet.image.load(os.path.join("texture","icon.png"))

# blocks of the game
BRICK = Block("BRICK",(0, 0), (0, 0), (0, 0), 1, os.path.join("texture","Brick.png"),destroyable = True)
GRASS = Block("GRASS",(0, 0), (0, 1), (1, 1), 2, os.path.join("texture","Grass.png"),destroyable = True)
DIRT = Block("DIRT",(0, 0), (0, 1), (1, 1), 2, os.path.join("texture","dirt.png"),destroyable = True)
STONE = Block("STONE",(0, 0), (0, 0), (0, 0), 1, os.path.join("texture","Stone.png"),destroyable = True)
MARBLE = Block("MARBLE",(0, 0), (0, 0), (0, 0), 1, os.path.join("texture","Marble.png"),destroyable = True)
WOOL = Block("WOOL",(0, 0), (0, 0), (0, 0), 1, os.path.join("texture","wool.png"), destroyable = True)
WOOD = Block("WOOD",(0, 0), (0, 0), (0, 0), 1, os.path.join("texture","WOOD.jpg"),destroyable = True)
LEAVES = Block("LEAVES",(0, 0), (0, 0), (0, 0), 1, os.path.join("texture","leaves.png"), destroyable = True)
#list of all types of blocks in the game
ALLBLOCKS = [BRICK,GRASS,STONE,MARBLE,WOOL,WOOD,LEAVES,DIRT]
# list of all types of destroyable blocks of the game
PLACEBLOCKS = [BRICK,GRASS,STONE,WOOL,WOOD,LEAVES,DIRT]
