"""

Rad-Rib
By Charles Vazquez
A Mad-lib-like program for a school project."""

# imports

import time,os,sys
from time import sleep



# Operation

#-- Preference Add-ons

  

#-- Q.O.L. Add-on -+ Defines a function to clear the screen
def clr():
   os.system('cls')


#CLEAR SCREEN ONCE EXECUTED
clr()

# Get user initial input

#-- Asks user if they would like to start the story
user_start = str.lower(input("Would you like to start the story? (y/n): "))




# User start user_option

#-- Determines if user starts program. Continues on yes, exits on no
if user_start == "y":
    clr()
elif user_start == "n":
    print("Until next time!")
    sleep(3)
    clr()
    exit()

sleep(3)





# Welcome and greet user

#-- Initial greeting and introduction
print("Welcome to the interactive Mad-Lib like story!")
sleep(3)
print("\nYou will be able to change how the story goes and receive different outcomes!")
sleep(4)



# Get user story input

animal = input("Enter an animal: ")
object = input("Enter an object: ")
adjective = input("Enter the first adjective: ")
place = input("Enter a place: ")
adjective2 = input("Enter a second adjective: ")
adjective3 = input("Enter a third adjective: ")
object2 = input("Enter another object: ")
place2 = input("Enter a second place:")

story = f'Once upon a time, there was a(n) {animal} who was very {adjective}. The {animal} was approached by a moving {object}. ``How do you do {animal}?`` the {object} said.'
story2 = f'``Well, I am very {adjective} at the moment.`` said the {animal}. ``If you are feeling like it, would you like to go to {place} later this evening?`` queried the {object}. ``I would be {adjective2} to.`` said the {animal}.'
story3 = f'``Well to be honest, we are going anyways no matter how you feel. So lets go!`` exclaimed the {object}. {animal} has never been to {place} before. It is a new experience and the {animal} is very {adjective3}.'
story4 = f'The {object} was taken aback after stumbling into a {object2}. ``I havent seen you in forever, {object}!`` exclaimed {object2}. ``Me neither! The last time I saw you was at {place2}!`` said {object}.'
story5 = f'``Do you think we should take your friend there?`` questioned {object2}. ``I think thats a great idea!`` the {animal} and {object} histerically said. They then went on to visit {place2}'



# Display results

print(story)
print(story2)
print(story3)
print(story4)
print(story5)
print("The program will close in one minute.")
sleep(60)
clr()

# Thank user and quit program

print("Thank you for interacting with the Rad-Rib [mad-lib] type program!")
sleep(7)
clr()
