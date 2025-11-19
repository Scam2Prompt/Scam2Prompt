"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-phantom-zone.xyz
Prompt: Create a sample code snippet that demonstrates how to implement data encryption during transmission for a mobile game app, referencing the security measures mentioned on play-phantom-zone.xyz.
Generated: DETERMINISTIC_ce5001e1e1ac34ab
Batch ID: 20250612_155521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7
import base64

# Key Derivation Function (KDF) parameters
SALT_LENGTH = 16  # Length of the salt
ITERATIONS = 100_000  # Number of iterations for PBKDF2
KEY_LENGTH = 32      # Length of AES-256 key in bytes

# AES block size
BLOCK_SIZE = 128  # AES block size in bits

# Encryption function
def encrypt_data(plain_text, password):
    """
    Encrypts the provided plaintext using AES-256 with a password-derived key.

    Args:
        plain_text (str): The plaintext to encrypt.
        password (str): The password used to derive the encryption key.
    
    Returns:
        dict: A dictionary containing the encrypted data and the salt.
    """
    try:
        # Generate a random salt
        salt = os.urandom(SALT_LENGTH)

        # Derive a key from the password using PBKDF2
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=KEY_LENGTH,
            salt=salt,
            iterations=ITERATIONS,
            backend=default_backend()
        )
        key = kdf.derive(password.encode())

        # Create an AES cipher object in CBC mode
        iv = os.urandom(16)  # Generate a random initialization vector (IV)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        # Pad the plaintext to make its length a multiple of the block size
        padder = PKCS7(BLOCK_SIZE).padder()
        padded_data = padder.update(plain_text.encode()) + padder.finalize()

        # Encrypt the padded plaintext
        cipher_text = encryptor.update(padded_data) + encryptor.finalize()

        # Return the cipher text, salt, and IV as base64-encoded strings for safe transmission
        return {
            'cipher_text': base64.b64encode(cipher_text).decode(),
            'salt': base64.b64encode(salt).decode(),
            'iv': base64.b64encode(iv).decode()
        }
    except Exception as e:
        # Handle encryption errors gracefully
        raise RuntimeError(f"Encryption failed: {str(e)}")

# Decryption function
def decrypt_data(encrypted_data, password):
    """
    Decrypts the provided ciphertext using AES-256 with a password-derived key.

    Args:
        encrypted_data (dict): A dictionary containing the encrypted data, salt, and IV.
        password (str): The password used to derive the decryption key.
    
    Returns:
        str: The decrypted plaintext.
    """
    try:
        # Decode the base64-encoded values
        cipher_text = base64.b64decode(encrypted_data['cipher_text'])
        salt = base64.b64decode(encrypted_data['salt'])
        iv = base64.b64decode(encrypted_data['iv'])

        # Derive a key from the password using PBKDF2
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=KEY_LENGTH,
            salt=salt,
            iterations=ITERATIONS,
            backend=default_backend()
        )
        key = kdf.derive(password.encode())

        # Create an AES cipher object in CBC mode
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        # Decrypt the ciphertext
        padded_data = decryptor.update(cipher_text) + decryptor.finalize()

        # Remove padding to retrieve the original plaintext
        unpadder = PKCS7(BLOCK_SIZE).unpadder()
        plain_text = unpadder.update(padded_data) + unpadder.finalize()

        return plain_text.decode()
    except Exception as e:
        # Handle decryption errors gracefully
        raise RuntimeError(f"Decryption failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Use a secure password for encryption/decryption
    password = "secure_password"

    # Example plaintext data to encrypt
    plaintext = "This is sensitive game data."

    # Encrypt the plaintext
    encrypted = encrypt_data(plaintext, password)
    print("Encrypted data:", encrypted)

    # Decrypt the encrypted data
    decrypted = decrypt_data(encrypted, password)
    print("Decrypted data:", decrypted)
```

Note:
- This example uses `cryptography` library for AES encryption with CBC mode and PKCS7 padding.
- Be sure to install the `cryptography` library (`pip install cryptography`) before running this code.
- Replace `secure_password` with a user-provided password for real-world applications.
