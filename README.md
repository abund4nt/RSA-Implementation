# RSA cryptosystem implementation in Python

> [!WARNING]
> This RSA implementation could be insecure, the repository is created for the purpose of learning about asymmetric cryptography, do not use this tool for sensitive things.

Simple script written in Python that implements the RSA cryptosystem. This tool allows us to encrypt/decrypt messages securely using RSA.

## Functionalities of the tool

When connecting to the server or using the tool locally, you will encounter the following interface

``` shell
Welcome to RSA Server


Select Option:
(1) Generate keys (private and public)
(2) Encrypt message
(3) Decrypt message
(4) Exit
```

This tool has 4 options, the first one allows us to generate a public and private key to encrypt/decrypt messages. Our public key can be disclosed through an insecure channel for a third party to encrypt data with it. Our private key should not be given to a third party for any reason, as it will be used to decrypt our messages. (For more information read the following [article](https://es.wikipedia.org/wiki/Criptograf%C3%ADa_asim%C3%A9trica)). The second one allows us to encrypt a message using a public key (send it in base64). The third one allows us to decrypt a message using a private key and in the fourth option we exit the tool.

![](https://i.imgur.com/bh740T4.png)

## Example of encrypting and decrypting a message

First of all we select option 1 and generate a public and private key, then we store both keys securely.

``` shell
Your private key:
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAu7L5kbU4NC+7RqQiVgMBfOx/w4cuniNLAsrZ9HPAACvHszSh
xS+HTvypNL7j+PqDKV0olvAwyswG6+kaH4Rm031/pT1831XmjijFGO1t8B//GjIw
VDguGvKB3ri1IA.....
-----END RSA PRIVATE KEY-----

In base64: LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLR....

Your public key:
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu7L5kbU4NC+7RqQiVgMB
f.....
-----END PUBLIC KEY-----

In base64: LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3M...
```

With both values saved, we can give our public key to a sender to encrypt a message with it. For this we select option 2.

``` shell
Enter the message to encrypt: Mi password is securepassword123

Enter the public key that will encrypt the message (base64): LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0F....

Your encrypted message is: 14746634659051772345090619160847739346107822025878135056179431840383544183296437967909270354886735311180345743247212097706211101979451086028894835680585248834437560595077643176436038963195768876269911488174549424136154017029571441970067895516962286416050993934884906175304494142739460796136689018735564315035027718985716888453925282184178223539865834082853819602735459279117003460750949613734854620605171680712533091450949344077259036144276006252259608802572121747059525003621833160828635385601464134106144846772874481867511654254510137807977887643414711944912069376356633491565114517263965263150144656557937396321386
```

We can see that it delivers the message encrypted correctly, in this step the sender delivers the encrypted message through an insecure channel, and we can decrypt it using our public key.

``` shell
Select Option: 3
Enter the encrypted message: 14746634659051772345090619160847739346107822025878135056179431840383544183296437967909270354886735311180345743247212097706211101979451086028894835680585248834437560595077643176436038963195768876269911488174549424136154017029571441970067895516962286416050993934884906175304494142739460796136689018735564315035027718985716888453925282184178223539865834082853819602735459279117003460750949613734854620605171680712533091450949344077259036144276006252259608802572121747059525003621833160828635385601464134106144846772874481867511654254510137807977887643414711944912069376356633491565114517263965263150144656557937396321386

Enter the private key that will encrypt the message (base64): LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb2dJQkFBS0NBUUVBdTdMNWtiVTROQys3UnFRaVZnTUJmT3gvdzRjdW5pT......

Decrypted message: b'Mi password is securepassword123'
```
## Brief explanation of RSA.

### Key generation.

To generate the keys in RSA, two different prime numbers $p$ and $q$ are chosen, these numbers are random and must have a similar bit length. With both numbers $n = pq$ is calculated. N is the modulus for the public and private keys.

Using euler's function we calculate $\phi = (p - 1)(q - 1)$. Then find a positive integer $e$ that is less than $\phi$ to use as a public exponent.

With these values, d is determined to be equal to $e d 1.

The public key is $n$ and $e$ and the private key is $n$ and $d$.

### Encryption

With $M$ being the plaintext message and $C$ being the encrypted message, Alice sends her public key to Bob over an insecure channel while keeping her private key secret. Bob uses the following formula to encrypt the message.

$c \equiv M^{e} \pmod n$

Basic example in Python.

``` python
from Crypto.Util.number import *

e = 0x10001

p, q = getPrime(1024), getPrime(1024)
n = p * 
message = bytes_to_long(input('Enter your message: ').encode())
enc_message = pow(message, e, n)
```

### Deciphered.

Alice can recover $M$ from $C$ using $d$.

$m \equiv c^{d} \pmod n$.

Basic Python example:

``` python
from Crypto.Util.number import *

p, q = getPrime(1024), getPrime(1024)
n = p * q
phi = (p - 1) * (q - 1)
e = 0x10001
d = inverse(e, phi)  # Calcular la clave privada d

enc_message = int(input('Enter the encrypted message: '))
dec_message = pow(enc_message, d, n)

original_message = long_to_bytes(dec_message)

print(original_message)
```

