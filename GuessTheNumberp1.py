#Importing random to use the functions
from random import randint

#Setting the random number(integer)
num = randint(1,20)

### MAIN CODE ###

#In this 6-iteration loop all the main code is executed
for guesses in range(1,6):
    
    #Asking for input and converting it into an integer
    guess = input('type in a number: ')
    guess = int(guess)
    
    ### MAIN LOGIC ###
    # Checking if the guess is equal, higher or lower than the numver to guess respectively
    
    if guess == num:
        print('Yay! you got it right')
        break


    if guess > num:
        print('lower')
    if guess < num:
        print('higher')
