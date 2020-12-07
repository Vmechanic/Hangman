import random

words = ["This is hangman", "Cool project", "Python is a snake", "Games are fun", "Testing code", "Basketball", "End of the list"]
isGameOver = False
isNewGame = True

#All these function names are exactly what it does basically self explanatory
def seperateWord():
    letterList = []
    for x in word:
        letterList.append(x)
    return letterList

def setUpTemplate():
    template = []
    for x in word:
        if x == " ":
            template.append(" ")
        else:
            template.append("_")
    return template

def getIndex(guess):
    indices = []
    for x in range(0,len(checkGuesses)):
        if checkGuesses[x] == guess:
            indices.append(x)
    return indices

def changeTemplate(indices,guess):
    for x in indices:
        template[x] = guess

def displayInformation(): 
    print(f"Guesses: \n {guesses}")   
    print(F"Wrong guesses: \n {wrongGuesses}")
    print("".join(template))

while isGameOver == False:
    if isNewGame == True:
        word = words[random.randrange(0,len(words)-1)].lower()
        checkGuesses = seperateWord()
        guesses = []
        wrongGuesses = []
        countWrongGuesses = 0
        template = setUpTemplate()
        isNewGame = False
    displayInformation()
    #step 1 ask player for guess
    guess = input("Guess a letter: ")
    #if the player's guess is guesses that means the player already guessed and should guess again
    if guess in guesses:
        guess = input("You already guessed this letter, pick another one: ")
    #if the player puts in more than 1 letter let the player guess again
    if len(guess) > 1:
        guess = input("Please guess one letter: ")
    #add to guesses list so the player knows what guesses he/she made
    guesses.append(guess)
    """
    if guess is in checkGuesses that means it is a correct guess
    get the index and use that index to change template such that it displays the guess in the correct slot
    else put the wrong guess into the wrongGuesses list and count it
    """
    if guess in checkGuesses:
        indices = getIndex(guess)
        changeTemplate(indices,guess)
    else:
        wrongGuesses.append(guess)
        countWrongGuesses += 1
    """if the player guessed wrong 0 times display information and print out you guessed 8 incorrect letters
        then ask if they want to play again
        else if the template is the same as the word then the player wins and ask if they want to play again
    """
    if (countWrongGuesses == 8):
        displayInformation()
        print("You guessed 8 incorrect letters. You lost!")
        response = input("Do you want to play again? Then type in yes or y. ")
        if response == "yes" or response == "y":
            isGameOver = False
            isNewGame = True
        else:
            isGameOver = True
    elif (word == "".join(template)):
        displayInformation()
        print("You win! You guessed all the correct letters!") 
        response = input("Do you want to play again? Then type in yes or y. ")
        if response == "yes" or response == "y":
            isGameOver = False
            isNewGame = True
        else:
            isGameOver = True
