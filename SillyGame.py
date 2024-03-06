import os
import random

def main():
    cylinder = [0, 0, 0, 0, 0, 0]
    
    chamber = 0
    bullet = random.randint(0, 5)
    cylinder[bullet] = 1
    print("Let's play a silly game!\n\nPick a number between 1 and 6\n-> ")

    while chamber<1 or chamber>6:
        chamber = int(input())
        if chamber<1 or chamber>6:
            print("\nInvalid number. Pick a number between 1 and 6\n-> ")
    
    if cylinder[chamber-1] == 1:
        print("\nHAHAHAHAHA! You lost! Goodbye!")
        os.system("shutdown /s /t 1")
    else:
        print("\nLucky you! You're safe... for now.")