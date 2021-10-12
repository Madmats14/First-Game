import pygame
from pygame.constants import QUIT
import random
import math

# initialize game
pygame.init()

# create screen
screen = pygame.display.set_mode((800,600))

# background
background = pygame.image.load("fondorural.png")

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
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemy_move_x = 1.5
enemy_move_y = 40

# Creating bullet
bullet_image = pygame.image.load("falafel.png")
bulletX = 0
bulletY = 480
bullet_move_x = 0
bullet_move_y = 2.5
bullet_state = "ready"

score = 0
font = pygame.font.Font("freesansbold.ttf", 28)
textX = 10
textY = 560

def show_score(x, y):
    vegan_score = font.render("Veganismo : " + str(score), True, (0, 160, 0))
    screen.blit(vegan_score, (x, y))
def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y):
    screen.blit(enemy_image, (x, y))    

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY,2))
    if distance < 27:
        return True

# game loop
running = True
while running:
    
     # screen color
    screen.fill((0, 0, 0))
     # background image
    screen.blit(background, (0, 0)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check if a button pressed or released
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_move = -5
            if event.key == pygame.K_RIGHT:
                player_move = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)                            
        
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
        enemy_move_x = 1.5
        enemyY += enemy_move_y
    elif enemyX >= 736:
        enemy_move_x = -1.5
        enemyY += enemy_move_y

    # bullet movement
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_move_y
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"    

    # collision
    collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1  
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)
 
    player(playerX, playerY)
    show_score(textX, textY)
    enemy(enemyX, enemyY)

    pygame.display.update()        