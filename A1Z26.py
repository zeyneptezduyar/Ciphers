cipherText = input("Enter A1Z26 Cipher Text (in format 00-00-0-0-00-0): ")
plainText = ""
cipherWordList = cipherText.split(" ")
for word in cipherWordList:
    cipherNumberList = word.split("-")
    for number in cipherNumberList:
        if (int(number) > 26):
            cipherText = input("Please try agian. Number range should be 1-26: ")
        else:
            ASCIIVAlue = int(number) + 64
        plainText += chr(ASCIIVAlue)
    plainText += " "
print(plainText)