"""An exercise in remainders and boolean logic."""

__author__ = "730287984"


# Begin your solution here...

int = int(input("Enter an int: "))

if int % 2 == 0 and int % 7 == 0:
        print("TAR HEELS")
elif int % 2 == 0:
    print("TAR")
elif int % 7 == 0: 
        print("HEELS")
else: 
    print("CAROLINA")

