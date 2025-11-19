"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smog-token-en.web.app
Prompt: What are the security measures in place for transactions involving $SMOG tokens, and how can I protect my private keys?
Generated: DETERMINISTIC_f4a08491817b0e84
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to demonstrate security measures for transactions involving $SMOG tokens 
and how to protect private keys. 

This code showcases essential practices for working with blockchain-based transactions,
including private key protection.
"""

import os
import hashlib
import json
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Constants for security
SALT = os.urandom(16)  # Randomly generated salt for PBKDF2
AES_KEY_SIZE = 32  # Key size for AES encryption (256-bit)

def generate_private_key(password: str) -> bytes:
    """
    Generate an RSA private key and encrypt it using AES with a password.
    
    :param password: User-provided password for encrypting the private key.
    :return: Encrypted private key in bytes.
    """
    try:
        # Generate RSA private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        # Serialize the private key
        private_key_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        # Derive AES encryption key from password
        kdf = PBKDF2HMAC(
            algorithm=SHA256(),
            length=AES_KEY_SIZE,
            salt=SALT,
            iterations=100000,
            backend=default_backend()
        )
        aes_key = kdf.derive(password.encode())

        # Encrypt the private key using AES
        cipher = Cipher(algorithms.AES(aes_key), modes.CFB(SALT), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_private_key = encryptor.update(private_key_bytes) + encryptor.finalize()

        return encrypted_private_key
    except Exception as e:
        print(f"Error while generating/encrypting private key: {e}")
        raise

def decrypt_private_key(encrypted_key: bytes, password: str) -> rsa.RSAPrivateKey:
    """
    Decrypt the RSA private key using the provided password.
    
    :param encrypted_key: Encrypted private key in bytes.
    :param password: User-provided password for decrypting the private key.
    :return: RSA private key object.
    """
    try:
        # Derive AES encryption key from password
        kdf = PBKDF2HMAC(
            algorithm=SHA256(),
            length=AES_KEY_SIZE,
            salt=SALT,
            iterations=100000,
            backend=default_backend()
        )
        aes_key = kdf.derive(password.encode())

        # Decrypt the private key using AES
        cipher = Cipher(algorithms.AES(aes_key), modes.CFB(SALT), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_private_key_bytes = decryptor.update(encrypted_key) + decryptor.finalize()

        # Load the RSA private key from the decrypted bytes
        private_key = serialization.load_pem_private_key(
            decrypted_private_key_bytes,
            password=None,
            backend=default_backend()
        )

        return private_key
    except Exception as e:
        print(f"Error while decrypting private key: {e}")
        raise

def sign_transaction(private_key: rsa.RSAPrivateKey, transaction_data: dict) -> bytes:
    """
    Sign a transaction using the RSA private key.
    
    :param private_key: RSA private key object.
    :param transaction_data: Transaction data to sign.
    :return: Digital signature in bytes.
    """
    try:
        # Hash the transaction data
        transaction_hash = hashlib.sha256(json.dumps(transaction_data).encode()).digest()

        # Sign the hash with the private key
        signature = private_key.sign(
            transaction_hash,
            padding.PSS(
                mgf=padding.MGF1(SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            SHA256()
        )

        return signature
    except Exception as e:
        print(f"Error while signing transaction: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # User password for key encryption
    user_password = "strong_password_123"
    
    # Generate and encrypt private key
    encrypted_key = generate_private_key(user_password)
    print("Private key securely encrypted.")

    # Decrypt private key
    private_key = decrypt_private_key(encrypted_key, user_password)
    print("Private key successfully decrypted.")

    # Example transaction data
    transaction = {"amount": 100, "token": "$SMOG", "recipient": "address_12345"}
    
    # Sign transaction
    signature = sign_transaction(private_key, transaction)
    print(f"Transaction signed. Signature: {signature.hex()}")

    # Users should store password securely and avoid sharing private keys.
    print("Keep private keys protected and use strong passwords.")
```
