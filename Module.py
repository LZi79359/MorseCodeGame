#makes the score global therefore it can be used in different functions throught this file
import os
scriptDir = os.path.dirname(os.path.abspath(__file__))
global score
score = 0
def letterChecker(string):
    """Takes a string,
       Uses .isalpha() to check if the string only has letters, if not user is prompted
       to enter a new string, and function is called again to do the same thing
       returns the string once it only contains letters"""
    #checks string, and returns true if it contains only alophabetical letters
    letterCheck = string.isalpha()
    previousLetter = ''
    consecutiveCount = 1
    #if string only contains letters:
    if letterCheck is True:
        #gives back the same string
        string = string.lower()
    #if string contains other characters:
    else:
        #user is prompted to give another input
        string = input("Input must be a letter, please try again:\n").lower()
        #uses the same fucntion to check that the given input is only letters
        return letterChecker(string)
    #itirates through every letter in the given string
    for letter in string:
        #compares the previous letter with the current letter
        if letter == previousLetter:
            #if the previous letter is the same as the previous one 1 is added to the consecutive count
            consecutiveCount += 1
            if consecutiveCount > 2:
                #if the consecutive count skips 2 the user prompted to give another input
                print("A letter has been repeated more than twice, make sure to spell words properly")
                string = input("Please try again:\n")
                return letterChecker(string)
        else:
            #if the previous letter does not match the previouse letter the consecutive count is reset and the previousLetter is sett to the current letter
            consecutiveCount = 1
            previousLetter = letter
    #returns the string
    return string
    
def displayTitle(titleFilePath):
    """Uses a filepath as a parameter
       Opens the file in the filepath, reads it, strips it and prints it to the user"""
    #handles exeptions for the file not being found and an Input/Output error.
    try:
        #opens a text file based on the file path given when the funcion is called.
        titleFile = open(titleFilePath, "r")
        #reads the text file and strips it, printing the result.
        print (titleFile.read().strip())
        #closes the file
        titleFile.close()
    #excepts when a file is not found and prints some text
    except FileNotFoundError:
        print("File could not be found....Exiting application")
    #excepts when there is an I/O error and prints some text
    except IOError:
        print("An I/O Error Occured....Exiting application")
    
def displayMenu():
    """Displays a main menu for the game and requests an input from the user, returning the
       input to be used in the main game"""
    #printing the options to the user:
    print("Please enter the letter indicated next to a prompt to continue to said prompt:")
    print("H. View High Scores")
    print("G. Start playing the game")
    print("A. Add words to text file")
    print("Q. Quit game")
    #waiting for user input
    userinput = input().lower()
    userinput = letterChecker(userinput)
    #returning user input
    return userinput

def generateRandomWord(wordsFilePath):
    """Takes a filepath as a parameter.
       Opens the text file and splits it into strings, which are then chosen at random
       The random word is returned"""
    #importing random
    import random
    #handles exeptions for the file not being found and an Input/Output error.
    try:
        #opening text file
        wordlist = open(wordsFilePath, "r")
        #reads the text file and splits the words into a list
        randomWord = wordlist.read().split()
        #chooses a random word from list and returns it
        return random.choice(randomWord)
        #closes text file
        wordlist.close()
    #excepts when a file is not found and uses an array of backup words instead
    except FileNotFoundError:
        backupWords = ["lazy", "disorder","am", "torch", "marble", "bay", "junior", "girl", "spite", "intermediate", "economic", "tension", "satisfied", "hesitate"]
        print("File not found.\nBackup words will be used instead.\n")
        return random.choice(backupWords)
    #excepts when there is an I/O error and prints some text
    except IOError:
        print("Unable to open file due to I/O Error...Exiting appliaction.")

def morsecodeconvertor(word):
    """Takes a string as a parameter,A
       Goes through each letter of the given string and converts it
       into morse code through the given dictionary returnes the string
       of morse code"""
    #a list of morse code cahracters
    morseDict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
        'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
        'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
        'y': '-.--', 'z': '--..'
                }
    morseCode = ''
    #goes through every character and converts it to morse code
    for char in word.lower():
        if char in morseDict:
            #puts a '|' in between every character
            morseCode += morseDict[char] + '|'
    return morseCode
        
def loadGameUIImages(filepath):
    """Takes a filepath as a parameter,
       Opens the text file, and splits it by newline characters
       Returns the list of the split text file"""
    #Handles exeptions for the file not being found and an Input/Output error.
    try:
        #opening text file
        textArt = open(filepath, "r")
        #reading the text file, and splitng the text file by blank lines
        splitTextArt = textArt.read().split("\n\n")
        return splitTextArt
        #closes text file
        textArt.close()
    #excepts when a file is not found and prints an error message
    except FileNotFoundError:
        print("File not found....Exiting Application")
    #excepts when there is an I/O error and prints some text
    except IOError:
        print("Unable to open file due to I/O Error...Exiting Application")

def updateUI(textArtlist, listindex):
    """Takes a list and a number as parameters,
       Takes the given list and prints the text tied to the index given"""
    print(textArtlist[listindex])

def menuChoiceG(randomWord):
    """Takes a string as a parameter,
       opens the text file with the morse code cypher and prints it's contents
       takes the given string and converts it into morse code with the
       morsecodeconvertor, and waits for an input the given input is then returned"""
    try:        
        #opens and read the text file with the cypher
        userCypher = open(os.path.join(scriptDir, "UserCypher.txt"))
        print(userCypher.read())
        userCypher.close()
        #converts the given word and prints it as morse code
        print(morsecodeconvertor(randomWord))
        userAns = input()
        userAns = letterChecker(userAns)
        return userAns.lower()
    #excepts when a file is not found and prints an error message
    except FileNotFoundError:
        print("Cypher file not found....please retry")
    #excepts when there is an I/O error and prints some text
    except IOError:
        print("Unable to open Cypher file due to I/O Error....please retry")
        
def nextTurn(randomWord, ansset, userAns):
    """Takes 2 strings and a set,
       checks if a string is in a set, while not in set:
           it checks if the strings match:
               it adds one to next turn count and adds 1 to the global score and prints correct
           if no:
               sets next next turn count to 2 and prints wrong along with the actual word
       while in set:
            the user is prompted to input a new string which is then checked by the letter checker
       returns the next turn count"""
    nextTurnCount = 0
    while userAns not in ansset:
            #if the inputs match the game repeats
            if randomWord == userAns:
                nextTurnCount = 1
                global score
                score += 1
                print ("correct\n")
                
            #if the inputs don't match the game stops and tells the user they made a mistake
            else:
                nextTurnCount = 2
                print("wrong")
                print(randomWord)
            break
    #while user ans is in ans set the user is prompted for another input which is then checked
    while userAns in ansset:
        userAns = input("That answer has already been given please try again:\n")
        userAns = letterChecker(userAns)
        break        
    return nextTurnCount

def highScoreFileChecker(name, score, filepath):
    """takes a string an integer and a filepath
       opens the given file, reads it and splis it, checking if
       the given string appeares in the file"""
    #Handles exeptions for the file not being found and an Input/Output error.
    try:
        #Opens a file in read mode
        highScoreFile = open(filepath, "r")
        
        #Reads the file and splits it into an array of different entries
        highScoreFileSplit = highScoreFile.read().split()
        #Takes user input and converts it to upper case

        #checks if the "name" is in the text file
        if name in highScoreFileSplit:
            #if "name" is in the text file it shows the user that the entry already exists and displays the entry
            print("Welcome back", name, "your high score is:", score)     
        else:
            print("Welcome", name)
    #excepts when a file is not found and prints an error message
    except FileNotFoundError:
        print("File not found...Exiting Application")
    #excepts when there is an I/O error and prints an error message
    except IOError:
        print("Unable to open file due to I/O Error...Exiting Application")

def updateHighScores (newplayer, newscore, filepath):
    """Takes a string an integer and a filepath
       Opens a text file, and iterates through every line and splits the text
       in the text file, and splits them by ':' and splits every line into player
       and score with which a dictionary is created if the newplayer string is
       already in the dictionary the score is changed to new score if the new
       score is larger if the newplaer string is not in the dictionary both the
       new player and the score are added to the dictionary which then gets
       written in the given file"""
    #read existing scores from the file into a dictionary
    scores = {}
    HighScoreFile = open(filepath, 'r')
    #go through each line in the file
    for line in HighScoreFile:
        #split the line into player and score using ':'
        player, score = line.strip().split(': ')
        #store the player and score in the dictionary
        scores[player] = int(score)
    #checks the if the new player is in the scores dictionary
    if newplayer in scores:
        #checks if the newscore is larger than the old score of the player
        if newscore > scores[player]:
            #if the newscore is larger the score for that player gets updated in the dictionary
            scores[player] = newscore
    else:
        #if newplayer is not in scores dictionary the newplayer is added
        scores[newplayer] = newscore
    #the file is opened in write 
    HighScoreUpdate = open(filepath, 'w')
    #Every entry in the dictionary is written in the text file
    for player, score in scores.items():
        HighScoreUpdate.write(f"{player}: {score}\n")
    
def highScoreTable (filepath):
    """takes a filepath as a parameter
       Opens a text file, and iterates through every line and splits the text
       in the text file, and splits them by ':' and splits every line into player
       and score with which a dictionary is created the dictionary is sorted based
       on the largest score and the first 10 are printed"""
    #read existing scores from the file into a dictionary
    scores = {}
    scoreFile = open(filepath, 'r')
    for line in scoreFile:
        player, score = line.strip().split(': ')
        scores[player] = int(score)
    #lambda allows the items in the dictionary to be stored based on the score, and reverse = true places it all in decending order
    sortedScores = sorted(scores.items(), key = lambda item: item[1], reverse = True)
    #prints the highest 10 scores in the sorted dictionary
    highScoreTable = sortedScores[:10]
    for player, score in highScoreTable:
        print(player, ": ", score)

def addWords(filepath):
    """takes a filepath as a parameter
       opens the file in readmode and splits it
       asks user for a new string and checks if that string is in the list of words
       taken from the file, and then either adds it or prints that its already in the file"""
    #Handles exeptions for the file not being found and an Input/Output error.
    try:
        #opens text file in read mode
        wordDictR = open(filepath, "r")
        #splits text file into a list
        WordDictRSplit = wordDictR.read().split()
        #closes text file
        wordDictR.close()
        #accepts user input and makes all characters lower case
        newWord = input("Enter the new word: ").lower()
        newWord = letterChecker(newWord)
        #checks if newWord is in the text file, if not:
        if newWord not in WordDictRSplit:
            #opens file in append mode to add words at end of document
            wordDictA = open(filepath, "a")
            #writes the word previously entred in the text file
            wordDictA.write(newWord)
            #closes file
            wordDictA.close()
            print(newWord, "has been added")
        #if newWord already is already there:
        else:
            print(newWord, "is already in the text file")
    #excepts when a file is not found and prints an error message
    except FileNotFoundError:
        print("Words File not found")
    #excepts when there is an I/O Error and prints an error message
    except IOError:
        print("Unable to open a file due to I/O Error")


