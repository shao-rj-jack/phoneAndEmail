#! python3
# Name: Jack Shao
# File: phoneAndEmail.py
# Description: Finds all phone numbers and email addresses in the clipboard

import pyperclip
import re

phoneRegex = re.compile(r'''(
                            (\d{3}|\(\d{3}\))?              # area code
                            (\s|-|\.)?                      # separator
                            (\d{3})                         # first 3 digits
                            (\s|-|\.)                       # separator
                            (\d{4})                         # last 4 digits
                            (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
                            )''', re.VERBOSE)

emailRegex = re.compile(r'''(
                             [a-zA-Z0-9._%+-]+  # username
                             @                  # @ sign
                             [a-zA-Z0-9.-]+     # domain name
                             (\.[a-zA-Z]{2,4})  # dot something
                             )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

# add all numbers and emails to matches list
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])  # join numbers with dash in between
    # check for extension and add if it exists
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
        print(groups[8] + '|')
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copy matches to clipboard and print results
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
