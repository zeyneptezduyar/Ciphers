cipherText = input("Enter Caesar Cipher Text: ")
cipherText = cipherText.upper()
plainText = ""
for char in cipherText:
    if (char.isalpha()):
        ASCIIValue = ord(char)
        if (ASCIIValue > 87):
            ASCIIValue -= 26
        ASCIIValue += 3
        plainText += chr(ASCIIValue)
    else:
        plainText += char
print(plainText)