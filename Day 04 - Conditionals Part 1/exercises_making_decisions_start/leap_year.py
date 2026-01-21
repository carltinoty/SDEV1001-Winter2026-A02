# Exercise 2
#1. create a file named `leap_year.py` in this folder.
#2. Write a program to determine if a user input year is a leap year. A year is a leap year if it is divisible by 4 but
#not by 100, or if it is divisible by 400. Here are some sample runs:
#```
#$ python leap_year.py
#Enter a year: 2008
#2008 is a leap year? true
#```
#```
#$ python leap_year.py
#Enter a year: 1900
#1900 is a leap year? false
#```
#3. (optional) test your project by running the following command `python test_do_not_touch/test_leap_year.py`

year= int(input("Enter a year: "))
leap_year= year % 4
if leap_year == 0:
    print(f"{year} is a leap year? True")
else:
    print(f"{year} is a leap year? False")


    