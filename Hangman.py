import random

words = ['Testing my code', 'This is hangman', 'Apple Pie', 'I like videogames', 'I like pizza', 'Playing games is fun', 'I am very happy today', 'This is a very long sentence', 'You will never guess this']

def makeTemplate():
    template = []
    for letters in word:
        if letters != ' ':
            template.append('_')
        else:
            template.append(' ')
    return template

def templateToString(template):
    stringTemplate = ''.join(template)
    return stringTemplate

def createSolution():
    solution = []
    for letters in word:
        solution.append(letters)
    return solution

def getGuessIndices(guess):
    indices = []
    for index in range(0, len(solution)):
        if solution[index] == guess:
            indices.append(index)
    return indices
    
def addGuessToIndices(guess):
    for index in getGuessIndices(guess):
        template[index] = guess
    return template

def checkGuess(guess):
    if guess in guesses:
        tryAgain = input(f'You already picked {guess}. Pick another letter: ').lower()
        checkGuess(tryAgain)
    elif len(guess) > 1:
        tryAgain = input(f'You guessed {guess} but you can only guess 1 letter. Pick another letter: ').lower()
        checkGuess(tryAgain)
    else:
        guesses.append(guess)
        if guess in solution and guess.upper() in solution:
            addGuessToIndices(guess.upper())
            addGuessToIndices(guess)
        elif guess in solution:
            addGuessToIndices(guess)
        elif guess.upper() in solution:
            addGuessToIndices(guess.upper())
        elif guess not in solution:
            wrongGuesses.append(guess)

guesses = []
wrongGuesses = []
word = random.choice(words)
template = makeTemplate()
solution =  createSolution()
correctSolution = ''.join(solution)
gameOver = False

print('Rules:')
print('    1: If you guess 8 incorrect letters you will lose')
print()
while gameOver == False:
    print(f'Guesses: {guesses}')
    print(f'Wrong guesses: {wrongGuesses}')
    print(templateToString(template))
    guess = input('Guess a letter: ')
    print()
    checkGuess(guess)
    if templateToString(template) == correctSolution:
        print('YOU WIN!')
        print(f'The correct answer was: {correctSolution}.')
        decision = input('Would you like to play again? y/n: ').lower()
        if decision == 'y':
            guesses = []
            wrongGuesses = []
            word = random.choice(words)
            template = makeTemplate()
            solution =  createSolution()
            correctSolution = ''.join(solution)
            gameOver = False
        else:
            gameOver = True
    elif len(wrongGuesses) == 8:
        gameOver = True
        correctSolution = ''.join(solution)
        print('YOU LOST!')
        print(f'The answer is: {correctSolution}')