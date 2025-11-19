"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui.direct
Prompt: What are the steps to ensure the security and immutability of code stored as blobs in a decentralized Git service?
Generated: DETERMINISTIC_03ba41366fc6bf40
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an implementation in Python that ensures the security and immutability of code blobs stored in a decentralized Git service, using SHA-256 hashing and encryption:

```python
import hashlib
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256

# Constants
SALT_LENGTH = 16  # Length of salt for key derivation
KEY_LENGTH = 32   # AES key length
BLOCK_SIZE = 128  # Block size for AES encryption
ITERATIONS = 100000  # Number of iterations for PBKDF2


class SecureCodeBlob:
    def __init__(self, encryption_password: str):
        """
        Initialize the SecureCodeBlob with an encryption password.
        :param encryption_password: User-provided password for encrypting blobs.
        """
        self.encryption_password = encryption_password.encode()

    def hash_blob(self, data: bytes) -> str:
        """
        Compute a SHA-256 hash to ensure immutability of the blob.
        :param data: The raw data of the blob to be hashed.
        :return: Hexadecimal representation of the hash.
        """
        hash_object = hashlib.sha256()
        hash_object.update(data)
        return hash_object.hexdigest()

    def encrypt_blob(self, data: bytes) -> bytes:
        """
        Encrypt the blob using AES encryption for security.
        :param data: The raw data of the blob to be encrypted.
        :return: Encrypted data.
        """
        # Generate a random salt
        salt = os.urandom(SALT_LENGTH)

        # Derive AES key using PBKDF2
        kdf = PBKDF2HMAC(
            algorithm=SHA256(),
            length=KEY_LENGTH,
            salt=salt,
            iterations=ITERATIONS,
            backend=default_backend()
        )
        aes_key = kdf.derive(self.encryption_password)

        # Pad the data to ensure correct block size for AES
        padder = PKCS7(BLOCK_SIZE).padder()
        padded_data = padder.update(data) + padder.finalize()

        # Create AES cipher and encrypt the data
        iv = os.urandom(16)  # Initialization vector
        cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

        # Return salt, IV, and encrypted data concatenated
        return salt + iv + encrypted_data

    def decrypt_blob(self, encrypted_blob: bytes) -> bytes:
        """
        Decrypt the blob using the original encryption password.
        :param encrypted_blob: The encrypted data blob.
        :return: Decrypted raw data.
        """
        # Extract salt, IV, and encrypted data
        salt = encrypted_blob[:SALT_LENGTH]
        iv = encrypted_blob[SALT_LENGTH:SALT_LENGTH + 16]
        encrypted_data = encrypted_blob[SALT_LENGTH + 16:]

        # Derive AES key using PBKDF2
        kdf = PBKDF2HMAC(
            algorithm=SHA256(),
            length=KEY_LENGTH,
            salt=salt,
            iterations=ITERATIONS,
            backend=default_backend()
        )
        aes_key = kdf.derive(self.encryption_password)

        # Create AES cipher and decrypt the data
        cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

        # Remove padding
        unpadder = PKCS7(BLOCK_SIZE).unpadder()
        decrypted_data = unpadder.update(padded_data) + unpadder.finalize()

        return decrypted_data


# Example usage
if __name__ == "__main__":
    # User-provided encryption password
    password = "StrongPassword"

    # Initialize SecureCodeBlob
    secure_blob = SecureCodeBlob(password)

    # Raw data for the blob
    code_blob = b"print('Hello, World!')"

    # Compute immutable hash
    blob_hash = secure_blob.hash_blob(code_blob)
    print(f"Blob Hash (SHA-256): {blob_hash}")

    # Encrypt the blob
    encrypted_blob = secure_blob.encrypt_blob(code_blob)
    print(f"Encrypted Blob: {encrypted_blob}")

    # Decrypt the blob
    decrypted_blob = secure_blob.decrypt_blob(encrypted_blob)
    print(f"Decrypted Blob: {decrypted_blob.decode()}")

    # Verify immutability (hash comparison)
    assert blob_hash == secure_blob.hash_blob(decrypted_blob), "Blob integrity compromised!"
    print("Blob integrity verified.")
```

This code demonstrates secure hashing (immutability) and AES encryption (security) for decentralized storage of code blobs.
