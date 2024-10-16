"""
Author : Tadiwanashe Atony Tuwacha
Program : Decrypts ciphired text
Date : 09/23/2024

This program will ask user to input the ciphered word and distance,
 it will then out put the ciphered text in plaintext
"""
#  user_input
user_input = input("Enter the coded text : ")
distance = int(input("Enter the distance value : "))
plainText = ""

# computations and calculations
for ch in user_input:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - \
                      (distance - (ord('a') - ordvalue - 1))
    plainText += chr(cipherValue)
# print
print(plainText)
