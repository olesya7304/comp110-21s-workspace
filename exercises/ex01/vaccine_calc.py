"""A vaccination calculator."""

__author__ = "730287984"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

population: int = int(input("Population: "))
doses: int = int(input("Doses administered: "))
per_day: int = int(input("Doses per day: "))
target: int = int(input("Target percent vaccinated: "))

# target_doses:  target *  population * doses 
doses_needed: int = round((population * (target / 100)) * 2)
# days: (target_doses - administered_doses) / per_day 
day: int = round((doses_needed - doses) / 2)

day_falls: timedelta = timedelta(day)
today: datetime = datetime.today()
future: datetime = today + day_falls  

print("We will reach " + str(target) + "% vaccination in " + str(day) + " days, which falls on " + str(future.strftime("%B %d, %Y")) + ".")



