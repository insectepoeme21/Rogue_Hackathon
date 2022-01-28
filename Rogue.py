import pygame as pg
from random import randint
from itertools import product

class Knight:
    def __init__(self, pos, HP=50, DMG=10, Ore = 10):
        self.HP = HP
        self.pos = pos
        self.DMG = DMG
        self.wealth = Ore

def move(player, direction):
    global doors
    new_pos = (player.position[0] + direction[0],player.position[1] + direction[1])
    if new_pos in doors:
        doors.remove(new_pos)
    else:
        if new_pos not in walls:
            player.position = new_pos
        if new_pos in KNIGHT_DICT.keys():
            fight(player, KNIGHT_DICT[new_pos])
    if new_pos in BAG_LIST:
        player.position = new_pos
        player.enrichement(BAG_LIST[new_pos])

class Player:
    def __init__(self, position, health = 100, weapon = ["wood stick", 10], wealth = 0, armour = 0):
        """
        poistion : la position du joueur exprimé paer une liste de longueur 2
        health : la santé du joueur exprimé en pourcentage (mais peut être supérieur à 100
        weapon : une liste avec l'arme du joueur et son dégat 
            ex: weapon = ["sword", 40]
        wealth : le nombre de pièce d'or du personnage
        """
        self.position = position 
        self.health = health
        self.weapon = weapon 
        self.wealth = wealth 
        self.armour = armour 


    def enrichement(self, coin_bags):
        wealth = self.wealth
        self.wealth = wealth + coin_bags 
 



def fight(player, knight):
    knight.HP -= player.weapon[1]
    if knight.HP > 0:
        player.health += player.armour - knight.DMG
    if player.health <= 0:
        pg.quit()
    if knight.HP <= 0:
        KNIGHT_DICT.pop(knight.pos)
        player.wealth += knight.ore

KNIGHT_DICT={}
walls = []
doors = []
player = Player((3, 3))
BAG_LIST = {}

pg.init()
COTE = 20 # largeur du rectangle en pixels
NB_CASES = 30
screen = pg.display.set_mode((COTE*NB_CASES, COTE*NB_CASES))
clock = pg.time.Clock()
pace = 10


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


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


        

running = True
while running:
    clock.tick(pace)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_s:
                move(player, (0, 1))
            if event.key == pg.K_z:
                move(player, (0, -1))
            if event.key == pg.K_q:
                move(player, (-1, 0))
            if event.key == pg.K_d:
                    move(player, (1, 0))

    for i in map:
        room(*i)


    screen.fill(BLACK)
    for x, y in walls:
        draw_rect(screen, x, y, COTE, WHITE)
    for x in doors:
        draw_rect(screen, *x , COTE, RED)
    draw_rect(screen, *player.position, COTE, GREEN)

    pg.display.update()
    

pg.quit()