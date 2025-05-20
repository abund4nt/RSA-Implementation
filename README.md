# Enhanced RSA Cryptosystem Implementation in Python

## Overview

This repository contains a Python implementation of the RSA (Rivest-Shamir-Adleman) asymmetric cryptosystem. RSA is one of the first public-key cryptosystems and is widely used for secure data transmission. This implementation serves as an educational tool to understand the fundamentals of asymmetric cryptography.

> [!WARNING]
> **Security Notice**: This implementation is for educational purposes only. It may contain vulnerabilities and should not be used for sensitive data in production environments. Always use well-vetted cryptographic libraries for real-world applications.

## Features

- Key pair generation (2048-bit RSA keys)
- Message encryption using public keys
- Message decryption using private keys
- Base64 encoding/decoding for key exchange
- Interactive command-line interface

## Getting Started

### Prerequisites

- Python 3.x
- PyCryptodome library (`pip install pycryptodome`)

### Installation

```bash
git clone https://github.com/your-repo/rsa-implementation.git
cd rsa-implementation
pip install -r requirements.txt
```

## Usage Guide

When you run the script, you'll be presented with an interactive menu:

```shell
Welcome to RSA Server

Select Option:
(1) Generate keys (private and public)
(2) Encrypt message
(3) Decrypt message
(4) Exit
```

### 1. Key Generation

Generating a key pair is the first step in using RSA cryptography:

```shell
Select Option: 1

[!] WARNING: The keys are being generated... keep them well stored.

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

**Important Security Notes:**
- The private key must be kept secret at all times
- The public key can be freely distributed
- Store keys securely (consider password protection for the private key)
- 2048-bit keys provide good security, but consider 3072 or 4096 bits for long-term security

### 2. Message Encryption

To encrypt a message using a recipient's public key:

```shell
Select Option: 2

Enter the message to encrypt: This is a secret message

Enter the public key that will encrypt the message (base64): LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0F....

Your encrypted message is: 14746634659051772345090619160847739346107822025878135056179431840383544183296437967909270354886735311180345743247212097706211101979451086028894835680585248834437560595077643176436038963195768876269911488174549424136154017029571441970067895516962286416050993934884906175304494142739460796136689018735564315035027718985716888453925282184178223539865834082853819602735459279117003460750949613734854620605171680712533091450949344077259036144276006252259608802572121747059525003621833160828635385601464134106144846772874481867511654254510137807977887643414711944912069376356633491565114517263965263150144656557937396321386
```

**Technical Details:**
- Messages are converted to numerical representation before encryption
- The public key's exponent (e) and modulus (n) are used for encryption
- The encryption formula: c ≡ mᵉ mod n

### 3. Message Decryption

To decrypt a message using your private key:

```shell
Select Option: 3

Enter the encrypted message: 14746634659051772345090619160847739346107822025878135056179431840383544183296437967909270354886735311180345743247212097706211101979451086028894835680585248834437560595077643176436038963195768876269911488174549424136154017029571441970067895516962286416050993934884906175304494142739460796136689018735564315035027718985716888453925282184178223539865834082853819602735459279117003460750949613734854620605171680712533091450949344077259036144276006252259608802572121747059525003621833160828635385601464134106144846772874481867511654254510137807977887643414711944912069376356633491565114517263965263150144656557937396321386

Enter the private key that will decrypt the message (base64): LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb2dJQkFBS0NBUUVBdTdMNWtiVTROQys3UnFRaVZnTUJmT3gvdzRjdW5pT......

Decrypted message: b'This is a secret message'
```

**Technical Details:**
- The private key's exponent (d) and modulus (n) are used for decryption
- The decryption formula: m ≡ cᵈ mod n
- The result is converted back from numerical representation to bytes

## RSA Cryptography Explained

### Mathematical Foundations

RSA is based on the practical difficulty of factoring the product of two large prime numbers (the factoring problem). The security of RSA relies on:

1. **Prime Factorization**: Difficulty in factoring large numbers
2. **Modular Arithmetic**: Properties of exponents in modular arithmetic
3. **Euler's Theorem**: Relationship between exponents and modulus

### Key Generation Process

1. **Select two distinct prime numbers** (p and q)
   - These should be large, random primes of similar length
   - In this implementation, we use 1024-bit primes (2048-bit modulus)

2. **Compute modulus (n)**
   - n = p × q
   - This will be part of both public and private keys

3. **Compute Carmichael's totient function (λ(n))**
   - λ(n) = lcm(p-1, q-1)
   - Where lcm is the least common multiple

4. **Choose public exponent (e)**
   - Typically 65537 (0x10001)
   - Must satisfy 1 < e < λ(n) and gcd(e, λ(n)) = 1

5. **Determine private exponent (d)**
   - d ≡ e⁻¹ mod λ(n)
   - This is the modular multiplicative inverse of e modulo λ(n)

### Encryption Process

Given a public key (n, e) and plaintext message M:

1. Convert M to an integer m (padding may be applied)
2. Compute ciphertext: c ≡ mᵉ mod n
3. The ciphertext c is sent to the recipient

### Decryption Process

Given a private key (n, d) and ciphertext c:

1. Compute plaintext integer: m ≡ cᵈ mod n
2. Convert m back to the original message M

### Security Considerations

1. **Key Size**: This implementation uses 2048-bit keys, which is considered secure until 2030
2. **Padding**: Proper padding (like OAEP) should be used in production
3. **Side-channel Attacks**: This implementation doesn't protect against timing attacks
4. **Random Number Generation**: The quality of random numbers affects security

## Implementation Details

### Key Components

1. **Key Generation**:
   - Uses `Crypto.PublicKey.RSA.generate()`
   - Default key size is 2048 bits
   - Public exponent is fixed at 65537 (common secure value)

2. **Message Conversion**:
   - Uses `Crypto.Util.number.bytes_to_long()` and `long_to_bytes()`
   - Handles conversion between bytes and large integers

3. **Base64 Encoding**:
   - Used for key exchange representation
   - Makes keys easier to copy and transmit

### Limitations

1. **Message Size**: RSA can only encrypt messages smaller than the modulus
2. **Performance**: RSA is slower than symmetric encryption
3. **Padding**: No padding scheme is implemented (vulnerable to certain attacks)
4. **Error Handling**: Minimal error handling for simplicity

## Advanced Topics

### Optimizations in Real Implementations

1. **Chinese Remainder Theorem (CRT)**: Speeds up decryption
2. **Window Exponentiation**: More efficient modular exponentiation
3. **Montgomery Reduction**: Faster modular arithmetic

### Common Vulnerabilities

1. **Small Exponent Attack**: When e is too small
2. **Common Modulus Attack**: Reusing modulus with different exponents
3. **Timing Attacks**: Leaking information through timing differences
4. **Padding Oracle Attacks**: Exploiting padding verification

## Example Use Cases

1. **Secure Message Exchange**:
   - Alice generates key pair, shares public key with Bob
   - Bob encrypts message with Alice's public key
   - Alice decrypts with her private key

2. **Digital Signatures** (not implemented here):
   - Sign by encrypting with private key
   - Verify by decrypting with public key

3. **Hybrid Cryptosystems**:
   - Use RSA to exchange symmetric keys
   - Use symmetric encryption for bulk data

## Extending the Implementation

To make this more production-ready, consider adding:

1. **Proper Padding Schemes** (OAEP or PKCS#1 v1.5)
2. **Key Serialization with Passwords**
3. **File Encryption/Decryption**
4. **Network Communication Support**
5. **Digital Signature Functionality**

## References

1. [Original RSA Paper](https://people.csail.mit.edu/rivest/Rsapaper.pdf)
2. [PKCS #1 Standard](https://tools.ietf.org/html/rfc8017)
3. [NIST Recommendations](https://csrc.nist.gov/publications/detail/sp/800-56b/rev-2/final)
4. [Applied Cryptography by Bruce Schneier](https://www.schneier.com/books/applied_cryptography/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Rivest, Shamir, and Adleman for the RSA algorithm
- The PyCryptodome developers for their excellent library
- All cryptographers who have contributed to making RSA secure
