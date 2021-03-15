# Crack vigenere key with frequency analysis
from pathlib import Path
from sys import argv
from collections import Counter
import string

# Provides series of methods to help with vigenere decryption
class Visualiser:
    def __init__(self, text = "exampleexample", split_point = 7):
        self.text = text
        self.split_point = split_point
        # ENGLISH alphabet letter frequency
        self.alphabet_frequency = {'A': 8.17, 'B': 1.49, 'C': 2.78, 'D': 4.25, 'E': 12.7, 'F': 2.23, 'G': 2.02, 'H': 6.09, 'I': 6.97, 'J': 0.15, 'K': 0.77, 'L': 4.03, 'M': 2.41, 'N': 6.75, 'O': 7.51, 'P': 1.93, 'Q': 0.1, 'R': 5.99, 'S': 6.33, 'T': 9.06, 'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15, 'Y': 1.97, 'Z': 0.07}

    def getKey(self):
        key = ""
        for i in range(1, self.split_point + 1):
            key += self.frequency(i)
        return key

    def frequency(self, position):
        """ Calculates each letter frequency on the specified key position (length: 1 to the key size)
        """
        initial_pos = position
        extract = ""
        i = 1
        for c in self.text:
            if(i == position):
                extract += c
                position += self.split_point
            i += 1

        #Calculate letter frequency
        freq = Counter(extract)
        for l in string.ascii_uppercase:
            if l not in freq:
                freq = {**freq, l : 0}

        sortedFreq = {key: val for key, val in sorted(freq.items(), key = lambda ele: ele[0])}
        sortedFreq = dict(map(lambda x : (x[0], round(x[1]/len(extract)*100, ndigits=2)), sortedFreq.items() ))
        if "\n" in sortedFreq: sortedFreq.pop("\n")
        print(f"LETTER FREQUENCY FOR POSITION [{initial_pos}]:")
        self.printFrequencies(sortedFreq)
        freqValues = list(sortedFreq.values())
        alphaValues = list(self.alphabet_frequency.values())
        letter = ""
        max_affinity = 0
        for s in string.ascii_uppercase:
            affinity = sum([v1 * v2 for v1, v2 in zip(alphaValues, freqValues)])
            if(max_affinity < affinity):
                letter = s
                max_affinity = affinity
            freqValues = self.rotateLeft(freqValues)
        print(f"Found letter {letter} to be the best match for key position {initial_pos}. AFFINITY: {max_affinity}")
        return letter

    def printFrequencies(self, list):
        [print(key, ':', value) for key, value in list.items()]
        pass

    def rotateRight(self, list):
        """ Rotates a list to the right
        """
        return list[-1:] + list[:-1]

    def rotateLeft(self, list):
        """ Rotates a list to the left
        """
        return list[1:] + list[:1]

    def printFormatted(self):
        i = 1
        split_no = 0
        for c in self.text:
            if(i < self.split_point):
                print(c, end="")
                i += 1
            else:
                print(c, end=" ")
                i = 1
                split_no += 1
            if(8 == split_no):
                split_no = 0
                print() # new line
        print()

if __name__ == '__main__':
    cipher = Path(argv[1]).read_text()
    view = Visualiser(cipher, int(argv[2]))
    view.printFormatted()
    view.frequency(int(argv[3]))
    print("THE FINAL KEY IS: ", view.getKey())
