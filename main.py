# Import shuffle from random dictionary
from random import shuffle

# Create Shuffle List Function
def shuffle_list(mylist):
    shuffle(mylist)

    #Return
    return mylist

# Create Player Guess Function
def player_guess():
    #Placeholder
    guess = " "

    while guess not in ["0", "1", "2"]:
        guess = input("Guess a number: 0, 1 or 2: ")

    # Return
    return int(guess)

# Create Check Guess Function
def check_guess(mylist, guess):
    if mylist[guess] == "O":
        print("Correct")
    else:
        print("Wrong guess!")
        print(mylist)

# INITIAL LIST
mylist = [" ", " ", "O"]

# SHUFFLE LIST
mixed_list = shuffle_list(mylist)

# USER GUESS
guess = player_guess()

# CHECK GUESS
check_guess(mixed_list, guess)