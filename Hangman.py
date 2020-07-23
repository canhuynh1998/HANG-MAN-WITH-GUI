import random, pygame, math, sys, pyttsx3
from Database import DatabaseAPI
pygame.init()
class Game:

    def __init__(self):
        '''Constructor'''
       
        pygame.font.init()
        self.RADIUS = 20
        
        self.database = DatabaseAPI()
        self.letters = self.inputLetter()
        self.guessedWord = []
        self.images = self.inputImage()

    def quitProgram(self, event):
        '''Check to quit the program'''
        # for event in pygame.event.get():
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    def drawTittle(self, window):
        '''Draw the tittle on the screen'''
        TITTLEFONT = pygame.font.SysFont('comicsans', 60)
        text = TITTLEFONT.render('HANG MAN', True, (0, 0, 0))
        window.blit(text, (200, 50))
    
    def backgroundImage(self, window):
        background = pygame.image.load('background.png')
        window.blit(background,(0,0))
    
    def inputImage(self):
        '''Input images into an images list'''
        images = []
        for i in range( 7 ):
            image = pygame.image.load('HANGMAN'+str(i)+'.png')
            images.append(image)
        return images

    def inputLetter(self):
        '''Create the character list and also put them in the right order'''
        WIDTH, GAP = 800, 15
        startX = round( ( WIDTH - ( self.RADIUS * 2 + GAP) * 13 ) /2 ) 
        startY = 400
        A = 97
        character = []
        '''put the alphabet into the list'''          
        for i in range(26):
            x = startX + GAP * 2 + ( ( self.RADIUS * 2 + GAP ) * ( i % 13) ) # i % 13 stimulus 2 rows
            y = startY + ( ( i // 13 ) *  ( GAP + self.RADIUS  * 2) )
            character.append([x, y, chr(A + i), True])  
        return character

    def callDatabase(self, choice):
        '''Call the database to generate the secret word'''
        self.database.connectDB(choice+'.db')
        res = self.database.select(
            '''SELECT letter FROM '''+choice+''' ORDER BY RANDOM() LIMIT 1''')
        print('You chose category : '+choice)
        return res[0]
    
    def draw(self, window, secretWord, guessed, i):
        '''Draw all the buttons, header and also show the secret word'''
       
        LETTERFONT = pygame.font.SysFont('comicsans', 30)
        window.fill((255, 255, 255))
        self.backgroundImage(window)
        self.drawTittle(window)
        self.showSecretWord(window, secretWord, guessed)
        for letter in self.letters:
            x, y, ltr, visible = letter
            if visible:
                pygame.draw.circle(window, (0, 0, 0), (x, y), self.RADIUS, 3)
                text = LETTERFONT.render(ltr, True, (0, 0, 0))
                window.blit(text, ( x - text.get_width() / 2, y - text.get_height() / 2))
        window.blit(self.images[i], (150, 100))
        pygame.display.update()

    def showSecretWord(self, window, secretWord, guessed):
        '''Display secret word in '*' format'''
        SECRETWORDFONT = pygame.font.SysFont('comicsans', 40)
        showedWord = ""
        for letter in secretWord:
            if letter in guessed:
                showedWord += letter + " "
            else:
                showedWord += "_ "
        text = SECRETWORDFONT.render(showedWord, True, (0, 0, 0))
        window.blit(text, (400, 200))

    def operation(self, window, choice):
        '''Main operation'''
        secretWord, guessed, letters = self.callDatabase(choice), self.guessedWord, self.letters
        FPS, i = 80, 0
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                self.quitProgram(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    print((mouseX, mouseY))
                    for letter in letters:
                        x, y, ltr, visible = letter
                        if visible:
                            distance = math.sqrt((mouseX - x)**2 + (mouseY - y)**2)
                            if distance <= self.RADIUS:
                                letter[3] = False
                                guessed.append(ltr)
                                if ltr not in secretWord:
                                    i += 1  #show the stage of the game
            self.draw(window, secretWord, guessed, i)       #put here so players can see how the word or if they are completely hung             
            
            won = True
            for letter in secretWord:
                if letter not in guessed:
                    won = False
                    break
            if won:
                self.guessedWord.clear()
                
                self.postGameWindow(window, 'YOU WON!', secretWord, letters)
                break
            if i == 6:
                self.guessedWord.clear()
                self.postGameWindow(window, 'YOU DID NOT GUESS THE CORRECT WORD!', secretWord, letters)
                break
 
    def message(self, window, message, WIDTH, HEIGHT):
        '''Show the message after guessing'''
        pygame.font.init()
        MESSAGEFONT = pygame.font.SysFont('comicsan', 40)
        text = MESSAGEFONT.render(message, True, (0, 0, 0))
        window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
        pygame.display.update()

    def returnMainMenuButton(self, window):
        '''Returning to main menu function'''
        run = True
        while run :
            for event in pygame.event.get():     #check quit the program or return to the main menu
                self.quitProgram(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    print((mouseX, mouseY))
                    if 800 >= mouseX >= 800 - 104 and 79 >= mouseY > 0: 
                        return False 
    
    def loadBackButton(self, window):
        '''Load the back button'''
        backbuttonImage = pygame.image.load('backbutton.png')
        window.blit(backbuttonImage, (800 - 104, 0))

    def postGameWindow(self, window, message, secretWord, letters):
        '''Show the message after the game'''
        WIDTH, HEIGHT = 800, 500
        self.guessedWord.clear()
        for letter in letters:
            x, y, ltr, visible = letter
            if not visible:
                letter[3] = True
            else:
                continue
        window.fill((255, 255, 255))
        self.sayoutloudTheWord(secretWord)
        run = True
        while run:      #This function doesn't need the quitProgram method because it has a counter to check when to stop the loop
            self.backgroundImage(window)
            for event in pygame.event.get():
                self.loadBackButton(window)
                self.message(window, message, WIDTH, HEIGHT)
                run = self.returnMainMenuButton(window)
                
    def sayoutloudTheWord(self, secretWord):  
        '''Say the word out for players'''  
        engine = pyttsx3.init()
        engine.say('The secret word is '+secretWord)
        engine.runAndWait()