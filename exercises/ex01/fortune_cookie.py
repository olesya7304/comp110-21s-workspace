"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730287984"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says...")

number: int = randint(1,1000)

if number <300:
    if number <100:
        print("A dubious friend may be an enemy in camouflage.")
    else: 
        print("A friend asks only for your time not your money.")
else:
    if number <=800:
        print("Your life will be happy and peaceful.")
    else:
        print("A fresh start will put you on your way.")


print("Now, go spread positive vibes!")





