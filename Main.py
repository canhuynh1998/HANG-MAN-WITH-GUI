from Hangman import Game
from screenDisplay import screenDisplay
import pygame

if __name__ == '__main__':
    pygame.init()
    WIDTH, HEIGHT = 800 , 500         #size of the screen
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    
    pygame.display.set_caption('HANG MAN')
    screen, game, clock = screenDisplay(), Game(), pygame.time.Clock()
    
    run = True
    while run :  
        clock.tick(80)
        choice = screen.welcomeWindow(window)
        print(choice)
        game.operation(window, choice)
        