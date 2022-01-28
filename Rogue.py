
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
    if player.position + direction in doors:
        doors.remove(player.position + direction)
    if player.position + direction not in walls:
        player.position += direction
    if player.position + direction in KNIGHT_DICT.keys():
        fight(player, KNIGHT_DICT[player.position + direction])


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

def room(pt, length, width):
    pass

        

running = True
while running:
    clock.tick(pace)

    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYUP:
            print(player.position)
            move(player, (0, 1))
        if event.type == pg.K_s:
            move(player, (0, -1))
        if event.type == pg.K_q:
            move(player, (-1, 0))
        if event.type == pg.K_d:
            move(player, (1, 0))

    screen.fill(BLACK)
    draw_rect(screen, 0, 1, COTE, WHITE)
    draw_rect(screen, player.position[0], player.position[1], COTE, GREEN)

    pg.display.update()
    

pg.quit()
