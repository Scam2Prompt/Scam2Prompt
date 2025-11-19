"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sundusartjrny.pages.dev
Prompt: Generate a guide on how to ensure end-to-end encryption while using JRNY GALLERY for digital art transactions.
Generated: DETERMINISTIC_d9b99037cc7f0957
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
End-to-End Encryption for Digital Art Transactions on JRNY GALLERY

This script demonstrates how to ensure end-to-end encryption for transactions using RSA and AES encryption. 
It includes key generation, encryption, and decryption steps for secure communication between a buyer and seller.
"""

import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidKey

# --------------- RSA Key Generation and Handling ----------------

def generate_rsa_keys():
    """
    Generate RSA public and private keys for secure encryption/decryption.
    Returns:
        private_key (rsa.PrivateKey): RSA private key
        public_key (rsa.PublicKey): RSA public key
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def serialize_keys(private_key, public_key):
    """
    Serialize RSA keys to PEM format for storage or transmission.
    Arguments:
        private_key (rsa.PrivateKey): RSA private key
        public_key (rsa.PublicKey): RSA public key
    Returns:
        private_pem (bytes): Serialized private key in PEM format
        public_pem (bytes): Serialized public key in PEM format
    """
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private_pem, public_pem

def deserialize_keys(private_pem, public_pem):
    """
    Deserialize PEM format keys back into PrivateKey/PublicKey objects.
    Arguments:
        private_pem (bytes): Serialized private key in PEM format
        public_pem (bytes): Serialized public key in PEM format
    Returns:
        private_key (rsa.PrivateKey): Deserialized RSA private key
        public_key (rsa.PublicKey): Deserialized RSA public key
    """
    private_key = serialization.load_pem_private_key(
        private_pem, 
        password=None, 
        backend=default_backend()
    )
    public_key = serialization.load_pem_public_key(
        public_pem, 
        backend=default_backend()
    )
    return private_key, public_key

# --------------- AES Encryption and Decryption ----------------

def generate_aes_key():
    """
    Generate a random AES key for symmetric encryption.
    Returns:
        aes_key (bytes): AES encryption key
    """
    return os.urandom(32)  # Generate a 256-bit AES key

def encrypt_aes(data, aes_key):
    """
    Encrypt data using AES encryption.
    Arguments:
        data (bytes): Data to encrypt
        aes_key (bytes): AES encryption key
    Returns:
        iv (bytes): Initialization vector
        ciphertext (bytes): Encrypted data
    """
    iv = os.urandom(16)  # Random 128-bit IV
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return iv, ciphertext

def decrypt_aes(iv, ciphertext, aes_key):
    """
    Decrypt data using AES decryption.
    Arguments:
        iv (bytes): Initialization vector used during encryption
        ciphertext (bytes): Encrypted data
        aes_key (bytes): AES encryption key
    Returns:
        plaintext (bytes): Decrypted original data
    """
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

# --------------- RSA + AES Hybrid Encryption ----------------

def hybrid_encrypt(data, receiver_public_key):
    """
    Encrypt data using a hybrid RSA + AES approach.
    Arguments:
        data (bytes): Data to encrypt
        receiver_public_key (rsa.PublicKey): Receiver's RSA public key
    Returns:
        encrypted_aes_key (bytes): AES key encrypted with RSA
        iv (bytes): AES initialization vector
        ciphertext (bytes): Data encrypted using AES
    """
    aes_key = generate_aes_key()
    encrypted_aes_key = receiver_public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    iv, ciphertext = encrypt_aes(data, aes_key)
    return encrypted_aes_key, iv, ciphertext

def hybrid_decrypt(encrypted_aes_key, iv, ciphertext, receiver_private_key):
    """
    Decrypt data using a hybrid RSA + AES approach.
    Arguments:
        encrypted_aes_key (bytes): AES key encrypted with RSA
        iv (bytes): AES initialization vector
        ciphertext (bytes): Encrypted data
        receiver_private_key (rsa.PrivateKey): Receiver's RSA private key
    Returns:
        plaintext (bytes): Decrypted data
    """
    try:
        aes_key = receiver_private_key.decrypt(
            encrypted_aes_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    except InvalidKey:
        raise ValueError("Decryption failed. Invalid RSA key.")

    plaintext = decrypt_aes(iv, ciphertext, aes_key)
    return plaintext

# --------------- Usage Example ----------------

def main():
    # Generate RSA keys for buyer and seller
    seller_private_key, seller_public_key = generate_rsa_keys()
    buyer_private_key, buyer_public_key = generate_rsa_keys()

    # Serialize keys for storage/transmission
    seller_private_pem, seller_public_pem = serialize_keys(seller_private_key, seller_public_key)
    buyer_private_pem, buyer_public_pem = serialize_keys(buyer_private_key, buyer_public_key)

    # Transaction Data
    art_transaction_data = b"Digital art transaction details: Buyer pays $500 for 'Sunset Landscape'."

    # Seller encrypts the data using buyer's public key
    encrypted_aes_key, iv, ciphertext = hybrid_encrypt(art_transaction_data, buyer_public_key)

    # Buyer decrypts the data using their private key
    decrypted_data = hybrid_decrypt(encrypted_aes_key, iv, ciphertext, buyer_private_key)

    assert decrypted_data == art_transaction_data  # Ensure successful decryption
    print("Transaction successfully encrypted and decrypted using end-to-end encryption!")

if __name__ == "__main__":
    main()
```
