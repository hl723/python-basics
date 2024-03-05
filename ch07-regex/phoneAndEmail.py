#! /usr/bin/env python3
# phoneAndEmail.py - Extracts phone numbers and email addresses on the clipboard
# Pastes the result back to the clipboard

import pyperclip, re

# Create phone regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))              # area code
    ([\s|\.|-])?                    # separator
    (\d{3})                         # middle three digits
    ([\s|\.|-])?                    # separator
    (\d{4})                         # last four digits
    (\s*(ext|ext.|x)\s*(\d{1, 5}))? # extension
    )''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    ([\w\d.+-]+)      # username
    @               # @
    ([\w\d]+)       # domain name
    (\.)             # .
    ([a-zA-Z])+     # top level domain extensions
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
    