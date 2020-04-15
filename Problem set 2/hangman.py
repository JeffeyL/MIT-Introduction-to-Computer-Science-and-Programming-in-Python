# Problem Set 2, hangman.py
# Name: Jeffrey Luo

# Hangman Game
# -----------------------------------
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    #Unique letters in secret_word
    secret_list = []

    #Extract all unique characters from the secret
    temp_secret = list(secret_word)
    for i in range(len(temp_secret)):
        if temp_secret[i] in secret_list:
            pass
        else:
            secret_list.append(temp_secret[i])

    #Compare sorted lists
    if sorted(secret_list) == sorted(letters_guessed):
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    #Final returned guessed word
    guessed_word = []

    #Create guessed word
    secret_list = list(secret_word)
    for i in range(len(secret_list)):
        if secret_list[i] in letters_guessed:
            guessed_word.append(secret_list[i])
        else:
            guessed_word.append("_")

    return "".join(guessed_word)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = list(string.ascii_lowercase)

    for i in range(len(letters_guessed)):
        if letters_guessed[i] in alphabet:
            alphabet.remove(letters_guessed[i])

    return "".join(alphabet)



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    #Number of guesses remaining
    guesses = 6
    #Number of warnings remaining
    warnings = 3
    #Convert secret word to a list of characters
    secret = list(secret_word)
    #Guessed letters
    guessed_letters = []
    #Unique letters in secret
    unique_letters = []
    temp_secret = list(secret_word)
    for i in range(len(temp_secret)):
        if temp_secret[i] in unique_letters:
            pass
        else:
            unique_letters.append(temp_secret[i])

    print("Welcome to Hangman!")
    print("I am thinking of a word that is " + str(len(secret)) + " letters long")

    #For testing purposes (or cheating, if you're into that)
    #print("TESTING: " + secret_word)

    while guesses > 0 and warnings > 0:
        print("---------------")
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters: " + get_available_letters(guessed_letters))
        guess = str.lower(input("Please guess a letter: "))
        if guess in list(get_available_letters(guessed_letters)):
            guessed_letters.append(guess)
            if guess in secret:
                print("Good guess: " + get_guessed_word(secret_word, guessed_letters))
            else:
                print("Oops! That letter is not in my word: " + get_guessed_word(guessed_letters))
        elif guess in list(string.ascii_lowercase):
            warnings -= 1
            print("Oops! You've already guessed that letter. You have " + str(warnings) + " warnings left.")
        else:
            warnings -= 1
            print("Oops! You've entered an invalid input. You have " + str(warnings) + " warnings left.")

        #Check for win
        if(is_word_guessed(secret_word, guessed_letters) == True):
            break

    #Outcomes
    if (is_word_guessed(secret_word, guessed_letters) == True):
        print("Congratulations, you won!")
        print("Your total score for this game is: " + str(guesses*len(unique_letters)))
    elif guesses == 0:
        print("Sorry, you ran out of guesses. The word was: " + secret_word)
    elif warnings == 0:
        print("Sorry, you ran out of warnings. The word was: " + secret_word)

    pass

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    #Immediately return false if lengths don't match
    if len(my_word) != len(other_word):
        return False

    #Words put into lists for easy comparison
    my_list = list(my_word)
    other_list = list(other_word)

    #Compare each character, if the characters match or if the character in my_word is an underscore, then pass
    for i in range(len(my_list)):
        if my_list[i] == other_list[i]:
            pass
        elif my_list[i] == "_":
            pass
        else:
            return False

    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    #List of possible matches
    matches = []

    for i in range(len(wordlist)):
        if match_with_gaps(my_word, wordlist[i]) == True:
            matches.append(wordlist[i])

    #Only print if there are matches
    if len(matches) == 0:
        print("No matches found")
    else:
        print(" ".join(matches))



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    #Number of guesses remaining
    guesses = 6
    #Number of warnings remaining
    warnings = 3
    #Convert secret word to a list of characters
    secret = list(secret_word)
    #Guessed letters
    guessed_letters = []
    #Unique letters in secret
    unique_letters = []
    temp_secret = list(secret_word)
    for i in range(len(temp_secret)):
        if temp_secret[i] in unique_letters:
            pass
        else:
            unique_letters.append(temp_secret[i])

    print("Welcome to Hangman!")
    print("I am thinking of a word that is " + str(len(secret)) + " letters long")

    #For testing purposes (or cheating, if you're into that)
    #print("TESTING: " + secret_word)

    while guesses > 0 and warnings > 0:
        print("---------------")
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters: " + get_available_letters(guessed_letters))
        guess = str.lower(input("Please guess a letter: "))
        if guess in list(get_available_letters(guessed_letters)):
            guessed_letters.append(guess)
            if guess in secret:
                print("Good guess: " + get_guessed_word(secret_word, guessed_letters))
            else:
                print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, guessed_letters))
        elif guess == "*":
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, guessed_letters))
        elif guess in list(string.ascii_lowercase):
            warnings -= 1
            print("Oops! You've already guessed that letter. You have " + str(warnings) + " warnings left.")
        else:
            warnings -= 1
            print("Oops! You've entered an invalid input. You have " + str(warnings) + " warnings left.")

        #Check for win
        if(is_word_guessed(secret_word, guessed_letters) == True):
            break

    #Outcomes
    if (is_word_guessed(secret_word, guessed_letters) == True):
        print("Congratulations, you won!")
        print("Your total score for this game is: " + str(guesses*len(unique_letters)))
    elif guesses == 0:
        print("Sorry, you ran out of guesses. The word was: " + secret_word)
    elif warnings == 0:
        print("Sorry, you ran out of warnings. The word was: " + secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
