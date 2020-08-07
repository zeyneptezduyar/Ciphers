cipherText = input("Enter Atbash Cipher Text: ")
cipherText = cipherText.upper()
plainText = ""
for char in cipherText:
    if (char.isalpha()):
        ASCIIValue = ord(char) - 65
        ASCIIValue = 90 - ASCIIValue
        plainText += chr(ASCIIValue)
    else:
        plainText += char
print(plainText)