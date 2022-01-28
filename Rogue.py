# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre

import pygame as pg
from random import randint
from itertools import product


KNIGHT_LIST = {}
KNIGHT_POS = {}
BAG_LIST = {}
POTION_LIST = {}

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
    if player.pos + direction in BAG_LIST:
        player.pos += direction
        player.enrichement()
    if player.pos + direction in POTION_LIST:
        player.pos += direction 




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

wall = []

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
       [(20, 6), 9, 5, [(25, 10)]],
       [(8, 13), 8, 5, [(10, 17), (8, 15)]],
       [(3, 24), 10, 5, [(10, 24)]],
       [(20, 15), 8, 10, [(25, 15), (20, 20)]]]    




class Player:
    def __init__(self, position, health, weapon, wealth, armour, weapon_list, potion_list):
        """
        poistion : la position du joueur exprimé paer une liste de longueur 2
        health : la santé du joueur exprimé en pourcentage (mais peut être supérieur à 100
        weapon : une liste avec l'arme du joueur et son dégat 
            ex: weapon = ["sword", 40]
        wealth : le nombre de pièce d'or du personnage
        potion_list : une liste des potions du joueur 
            ex : potion = ["health", 50]
        """
        self.position = position 
        self.health = health
        self.weapon = weapon 
        self.wealth = wealth 
        self.armour = armour 
        self.weapon_list = weapon_list 
        self.potion_list = potion_list

    def enrichement(self, coin_bags):
        wealth = self.wealth
        self.wealth = wealth + coin_bags 
    
    def use_potion(self):
        potions = self.potion_list 
        potion = potions.pop()
        if potion[0] == 'health':
            self.health += potion[1]
        # to be continued 

        self.potion_list = potions



        




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
        
        if event.type = pg.K_m:
            player.use_potion()




        if event.type == pg.QUIT:
            running = False


    screen.fill(BLACK)
    draw_rect(screen, 0, 1, COTE, WHITE)

    pg.display.update()
    

pg.quit()
