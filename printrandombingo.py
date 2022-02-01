# call Random 7 letter word from 7 letter word file, scramble up the word
# then get the user to guess the word from the scrambled letters

import random

def PrintScrambedBingo():
    with open('BingoWords.txt') as f:
        lines = f.readlines()
        line = str(random.choice(lines))
        lineWithoutBreak = line.replace('\n', '')
        print(lineWithoutBreak)
        unscrambledBingo = list(lineWithoutBreak)
        print(unscrambledBingo)
        random.shuffle(unscrambledBingo)
        scrambledBingo = ''.join(unscrambledBingo)
        scrambledBingoWithoutBreak = str(scrambledBingo.replace('\n', ''))
        print(scrambledBingoWithoutBreak)   
    
#guess = input("Guess the Bingo from the scrambled letters: \n")

#unscrambledBingo1 = str(unscrambledBingo)
#print(unscrambledBingo1)


#    print("Congratulations, you are a Scramble genius!")
# else:

# while guess != unscrambledBingo:
 #   print('This time it was incorrect, try again.')
# else:
#    print('Congratulations, you have unscrambled the Bingo!')

PrintScrambedBingo()