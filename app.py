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



# Get user secondary input

#-- User will decide if the story
user_option = str.lower(input("\nFirst, choose the story of 'The Serpent and the Tree', or 'The Raccoon and the Tree'. (serpent/raccoon): "))

# Build story - Option 1

if user_option == "serpent":
   clr()
   sleep(1.5)
   print("\nThe serpent was very exhausted slithering all day and decides to rest next to a tree.")
   sleep(1)


tree_op1 = str.lower(input("\nThe tree notices this. Should he inquiry the snake? (y/n): "))


sleep(2)

if tree_op1 == "y":
   print("\n'Why are you so tired, little one?' The tree says to the serpent.")
   sleep(2)
   print("\n'I'm tired of moving all the time, I wish I was like you so all I could do is wait', the serpent complains.")
   



# Display results






# Thank user and quit program


