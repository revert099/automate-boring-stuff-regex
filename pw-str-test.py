"""
    Password Strength detector
    A strong password has several rules:
        It must be at least 8 characters long
        It must contain both uppercase and lowercase letters
        It must contain at least one digit
        It must contain at least one special character from the set: @#$%^&+=
    Author: Jacob Winsor
"""
import re

password = input("Enter a string to test its strength: ")

pw_regex = re.compile(r'^(?=.{8,})(?=.[^\w\s]).*$')

if pw_regex.match(password):
    print("Strong password")
else:
    print("Weak password")


