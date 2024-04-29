"""

Rad-Rib
By Charles Vazquez
A Mad-lib-like program for a school project."""

# imports

import time,os,sys
from time import sleep

# Operation

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value

def clr():
   os.system('cls')

# Get user initial input

user_start = str.lower(input("Would you like to start the program? (y/n): "))

# User start option


if user_start == "y":
    clr()
elif user_start == "n":
    print("Until next time!")
    sleep(3)
    clr()
    exit()

sleep(3)


# Welcome and greet user

typingPrint("Welcome to the interactive Mad-Lib like story!")
sleep(0.3)
typingPrint(" You will be able to change how the story goes and receive different outcomes!")

# Get user secondary input



# Build story



# Display results



# Thank user and quit program


