from cryptography.fernet import Fernet

#generate key
key = Fernet.generate_key()
 
# write key to file
with open('filekey.key', 'wb') as file_key:
   file_key.write(key)

with open('filekey.key', 'rb') as file_key:
    key = file_key.read()

fn = Fernet(key)

# read file to encrypt
with open('myfile.txt', 'rb') as file:
    original_file = file.read()

# encrypt file
encrypted_file = fn.encrypt(original_file)
print("********encrypting file finished********")

# write encrypted texts to file
with open('encrypted_file.txt', 'wb') as encrypted:
    encrypted.write(encrypted_file)
    print("********..........done writing to file********")
