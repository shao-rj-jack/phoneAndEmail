#! python3
# Name: Jack Shao
# File: phoneAndEmail.py
# Description: Finds all phone numbers and email addresses in the clipboard

import pyperclip
import re
import requests
import bs4
import sys


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, bs4.element.Comment):
        return False
    return True


def text_from_html(body):
    soup = bs4.BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return ' '.join(visible_texts)


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

if len(sys.argv) == 1:
    # get text from clipboard
    text = str(pyperclip.paste())
else:
    # get text from web page
    res = requests.get(sys.argv[1])
    res.raise_for_status()
    text = text_from_html(res.text)

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
