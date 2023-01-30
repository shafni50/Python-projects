import random 
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses a word from the list
    while '_' in word or ' ' in word:
        word = random.choice(words)

        return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(words) #letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  #what the user has guessed

#getting user input
#when letters used
#join([a, b, cd]) --> 'a b cd'
    while len(word_letters) > 0:
        print('You have these letters: ',' '.join(used_letters))
 #what current word  is
        word_lists = [letter if letter in used_letters else '_' for letter in word]
        print('current word: '' '.join(word_lists))

        user_letter = input('guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('Sorry you have used that letter. Please try again. ')

        else :
            print("invalid character. Please try again")

user_input = input("Type something: ")
print(user_input)

#gets here where len(words_letters) == 0
hangman()