import pygame
from sys import exit

pygame.init() #initializes pygame

#displays the surface that the player sees (stored in a variable 'screen'):
#set_mode((width,height)) - size of the window in pixels

screen = pygame.display.set_mode((2000, 1300))

pygame.display.set_caption("Domino's Domino")

clock = pygame.time.Clock()

score_font = pygame.font.Font(None, 50)

#SURFACES
score_surface = pygame.Surface((400, 100))
text_surface = score_font.render("Score:", False, 'green')
#/SURFACES

#SURFACE_COLORS
screen.fill('cornsilk')
score_surface.fill('darkcyan')
#/SURFACE_COLORS

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #pygame uninitialised
            exit() #assures that the code (in this case the while loop) is terminated
    
    #SURFACE_POSITIONING
    screen.blit(score_surface,(25,75))
    screen.blit(text_surface,(25,25))
    #/SURFACE_POSITIONING

    pygame.display.update() #updates the display surface
    clock.tick(60)