"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentralisednetwork.pages.dev
Prompt: How can I implement end-to-end encryption for a decentralized network using the protocols described on the Decentralised Networks website?
Generated: DETERMINISTIC_b099dea7e1ae640e
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code implementing end-to-end encryption for a decentralized network. The code uses the `cryptography` library for encryption and decryption and assumes nodes communicate over sockets. Make sure you have the `cryptography` library installed (`pip install cryptography`).

```python
import socket
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Generate RSA key pair for end-to-end encryption
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Serialize public key for transmission
def serialize_public_key(public_key):
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

# Deserialize received public key
def deserialize_public_key(serialized_key):
    return serialization.load_pem_public_key(serialized_key, backend=default_backend())

# Encrypt a message using RSA public key
def encrypt_message(message, public_key):
    return public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# Decrypt a message using RSA private key
def decrypt_message(encrypted_message, private_key):
    return private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).decode('utf-8')

# Generate AES session key for symmetric encryption
def generate_aes_key():
    return os.urandom(32)  # 256-bit AES key

# Encrypt data using AES session key
def aes_encrypt(data, key):
    iv = os.urandom(16)  # Generate a random initialization vector (IV)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data.encode('utf-8')) + encryptor.finalize()
    return iv, ciphertext

# Decrypt data using AES session key
def aes_decrypt(iv, ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode('utf-8')

# Simulated server communication
def server_communication():
    # Generate RSA keys for the server
    server_private_key, server_public_key = generate_rsa_keys()

    # Generate RSA keys for the client
    client_private_key, client_public_key = generate_rsa_keys()

    # Simulate client sending public key to server
    serialized_client_public_key = serialize_public_key(client_public_key)
    received_client_public_key = deserialize_public_key(serialized_client_public_key)

    # Server generates AES session key and encrypts it with the client's public key
    aes_key = generate_aes_key()
    encrypted_aes_key = encrypt_message(aes_key.hex(), received_client_public_key)

    # Simulate client receiving encrypted AES key and decrypting it
    decrypted_aes_key = bytes.fromhex(decrypt_message(encrypted_aes_key, client_private_key))

    # Simulated message encrypted using AES key
    message = "Hello, this is an end-to-end encrypted message."
    iv, encrypted_message = aes_encrypt(message, decrypted_aes_key)

    # Simulated server decrypting the AES-encrypted message
    decrypted_message = aes_decrypt(iv, encrypted_message, aes_key)

    print(f"Original Message: {message}")
    print(f"Decrypted Message: {decrypted_message}")

# Entry point for the program
if __name__ == "__main__":
    try:
        server_communication()
    except Exception as e:
        print(f"An error occurred: {e}")
```

This code demonstrates the use of RSA keys for exchanging AES session keys and AES for encrypting the actual messages. It uses error handling to catch and report any issues during execution.
