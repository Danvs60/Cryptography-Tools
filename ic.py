import string
from collections import Counter
from pathlib import Path
from sys import argv

class CoincidenceIndex:

    def __init__(self, from_index = 1, to_index = 5):
        self.from_index = from_index
        self.to_index = to_index

    def extractsForKeyLength(self, text, length):
        extracts = []
        for i in range(length):
            j = 0
            extracts.append("")
            for c in text:
                if(j % length == 0):
                    extracts[i] += c
                j += 1
            text = text[1:]

        return extracts

    def indexOfCoincidence(self, sequence):
        """ Calculates the index of coincidence of a sequence of characters
        """
        count = Counter(sequence)
        index = sum([f[1] * (f[1] - 1) for f in count.items()])
        index /= len(sequence) * (len(sequence) - 1)
        return index

    def calculateIC(self, text, alphabet_len = 26):
        """ This function calculates the index of coincidence based of a text on Friedman's method. And returns the best key length for the given text.
        """
        ics = []
        for i in range(self.from_index, self.to_index + 1):
            extract = self.extractsForKeyLength(text, i)
            index = sum([self.indexOfCoincidence(ex) for ex in extract]) / len(extract)
            ics.append(index)

        return ics.index(max(ics)) + self.from_index

if __name__ == '__main__':
    # DEBUGGING
    c = CoincidenceIndex(4,6)
    # print(c.extractsForKeyLength("ABCDABCDABCDABCDABCDABCDABCDABCD", 4))
    # print(c.indexOfCoincidence("AAAAAAAAAAAAAABC"))
    c.calculateIC("SIEORISORNOSIFOSDIGJSERNVDOS")
