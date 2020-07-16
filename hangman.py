from random import choice
from string import ascii_lowercase


def play_game(guess):
    attempts = 8
    hide_word = '-' * len(guess)
    result = False
    guess_letters = []
    while attempts > 0:
        print('\n' + hide_word)
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print('You should input a single letter')

        elif letter not in ascii_lowercase:
            print('It is not an ASCII lowercase letter')

        elif letter in guess_letters:
            print('You already typed this letter')
        elif letter in guess:
            for i in range(len(guess)):
                if letter == guess[i]:
                    temp = list(hide_word)
                    temp[i] = letter
                    hide_word = ''.join(temp)
        else:
            print('No such letter in the word')
            attempts -= 1

        if hide_word == guess:
            result = True
            break
        guess_letters.append(letter)

    if result:
        print('\n' + hide_word)
        print('You survived!')
    else:
        print('You are hanged!')


print('H A N G M A N')

while True:
    option = input('Type "play" to play the game, "exit" to quit: ')
    if option == 'play':
        words = ['python', 'java', 'kotlin', 'javascript']
        guess = choice(words)
        play_game(guess)
    elif option == 'exit':
        break
