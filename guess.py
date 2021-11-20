print("Welcome To The Game, Type Your Guess In Between 1 To 9")
number = str(4)
chance = 5
guess = "guess"

for i in guess:
    guess = (input("Enter Your Guess : "))
    chance=chance-1   
    if(guess > number):
        print("Your Guess Is So High, Try A Number Lesser Than", guess)
        
    if(guess < number): 
         print("Your Guess Is So Low, Try A Number Higher Than", guess)
        

    if (guess == number):
        print("CONGRADRULATIONS, You Guessed The Number!!!")
if  not chance<0 :  
    print("You Lost!!!, The Number Is", number)