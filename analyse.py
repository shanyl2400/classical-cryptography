#!/usr/bin/python3
import matplotlib.pyplot as plt


def calculateWords(path):
    dictionary = {}
    for i in range(26):
        ch = ord('A') + i
        dictionary[chr(ch)] = 0

    with open(path) as fp:
        plaintext = fp.read()
        for c in plaintext:
            if not c.isalpha():
                continue
            c = c.upper()
            if not c in dictionary:
                dictionary[c] = 1
            else:
                dictionary[c] = dictionary[c] + 1
    return dictionary


def showPie(dic):
    chars = dic.keys()
    freq = dic.values()

    plt.pie(x=freq, labels=chars)

    plt.xlabel('char')
    plt.ylabel('freq')
    plt.title("alphabet statistics")
    plt.show()


def showBar(dic):
    chars = dic.keys()
    freq = dic.values()
    plt.bar(chars, freq, label='times')

    plt.xlabel('char')
    plt.ylabel('freq')
    plt.title("alphabet statistics")
    plt.legend()
    plt.show()


dic = calculateWords("plain-2.txt")
# showPie(dic)
showBar(dic)
