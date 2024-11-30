#import random module from python
import random

class Sadle:
  text_file = 'alice.txt'
  def __init__(self, text_file):
    self.text_file = text_file
  
  f = open(text_file, "r")
  
  turns = 6
  
  words = []
  
  for x in f:
    _words = x.split()
    for word in _words:
      words.append(word)
      
  random_word = str(random.choice(words))
  failed = len(random_word)
  
  
      


    
  def start_game(self):
    print("\nYour analysis has been save to you file path. \n Take a break by playing Sadle! See if you can guess the word of the day that we have chosen from your text.")
    while self.turns != 0: 
        user_guess = input("You have " + str(self.turns) + " chances left to guess the word! ")
        for x in user_guess.upper(): 
            if x in self.random_word.upper():
                print(x + " correct!", end ="\n")
    
            else:
              print(x + " wrong!")
    
    
        self.turns -= 1

        if self.random_word is not int:
          if self.random_word.upper() == user_guess.upper():
              print("\nYou won!\nThe word is ", self.random_word,"!")
              exit()
    
    print("Out of guesses:( The word was " + self.random_word.upper() + " Try again!")
    exit()

