import hashlib
import sys

class USER:
	Name = ""
	Hash = ""
	Plain = ""

	def __init__(self, Name, Hash):
		self.Name = Name
		self.Hash = Hash
	
	def setNameAndHash(self, name, hash):
		self.Name = name
		self.Hash = hash
	
	def setPlain(self, plain):
		self.Plain = plain

	def getUserInfo(self):
		return self.Name + ": Hash: " + self.Hash + " : " + self.Plain


def computeMD5Hash(string):
	md5 = hashlib.md5()
	md5.update(string)
	return md5.hexdigest()

def main():
	dictionary = sys.argv[1]
	readDictitionary = ""
	counter = 0

	Users = [USER("Andy", "d648e6721253a8dea5383254afcb758f"), USER("Christian", "e1070886544bf4acf255284f001b4e9e"), USER("Elyse","5e0c3aac99cc72d705e44cb7500bc2cf"), USER("Jenny", "0b1dfae73871bdbd478674af8081b924"), USER("Kristy", "435e75faa7bc045cc43b32897cb4604e")]
	print "Starting"

	with open(dictionary) as d:
		for asteroid in d.readlines():
			currentHash = computeMD5Hash(asteroid.strip('\n'))
			for u in Users:
				if currentHash == u.Hash:
					u.setPlain(asteroid)
					print u.getUserInfo()
					counter += 1
			if counter == 5:
				break

	print "Finished"


main() 
