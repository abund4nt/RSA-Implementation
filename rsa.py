import time
import base64
from Crypto.PublicKey import RSA
from Crypto.Util.number import *

menu = '''
\tTool for encrypting/decrypting messages using the RSA cryptosystem.\n
(1) Generate keys (private and public)
(2) Encrypt message
(3) Decrypt message
(4) Exit
'''

e = 0x10001

while True:

    print(menu)
    option_user = int(input('Select Option: '))
    
    if option_user == 1:
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        
        print("\n[!] WARNING: The keys are being generated... keep them well stored.\n")
        time.sleep(1.5)

        print(f"Your private key:\n{private_key.decode()}\n\nIn base64: {base64.b64encode(private_key).decode()}\n")
        print(f"Your public key:\n{public_key.decode()}\n\nIn base64: {base64.b64encode(public_key).decode()}")
    
    elif option_user == 2:
        plain_message = bytes_to_long(input('\nEnter the message to encrypt: ').encode())
        pubkey_message = input('\nEnter the public key that will encrypt the message (base64): ')
        pubkey_message = base64.b64decode(pubkey_message)
        pubkey_message = RSA.import_key(pubkey_message)
        
        encrypted_message_one = pow(plain_message, pubkey_message.e, pubkey_message.n)
        print(f"\nYour encrypted message is: {encrypted_message_one}\n")
    
    elif option_user == 3:
        encrypted_message_two = input('Enter the encrypted message: ')
        privkey_message = input('\nEnter the private key that will encrypt the message (base64): ')
        privkey_message = base64.b64decode(privkey_message)
        privkey_message = RSA.import_key(privkey_message)

        m = pow(int(encrypted_message_two), privkey_message.d, privkey_message.n)
        print(f"\nDecrypted message: {long_to_bytes(m)}\n")

    elif option_user == 4:
        print('Goodbye! thank you for using the tool')
        exit()
