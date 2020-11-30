##### 10 - Game over ####
import pygame, random
from pygame.locals import *

jogando = 2 

# Helper functions
def on_grid_random():
    x = random.randint(0,19)
    y = random.randint(0,19)

    return (x * 30, y * 30)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# Macro definition for snake movement.
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def jogar(status, screen):

    snake = [(270, 180), (300, 210), (330,240)]
    snake_skin = pygame.image.load('Images/dudaCobra.png')
    apple_pos = on_grid_random()
    apple = pygame.image.load('Images/tApple.png')
    screen.fill((0,0,0))
    background = pygame.image.load('Images/background.png').convert()
    screen.blit(background, (0,0))

    my_direction = DOWN

    clock = pygame.time.Clock()

    font = pygame.font.Font('freesansbold.ttf', 18)
    score = 0

    game_over = False
    while not game_over:

        clock.tick(6)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_UP and my_direction != DOWN:
                    my_direction = UP
                if event.key == K_DOWN and my_direction != UP:
                    my_direction = DOWN
                if event.key == K_LEFT and my_direction != RIGHT:
                    my_direction = LEFT
                if event.key == K_RIGHT and my_direction != LEFT:
                    my_direction = RIGHT

        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append((0,0))
            score = score + 1
            
        # Check if snake collided with boundaries
        if snake[0][0] >= 600 or snake[0][1] >= 600 or snake[0][0] < 0 or snake[0][1] < 0:
            game_over = True
            break
        
        # Check if the snake has hit itself
        for i in range(1, len(snake) - 1):
            if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                game_over = True
                break

        if game_over:
            break 
        
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])
            
        # Actually make the snake move.
        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 30)
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 30)
        if my_direction == RIGHT:
            snake[0] = (snake[0][0] + 30, snake[0][1])
        if my_direction == LEFT:
            snake[0] = (snake[0][0] - 30, snake[0][1])
        

        
        screen.fill((0,0,0))
        background = pygame.image.load('Images/background.png').convert()
        screen.blit(background, (0,0))

        screen.blit(apple, apple_pos)

        score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
        score_rect = score_font.get_rect()
        score_rect.topleft = (600 - 120, 10)
        screen.blit(score_font, score_rect)
        
        for pos in snake:
            screen.blit(snake_skin,pos)

        pygame.display.update()
    
    while True:
        game_over_font = pygame.font.Font('freesansbold.ttf', 75)
        game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
        game_over_rect = game_over_screen.get_rect()
        game_over_rect.midtop = (600 / 2, 10)
        screen.blit(game_over_screen, (90, 200))
        button = pygame.image.load("Images/botao.png")
        screen.blit(button, (0,0))
        pygame.display.update()
        menu = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()   
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] >= 223 and pos[0] <= 370 and pos[1] >= 455 and pos[1] <= 510:
                    menu = True
                    return
        if menu:
            return
        pygame.display.update()

