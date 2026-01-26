## Exercise 4

#1. create a filed named `zodiac.py` in this folder.
#2. Write a program to find out the Chinese Zodiac sign for a given year. The Chinese Zodiac is based on a 12-year cycle, with each year represented by an animal— monkey, rooster, dog, pig, rat, ox, tiger, rabbit, dragon, snake, horse, or sheep —in this cycle. Note year % 12 determines the Zodiac sign. 1900 is the year of the rat because 1900 % 12 is 4. Here are some sample runs:
#```
#Enter a year: 1900
#rat
#```
#```
#Enter a year: 1887
#pig
#```

year= int(input("Enter a year:"))
zodiac= (year - 1900) % 12

match zodiac:
    case 0:
        print("Rat")
    case 1:
        print("Ox")
    case 2:
        print("Tiger")
    case 3:
        print("Rabbit")
    case 4:
        print("Dragon")
    case 5:
        print("Snake")
    case 6:
        print("Horse")
    case 7:
        print("Sheep")
    case 8:
        print("Monkey")
    case 9:
        print("Rooster")
    case 10:
        print("Dog")
    case 11:
        print("Pig")
    case _:
        print("ERROR")
 
