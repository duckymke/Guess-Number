# this project is to get a better understanding of functions, if else, and random properites

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x}:'))
        if guess > random_number:
            print("guess a lower number")
        elif guess < random_number:
            print("guess a higher number")

guess(1000)