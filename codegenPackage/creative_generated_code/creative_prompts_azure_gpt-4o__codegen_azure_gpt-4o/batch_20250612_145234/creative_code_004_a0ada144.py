"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://districtchronicles.com
Prompt: Suggest technologies or frameworks for developing a secure, encrypted system for handling user data, inspired by Pixxie928's "ระบบเข้ารหัสข้อมูล" for protecting personal information.
Generated: DETERMINISTIC_a0ada14482962bf4
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from cryptography.fernet import Fernet
import os

class SecureDataHandler:
    """
    A secure system for handling user data with encryption and decryption mechanisms.
    Uses the cryptography library for strong encryption.
    """

    def __init__(self, key_file: str = "encryption_key.key"):
        """
        Initializes the SecureDataHandler with a key file for encryption and decryption.

        :param key_file: Filepath for storing the encryption key.
        """
        self.key_file = key_file
        self.key = self._load_or_generate_key()

    def _load_or_generate_key(self) -> bytes:
        """
        Loads an existing encryption key from the key file or generates a new one.

        :return: The encryption key as bytes.
        """
        if os.path.exists(self.key_file):
            # Load existing key
            with open(self.key_file, "rb") as key_file:
                return key_file.read()
        else:
            # Generate a new key
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as key_file:
                key_file.write(key)
            return key

    def encrypt_data(self, data: str) -> bytes:
        """
        Encrypts the given data using the encryption key.

        :param data: The plaintext data to encrypt.
        :return: The encrypted data as bytes.
        """
        try:
            fernet = Fernet(self.key)
            encrypted_data = fernet.encrypt(data.encode())
            return encrypted_data
        except Exception as e:
            raise ValueError(f"Error encrypting data: {e}")

    def decrypt_data(self, encrypted_data: bytes) -> str:
        """
        Decrypts the given encrypted data using the encryption key.

        :param encrypted_data: The encrypted data to decrypt.
        :return: The decrypted plaintext data as a string.
        """
        try:
            fernet = Fernet(self.key)
            decrypted_data = fernet.decrypt(encrypted_data).decode()
            return decrypted_data
        except Exception as e:
            raise ValueError(f"Error decrypting data: {e}")

if __name__ == "__main__":
    # Example usage of SecureDataHandler
    handler = SecureDataHandler()

    # Data to protect
    user_data = "Sensitive Personal Information"

    # Encrypt the data
    encrypted = handler.encrypt_data(user_data)
    print(f"Encrypted Data: {encrypted}")

    # Decrypt the data
    decrypted = handler.decrypt_data(encrypted)
    print(f"Decrypted Data: {decrypted}")
```
