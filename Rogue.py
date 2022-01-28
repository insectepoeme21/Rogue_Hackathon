# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre

import pygame as pg
from random import randint
from itertools import product


"""KNIGHT_LIST=
KNIGHT_POS={}

class Knight:
    def __init__(self, pos, HP=50, DMG=10, Ore = 10):
        self.HP = HP
        self.pos = pos
        self.DMG = DMG
        self.wealth = Ore

def move(player, direction):
    if player.pos + direction not in walls:
        player.pos += direction
    if player.pos + direction in KNIGHT_POS.keys():
        fight(player, KNIGHT_POS[player.pos + direction])
"""



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
GRAY = (150, 150, 150)

walls = []
doors = []
paths = []

def draw_rect(screen, x, y, size, color):
    rect = pg.Rect(x*size, y*size, size, size)
    pg.draw.rect(screen, color, rect)




def room(pt, lenX, lenY, door):
    for i in range(lenX):
        walls.append((pt[0]+i, pt[1]))
        walls.append((pt[0]+i, pt[1]+lenY-1))
    for i in range(1, lenY-1):
        walls.append((pt[0], pt[1]+i))
        walls.append((pt[0]+lenX-1, pt[1]+i))
    
    for i in door:
        doors.append(i)
        walls.remove(i)
    
map = [[(2, 2), 9, 7, [(4, 8), (10, 6)]],
       [(20, 6), 9, 5, [(25, 10),(20,8)]],
       [(8, 13), 8, 5, [(10, 17), (8, 15)]],
       [(3, 24), 10, 5, [(10, 24)]],
       [(20, 15), 8, 10, [(25, 15), (20, 20)]]]

paths = [(4,9+i) for i in range(7)]
for i in range(1,4):
    paths += [(4+i, 15)]
for i in range(6):
    paths += [(10, 18+i)]
for i in range(10):
    paths += [(10+i, 20)]
for i in range(4):
    paths += [(25, 11+i)]
for i in range(5):
    paths += [(11+i, 5)]
for i in range(3):
    paths += [(15, 6+i)]
for i in range(4):
    paths += [(16+i, 8)]



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

    for i in map:
        room(*i)
    

        


    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False


    


    screen.fill(BLACK)
    for x, y in walls:
        draw_rect(screen, x, y, COTE, WHITE)
    for x in doors:
        draw_rect(screen, *x , COTE, RED)
    for x in paths:
        draw_rect(screen, *x, COTE, GRAY)

    pg.display.update()
    

pg.quit()
