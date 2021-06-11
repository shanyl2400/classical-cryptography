#!/usr/bin/python3

offset = 6


def encrypt(text):
    res = ""
    for c in text:
        if (c.isalpha()):
            d = ord(c.upper())
            d = (d + offset) % 26 + ord('A')
            c = chr(d)
        res = res + c
    return res


def decrypt(cipher):
    res = ""
    for c in cipher:
        if (c.isalpha()):
            d = ord(c.upper())
            d = (d - offset) % 26 + ord('A')
            c = chr(d)
        res = res + c
    return res
