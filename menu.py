import pygame
from pygame.locals import *

jogando = 1
menu = 2 
credit = 3

def start():
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption('Maria Cascavel e Thiçã')    
    thica = pygame.image.load('Images/thica.png')
    pygame.display.set_icon(thica)
    screen.fill((0,0,0))
    background = pygame.image.load('Images/menu.png').convert()
    screen.blit(background, (0,0))

    return screen

def menu_game(status, screen):
    #print("Menu ",status)
    while status == credit:
        creditos = pygame.image.load('Images/creditos.png').convert()
        screen.blit(creditos, (0,0))    
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()  
            if event.type == pygame.MOUSEBUTTONDOWN:   
                pos = pygame.mouse.get_pos()
                if pos[0] >= 55 and pos[0] <= 225 and pos[1] >= 495 and pos[1] <= 565:
                    status = menu
                    return


    