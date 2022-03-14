import random

#logic
#for this we need to have the computer loop through a set of numbers 
# and pick a random one. then the user needs to give feedback so the computer 
# can narrow its range. it continues like that.

# first we must define a function to get the job done
def computer_guess(x):
# next we define all the variables needed for the function of work
    low = 1
    high = x
    feedback = ''
# here we get the computer to loop through the range if the first guess is not correct
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
# after the computer has guessed incorrectly, the user should give it a hint!
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
# after the hint, the computer should adjust its range       
        if feedback == 'h':
            high == guess - 1
        elif feedback == 'l':
            low == guess + 1

    print('Computer has won Muhahaha')

computer_guess(5)

