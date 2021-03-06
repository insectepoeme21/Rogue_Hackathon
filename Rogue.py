
import pygame as pg
from random import randint
from itertools import product
from ctypes.wintypes import SIZE

class Knight:
    def __init__(self, pos, HP=50, DMG=10, Ore = 10):
        self.HP = HP
        self.pos = pos
        self.DMG = DMG
        self.ore = Ore

def move(player, direction):
    global doors
    new_pos = (player.position[0] + direction[0],player.position[1] + direction[1])
    if new_pos in doors:
        doors.remove(new_pos)
        player.position = new_pos
        pg.mixer.music.load("door.mp3")
        pg.mixer.music.play()
    else:
        if new_pos not in walls and new_pos not in KNIGHT_DICT.keys() and new_pos not in tools.keys() and new_pos not in BOSS_DICT.keys():
            player.position = new_pos
        if new_pos in BOSS_DICT.keys():
            fight(player, BOSS_DICT[new_pos])
        if new_pos in KNIGHT_DICT.keys():
            fight(player, KNIGHT_DICT[new_pos])
        if new_pos in BAG_LIST:
            player.position = new_pos
            player.enrichement(BAG_LIST[new_pos])
            del BAG_LIST[new_pos]
            pg.mixer.music.load("coin.mp3")
            pg.mixer.music.play()
        if new_pos in tools.keys():
            pg.mixer.music.load("sword.mp3")
            pg.mixer.music.play()
            player.position = new_pos
            player.weapon = tools[new_pos]
            del tools[new_pos]

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
    pg.mixer.music.load("grrr.mp3")
    pg.mixer.music.play()
    knight.HP -= player.weapon[1]
    if knight.HP > 0:
        player.health += player.armour - knight.DMG
        print(f"PLayer has now {player.health} HP")
    if player.health <= 0:
        pg.quit()
    if knight.HP <= 0:
        player.wealth += knight.ore
        print(f"PLayer has now {player.wealth} Gold")
        del KNIGHT_DICT[knight.pos]


KNIGHT_DICT={(23,18) : Knight((23,18)), (12, 15) : Knight((12, 15))}
BOSS_DICT = {(8, 26) : Knight((8, 26), HP = 200, DMG = 20)}
tools = {(4, 11):("sword", 40), (15, 6):("axe", 20)}
BAG_LIST = {(10, 21) : 10, (13, 20) : 20, (14, 20) : 30, (19, 20) : 10, (11, 5) : 15}


walls = []
doors = []
paths = []
player = Player((3, 3))
VICTORY = False

pg.init()
COTE = 20 # largeur du rectangle en pixels
NB_CASES = 33
screen = pg.display.set_mode((COTE*NB_CASES, COTE*NB_CASES))
clock = pg.time.Clock()
pace = 10


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (150, 150, 150)


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
    
map = [[(2, 2), 9, 7, [(4, 8), (10, 5)]],
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

sword = pg.image.load("sword.png")
knight = pg.image.load("knight.png")
coin = pg.image.load("dollar-coin.png")
wood = pg.image.load("wood.png")
boss = pg.image.load("boss.png")
axe = pg.image.load("axe.png")
digger = pg.image.load("mineur.png")
brick = pg.image.load("wall.png")
dooor = pg.image.load("door.png")
ladder = pg.image.load("ladder.png")
cup = pg.image.load("cup.png")

for i in map:
    room(*i)
        

running = True
while running:
    clock.tick(pace)

    if not VICTORY:
    



        screen.fill(BLACK)
        for x in doors:
            screen.blit(dooor, (x[0]*COTE, x[1]*COTE))

        for x in KNIGHT_DICT.keys():
            screen.blit(knight, (x[0]*COTE, x[1]*COTE))

        for i, j in walls:
            screen.blit(brick, (i*COTE, j*COTE))
        for i, j in paths:
            screen.blit(wood, (i*COTE, j*COTE))
        for x in BOSS_DICT.keys():
            screen.blit(boss, (x[0]*COTE, x[1]*COTE))
        for pos, value in tools.items():
            if value[0] == "sword":
                screen.blit(sword, (pos[0]*COTE +2, pos[1]*COTE +2))
            elif value[0] == "axe":
                screen.blit(axe, (pos[0]*COTE +2, pos[1]*COTE +2))
        for x in BAG_LIST.keys():
            screen.blit(coin, (x[0]*COTE +2, x[1]*COTE +2))
        

        screen.blit(ladder, (4*COTE +3, 26*COTE -3))

        GOLD =  (255,215,0)

        health_rect = pg.Rect(100, 31*COTE, max(2.5*player.health, 250), COTE)
        damage_rect = pg.Rect(100 + 2.5*player.health,31*COTE, max(0, 250 - 2.5*player.health), COTE)
        pg.draw.rect(screen, GREEN, health_rect)
        pg.draw.rect(screen, RED, damage_rect)
        wealth_rect = pg.Rect(150, 32*COTE, player.wealth, COTE)
        pg.draw.rect(screen, GOLD, wealth_rect)


        # Affichage du texte 
        font_obj=pg.font.SysFont("Arial", 20)

        coin_txt = font_obj.render(f"Wealth: {player.wealth} coins", True, GOLD) 
        health_txt = font_obj.render(f"Healthbar:", True, GREEN)
        txt = font_obj.render(f"Your Character:", True, WHITE)

        screen.blit(coin_txt, (0, 32*COTE))
        screen.blit(health_txt, (0,31*COTE))
        screen.blit(txt, (0, 30*COTE - 5))



        screen.blit(digger, (player.position[0]*COTE , (player.position[1]-0.5)*COTE))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    move(player, (0, 1))
                if event.key == pg.K_UP:
                    move(player, (0, -1))
                if event.key == pg.K_LEFT:
                    move(player, (-1, 0))
                if event.key == pg.K_RIGHT:
                        move(player, (1, 0))
                if player.position == (4, 26) and event.key == pg.K_DOWN:
                    pg.mixer.music.load("victory.mp3")
                    pg.mixer.music.play()
                    VICTORY = True
            
    if VICTORY:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.blit(cup, (180, 200))
        font_obj=pg.font.SysFont("Bauhaus 93", 40)
        txt = font_obj.render("VICTORY", True, GOLD)
        screen.blit(txt, (13*COTE, 24*COTE))
        pg.display.update()

    pg.display.update()
    
pg.quit()
