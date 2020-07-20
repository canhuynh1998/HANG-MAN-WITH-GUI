import random, pygame, math
from Database import DatabaseAPI

class Game:

    def __init__(self):
        '''Constructor'''
        pygame.init()

        self.RADIUS = 20
        
        self.database = DatabaseAPI()
        self.letters = self.inputLetter()
        self.guessedWord = []
        self.images = self.inputImage()

    def quitProgram(self):
        '''Check to quit the program'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
    def drawTittle(self, window):
        '''Draw the tittle on the screen'''
        TITTLEFONT = pygame.font.SysFont('comicsans', 60)
        text = TITTLEFONT.render('HANG MAN', True, (0, 0, 0))
        window.blit(text, (200, 50))


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
                showedWord += "* "
        text = SECRETWORDFONT.render(showedWord, True, (0, 0, 0))
        window.blit(text, (400, 200))

    def operation(self, window, choice):
        '''Main operation'''
        secretWord, guessed = self.callDatabase(choice), self.guessedWord
        FPS, i = 60, 0
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    for letter in self.letters:
                        x, y, ltr, visible = letter
                        if visible:
                            distance = math.sqrt((mouseX - x)**2 + (mouseY - y)**2)
                            if distance < self.RADIUS:
                                letter[3] = False
                                guessed.append(ltr)
                                print(guessed)
                                if ltr not in secretWord:
                                    i += 1
                                   
            self.draw(window, secretWord, guessed, i)                 
            
            won = True
            for letter in secretWord:
                if letter not in guessed:
                    won = False
                    break
            if won:
                self.message(window, 'YOU WON!')
                break
            if i == 6:
                self.message(window, 'YOU DID NOT GUESS THE CORRECT WORD!')
                break

    def message(self, window, message):
        WIDTH, HEIGHT = 800, 500
        pygame.time.delay(1000)
        window.fill((255, 255, 255))
        MESSAGEFONT = pygame.font.SysFont('comicsan', 40)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            text = MESSAGEFONT.render(message, True, (0, 0, 0))
            window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
            pygame.display.update()
        
        
