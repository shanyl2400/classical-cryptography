#!/usr/bin/python3
import random

alphabetPath = "alphabet"


def encrypt(text):
    dic = readAlphabet(alphabetPath)
    return doSubstitution(text, dic["key"], dic["value"])


def decrypt(cipher):
    dic = readAlphabet(alphabetPath)
    return doSubstitution(cipher, dic["value"], dic["key"])


def doSubstitution(data, key, value):
    res = ""
    data = data.upper()
    for c in data:
        r = substitute(c, key, value)
        res = res + r
    return res


def createAlphabet(name):
    alphabet = []

    out = open(name, "w")
    for i in range(26):
        ch = ord('A') + i
        alphabet.append(chr(ch))

    for c in alphabet:
        out.write(c)

    out.write("\n")

    random.shuffle(alphabet)
    for c in alphabet:
        out.write(c)


# createAlphabet("alphabet")
def readAlphabet(path):
    key = ""
    value = ""
    with open(path) as fp:
        alphabet = fp.read()
        alphabetPairs = alphabet.split("\n")
        key = alphabetPairs[0]
        value = alphabetPairs[1]
    return {"key": key, "value": value}


def substitute(c, key, value):
    for index in range(len(key)):
        if key[index] == c:
            return value[index]
    return c
