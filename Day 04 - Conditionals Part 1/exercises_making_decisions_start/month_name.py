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

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("ERROR")
