The assumptions on the ransomware are as follows: 
    1) An attacker has already broken into a victim’s Linux/Unix machine on which Python 3.5 or above and pycryptodome package are installed; 
    2) the attacker put its ransomware program, which is not necessary to be a single file, in the victim’s machine; 
    3) the victim has three to four text files and a python file in the directory where ransomware locates. Note that the text files have extension “.txt” and the python file has extension “.py”.

The ransomware should perform the following: 
    1) It generates a random alphabet table for symmetric encryption using substitutioncipher.
    2) It encrypts all .txt files to .enc files in the current directory using the key that the attacker generated in step 1). The files in the other folders or the files in the same folder but having different file extensions must not be impacted by the ransomware.
    3) It comments out all the content of the existing .py files in the target folder (do not delete the content) and replicates itself to the .py files for the further propagation.
    4) The key in step 1) is encrypted to key.bin using public key encryption. (RSA 2048 from Lab2)
    5) It will finally display a message for asking ransom “Your text files are encrypted. To decrypt them, you need to pay me $10,000 and send key.bin in your folder to [me].” “[me]” should be your email address. 

Other requirements:
    - In step 1), the key used to encrypt files must not appear in the source code of the 
ransomware program and must not be stored in the plaintext format in the victim’s system. 
    - Ignore numbers, special characters and spaces in the encryption process of substitution 
cipher.
    - All .txt files locating in the folder where ransomware program is located must be deleted 
after they are encrypted to the .enc files.
    - You must implement substitution encryption by yourself and use pycryptodome for public 
key encryption.
    - The infected .py file in step 3) shares the public key of your original ransomware. 

Your next task is to write programs, key-recovery and file-recovery programs that recover (decrypt) all the encrypted files if the victim pays the ransom. 
    6) The key-recovery program decrypt the encrypted key (key.bin) and store the decrypted key in key.txt. 
    7) The file-recovery program must allow a user to decrypt the encrypted files created in step 2) using the key file created in 6). 
    You do not need to recover the infected .py file in step 3).
