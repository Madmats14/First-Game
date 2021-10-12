import pygame
from pygame.constants import QUIT
import random

# initialize game
pygame.init()

# create screen
screen = pygame.display.set_mode((800,600))

# title caption and icon
pygame.display.set_caption("Apo fires falafel!")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Creating a player
player_image = pygame.image.load("apo.png")
playerX = 370
playerY = 480
player_move = 0

# Creating enemy
enemy_image = pygame.image.load("gauchoenemy.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemy_move_x = 0.3
enemy_move_y = 40

def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y):
    screen.blit(enemy_image, (x, y))    

# game loop
running = True
while running:
    
     # screen color
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check if a button pressed or released
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_move = -0.1
            if event.key == pygame.K_RIGHT:
                player_move = 0.1            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_move = 0
    
    # set the player onscreen
    playerX += player_move
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemy_move_x
    if enemyX <= 0:
        enemy_move_x = 0.3
        enemyY += enemy_move_y
    elif enemyX >= 736:
        enemy_move_x = -0.3
        enemyY += enemy_move_y

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()        