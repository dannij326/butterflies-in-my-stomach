import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  # choose a random word
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word
    
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # guessed letters
    
    lives = 7
    
    # time for some input
    while len(word_letters) > 0 and lives > 0:
        # update player and add to used letters 
        print('You have', lives, 'lives left and you have used these letters: ', ''.join(used_letters))
        
        # current word progress
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ''.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            else:
                lives -= 1   # lose a life if wrong
                print('Letter is NOT in word, you lose a life.')
                
        elif user_letter in used_letters:
            print('You have used that letter, try another one.')
            
        else:
            print('Invalid character, please try again.')
            
    # only gets here if len(word_letters) == 0 or lives == 0
    if lives == 0:
        print('POW you\'re dead! Better luck next time. The word was', word)
    else:
        print('Way to go! You guessed the right word', word, '!!!')
        
    hangman()