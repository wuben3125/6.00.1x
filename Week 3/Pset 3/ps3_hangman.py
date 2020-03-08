# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
        
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    wordDisplay = ''
    for char in list(secretWord):
        if char not in lettersGuessed:
            wordDisplay += '_ ' # extra space for readability
        else:
            wordDisplay += (char + ' ')
    return wordDisplay



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return ''.join(sorted(lettersGuessed))
    

def hangman(secretWord = chooseWord(wordlist)):
    '''
    secretWord: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    numFails = 0
    lettersGuessed = []
    roundNum = 1
    
    print("Hi, welcome to Hangman. If you ever want to leave, type 'stop' into the prompt.")
    print()
    
    while numFails < 8:
        print('- Round:', roundNum)
        print('Word:', getGuessedWord(secretWord, lettersGuessed))
        print('Your guessed letters:', getAvailableLetters(lettersGuessed))
        print('Number of mistakes left:', (8-numFails))
        
        letter = input('Guess a letter: ').lower()
        # assuming the user only puts in letters, and not numbers, etc.
        if letter == 'stop':
            print('Okay, see ya then.')
            return 
            # blank return to end program
        else:
            if letter in lettersGuessed:
                print('You already guessed that! Try again.')
                
            else:
                lettersGuessed += letter
                if letter in secretWord:
                    print('Nice! You got a letter!')
                    
                    
                    if isWordGuessed(secretWord, lettersGuessed):
                        print("You won!")
                        print("Word:", secretWord)
                        print("Your guessed letters:", getAvailableLetters(lettersGuessed))
                        return # ends the program
                    
                else:
                    print('Yikes. You guessed wrong...')
                    
                    numFails += 1
        roundNum += 1
        print() # newline
            
    print("Welp, looks like you lost the game.")
    print("Word:", secretWord)
    print("Your guessed letters:", getAvailableLetters(lettersGuessed))
    
 
            
        
        
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
