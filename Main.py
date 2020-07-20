from Hangman import Game
from screenDisplay import screenDisplay
import pygame

if __name__ == '__main__':
    WIDTH, HEIGHT = 800 , 500         #size of the screen
    screenDisplay = screenDisplay()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('HANG MAN')
    run = True
    pygame.time.delay(10)

    while run :  
        window.fill((255, 255, 255))
        screenDisplay.welcomeWindow(window)
  