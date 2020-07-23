import pygame, sys
from Hangman import Game

class screenDisplay:

    def __init__(self):
        '''constructor'''
        pygame.init()
        pygame.font.init()
        '''size for button'''
        self.X, self.Y = 400 , 270
        self.width, self.height = 100 , 60

        self.LETTERFONT = pygame.font.SysFont('comicsans', 30)      #font for the welcoming scence
    
    def quitProgram(self, event):
        '''Check to quit the program'''
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    def welcomeWindow(self, window):#, HEADERFONT):
        '''The welcoming window. It also asks for selection of catergories'''
        run = True
        pygame.time.delay(10)
        while run:
            window.fill((255, 255, 255))
            self.draw(window)
            for event in pygame.event.get():
                self.quitProgram(event)      #check when to stop the program
                return self.buttonFunction(window)
   
    def welcomeImage(self, window):
        '''welcome image'''
        welcomeImage = pygame.image.load('WELCOME-)(.png')
        window.blit(welcomeImage, ( 30, 50))
        
    def promptCatergory(self, window):
        '''prompt users to choose the category'''
        prompt = self.LETTERFONT.render('What category do you want to choose ?', True, (0, 0, 0) )
        window.blit(prompt, (380, 100))
       
    def buttonFunction(self, window):
        '''Call the function of the button'''
        run = True
        while run :
            for event in pygame.event.get():
                self.quitProgram(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY= pygame.mouse.get_pos()
                    print((mouseX, mouseY))
                    if (self.X + self.width >= mouseX >= self.X) and (self.Y + self.height >= mouseY >= self.Y):
                        return 'Animal'
                    if (self.X + self.width >= mouseX >= self.X) and (self.Y + self.height + 80 >= mouseY >= self.Y + 80):
                        return 'Fruit'
                    print((mouseX, mouseY))

    def animalButton(self, window):
        '''Create animal button'''
        pygame.draw.rect(window, (255, 255, 255), (self.X, self.Y, self.width, self.height), 3)
        animalButton = self.LETTERFONT.render('ANIMAL', True, (255, 255, 255))    #put 'ANIMAL' on the screen
        window.blit(animalButton, (self.X + 10, self.Y + 20))
        
    def fruitButton(self, window):
        '''create fruit button'''
        pygame.draw.rect(window, (255, 255, 255), (self.X, self.Y + 80, self.width, self.height), 3)
        animalButton = self.LETTERFONT.render('FRUIT', True, (255, 255, 255))    #put 'ANIMAL' on the screen
        window.blit(animalButton, (self.X + 15, self.Y + 102))
    
    def backgroundImage(self, window):
        background = pygame.image.load('background.png')
        window.blit(background,(0,0))
      
    def draw(self, window):
        '''Draw all the buttons on the screen'''
        self.backgroundImage(window)
        self.animalButton(window)
        self.fruitButton(window)
        self.welcomeImage(window)
        self.promptCatergory(window)
        pygame.display.update()

