import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, not it. Aim higher.')
        elif guess > random_number:
            print('Sorry, not it.  Aim lower.')
    
    print(f'Yup, you did it! You guessed the number {random_number} correctly!')
    
def computer_guess(x):
    low = 1
    high = x
    feedbk = ''
    while feedbk != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high  # or low b/c low = high
        feedbk = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedbk == 'h':
            high = guess - 1
        elif feedbk == 'l':
            low = guess + 1
            
    print(f'Woo Hoo! The computer guessed your number, {guess}, correctly!')

guess(1000)

print('Now its my turn to guess!')

computer_guess(1000)
