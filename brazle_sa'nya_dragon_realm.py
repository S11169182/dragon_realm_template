# <Dragon Realm>, <Brazle Sa’nya>, <12/10/20> <11:50>, <Version 0.6>

import random # Import the library for random numbers. 
import time # Import the library for time.

# Create our first function to display an intro.
# The intro will be a multi-line comment.
def display_intro():
    print(""" Hello Adventurers! Hello Adventurer. You will need to fight against the Dragons in the relays. Please do your best and be careful. The task will carry on and will get deeply challenging. \n""")

def choose_cave():
    cave = "" # Declare a variable named cave initialize it to an EMPTY STRING.
    while cave != "1" and cave != "2":  # (!= means NOT equal. And is a Boolean keyword. The other Boolean keywords are OR and Not)Create a while loop that will as long as cave is NOT equal to 1 and 2.
        cave = input("Which Cave do you want to explore? Choose 1 or 2.\n") # Use input() to allow the player to choose between cave 1 or 2.

    return cave # Return the cave variable.

def check_cave (chosen_cave) : # Define a function named check_cave that takes chosen_cave as an argument.
    print("Traveling past the hills, approaching the caves of the dangerous mountains.\n") #print() a string that describes approaching the cave.
    time.sleep (3) # Sleep for 2-3 seconds.
    print("The cave is dark and deep with a big hole as the door ")# print() a string that describes being just outside the cave.
    time.sleep (3)
    print("You made it to the two paths, being tired because of fitting all does monster you decided to rest before rushing into one of the caves.\n")
    time.sleep (3) # Sleep for 2-3 seconds.
    print("You have choosen your cave, and wondered deep inside it. While walking you can feel the presence of something strong up ahead. Moving towards this trembling feeling, You finally see one of the dragons told in the legend!\n") # print() a string that describes seeing the dragon.
    time.sleep (3) # Sleep for 2-3 seconds.
    print(" \n") # print() a string that describes the dragon noticing / seeing you.
    time.sleep (3) # Sleep for 2-3 seconds.



   friendly_cave = random.radint(1, 2) # Declare a variable called friendly_cave and randomly assign it a value of 1 or 2.


    if chosen_cave == str (friendly_cave) # Check if the chosen_cave IS EQUAL to the friendly_cave.  Make sure to convert friendly_cave into a str().
       print ("# Hello there, I can help you!\n".
   else # Else, the player the chose the bad cave. 
       print ("# Hahaha you thought I could help you? This was my trap to finally eat you!\n". 


# Define a variable called play_again, assign it a string value of "yes".


# Create a while loop to play until the player inputs "no" or "n" when asked.
    # Call the function to display the intro.
    # Declare cave_number and assign the value of the choose_cave function.
    # Call the check_cave function by passing it the cave_number argument.


    # Use input() to determine if the player wants to play again.  


# Version Numbers
# v0.0 is all of the program information.
# v0.1 will import the two required libraries.
# v0.2 completes the function to display the intro. 
# v0.3 completes the function to choose a cave.
# v0.4 completes the completes the print statements for the check_cave function.
# v0.5 declares and assigns the friendly_cave variable.
# v0.6 completes the check for friendly vs. non-friendly dragon in check_cave.
# v0.7 declares the variable to play again, and assigns its value. 
# v0.8 creates the while loop and the first three statements of the loop.
# v0.9 checks to see if the player wants to play again or quit.
# v1.0 is the finish version that exectures correctly with no errors or bugs.
