#imports the function module
import Luke_Zammit_4_1A_Module
import os
#Get the directory of the current script
scriptDir = os.path.dirname(os.path.abspath(__file__))
#Displays the title from the specified file path
Luke_Zammit_4_1A_Module.displayTitle(os.path.join(scriptDir, "yourgamenameword.txt"))
#Initializes the display menu
displayMenu = ''
#Main loop for the game menu
while displayMenu != "q":
    #Loads the text art for the game UI
    splitTextArt = Luke_Zammit_4_1A_Module.loadGameUIImages(os.path.join(scriptDir, "TextArt.txt"))
    textArt = Luke_Zammit_4_1A_Module.updateUI(splitTextArt, 0)
    displayMenu = Luke_Zammit_4_1A_Module.displayMenu()
    #Continues of the user's choice
    if displayMenu == "h":#If user chooses to view high scores
        textArt = Luke_Zammit_4_1A_Module.updateUI(splitTextArt,1)
        Luke_Zammit_4_1A_Module.highScoreTable(os.path.join(scriptDir, "HighScores.txt"))
    
    elif displayMenu == "g":#iIf user chooses to play the game
        #Initilizes game variables and retrieves player's name
        nextTurnCount = 1
        usedRandomWords = set()
        userAnsList = set()
        player = input("Who is playing?\n")
        player = Luke_Zammit_4_1A_Module.letterChecker(player)
        Luke_Zammit_4_1A_Module.highScoreFileChecker(player,Luke_Zammit_4_1A_Module.score, os.path.join(scriptDir, "HighScores.txt"))

        #Main game loop
        while nextTurnCount == 1:#if the user gets the correct answer this loops again until it's wrong
            textArt = Luke_Zammit_4_1A_Module.updateUI(splitTextArt,2)
            print("Score: ",Luke_Zammit_4_1A_Module.score)
            #generate random word and checks if the game is in the usedRandomWords set
            randomWord = Luke_Zammit_4_1A_Module.generateRandomWord(os.path.join(scriptDir, "ListOfWords.txt"))
            while randomWord in usedRandomWords:
                #generates a new random word
                randomWord = Luke_Zammit_4_1A_Module.generateRandomWord(os.path.join(scriptDir, "ListOfWords.txt"))
            while randomWord not in usedRandomWords:
                #starts the game
                userAns = Luke_Zammit_4_1A_Module.menuChoiceG(randomWord)
                nextTurnCount = Luke_Zammit_4_1A_Module.nextTurn(randomWord, userAnsList, userAns)
                usedRandomWords.add(randomWord)
                userAnsList.add(userAns)
                
        while nextTurnCount == 2:#if the user gets the wrong answer the game over screen is shown along with the score, the high score is updated and the user is shown the main menu
            textArt = Luke_Zammit_4_1A_Module.updateUI(splitTextArt, 3)
            print("Your score is: ", Luke_Zammit_4_1A_Module.score)
            
            Luke_Zammit_4_1A_Module.updateHighScores(player, Luke_Zammit_4_1A_Module.score, os.path.join(scriptDir, "HighScores.txt"))
            Luke_Zammit_4_1A_Module.score = 0
            break

    elif displayMenu == "a":#if the user chooses to add words
        textArt = Luke_Zammit_4_1A_Module.updateUI(splitTextArt, 5)
        Luke_Zammit_4_1A_Module.addWords(os.path.join(scriptDir, "ListOfWords.txt"))

    elif displayMenu != "h" or "g" or "a" or "q":#if the user enters an invalid input
        splitTextArt = Luke_Zammit_4_1A_Module.loadGameUIImages(os.path.join(scriptDir, "TextArt.txt"))
        print("Invalid Input please try again")
        
while displayMenu == "q":#if the user decides to quit the program
    print("Exiting program. Thank you for playing!")
    break
