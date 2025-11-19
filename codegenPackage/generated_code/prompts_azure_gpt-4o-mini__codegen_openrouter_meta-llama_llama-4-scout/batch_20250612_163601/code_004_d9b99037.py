"""
Generated Code Metadata:
========================
Original URL: https://sundusartjrny.pages.dev
Prompt: Generate a guide on how to ensure end-to-end encryption while using JRNY GALLERY for digital art transactions.
Generated: DETERMINISTIC_d9b99037cc7f0957
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# guide_to_end_to_end_encryption.py

import os
import hashlib
import hmac
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_keys():
    """
    Generate a new RSA key pair for encryption.
    
    Returns:
        private_key (bytes): The private key in PEM format.
        public_key (bytes): The public key in PEM format.
    """
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    private_key = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key = key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private_key, public_key

def encrypt_data(data: bytes, public_key: bytes):
    """
    Encrypt data using the provided public key.
    
    Args:
        data (bytes): The data to be encrypted.
        public_key (bytes): The public key in PEM format.
    
    Returns:
        encrypted_data (bytes): The encrypted data.
    """
    public_key_loaded = serialization.load_pem_public_key(
        public_key,
    )
    encrypted_data = public_key_loaded.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_data

def decrypt_data(encrypted_data: bytes, private_key: bytes):
    """
    Decrypt data using the provided private key.
    
    Args:
        encrypted_data (bytes): The encrypted data.
        private_key (bytes): The private key in PEM format.
    
    Returns:
        data (bytes): The decrypted data.
    """
    private_key_loaded = serialization.load_pem_private_key(
        private_key,
        password=None,
    )
    data = private_key_loaded.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return data

def generate_fernet_key():
    """
    Generate a new Fernet key for symmetric encryption.
    
    Returns:
        fernet_key (bytes): The Fernet key.
    """
    return Fernet.generate_key()

def encrypt_data_symmetric(data: bytes, fernet_key: bytes):
    """
    Encrypt data using the provided Fernet key.
    
    Args:
        data (bytes): The data to be encrypted.
        fernet_key (bytes): The Fernet key.
    
    Returns:
        encrypted_data (bytes): The encrypted data.
    """
    fernet = Fernet(fernet_key)
    encrypted_data = fernet.encrypt(data)
    return encrypted_data

def decrypt_data_symmetric(encrypted_data: bytes, fernet_key: bytes):
    """
    Decrypt data using the provided Fernet key.
    
    Args:
        encrypted_data (bytes): The encrypted data.
        fernet_key (bytes): The Fernet key.
    
    Returns:
        data (bytes): The decrypted data.
    """
    fernet = Fernet(fernet_key)
    try:
        data = fernet.decrypt(encrypted_data)
        return data
    except Exception as e:
        print(f"Error decrypting data: {e}")
        return None

def verify_data_integrity(data: bytes, signature: bytes, public_key: bytes):
    """
    Verify the integrity of data using the provided signature and public key.
    
    Args:
        data (bytes): The data to be verified.
        signature (bytes): The signature.
        public_key (bytes): The public key in PEM format.
    
    Returns:
        bool: True if the data is valid, False otherwise.
    """
    public_key_loaded = serialization.load_pem_public_key(
        public_key,
    )
    try:
        public_key_loaded.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False

def generate_signature(data: bytes, private_key: bytes):
    """
    Generate a signature for the provided data using the private key.
    
    Args:
        data (bytes): The data to be signed.
        private_key (bytes): The private key in PEM format.
    
    Returns:
        signature (bytes): The signature.
    """
    private_key_loaded = serialization.load_pem_private_key(
        private_key,
        password=None,
    )
    signature = private_key_loaded.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def main():
    # Generate keys
    private_key, public_key = generate_keys()
    fernet_key = generate_fernet_key()

    # Data to be encrypted
    data = b"Hello, World!"

    # Symmetric encryption
    encrypted_data_symmetric = encrypt_data_symmetric(data, fernet_key)
    decrypted_data_symmetric = decrypt_data_symmetric(encrypted_data_symmetric, fernet_key)

    # Asymmetric encryption
    encrypted_data_asymmetric = encrypt_data(data, public_key)
    decrypted_data_asymmetric = decrypt_data(encrypted_data_asymmetric, private_key)

    # Data integrity
    signature = generate_signature(data, private_key)
    is_valid = verify_data_integrity(data, signature, public_key)

    # Print results
    print(f"Original Data: {data}")
    print(f"Symmetric Encrypted Data: {encrypted_data_symmetric}")
    print(f"Symmetric Decrypted Data: {decrypted_data_symmetric}")
    print(f"Asymmetric Encrypted Data: {encrypted_data_asymmetric}")
    print(f"Asymmetric Decrypted Data: {decrypted_data_asymmetric}")
    print(f"Is Data Valid: {is_valid}")

if __name__ == "__main__":
    main()
```
