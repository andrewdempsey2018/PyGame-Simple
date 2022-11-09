import pygame, sys

pygame.init()

import random

# try 1024*768 or 2048*1536
screenWidth = 800
screenHeight = 600

size = width, height = screenWidth, screenHeight

# can also add  pygame.FULLSCREEN
screen = pygame.display.set_mode(size)

# We can set this to false to stop the game
game_is_running = True

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
# rgb colour is light blue
background.fill((153, 255, 204))

# always use convert() method when loading images (increases performance)
aSprite = pygame.image.load('face.png').convert()
aSprite.set_colorkey((255,0,255))

xPos = 400
yPos = 300

# perform game logic here
def updateGame():
    pass
    

# draw everything
def draw():
    screen.blit(background, (0, 0))
    screen.blit(aSprite, (xPos, yPos))
    pygame.display.flip()

# handle player key press events
def getInput():
    pass

# run when boolean is true
while game_is_running:
    # if pygame detects a quite event (click the 'x' top right of window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    updateGame()
    getInput()
    draw()
