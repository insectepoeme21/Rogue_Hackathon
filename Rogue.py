# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre

import pygame as pg
from random import randint
from itertools import product


KNIGHT_LIST=
KNIGHT_POS={}

class Knight:
    def __init__(self, pos, HP=50, DMG=10, Ore = 10):
        self.HP = HP
        self.pos = pos
        self.DMG = DMG
        self.wealth = Ore

def move(player, direction):
    if player.pos + direction not in wall:
        player.pos += direction
    if player.pos + direction in KNIGHT_POS.keys():
        fight(player, KNIGHT_POS[player.pos + direction])




pg.init()
COTE = 20 # largeur du rectangle en pixels
NB_CASES = 30
screen = pg.display.set_mode((COTE*NB_CASES, COTE*NB_CASES))
clock = pg.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)



running = True
while running:
    clock.tick(pace)
    
    for event in pg.event.get():
        if event.type == pg.K_z:
            move(player, (0, 20))
        if event.type == pg.K_s:
            move(player, (0, -20))
        if event.type == pg.K_q:
            move(player, (-20, 0))
        if event.type == pg.K_d:
            move(player, (20, 0))


        



    pg.display.update()
    

pg.quit()
