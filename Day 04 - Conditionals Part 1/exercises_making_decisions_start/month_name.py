## Exercise 5
#1. create a file named `month_name.py` in this folder.
#2. Write a program that will take a month number from the user and print the name of the month. If the user enters a number that is out of the range 1 to 12, the program should print an error message. Do this using a `match` statement. Here are some sample runs.
#```
#$ python month_name.py
#Enter a month number (1-12): 1
#Month is:
#January
#```
#```
#$ python month_name.py
#Enter a month number (1-12): 4
#Month is:
##April
#```
#4. (optional) test your project by running the following command `python test_do_not_touch/test_month_name.py`

month= int(input("Enter a month number (1-12): "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else: 
    print("ERROR")