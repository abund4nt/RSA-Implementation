# RSA cryptosystem implementation in Python
Simple script written in Python that implements the RSA cryptosystem. This tool allows us to encrypt/decrypt messages securely using RSA.

## Test the tool

``` shell
nc 164.92.110.223 6784
```

## Functionalities of the tool
This tool has 4 options, the first one allows us to generate a public and private key to encrypt/decrypt messages. Our public key can be disclosed through an insecure channel for a third party to encrypt data with it. Our private key should not be given to a third party for any reason, as it will be used to decrypt our messages. (For more information read the following [article](https://es.wikipedia.org/wiki/Criptograf%C3%ADa_asim%C3%A9trica)).

![](https://i.imgur.com/bh740T4.png)

