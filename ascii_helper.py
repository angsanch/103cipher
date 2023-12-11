##
## EPITECH PROJECT, 2023
## ascii_helper.py
## File description:
## convert to ascii and back
##

def str_to_ascii(string):
    result = []
    for i in string:
        result.append(ord(i))
    return result

def ascii_to_str(asc):
    result = ""
    for i in asc:
        result += chr(int(i))
    return (result)

def trailing_zero(short, length):
    for i in range(length - len(short)):
        short.append(0)
    return short
