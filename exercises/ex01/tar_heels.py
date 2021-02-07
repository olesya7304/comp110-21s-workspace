"""An exercise in remainders and boolean logic."""

__author__ = "730287984"


# Begin your solution here...

number = int(input("Enter an int: "))

if number % 2 == 0 and number % 7 == 0:
        print("TAR HEELS")
elif number % 2 == 0:
    print("TAR")
elif number % 7 == 0: 
        print("HEELS")
else: 
    print("CAROLINA")

