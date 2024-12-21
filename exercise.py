# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

import string
lowercase_alphabet = string.ascii_lowercase 

def check_letter():
    letter = input('Please enter a letter: a-z or A-Z ')
    lower_case_letter = letter.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']

    if not(lower_case_letter in lowercase_alphabet):
        print("not alphabetical entry, please try again")
    
    if lower_case_letter in vowels:
        print(f"The letter {lower_case_letter} is a vowel")
    else:
        print(f"The letter {lower_case_letter} is a consonant")

    
# Call the function
#check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    voting_age = 18
    user_age = int(input("Please enter your age: "))
    
    if user_age < 0:
        print(f'{user_age} is an Invalid value, Please enter a positive number')
        return
    
    if user_age < voting_age:
        print("You are Unable to vote")
    else:
        print("You are able to vote")


# Call the function
#check_voting_eligibility()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dogs_age = int(input("Input a dog's age: "))
    dogs_years = 0
    if dogs_age <= 2:
        dogs_years = dogs_age * 10
        print(f"The Dog's age in dog years in {dogs_years}")
        return
    

    dogs_years = 20 + (dogs_age -2)*7
    print(f"The Dog's age in dog years in {dogs_years}")



# Call the function
#calculate_dog_years()


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    is_it_cold = input("Is it cold? Please enter yes/no ")
    is_it_raining = input("Is it raining? Please enter yes/no ")
    is_it_cold = True if is_it_cold  in ["yes", "YES", "Yes"] else False
    is_it_raining = True if is_it_raining in ["yes", "YES", "Yes"] else False
    
    if is_it_cold and is_it_raining:
        print("Wear a waterproof coat.")
    elif is_it_cold and not is_it_raining:
        print("Wear a warm coat.")
    elif is_it_raining and not is_it_cold:
        print("Carry an umbrella")
    elif not is_it_cold and not is_it_raining:
        print("Wear Light clothing")
    
# Call the function
weather_advice()

