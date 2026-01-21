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

if zodiac == 0:
    print("Rat")
elif zodiac == 1:
    print("Ox")
elif zodiac == 2:
    print("Tiger")
elif zodiac == 3:
    print("Rabbit")
elif zodiac == 4:
    print("Dragon")
elif zodiac == 5:
    print("Snake")
elif zodiac == 6:
    print("Horse")
elif zodiac == 7:
    print("Sheep")
elif zodiac == 8:
    print("Monkey")
elif zodiac == 9:
    print("Rooster")
elif zodiac == 10:
    print("Dog")
elif zodiac == 11:
    print("Pig")
else:
    print("ERROR")