import pygame
from Database_Functions import *
from Maze_Generator import *
from Data_Structure_Classes import *


from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


pygame.init()

screenWidth = 800
screenHeight = 500
screen = pygame.display.set_mode([screenWidth, screenHeight])


running = True
while running:
    for event in pygame.event.get():    # Checks events
        if event.type == KEYDOWN:    #Checks for pressed keys
            pass
        elif event.type == QUIT:
            running = False