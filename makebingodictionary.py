# Get all the 7 letter words from the Collins Scrabble dictionary and put it
# into a new file

allscrabblewords = open('Collins Scrabble Words (2019).txt', 'r')

bingowords = open('Bingowords.txt', 'w')

for line in allscrabblewords:
    if len(line) == 8:
        bingowords.write(line + '\n')

    else:
        pass

bingowords.close()
