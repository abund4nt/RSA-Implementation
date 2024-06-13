# RSA cryptosystem implementation in Python

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
## Breve explicacion de RSA.

**Generacion de claves.**

Para generar las claves en RSA se eligen dos numeros primos distintos $p$ y $q$, estos numeros son aleatorios y deben tener una longitud de bits parecida. Con ambos numeros se calcula $n = pq$. N es el modulo para las clave publica y privada.

Utilizando la funcion de euler se calcula $\phi = (p - 1)(q - 1).$. Luego se busca un enetero positivo $e$ que sea menor que $\phi$ para utilizarlo como exponente publico.

Con estos valores se determina d, esta debe satisacer la congruencia $e \dot d \equal 1 mod \phi$
