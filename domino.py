import pygame
from sys import exit

pygame.init() #initializes pygame

#displays the surface that the player sees (stored in a variable 'screen'):
#set_mode((width,height)) - size of the window in pixels
SW, SH = 2000, 1300 #screen width, screen size
screen = pygame.display.set_mode((SW, SH))

pygame.display.set_caption("Domino's Domino")
icon = pygame.image.load('domino.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

score_font = pygame.font.Font(None, 50) #text font upto change

#GRID_SIZING
GRID_X, GRID_Y = 750, 74 #distance of grid from starting point in (x, y) coodinates
GRID_SIZE = 1152 #size of playing grid is 1152px
BLOCK_SIZE = 96
#/GRID_SIZING

#SURFACES
score_surface = pygame.Surface((650, SH))
text_surface = score_font.render("Score:", False, '#262724')
grid_background_surface = pygame.Surface((GRID_SIZE + 40, GRID_SIZE + 40))
#/SURFACES

#SURFACE_COLORS
screen.fill('#f9f9f1')
score_surface.fill('#e3e8d4')
grid_background_surface.fill('#ebede6')
#/SURFACE_COLORS

#RECTANGLES
domino_block = pygame.Rect(200, 500, BLOCK_SIZE * 2, BLOCK_SIZE)
#/RECTANGLES

def drawGrid():
    for x in range(GRID_X, GRID_X + GRID_SIZE, BLOCK_SIZE):
        for y in range(GRID_Y, GRID_Y + GRID_SIZE, BLOCK_SIZE):
            grid_square = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#cacab5", grid_square, 2, border_radius=20)
    grid_square = pygame.Rect(GRID_X, GRID_Y, GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, "#cacab5", grid_square, 4, border_radius=20)

def drawDomino(): #argument defined outside of function, initial coordinates hardcoded
    pygame.draw.rect(screen, '#FFFFFF', domino_block, BLOCK_SIZE, border_radius=20)
    pygame.draw.rect(screen, '#000000', domino_block, 2, border_radius=20)
    pygame.draw.line(screen, '#000000', (domino_block.centerx, domino_block.top), (domino_block.centerx, domino_block.bottom), 2)
            

mouse_pos_old = (0, 0)
domino_pos_old = (0, 0)
click = False

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #pygame uninitialised
            exit() #assures that the code (in this case the while loop) is terminated
        if event.type == pygame.MOUSEBUTTONDOWN:
            if domino_block.collidepoint(pygame.mouse.get_pos()) and not click:
                click = True
                mouse_pos_old = pygame.mouse.get_pos()
                domino_pos_old = domino_block.center
        if event.type == pygame.MOUSEBUTTONUP:
            click = False

    if click:
        mouse_pos = pygame.mouse.get_pos()
        dx = mouse_pos[0] - mouse_pos_old[0]
        dy = mouse_pos[1] - mouse_pos_old[1]
        domino_block.center = (domino_pos_old[0] + dx, domino_pos_old[1] + dy)
    
    screen.fill('#f9f9f1')

    #SURFACE_POSITIONING
    screen.blit(score_surface,(0,0))
    screen.blit(text_surface,(75,50))
    screen.blit(grid_background_surface,(GRID_X - 20, GRID_Y - 20))
    #/SURFACE_POSITIONING

    drawGrid()
    drawDomino()

    pygame.display.update() #updates the display surface
    clock.tick(60) #max 60fps