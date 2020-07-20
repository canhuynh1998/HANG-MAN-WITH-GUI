import sqlite3

class DatabaseAPI:

    def __init__(self):
        '''constructor and create a table'''
        self.connection = None
        self.cursor = None
        
    def connectDB(self, db_name=':memory:'):
        '''connect to the database'''
        try:
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
            return True
        
        except sqlite3.Error as error:
            print(error)
            return False

    def createTable(self, queryString):
        '''create the table for the database'''
        try:
            self.cursor.execute(queryString)
        except sqlite3.Error as error:
            print(error)

    def insert(self, queryString, data):
        '''insert data into the database'''
        try:
            with self.connection:
                self.cursor.execute(queryString, data)
        except sqlite3.Error as error:
            print(error)

    def delete(self, queryString):
        '''delete data from the database'''
        try:
            with self.connection:
                self.cursor.execute(queryString)
        except sqlite3.Error as error:
            print(error)

    def select(self, queryString):
        '''select data from the database'''
        try:
            self.cursor.execute(queryString)
            return self.cursor.fetchone()
        except sqlite3.Error as error:
            print(error)
            return None  

    def close(self):
        '''close the database'''
        try:
            self.connection.close()

        except sqlite3.Error as error:
            print(error)


''' CREATING Fruit Table'''
fruitTable = DatabaseAPI()
fruitTable.connectDB('Fruit.db')
# fruitTable.createTable('''CREATE TABLE Fruit(
#     id INTEGER,
#     letter TEXT
# )''')

# with open('fruit.txt') as file:
#     for line in file:
#         letter = line.strip()
# wordList = letter.split()
# for i in range(len(wordList)):
#     fruitTable.insert('''INSERT INTO Fruit VALUES(:id, :letter)''',{'id': int(i), 'letter':wordList[i]})
# # fruitRes = fruitTable.select('''SELECT letter FROM Fruit ''')#ORDER BY RANDOM() LIMIT 1''')
fruitTable.connection.commit()
fruitTable.close()



'''Creating Animal Table'''
animalTable = DatabaseAPI()
animalTable.connectDB('Animal.db')
# animalTable.createTable('''CREATE TABLE Animal(
#     id INTEGER,
#     letter TEXT
# )''')

# with open('animal.txt') as file:
#     for line in file:
#         letter = line.strip()
# wordList = letter.split()
# for i in range(len(wordList)):
#     animalTable.insert('''INSERT INTO Animal VALUES(:id, :letter)''',{'id': int(i), 'letter':wordList[i]})
# # animalRes = animalTable.select('''SELECT letter FROM Animal''')# ORDER BY RANDOM() LIMIT 1''')
animalTable.connection.commit()
animalTable.close()


