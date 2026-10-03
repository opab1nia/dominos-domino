import pygame
from sys import exit

pygame.init() #initializes pygame

#displays the surface that the player sees (stored in a variable 'screen'):
#set_mode((width,height)) - size of the window in pixels
#size of playing grid is 1152px
SW, SH = 2000, 1300

screen = pygame.display.set_mode((SW, SH))

pygame.display.set_caption("Domino's Domino")

clock = pygame.time.Clock()

score_font = pygame.font.Font(None, 50) #text font upto change

#GRID_SIZING
GRID_X, GRID_Y = 750, 74
GRID_SIZE = 1152   
BLOCK_SIZE = 96
#/GRID_SIZING

#SURFACES
score_surface = pygame.Surface((650, SH))
text_surface = score_font.render("Score:", False, '#262724')
#/SURFACES

#SURFACE_COLORS
screen.fill('#f9f9f1')
score_surface.fill('#e3e8d4')
#/SURFACE_COLORS

def drawGrid():
    for x in range(GRID_X, GRID_X + GRID_SIZE, BLOCK_SIZE):
        for y in range(GRID_Y, GRID_Y + GRID_SIZE, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "grey", rect, 1)

drawGrid()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #pygame uninitialised
            exit() #assures that the code (in this case the while loop) is terminated
    
    #SURFACE_POSITIONING
    screen.blit(score_surface,(0,0))
    screen.blit(text_surface,(75,50))
    #/SURFACE_POSITIONING

    pygame.display.update() #updates the display surface
    clock.tick(60)