#!/usr/bin/python3
import random

alphabetPath = "m_alphabet"
alphabetSize = 5

encryptMode = "encrypt"
decryptMode = "decrypt"


def encrypt(text):
    return doSubstitution(text, encryptMode)


def decrypt(cipher):
    return doSubstitution(cipher, decryptMode)


def doSubstitution(data, mode):
    dic = readAlphabet(alphabetPath)
    key = dic["key"]
    value = dic["value"]
    size = len(value)
    offset = 0

    res = ""
    data = data.upper()
    for c in data:
        r = ""
        if mode == decryptMode:
            r = substitute(c, value[offset % size], key)
        else:
            r = substitute(c, key, value[offset % size])
        res = res + r
        offset = offset + 1
    return res


def createAlphabets(name):
    alphabet = []

    out = open(name, "w")
    for i in range(26):
        ch = ord('A') + i
        alphabet.append(chr(ch))

    for c in alphabet:
        out.write(c)

    out.write("\n")

    for i in range(alphabetSize):
        random.shuffle(alphabet)
        for c in alphabet:
            out.write(c)
        out.write("\n")


def readAlphabet(path):
    key = ""
    value = []
    with open(path) as fp:
        alphabet = fp.read()
        alphabets = alphabet.split("\n")
        for index in range(len(alphabets)):
            if len(alphabets[index]) < 1:
                continue
            if index == 0:
                key = alphabets[index]
            else:
                value.append(alphabets[index])
    return {"key": key, "value": value}


def substitute(c, key, value):
    for index in range(len(key)):
        if key[index] == c:
            return value[index]
    return c
