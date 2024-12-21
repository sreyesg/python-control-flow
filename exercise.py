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
check_letter()
