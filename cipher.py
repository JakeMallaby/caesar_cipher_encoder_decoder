def decrypt():
    #cipher to be decrypted
    messageCipher = input("enter cipher to decrypt:").strip()
    # alphabet
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #shift value to be used to decrypt
    shiftKey = int(input("enter shift val to decrypt:"))
    decryptedMessage = ""

    # iteration over chars of the input cipher
    for ch in messageCipher:
        if ch in letters:                        #if the character is in the letters var it will find the position in that string
            position = letters.find(ch)
            newPos = (position - shiftKey) % 26      #it does the position - the shift value % 26 to find the new position of the character
            newChar = letters[newPos]           # the newchar is put into a letters list which will now be the decipherd message
            decryptedMessage += newChar
        else:
            decryptedMessage += ch
    print("the decripted message is:\n")
    print(decryptedMessage)

decrypt()