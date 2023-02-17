import glob, random, sys, os, itertools
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

#get the ciphertext in .enc and decode from bytes to string
for file_name in glob.glob('*.enc'):
	with open(file_name,'rb') as tf:
		encoded_data = tf.read()
		#decode data in bytes to string
		data = encoded_data.decode()
		#print(data)

#decrypt the encrypted symmetric key
file_in = open("key.bin", "rb") 
private_key = RSA.import_key(open("ransomprvkey.pem").read()) 
enc_data = file_in.read(private_key.size_in_bytes())
cipher_rsa = PKCS1_OAEP.new(private_key)

#decrypt rsakey
rsa_key = cipher_rsa.decrypt(enc_data)
#print(rsa_key)
file_in.close()

#store decrypted key in key.txt
key_file = open("key.txt","wb")
key_file.write(rsa_key)
key_file.close()

#decode key from bytes to string
key = rsa_key.decode("utf-8")

def decrypt(data, key):
	alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	charsA = key
	charsB = alphabets
	translated = ''
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


