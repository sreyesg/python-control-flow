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
check_voting_eligibility()
