# This is a guess the number game.

import random

print('Hello, What is your name?')
name = input()

print('Well, '+name+', I am thiking a number between 5 to 10')
secretNumber = random.randint(5,10)

for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess > secretNumber:
        print('your guess is too high.')
    elif guess < secretNumber:
        print('your guess is too low.')
    else:
        break

if guess == secretNumber:
    print('Good job, '+name+'! You guessed my number in '+str(guessesTaken)+' guesses.')
else:
    print('Nope, The number I was thinking of was '+str(secretNumber)+'.')


