"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: How can I implement a secure document storage system using the techniques described by EasyDoc for managing corporate files?
Generated: DETERMINISTIC_ac6c9aa9d368282d
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a secure document storage system. It uses techniques for encryption, file management, and secure authentication. The implementation is designed using Python.

```python
import os
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.keywrap import aes_key_wrap, aes_key_unwrap
from cryptography.exceptions import InvalidKey

# Configuration for secure document storage
STORAGE_DIRECTORY = "./secure_documents"
SALT = b"EasyDocSalt123456"  # A fixed salt for key derivation (use a secure one in production)
KEY_ITERATIONS = 100_000    # Number of iterations for PBKDF2
KEY_LENGTH = 32             # AES-256 key length

# Ensure the storage directory exists
os.makedirs(STORAGE_DIRECTORY, exist_ok=True)

def derive_key(password: str) -> bytes:
    """
    Derive a secure encryption key from a user-provided password using PBKDF2.
    """
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=KEY_LENGTH,
        salt=SALT,
        iterations=KEY_ITERATIONS,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(filepath: str, password: str) -> str:
    """
    Encrypt a file and store it securely in the storage directory.
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File '{filepath}' not found.")

    # Generate encryption key from password
    encryption_key = derive_key(password)

    # Read file contents
    with open(filepath, 'rb') as file:
        plaintext = file.read()

    # Pad the plaintext to make it compatible with AES block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # Create AES cipher in CBC mode
    iv = os.urandom(16)  # Initialization vector
    cipher = Cipher(algorithms.AES(encryption_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the padded data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Create a secure filename
    secure_filename = hashlib.sha256(filepath.encode()).hexdigest() + ".enc"
    encrypted_filepath = os.path.join(STORAGE_DIRECTORY, secure_filename)

    # Store the encrypted file along with the IV
    with open(encrypted_filepath, 'wb') as encrypted_file:
        encrypted_file.write(iv + ciphertext)

    return encrypted_filepath

def decrypt_file(encrypted_filepath: str, password: str, output_filepath: str) -> None:
    """
    Decrypt an encrypted file and save it to the specified output path.
    """
    if not os.path.isfile(encrypted_filepath):
        raise FileNotFoundError(f"Encrypted file '{encrypted_filepath}' not found.")

    # Generate encryption key from password
    encryption_key = derive_key(password)

    # Read encrypted file contents
    with open(encrypted_filepath, 'rb') as encrypted_file:
        data = encrypted_file.read()

    # Separate the IV and ciphertext
    iv = data[:16]
    ciphertext = data[16:]

    # Create AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(encryption_key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    # Write the decrypted data to the output file
    with open(output_filepath, 'wb') as output_file:
        output_file.write(plaintext)

def list_encrypted_files() -> list:
    """
    List all encrypted files in the storage directory.
    """
    return [f for f in os.listdir(STORAGE_DIRECTORY) if f.endswith(".enc")]

def delete_encrypted_file(encrypted_filepath: str) -> None:
    """
    Delete an encrypted file from the storage directory.
    """
    if os.path.isfile(encrypted_filepath):
        os.remove(encrypted_filepath)
    else:
        raise FileNotFoundError(f"File '{encrypted_filepath}' not found.")

# Example usage:
# Encrypt a file
# encrypted_file = encrypt_file("example.txt", "securepassword")
# Decrypt the file
# decrypt_file(encrypted_file, "securepassword", "example_decrypted.txt")
# List encrypted files
# print(list_encrypted_files())
# Delete an encrypted file
# delete_encrypted_file(encrypted_file)
```

This code ensures secure storage, encryption, and decryption of files using AES encryption and best practices like padding and key derivation. It also includes error handling for invalid files and provides utility functions for managing stored documents.
