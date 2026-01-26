## Exercise 6
#1. Create  file named `package_selector.py` in this folder.
#2. Write a program for a gym so that it can determine which membership package a person should purchase. There are three packages:
#    - Package A: $40/month, 4 months
#    - Package B: $55/month, 8 months
#    - Package C: $75/month, 12 months
#    - Package D: $100/month, 12 month
#Note: ensure you have the words "You have selected Package A" or which ever package you select

print("Welcome to the Ultimate Gym")
print("""
    Please select a membership package:
    - Package A: $40/month, 4 months (short-term package)
    - Package B: $55/month, 8 months (standard package)
    - Package C: $75/month, 12 months (regular package)
    - Package D: $100/month, 12 month (premium package, includes 4 free personal training sessions)
""")
print()

##Enter the package letter (A/B/C/D): A
#You have selected Package A
#Your monthly fee is $40
#Your total fee is $160
package_choice= input("Enter the package letter (A/B/C/D): ").upper()
match package_choice:
        case "A":
            permonth= 40 
            month = 4 
        case "B":
            permonth = 55
            month = 8
        case "C":
            permonth = 75
            month = 12
        case "D":
            permonth = 100
            month = 12
        case _:
            print("ERROR")

total_per_year= permonth * month
print(f"You have selected Package {package_choice}")
print(f"Your monthly fee is ${permonth}")
print(f"Your total fee is ${total_per_year}")
    
