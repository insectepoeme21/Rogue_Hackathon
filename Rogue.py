# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre

import pygame as pg
from random import randint
from itertools import product


KNIGHT_LIST=[]
KNIGHT_POS={}
walls = []
class Knight:
    def __init__(self, pos, HP=50, DMG=10, Ore = 10):
        self.HP = HP
        self.pos = pos
        self.DMG = DMG
        self.wealth = Ore

def move(player, direction):
    if player.position + direction not in walls and not in doors:
        player.position += direction
    if player.position + direction in KNIGHT_POS.keys():
        fight(player, KNIGHT_POS[player.position + direction])
 



def fight(player, knight):
    knight.HP -= player.weapon[1]
    if knight.HP > 0:
        player.health -= knight.DMG
    if player.health < 0:
        pg.quit()



pg.init()
COTE = 20 # largeur du rectangle en pixels
NB_CASES = 30
screen = pg.display.set_mode((COTE*NB_CASES, COTE*NB_CASES))
clock = pg.time.Clock()
pace = 2


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)



def draw_rect(screen, x, y, size, color):
    rect = pg.Rect(x*size, y*size, size, size)
    pg.draw.rect(screen, color, rect)

def room(pt, length, width):
    pass

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


        


    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False


    


    screen.fill(BLACK)
    draw_rect(screen, 0, 1, COTE, WHITE)

    pg.display.update()
    

pg.quit()
