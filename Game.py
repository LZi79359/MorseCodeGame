#imports the function module
import Module
import os
#Get the directory of the current script
scriptDir = os.path.dirname(os.path.abspath(__file__))
#Displays the title from the specified file path
Module.displayTitle(os.path.join(scriptDir, "yourgamenameword.txt"))
#Initializes the display menu
displayMenu = ''
#Main loop for the game menu
while displayMenu != "q":
    #Loads the text art for the game UI
    splitTextArt = Module.loadGameUIImages(os.path.join(scriptDir, "TextArt.txt"))
    textArt = Module.updateUI(splitTextArt, 0)
    displayMenu = Module.displayMenu()
    #Continues of the user's choice
    if displayMenu == "h":#If user chooses to view high scores
        textArt = Module.updateUI(splitTextArt,1)
        Module.highScoreTable(os.path.join(scriptDir, "HighScores.txt"))
    
    elif displayMenu == "g":#iIf user chooses to play the game
        #Initilizes game variables and retrieves player's name
        nextTurnCount = 1
        usedRandomWords = set()
        userAnsList = set()
        player = input("Who is playing?\n")
        player = Module.letterChecker(player)
        Module.highScoreFileChecker(player,Module.score, os.path.join(scriptDir, "HighScores.txt"))

        #Main game loop
        while nextTurnCount == 1:#if the user gets the correct answer this loops again until it's wrong
            textArt = Module.updateUI(splitTextArt,2)
            print("Score: ",Module.score)
            #generate random word and checks if the game is in the usedRandomWords set
            randomWord = Module.generateRandomWord(os.path.join(scriptDir, "ListOfWords.txt"))
            while randomWord in usedRandomWords:
                #generates a new random word
                randomWord = Module.generateRandomWord(os.path.join(scriptDir, "ListOfWords.txt"))
            while randomWord not in usedRandomWords:
                #starts the game
                userAns = Module.menuChoiceG(randomWord)
                nextTurnCount = Module.nextTurn(randomWord, userAnsList, userAns)
                usedRandomWords.add(randomWord)
                userAnsList.add(userAns)
                
        while nextTurnCount == 2:#if the user gets the wrong answer the game over screen is shown along with the score, the high score is updated and the user is shown the main menu
            textArt = Module.updateUI(splitTextArt, 3)
            print("Your score is: ", Module.score)
            
            Module.updateHighScores(player, Module.score, os.path.join(scriptDir, "HighScores.txt"))
            Module.score = 0
            break

    elif displayMenu == "a":#if the user chooses to add words
        textArt = Module.updateUI(splitTextArt, 5)
        Module.addWords(os.path.join(scriptDir, "ListOfWords.txt"))

    elif displayMenu != "h" or "g" or "a" or "q":#if the user enters an invalid input
        splitTextArt = Module.loadGameUIImages(os.path.join(scriptDir, "TextArt.txt"))
        print("Invalid Input please try again")
        
while displayMenu == "q":#if the user decides to quit the program
    print("Exiting program. Thank you for playing!")
    break
