## Exercise 3

#1. create a file named `rock_paper_scissors.py` in this folder.
#2. Write a program that plays the scissor-rock-paper game. (A scissor cuts paper, a rock can knock a scissor, and a paper can wrap a rock.) The program randomly generates a number 0, 1, or 2 representing scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or 2 and displays a message indicating whether the user or the computer wins, loses, or draws. Here are sample runs:
#- First, you winning
#```
#$ python rock_paper_scissors.py
#Scissor (0), rock (1), paper (2): 1
#The computer is scissor. You are rock. You win
#```
#- Second, you losing
#```
#$ python rock_paper_scissors.py
#Scissor (0), rock (1), paper (2): 2
#The computer is scissor. You are paper. You lose
#```
#- Third a tie
#```
#$ python rock_paper_scissors.py
#Scissor (0), rock (1), paper (2): 0
#The computer is scissor. You are scissor. It is a draw
#```
#Note: again you'll need to use the `random` module `random.randint(0, 2)` to generate a random number between 0 and 2
#3. (optional) test your project by running the following command `python test_do_not_touch/test_rock_paper_scissors.py`

import random
computer_pick= random.randint(0,2)
pick= int(input("Scissor (0), rock (1), paper (2): "))
if computer_pick == 0:
    computer_pick = "scissor"
elif computer_pick == 1:
    computer_pick = "rock"
else:
    computer_pick = "paper"

if pick == 0:
    pick = "scissor"
elif pick == 1:
    pick = "rock"
else:
    pick = "paper"

if pick == computer_pick:
    print(f"The computer is {computer_pick}. You are {pick}. It is a draw")
else:  
    if (pick == 0 and computer_pick == 2) or (pick == 1 and computer_pick == 0) or (pick == 2 and computer_pick == 1):
        print(f"The computer is {computer_pick}. You are {pick}. You win")