#!/usr/bin/python3


# ex>0124> funcion is_leap > added text to input() 
# ------------------------------------------------

def is_leap(year):
    leap = False

    # enter code edit
    if year % 100 == 0:  # century year
        if year % 400 == 0:
            print('{} is leap year'.format(year))
        else:
            print('{} is not leap year'.format(year))
    else:
        if year % 4 == 0:
            print('{} is leap year'.format(year))
        else:
            print('{} is not leap year'.format(year))


year = int(input("Input year: "))
print(is_leap(year))
