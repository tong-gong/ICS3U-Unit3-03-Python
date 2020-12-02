#!/usr/bin/env python3

# Created by Tong Gong
# Created time November 2020
# This is a  "Number Guessing Game" program.

import constants
import random


def main():
    # This is the function to play the "Number Guessing Game" program.

    random_number = random.randint(1, 10)   # a number between 1 and 10

    # Input
    userinput = int(input("Enter the number you guess:"))
    print("")

    # Process & output
    if userinput == random_number:
        print("You guessed right")
    else:
        print("you are not right")


if __name__ == "__main__":
    main()
