from pathlib import Path
from sys import argv
from caesar_salad import CaesarCipher
from vigenere_visualiser import Visualiser
from ic import CoincidenceIndex

# Author: Daniel Bartolini
# Login: db666
class Vigenere:
    def __init__(self, ciphertext, key = "", key_length = 0):
        """Vigenere constructor, state the key used for encryption"""
        self.key = key
        self.ciphertext = ciphertext
        self.shifter = CaesarCipher()
        self.key_length = key_length
        if(self.key_length < 1):
            self.findKeyLength()
        if(len(key) < 1):
            self.findKey()

    def findKeyLength(self):
        """ Finds the best key length for the given text, if required
        """
        ci = CoincidenceIndex(1, 10)
        self.key_length = ci.calculateIC(self.ciphertext)

    def findKey(self):
        """ Finds the key of the given ciphertext, with a given length
        """
        key_finder = Visualiser(self.ciphertext, self.key_length)
        self.key = key_finder.getKey()

    def decrypt(self):
        """Decrypts a string using the field key
        """
        print(f"\n>> Decrypting the ciphertext using the key {self.key}")
        plaintext = ""
        key_count = 0
        for c in self.ciphertext:
            current_shift = -ord(self.key[key_count].upper()) - 65
            plaintext += self.shifter.shift(c, current_shift)
            key_count = (key_count + 1) % len(self.key)

        return plaintext

    def encrypt(self, plaintext, start_count):
        # Not needed for now
        pass


if __name__ == "__main__":
    if(len(argv) > 1):
        cipher = Path(argv[1]).read_text()
        key = ""
        key_length = 0

        # check further arguments
        if(len(argv) > 2):
            if(argv[2] == "-k"):
                key = argv[3]
            elif(argv[2] == "-kl"):
                key_length = int(argv[3])

        # decrypt
        v = Vigenere(cipher, key, key_length)
        i = 1
        for c in v.decrypt():
            if(i % 30 == 0):
                print(c, end=" ")
            else:
                print(c, end="")
            i += 1

    else:
        print("Bad program usage. Example of proper usage below:\n",
            "python vigenere.py mandatory{txt file address} optional{-k string:DECRYPTION_KEY || -kl int:KEY_LENGTH}",
        )
