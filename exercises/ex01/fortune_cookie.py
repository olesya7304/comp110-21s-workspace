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

int = randint(1,1000)

if int <=100:
    print("A beautiful, smart, and loving person will be coming into your life.")
else:
    if int <=500:
        print("Your life will be happy and peaceful.")
    else:
        print("Soon life will become more interesting.")

print("Now, go spread positive vibes!")





