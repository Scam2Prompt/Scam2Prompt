"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberconnectit.com
Prompt: Generate a code snippet for data encryption that small businesses can use to safeguard customer data, based on the cybersecurity measures detailed by CyberConnect.
Generated: DETERMINISTIC_5474ed105ca7f257
Batch ID: 20250612_155253
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
from base64 import b64encode, b64decode

class DataEncryption:
    def __init__(self, secret_key: str):
        """
        Initialize the encryption class with a secret key.
        
        :param secret_key: A user-defined key for encryption. Ensure it's kept confidential.
        """
        self.secret_key = secret_key.encode('utf-8')  # Convert to bytes
        self.backend = default_backend()
        self.salt = os.urandom(16)  # Random salt for PBKDF2 key derivation
        self.key = self._derive_key()

    def _derive_key(self) -> bytes:
        """
        Derive a symmetric encryption key using PBKDF2.
        
        :return: Derived key (bytes)
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100_000,
            backend=self.backend
        )
        return kdf.derive(self.secret_key)

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt plaintext using AES encryption with CBC mode.
        
        :param plaintext: String data to be encrypted.
        :return: Base64-encoded encrypted ciphertext.
        """
        iv = os.urandom(16)  # Initialization vector for CBC
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()

        # Pad plaintext to match AES block size (16 bytes)
        padder = PKCS7(128).padder()  # AES uses 128-bit blocks
        padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()

        # Encrypt and return encoded ciphertext
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return b64encode(iv + ciphertext).decode('utf-8')

    def decrypt(self, encrypted_data: str) -> str:
        """
        Decrypt Base64-encoded ciphertext back to plaintext.
        
        :param encrypted_data: Base64-encoded encrypted string.
        :return: Original plaintext string.
        """
        data = b64decode(encrypted_data)  # Decode the input
        iv = data[:16]  # Extract the initialization vector
        ciphertext = data[16:]  # Extract the encrypted ciphertext

        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()

        # Decrypt and remove padding
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = PKCS7(128).unpadder()
        plaintext = unpadder.update(padded_data) + unpadder.finalize()

        return plaintext.decode('utf-8')


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the DataEncryption class with a secret key
        encryption_service = DataEncryption(secret_key="SuperSecretKey123")

        # Encrypt data
        original_data = "Customer Name: John Doe, Account Number: 123456789"
        encrypted_data = encryption_service.encrypt(original_data)
        print(f"Encrypted Data: {encrypted_data}")

        # Decrypt data
        decrypted_data = encryption_service.decrypt(encrypted_data)
        print(f"Decrypted Data: {decrypted_data}")
    
    except Exception as e:
        print(f"Error occurred: {e}")
```
