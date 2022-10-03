from random import randint
from typing import List, Union
class Hangman:
    def __init__(self):
        """Initialising attributes"""
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions','check']
        self.wordtofind = ""
        self.well_guessed_letters = []
        self.bad_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
        self.lives = 5
        self.incorrect_flag = True

    def word(self):
        """ getting the word to find randomly """
        i=len(self.possible_words)
        r = randint(0,i-1)
        self.wordtofind = self.possible_words[r]
        self.word_to_find = list(self.wordtofind)

    def guess(self):
        """ initialize the well_guessed_letters to blanks """
        self.word()
        letter_count = len(self.word_to_find)
        for x in range(letter_count):
            self.well_guessed_letters.append("_")
        print(self.well_guessed_letters)

    def play(self):
        """ method that asks the player to guess the letter """
        letter = ""
        #accepts only alphabets
        while True: 
            letter = input("Enter a letter ")
            if not letter.isalpha():
                print("Letters Only Please")
                continue
            else:
                break
        self.turn_count += 1
        self.incorrect_flag = True
        for y in range(len(self.word_to_find)):
            if self.word_to_find[y] == letter.lower():
                self.well_guessed_letters[y] = letter.upper()
                self.incorrect_flag = False
        if self.incorrect_flag == True:
            self.bad_guessed_letters.append(letter.upper())
            self.error_count += 1
            self.lives -= 1  
        print(self.well_guessed_letters)

    def game_over(self):
        """Stop the game"""
        print("Game Over !!")

    def well_played(self):
        """ Congratulating on winning """
        print(f"You found the word: {self.wordtofind} in {self.turn_count} turns with {self.error_count} errors!.")

    def start_game(self):
        """ Game flow """
        chance = self.lives
        print(f"lives = {chance}")
        self.guess()
        for life in range(chance):
            print (f"Try {life+1} ")
            self.play()
            chance -= 1
            # since correct letter was guessed, giving a chance to guess the word
            if self.incorrect_flag == False:
                wordguess = input("Guess the word ")
                if wordguess == self.wordtofind:
                    self.well_played()
                    self.game_over()
                    break
            if chance == 0:
                self.game_over()
                print(f""" 
                Well guessed letters : {self.well_guessed_letters} 
                Bad Guesses : {self.bad_guessed_letters} 
                Life remaining : {self.lives} 
                Errors : {self.error_count}
                No of turns : {self.turn_count}""")
            
            else :
                continue
        
            
