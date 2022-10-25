# Given a text file file.txt that contains a list of phone numbers (one per line), write a one-liner bash
# script to print all valid phone numbers.
# You may assume that a valid phone number must appear in one of the following two formats: (xxx)
# xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

import re

if __name__ == "__main__":
    with open('file.txt', 'r') as f:
        phone_number = f.read()
        phone_number = phone_number.split("\n")
    for number in phone_number:
        if re.match(r"^[\d]{3}-[\d]{3}-[\d]{4}|([(][\d]{3}[)]\s)[\d]{3}-[\d]{4}", number):
            print(number)