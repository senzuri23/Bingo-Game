# call Random 7 letter word from 7 letter word file, scramble up the word
# then get the user to guess the word from the scrambled letters

import random

# Gets random word from Bingo word list file
def get_unscrambled_word():
    with open('BingoWords.txt') as f:
        lines = f.readlines()
        line = str(random.choice(lines))
        unscrambledBingo = line.replace('\n', '')
        return unscrambledBingo

# Scrambles word
def scramble_word(word):
        randomWord = list(word)
        random.shuffle(randomWord)
        scrambledBingo = ''.join(randomWord)
        return scrambledBingo 

# Takes unscrambled word, scrambles it, prints the scrambled word.
# Then player is asked to guess the word until they guess correctly
def play():
        picked_word = get_unscrambled_word()
        qn = scramble_word(picked_word)
        print(picked_word)
        print(qn)   

        #guess = input("Guess the Bingo from the scrambled letters: \n")

        while True:
                guess = input('Guess the Bingo from the scrambled letters:')

                if guess == picked_word:
                        print('Congratulations, you guessed the Bingo correctly.')
                        break

play()