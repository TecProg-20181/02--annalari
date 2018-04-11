import random
import string

WORDLIST_FILENAME = "palavras.txt"

def openFile(fileName):
    return open(fileName, 'r', 0)

def readLine(inFile):
    return inFile.readline()

def createList(line):
    return string.split(line)

def chooseWord(wordlist):
    return random.choice(wordlist)

def header(wordList, secretWord):
    print "------------"
    print "Loading word list from file..."
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

#    for letter in secretWord:
#        if letter in secretLetters:
#            secretLetters.append(letter)
#        else:
#            pass

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord(secretWord,lettersGuessed):

    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else :
            guessed += '_'

    return guessed

def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

def hangman(secretWord):

    guesses = 8
    lettersGuessed = []
    
    

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print 'You have ', guesses, 'guesses left.'

        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = getGuessedWord(secretWord, lettersGuessed)
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_'

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = getGuessedWord(secretWord, lettersGuessed)
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_'

            print 'Good Guess: ', guessed
        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = getGuessedWord(secretWord, lettersGuessed)
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_'

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'

inFile = openFile(WORDLIST_FILENAME)
line = readLine(inFile)
wordlist = createList(line)
secretWord = chooseWord(wordlist).lower()



header(wordlist, secretWord)
hangman(secretWord)
