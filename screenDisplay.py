import pygame, sys
from Hangman import Game

class screenDisplay:

    def __init__(self):
        '''constructor'''
        pygame.init()

        '''size for button'''
        self.X, self.Y = 400 , 150
        self.width, self.height = 100 , 60

        self.LETTERFONT = pygame.font.SysFont('comicsans', 30)      #font for the welcoming scence
        
    def welcomeWindow(self, window):#, HEADERFONT):
        '''The welcoming window. It also asks for selection of catergories'''
        self.quitProgram()      #check when to stop the program
        
        pygame.time.delay(100)
        window.fill((255, 255, 255))

        '''welcome image'''
        welcomeImage = pygame.image.load('WELCOME-)(.png')
        window.blit(welcomeImage, ( 30, 50))
       
        self.animalButton(window)
        self.fruitButton(window)
       
        prompt = self.LETTERFONT.render('What category do you want to choose ?', True, (0, 0, 0) )
        window.blit(prompt, (380, 100))
       
        pygame.display.update() #only use 1 time or else it won't be stable

    def quitProgram(self):
        '''Quit game function. Have to put this function in every window'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
    def animalButton(self, window):#, BUTTONFONT):
        '''put animal button on the screen'''  
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        game = Game()
        animalButton = self.LETTERFONT.render('ANIMAL', True, (0, 0, 0))    #put 'ANIMAL' on the screen
  
        if (self.X + self.width > mouse[0] > self.X) and (self.Y + self.height > mouse[1] > self.Y):
            pygame.draw.rect(window, (0, 0 , 0), (self.X, self.Y, self.width, self.height), 3)
            if click[0] == 1 :
                window.fill((255, 255,255))
                animalButton = self.LETTERFONT.render('', True, (0, 0, 0))  #overwrite the button so that everything can be cleaned               
                game.operation(window, 'Animal')     
        else:
            pygame.draw.rect(window, (0, 0, 0), (self.X, self.Y, self.width, self.height), 3)   
        window.blit(animalButton , (self.X + 10, self.Y + 22) )
 

    def fruitButton(self, window):#, BUTTONFONT):
        '''put fruit button on the screen'''  
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        game = Game()
        fruitButton = self.LETTERFONT.render('FRUIT', True, (0, 0, 0))    #put 'ANIMAL' on the screen
  
        if (self.X + self.width > mouse[0] > self.X) and (self.Y + self.height + 80> mouse[1] > self.Y + 80):
            pygame.draw.rect(window, (0, 0 , 0), (self.X, self.Y+ 80, self.width, self.height), 3)
            if click[0] == 1 :
                window.fill((255, 255,255))
                fruitButton = self.LETTERFONT.render('', True, (0, 0, 0))  #overwrite the button so that everything can be cleaned               
                game.operation(window, 'Fruit')     
        else:
            pygame.draw.rect(window, (0, 0, 0), (self.X, self.Y + 80, self.width, self.height), 3)   
        window.blit(fruitButton , (self.X + 10, self.Y + 102) )
   

