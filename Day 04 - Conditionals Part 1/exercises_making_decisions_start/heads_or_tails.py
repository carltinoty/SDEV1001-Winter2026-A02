## Exercise 1

#1. create a file named `heads_or_tails.py` in this folder.
#2. Write a program that lets the user guess whether the flip of a coin results in heads or tails. The program
#randomly generates an integer 0 to 1, which represents heads or tails. The program prompts the user to enter
#a guess and reports whether the guess is correct or incorrect.
#    - import the `random` module to generate a random numbers
 #   - use `random.randint(0, 1)` to generate a random number between 0 and 1
#1. The output should look like the following
# for a correct response
#```
#$ python heads_or_tails.py
#Guess the coin flip! Enter heads or tails (h/t): h
#The coin flip was: tails
#you guessed wrong!
#```
#- for an incorrect response
#```
#$ python heads_or_tails.py
#Guess the coin flip! Enter heads or tails (h/t): t
#The coin flip was: tails
#you guessed correct!
#```
#1. (optional) test your project by running the following command `python test_do_not_touch/test_heads_or_tails.py`

import random

heads_or_tails= random.randint(0,1)
user_choice= input("Guess the coin flip! Enter heads or tails (h/t): ")

if heads_or_tails == 0 and user_choice == "t" or heads_or_tails == 1 and user_choice == "h":
    print("You Guessed right!")
else:
    print("You guessed wrong!")

