
print("Welcome To The Game, Type Your Guess In Between 1 To 9")
import random

class Game:
    Number = random.randrange(1,10+1)
    IsGuessed = False
    nGuesses = 0
    def numCheck(a):
       if a==Game.Number:
          Game.IsGuessed = True
          print(f"You guessed It! in {Game.nGuesses}")
       elif a>Game.Number:
           print("please enter a Smaller number.")
       elif a<Game.Number:
           print("please enter a Greater number.")
          
          
    def __init__(self):
        i =0
        while(not Game.IsGuessed):
           if(i!=5):
               Game.nGuesses+=1
               userInput = int(input("Enter your guess: "))
               Game.numCheck(userInput)
               i+=1
           else:
               break
        if i==5:
            print("Max Attempt Reached!")

Game()
