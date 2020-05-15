from random import randint
num = randint(1,20)
for guesses in range(1,6):
    guess = input('type in a number: ')
    guess = int(guess)

    if guess == num:
        print('Yay! you got it right')
        break


    if guess > num:
        print('lower')
    if guess < num:
        print('higher')
