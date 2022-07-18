import pygame as pg
import os
#Game options/Settings
VERSION = "0.12.5 Alpha"
TITLE = "Flappy Fish"
WIDTH = 495
HEIGHT = 880
FPS = 30

#Player properties
PLAYER_ACC = 0.8
PLAYER_FRICTION = 0
GRAVITY = 0.4

#Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#etc.
FONT_NAME = "comicsans"
bg = pg.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)) + '\\Flappy-Img', 'bg r1.png'))