# In this program, I want It to encrypt a string by changing Its value to the 7 alphabet after It.
# If the incrementation is not possible. You return to the first alphabet
# This will also be my of practicing classes
import time
# Create a class that takes the original file
class Encrypt:

    def __init__(self, originalfile, increment):
        self.originalfile = originalfile
        self.increment = increment

    # The method that will read the file
    def encryptfile(self):
        f = open(self.originalfile, "r")
        text = f.read()

        # Turning my string into a list
        string_list = list(text.strip(" "))

        # print(" The old list is : ", string_list)
        # Adding 5 to each character of the list
        for i in range(0,len(string_list)-1):

            # Getting the ASCII code of the character
            ascii = ord(string_list[i])

            # Incrementing It by 5
            ascii += int(self.increment)

            # Replacing It by the new character
            string_list[i] = chr(ascii)

        #print(" The new list is : ", string_list)

        new_text = "".join(string_list)
        f2 = open("/home/mohamed/Documents/Adonis Programming/encrypted.txt","w+")
        f2.write(new_text)

    def decryptfile(self):
        f = open(self.originalfile, "r")
        text = f.read()

        # Turning my string into a list
        string_list = list(text.strip(" "))

        # print(" The old list is : ", string_list)
        # Adding 5 to each character of the list
        for i in range(0,len(string_list)-1):

            # Getting the ASCII code of the character
            ascii = ord(string_list[i])

            # Incrementing It by 5
            ascii -= int(self.increment)

            # Replacing It by the new character
            string_list[i] = chr(ascii)

        #print(" The new list is : ", string_list)

        new_text = "".join(string_list)
        print(new_text)

operation = input("Enter 1 If you want to encrypt your text \nEnter 2 If you want to decrypt your text file\n")
inc = input("Choose the step of encryption : ")
src = input(("Enter the path to your text file : "))

my_encryption = Encrypt(src, inc)

if(operation == "1"):
    print("Encrypting File")
    time.sleep(3)
    my_encryption.encryptfile()
    print("Your file has been encrypted and secured")

elif(operation == "2"):
    print("Decrypting File")
    time.sleep(3)
    my_encryption.decryptfile()
    print("Your file has been decoded and ready to read")

