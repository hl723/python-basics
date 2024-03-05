#! /usr/bin/env python

# Checks if a given password meets basic requirments
# >=8 chars long
# Contains both upper and lowercase letters
# Has at least one digit 

import re
import sys

def checkPwdStrength(pwd):
    upperRe = re.compile(r'[A-Z]+')
    lowerRe = re.compile(r'[a-z]+')
    digitRe = re.compile(r'\d+')

    if len(pwd) >= 8:
        print(f"PASS Password is at least 8 characters long.")
    else:
        print(f'FAIL Password too short! Need >=8 characters!')
    
    upperMatches = upperRe.findall(pwd)
    if len(upperMatches):
        print(f'PASS Found {len(upperMatches)} groups of uppercase letters.')
    else:
        print(f'FAIL Need at least one uppercase letter!')

    lowerMatches = lowerRe.findall(pwd)
    if len(lowerMatches):
        print(f'PASS Found {len(lowerMatches)} groups of lowercase letters.')
    else:
        print(f'FAIL Need at least one lowercase letter!')
    
    digitMatches = digitRe.findall(pwd)
    if len(digitMatches):
        print(f'PASS Found {len(digitMatches)} groups of digits.')
    else:
        print(f'FAIL Need at least one digit!')


def main():
    if len(sys.argv) != 2:
        print("Usage: ./pwd_strength.py <password>")
    else:
        checkPwdStrength(sys.argv[1])

if __name__=='__main__':
    main()
    