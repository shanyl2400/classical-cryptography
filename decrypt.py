#!/usr/bin/python3
import caesar
import substitution
import msubstitution

# input = input("Please enter the plain text path:")
cipherPath = "cipher.txt"
plainPath = "cipher_plain.txt"

plain = ""
with open(cipherPath) as fp:
    ciphertext = fp.read()
    plain = plain + msubstitution.decrypt(ciphertext)

open(plainPath, "w").write(plain)
