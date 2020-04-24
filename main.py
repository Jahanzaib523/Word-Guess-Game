from os import system, name
from time import sleep
from draw import *

# clear screen


def clear():
    system('cls')

# find letter in word


def existance(letter, word):
    return word.find(letter)

# update asterik string if correct guess


def setguess(letter, word, guess):
    count = 0
    index = word.find(letter)
    while index >= 0:
        count += 1
        guess = guess[:index] + word[index] + guess[index + 1:]
        word = word[:index] + '*' + word[index + 1:]
        index = word.find(letter)
    return count, guess

# find if all asterik are found
#word is guessed


def checkwin(guess):
    return guess.find("*")


# steps perform by player one
def move_pl1():
    print("Player one's turn")
    word = input('Enter word ')
    clear()
    guess = "*" * len(word)
    print(guess)
    return word, guess

# steps perform by player two


def move_pl2():
    print("Player two's turn")
    letter = input('Enter letter ')
    clear()
    return letter


if __name__ == "__main__":
    # initialize variables
    word, guess = move_pl1()
    ls_wrong = []
    tries = 8
    message = ""

    # initialize board
    init()
    design(guess, tries, message, ls_wrong)

    # repeats until number of tries
    while tries:
        message = ""
        letter = move_pl2()

        # initial checks to ensure length is one
        if(len(letter) > 1 or len(letter) < 1):
            print("Guess letter must be one \n try again")
            message = "Guess letter must be one \n !!! try again!!!"
        else:
            exists = existance(letter, word)
            # if letter doesn't exist in word
            if exists < 0:
                tries -= 1
                print("You guessed wrong ")
                print("Remaining tries ", tries)
                message = "You guessed wrong "
                ls_wrong.append(letter)
            # if letter exists in word
            else:
                temp, t_guess = setguess(letter, word, guess)
                # checks for previously entered letter
                if(temp > 0 and t_guess == guess):
                    tries -= 1
                    print("already Searched")
                    print("You guessed wrong ")
                    print("Remaining tries ", tries)
                    message = "Already Searched"
                else:
                    guess = t_guess
                    print(guess)
                    # checks if player wins
                    if checkwin(guess) < 0:
                        print("you won")
                        message = "!!!!Y O U   W O N!!!"
                        design(guess, tries, message, ls_wrong)
                        break
        design(guess, tries, message, ls_wrong)

    # message if player loose
    if tries == 0:
        print("You lose")
        message = "!!! Y O U   L O O S E !!!!"
        design(guess, tries, message, ls_wrong)

    getscreen()._root.mainloop()
