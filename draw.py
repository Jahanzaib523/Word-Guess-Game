from turtle import *
import random

# initializing board


def init():
    speed('fastest')
    title("Guess The Word")
    bgcolor("yellow")
    hideturtle()

# prints string on board


def printstr(string, x, y, font):
    penup()
    goto(x, y)
    write(string, move=False, align="left", font=font)
    pendown()

# set locations of word to be guessed


def print_stars(guess):
    printstr("Guess The Word: ", -290, 250, ("Arial", 16, "bold"))
    printstr(guess, -290, 220, ("Arial", 12, "normal"))


# set location of remaining tries
def print_tries(tries):
    printstr("Tries: ", 200, 250, ("Arial", 16, "bold"))
    printstr(str(tries), 260, 253, ("Arial", 12, "normal"))


# set Win/Loss messages
def print_message(message):
    printstr(message, -140, 150, ("Arial", 20, "bold"))


# Shows list of wrong tries
def print_wrong(ls_wrong):
    printstr("Wrong Guesses ", -290, -200, ("Arial", 16, "bold"))
    loc = -290
    for letter in ls_wrong:
        printstr(letter, loc, -220, ("Arial", 12, "normal"))
        loc += 20

# Draws ambulance


def ambulance(tries):
    showturtle()
    speed('fastest')
    if tries < 8:
        if(tries == 7):
            speed('slow')
        penup()
        color("magenta", "cyan")
        goto(-130, 50)
        pendown()
        begin_fill()
        for i in range(4):
            forward(150)
            right(90)
        end_fill()
    if tries < 7:
        if(tries == 6):
            speed('slow')
        penup()
        color("cyan", "magenta")
        goto(20, 0)
        pendown()
        begin_fill()
        for i in range(4):
            forward(100)
            right(90)
        end_fill()
    if tries < 6:
        if(tries == 5):
            speed('slow')
        penup()
        color("black")
        goto(60, -120)
        pendown()
        begin_fill()
        circle(25)
        end_fill()
    if tries < 5:
        if(tries == 4):
            speed('slow')
        penup()
        color("black")
        goto(-80, -120)
        pendown()
        begin_fill()
        circle(25)
        end_fill()
    if tries < 4:
        if(tries == 3):
            speed('slow')
        penup()
        color("cyan", "white")
        goto(50, -10)
        pendown()
        begin_fill()
        for i in range(4):
            if(i % 2 == 0):
                forward(50)
                right(90)
            else:
                forward(20)
                right(90)
        end_fill()
    if tries < 3:
        if(tries == 2):
            speed('slow')
        penup()
        goto(-80, 70)
        pendown()
        color("red", "blue")
        begin_fill()
        for i in range(4):
            forward(20)
            right(90)
        end_fill()
        penup()
        goto(-75, 65)
        pendown()
        color("blue", "red")
        begin_fill()
        for i in range(4):
            forward(10)
            right(90)
        end_fill()
    if tries < 2:
        if(tries == 1):
            speed('slow')
        penup()
        color("red")
        goto(-80, 0)
        pendown()
        begin_fill()
        for i in range(4):
            if(i % 2 == 0):
                forward(50)
                right(90)
            else:
                forward(20)
                right(90)
        end_fill()
    if tries < 1:
        if(tries == 0):
            speed('slow')
        penup()
        color("red")
        goto(-65, 15)
        pendown()
        begin_fill()
        for i in range(4):
            if(i % 2 == 1):
                forward(50)
                right(90)
            else:
                forward(20)
                right(90)
        end_fill()
    speed('fastest')
    color("black")
    hideturtle()

# call all above methods


def design(guess, tries, message, ls_wrong):
    clear()
    print_tries(tries)
    print_wrong(ls_wrong)
    print_message(message)
    print_stars(guess)
    ambulance(tries)
