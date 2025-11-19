"""
Generated Code Metadata:
========================
Original URL: https://cyberconnectit.com
Prompt: Generate a code snippet for data encryption that small businesses can use to safeguard customer data, based on the cybersecurity measures detailed by CyberConnect.
Generated: DETERMINISTIC_5474ed105ca7f257
Batch ID: 20250612_155253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode
import secrets

class DataEncryptor:
    """
    A class to handle encryption and decryption of sensitive data using AES-256 in CBC mode.
    """
    
    def __init__(self):
        """
        Initialize the encryptor with a securely generated key and IV.
        """
        self.key = secrets.token_bytes(32)  # 256-bit key for AES-256
        self.iv = secrets.token_bytes(16)   # 128-bit IV for AES
        
    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the given plaintext using AES-256 in CBC mode.
        
        Args:
            plaintext: The data to be encrypted.
            
        Returns:
            Base64 encoded string containing IV and ciphertext.
            
        Raises:
            ValueError: If plaintext is empty.
        """
        if not plaintext:
            raise ValueError("Plaintext cannot be empty")
            
        # Convert plaintext to bytes
        plaintext_bytes = plaintext.encode('utf-8')
        
        # Pad the plaintext to be a multiple of the block size
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext_bytes) + padder.finalize()
        
        # Encrypt the data
        cipher = Cipher(
            algorithms.AES(self.key),
            modes.CBC(self.iv),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        # Combine IV and ciphertext and return as base64
        combined = self.iv + ciphertext
        return urlsafe_b64encode(combined).decode('utf-8')
        
    def decrypt(self, encrypted_data: str) -> str:
        """
        Decrypts the given encrypted data.
        
        Args:
            encrypted_data: Base64 encoded string containing IV and ciphertext.
            
        Returns:
            Decrypted plaintext string.
            
        Raises:
            ValueError: If encrypted_data is empty or invalid.
        """
        if not encrypted_data:
            raise ValueError("Encrypted data cannot be empty")
            
        try:
            # Decode base64 and split IV and ciphertext
            combined = urlsafe_b64decode(encrypted_data.encode('utf-8'))
            iv = combined[:16]
            ciphertext = combined[16:]
            
            # Decrypt the data
            cipher = Cipher(
                algorithms.AES(self.key),
                modes.CBC(iv),
                backend=default_backend()
            )
            decryptor = cipher.decryptor()
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            
            # Unpad the plaintext
            unpadder = padding.PKCS7(128).unpadder()
            plaintext_bytes = unpadder.update(padded_plaintext) + unpadder.finalize()
            
            return plaintext_bytes.decode('utf-8')
            
        except Exception as e:
            raise ValueError("Decryption failed") from e
            
    def save_key(self, file_path: str):
        """
        Saves the encryption key to a file.
        
        Args:
            file_path: Path to the file where the key will be stored.
            
        Raises:
            IOError: If there's an issue writing the file.
        """
        try:
            with open(file_path, 'wb') as f:
                f.write(self.key)
        except IOError as e:
            raise IOError(f"Failed to save key: {e}")
            
    def load_key(self, file_path: str):
        """
        Loads the encryption key from a file.
        
        Args:
            file_path: Path to the file containing the key.
            
        Raises:
            IOError: If there's an issue reading the file.
            ValueError: If the key is invalid.
        """
        try:
            with open(file_path, 'rb') as f:
                key = f.read()
                if len(key) != 32:
                    raise ValueError("Invalid key length")
                self.key = key
        except IOError as e:
            raise IOError(f"Failed to load key: {e}")
```
