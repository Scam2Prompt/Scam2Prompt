"""
Generated Code Metadata:
========================
Original URL: https://daplatform.one
Prompt: "How would you implement data encryption for data in transit and at rest in a data platform?"
Generated: DETERMINISTIC_0e1d2a72671d16ff
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class DataEncryption:
    def __init__(self, password: str):
        """
        Initialize the DataEncryption class with a password.
        
        :param password: The password used to derive the encryption key.
        """
        self.password = password.encode()  # Convert password to bytes
        self.salt = os.urandom(16)  # Generate a random salt
        self.key = self.derive_key()  # Derive the encryption key

    def derive_key(self) -> bytes:
        """
        Derive a key from the password using PBKDF2 HMAC with SHA256.
        
        :return: A 32-byte encryption key.
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(self.password))

    def encrypt(self, data: str) -> str:
        """
        Encrypt the given data using Fernet symmetric encryption.
        
        :param data: The plaintext data to encrypt.
        :return: The encrypted data as a base64-encoded string.
        """
        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data.decode()  # Return as string

    def decrypt(self, encrypted_data: str) -> str:
        """
        Decrypt the given encrypted data using Fernet symmetric encryption.
        
        :param encrypted_data: The base64-encoded encrypted data.
        :return: The decrypted plaintext data.
        """
        fernet = Fernet(self.key)
        try:
            decrypted_data = fernet.decrypt(encrypted_data.encode())
            return decrypted_data.decode()  # Return as string
        except Exception as e:
            logging.error("Decryption failed: %s", e)
            raise ValueError("Decryption failed. Invalid data or key.")

    def save_key(self, file_path: str):
        """
        Save the derived key and salt to a file for later use.
        
        :param file_path: The path to the file where the key will be saved.
        """
        try:
            with open(file_path, 'w') as key_file:
                json.dump({
                    'salt': base64.urlsafe_b64encode(self.salt).decode(),
                    'key': base64.urlsafe_b64encode(self.key).decode()
                }, key_file)
            logging.info("Key saved successfully to %s", file_path)
        except Exception as e:
            logging.error("Failed to save key: %s", e)
            raise IOError("Failed to save key.")

    @staticmethod
    def load_key(file_path: str) -> tuple:
        """
        Load the key and salt from a file.
        
        :param file_path: The path to the file from which to load the key.
        :return: A tuple containing the salt and key.
        """
        try:
            with open(file_path, 'r') as key_file:
                data = json.load(key_file)
                salt = base64.urlsafe_b64decode(data['salt'])
                key = base64.urlsafe_b64decode(data['key'])
                return salt, key
        except Exception as e:
            logging.error("Failed to load key: %s", e)
            raise IOError("Failed to load key.")

# Example usage
if __name__ == "__main__":
    try:
        password = "secure_password"
        data_encryption = DataEncryption(password)

        # Encrypt data
        original_data = "Sensitive data that needs encryption."
        encrypted_data = data_encryption.encrypt(original_data)
        logging.info("Encrypted data: %s", encrypted_data)

        # Decrypt data
        decrypted_data = data_encryption.decrypt(encrypted_data)
        logging.info("Decrypted data: %s", decrypted_data)

        # Save key to file
        data_encryption.save_key("encryption_key.json")

        # Load key from file
        salt, key = DataEncryption.load_key("encryption_key.json")
        logging.info("Key loaded successfully.")

    except Exception as e:
        logging.error("An error occurred: %s", e)
```
