#File created by Nolan Keith on September 29, 2023


#import libraries and modeules
import pygame as pg
from pygame.sprite import Sprite
import random
import os 

vec = pg.math.Vector2

#setup asset folders here 
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

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

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        # self.image = pg.Surface((50,50))
        # self.image.fill(GREEN)
        self.image = pg.image.load(os.path(img_folder, 'theBell.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -5
        if keys[pg.K_RIGHT]:
            self.acc.x = 5

    def update(self):
        # self.rect.x += 5
        # self.rect.y += 5
        self.acc = vec(0,0)
        self.controls()
        # if friction - apply here
        self.acc.x += self.vel.x
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.y > HEIGHT:
            self.rect.y = 0
        self.rect.midbottom = self.pos

#init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game....")
clock = pg.time.Clock()

#create a group for all sprites
all_sprites = pg.sprite.Group()

#instantiate the player class
player = Player()

#add player to Sprites group
all_sprites.add(player)

#Game loop
running = True
while running:
    #keep the loop running
    clock.tick(FPS)

    for event in pg.event.get():
        #check for closed window
        if event.type == pg.QUIT:
            running = False

    ########## Update ###########
    # Update all sprites
    all_sprites.update()

    ########## Draw ###########
    #draw the background screen
    screen.fill(GREEN)

    #draw all sprites
    all_sprites.draw(screen)

    #buffer - after drawing everything, flip display
    pg.display.flip()

pg.quit()
