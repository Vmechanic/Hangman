word = "This is hangman".lower()

wordIntoList = []
guesses = []
wrongGuesses = []
template = ""
gameOver = False

for x in word:
    if x == " ":
        template += " "
    else:
        template += "_"

template = list(template)

for x in word:
    wordIntoList.append(x)

def findLetter(list,guess):
    letterIndices = []
    for x in range(0, len(list)):
        if(list[x] == guess):
            letterIndices.append(x)
    return letterIndices

def notifyPlayer():
  print("Letters you guessed: )")
  print(guesses)
  print("\nLetters you guessed wrong: ")
  print(wrongGuesses)
  print("".join(template))
            
print("".join(template) + "\n")
print("There are " + str(len(word.replace(" ",""))) + " letters you have to guess (spaces excluded).\n")

while gameOver == False:
    guess = input("Guess a letter: ").lower()
    if guess in guesses:
        guess= input("You guessed this letter already. Pick another one: ")
    if len(guess) > 1:
        guess = input("You can't guess multiple letters try again: ")
    guesses.append(guess)
    if guess in word:
        for x in findLetter(wordIntoList, guess):
            template[x] = guess
        notifyPlayer()
    else:
        wrongGuesses.append(guess)
        notifyPlayer()
    if (len(wrongGuesses) == 8):
        gameOver = True
        print("You guessed 8 incorrect letters. You lost!")
    elif (word == "".join(template)):
        gameOver = True
        print("You win! You guessed all the correct letters!")
