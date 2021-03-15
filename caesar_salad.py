from sys import argv
from pathlib import Path

class CaesarCipher:
	def __init__(self):
		# Null constructor
		pass

	def encrypt(self, input, key):
		return 0;

	def decrypt(self, input, key):
		plaintext = ""
		for l in input:
			plaintext += self.shift(l, -key)
		print(f"\nText to decipher:\n{input}\nCaesar key: {key} \n\nProcessed plaintext:\n{plaintext}\n")
		return plaintext;

	def shift(self, letter, key):
		ascii = ord(letter)
		base = 0
		
		if(ascii >= 65 and ascii <= 90):
			base = 65
		elif(ascii >= 97 and ascii <= 122):
			base = 97
		
		shift = (ascii - base + key) % 26
		
		return chr(base + shift)

if __name__ == '__main__':
	# flags can be:
	# -d --> decrypt a file
	# -e --> encrypt a file
	# -D --> decrypt string in all shifts
	# -E --> encrypt string in all shifts
	flag = argv[1]

	word = argv[2]
	key = int(argv[3])

	ciph = CaesarCipher()

	if(flag == "-d"):
		word = Path(word).read_text()
		ciph.decrypt(word, key)
	elif(flag == "-e"):
		ciph.encrypt(word, key)
	elif(flag == "-D"):
		for i in range(0, 26):
			ciph.decrypt(word,i)
	else:
		print("work in progress")
