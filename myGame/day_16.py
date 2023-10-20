# This file is created by Nolan Keith

#import libraries and modeules
import pygame as pg
import random

#game settings
WIDTH = 360
HEIGHT = 480
FPS = 30


#define colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game....")
clock = pg.time.Clock()


#Game loop
running = True
while running:
    #keep the loop running
    clock.tick(FPS)

    for event in pg.event.get():
        #check for closed window
        if event.type == pg.QUIT:
            running = False

    # Update

    # Draw
    screen.fill(BLACK)

    #buffer - after drawing everything, flip display
    pg.display.flip()

pg.quit()
