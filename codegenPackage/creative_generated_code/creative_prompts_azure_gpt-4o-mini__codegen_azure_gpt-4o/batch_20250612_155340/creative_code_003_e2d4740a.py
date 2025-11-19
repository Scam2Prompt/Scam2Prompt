"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mymonero.co
Prompt: Explain how to implement local encryption for app data in a MyMonero-like application, ensuring user privacy and security.
Generated: DETERMINISTIC_e2d4740ad75d5f42
Batch ID: 20250612_155340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hmac

# Function to derive a secure key from a passphrase
def derive_key(passphrase: str, salt: bytes) -> bytes:
    """
    Derives a symmetric encryption key using PBKDF2.
    Args:
        passphrase (str): The user-provided passphrase.
        salt (bytes): A random salt for key derivation.
    Returns:
        bytes: The derived symmetric encryption key.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashlib.sha256,
        length=32,  # Length of the derived key
        salt=salt,
        iterations=100_000,  # Iterations for key derivation
        backend=default_backend()
    )
    return kdf.derive(passphrase.encode('utf-8'))

# Function to encrypt data
def encrypt_data(data: bytes, key: bytes) -> tuple:
    """
    Encrypts application data using AES with CBC mode and PKCS7 padding.
    Args:
        data (bytes): Data to encrypt.
        key (bytes): Symmetric key for encryption.
    Returns:
        tuple: (encrypted_data, initialization_vector)
    """
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Create AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad the data before encryption
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Encrypt the data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return encrypted_data, iv

# Function to decrypt data
def decrypt_data(encrypted_data: bytes, key: bytes, iv: bytes) -> bytes:
    """
    Decrypts application data using AES with CBC mode and PKCS7 padding.
    Args:
        encrypted_data (bytes): Data to decrypt.
        key (bytes): Symmetric key for decryption.
        iv (bytes): Initialization vector used during encryption.
    Returns:
        bytes: Decrypted application data.
    """
    # Create AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the data
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding after decryption
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data

# Function to generate a HMAC for integrity verification
def generate_hmac(data: bytes, key: bytes) -> bytes:
    """
    Generates a HMAC for the given data to ensure its integrity.
    Args:
        data (bytes): Data to protect.
        key (bytes): Symmetric key for HMAC generation.
    Returns:
        bytes: The HMAC.
    """
    h = hmac.HMAC(key, hashlib.sha256(), backend=default_backend())
    h.update(data)
    return h.finalize()

# Example usage
if __name__ == "__main__":
    try:
        # User-provided passphrase (keep it secure)
        passphrase = "secure-passphrase"

        # Generate a random salt for key derivation
        salt = os.urandom(16)

        # Derive a symmetric key from the passphrase
        key = derive_key(passphrase, salt)

        # Example data to encrypt
        app_data = b"Sensitive application data"

        # Encrypt the data
        encrypted_data, iv = encrypt_data(app_data, key)

        # Generate HMAC for integrity verification
        data_hmac = generate_hmac(encrypted_data, key)

        # Decrypt the data
        decrypted_data = decrypt_data(encrypted_data, key, iv)

        # Verify integrity by regenerating HMAC and comparing
        regenerated_hmac = generate_hmac(encrypted_data, key)
        if regenerated_hmac != data_hmac:
            raise ValueError("Data integrity verification failed!")

        # Print results
        print("Original Data:", app_data)
        print("Encrypted Data:", encrypted_data)
        print("Decrypted Data:", decrypted_data)
        print("Integrity Verified:", regenerated_hmac == data_hmac)

    except Exception as e:
        print(f"An error occurred: {e}")
```
