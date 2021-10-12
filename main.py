import pygame
from pygame.constants import QUIT

# initialize game
pygame.init()

# create screen
screen = pygame.display.set_mode((800,600))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("battleship.png")
pygame.display.set_icon(icon)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False