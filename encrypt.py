#!/usr/bin/python3
import caesar
import substitution
import msubstitution

# input = input("Please enter the plain text path:")
plainPath = "plain.txt"
cipherPath = "cipher.txt"

cipher = ""
with open(plainPath) as fp:
    plaintext = fp.read()
    cipher = cipher + msubstitution.encrypt(plaintext)

open(cipherPath, "w").write(cipher)
