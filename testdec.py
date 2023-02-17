import glob, random, sys, os, itertools
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


key = "AOKIBEVFZWDPUMLGTQRNJHSYXC"
data = "Fuvvs, g fnwu qgjjuqqogvvz aujmzytua tuit oevu 1"
def decrypt(data, key):
	alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	charsA = alphabets
	charsB = key
	translated = ''
	print(data)
	#translate the message again, swap B and A
	charsA, charsB = charsB, charsA

	for symbol in data:
		if symbol.upper() in charsA:
			symIndex = charsA.find(symbol.upper())
			if symbol.isupper():
				translated += charsB[symIndex].upper()
			else:
				translated += charsB[symIndex].lower()
		else:
			translated += symbol
	return translated

#print decrypted data	
print(decrypt(data, key))


