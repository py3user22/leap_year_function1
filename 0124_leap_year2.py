#!/usr/bin/python3


# ex>0124> funcion is_leap  using True/False output
# ------------------------------------------------

def is_leap(year):
    leap = False

    # Write your logic here
    if year % 100 == 0:  # century year
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False

year = int(input('Enter a year: '))
print(is_leap(year))
