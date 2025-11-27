"""
This script extracts email addresses and phone numbers from the clipboard.

Automate the boring stuff exercise. Designed to suit Australian phone number formats.
Author: Jacob Winsor
"""

import pyperclip
import re

# Regular expression for matching email addresses
email_regex = re.compile(r'''
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    \.[a-zA-Z]{2,4}
''', re.VERBOSE)

# Regular expression for matching phone numbers
phone_regex = re.compile(r'''
    (?:^|\t)                # optional tab (for csv)
    (?:\+?61|0)?            # country code or leading zero 
    (\d{3}\s?\d{3}\s?\d{3}) # main number
'''
, re.VERBOSE)

# Get text from clipboard
text = str(pyperclip.paste())

# Find all email addresses and phone numbers in the text
emails = email_regex.findall(text)
phones = phone_regex.findall(text)

# Format phone numbers
formatted_phones = []
for phone in phones:
    formatted_phone = ''.join(phone)
    formatted_phones.append(formatted_phone)    

# Combine results
results = []
if emails:
    results.append('Emails:')
    for email in emails:
        results.append(email)  # email is a tuple due to regex groups
if phones:
    results.append('Phone Numbers:')
    for phone in formatted_phones:
        results.append(phone)

# Copy results to clipboard
if results:
    result_text = '\n'.join(results)
    pyperclip.copy(result_text)
    print('Copied to clipboard:')
    print(result_text)
else:
    print('No email addresses or phone numbers found.')