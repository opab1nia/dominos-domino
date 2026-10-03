import pygame
from sys import exit

pygame.init() #initializes pygame

#displays the surface that the player sees (stored in a variable 'screen'):
#set_mode((width,height)) - size of the window in pixels
screen = pygame.display.set_mode((2000, 1300))
pygame.display.set_caption("Domino's Domino")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #pygame uninitialised
            exit() #assures that the code (in this case the while loop) is terminated
    #draw all our elements
    #update everything
    pygame.display.update() #updates the display surface
    clock.tick(60)