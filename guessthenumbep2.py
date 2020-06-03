from random import randint
num = randint(1,20)
guesses = 1
score = 0
while guesses < 6:
    print(guesses)
    print('your score is ',score)
    guess = input('type in a number: ')
    guess = int(guess)
    if guess < 0 or guess > 20:
        print('guess within the range!')
        guesses = guesses - 1

    if guess == num:
        print('Yay! you got it right')
        print('in',guesses,'guesses')
        print('your score was',score)
        break
    if guesses == 5:
        print('the number was', num)


    if guess > num:
        print('lower')
        guesses = guesses + 1
        score = score - 10
    if guess < num:
        print('higher')
        guesses = guesses + 1
        score = score - 10    
