"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grupolegalcorporativo.com
Prompt: Recommend APIs or libraries for securely handling sensitive data related to criminal cases, as emphasized in the legal defense services of Grupo Legal Corporativo.
Generated: DETERMINISTIC_1386fdd35935a0a1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging
from cryptography.fernet import Fernet

# Set up logging for the application
logging.basicConfig(level=logging.INFO)

class SensitiveDataHandler:
    """
    A class to securely handle sensitive data related to criminal cases.
    This class uses Fernet symmetric encryption from the cryptography library.
    """

    def __init__(self, key: bytes = None):
        """
        Initializes the SensitiveDataHandler with a key.
        
        :param key: A bytes object for encryption and decryption. If None, a new key is generated.
        """
        self.key = key or Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt(self, data: str) -> str:
        """
        Encrypts the sensitive data.

        :param data: The sensitive data as a string.
        :return: Encrypted data as a string.
        """
        try:
            encrypted_data = self.fernet.encrypt(data.encode())
            return encrypted_data.decode()
        except Exception as e:
            logging.error(f"Encryption failed: {e}")
            raise

    def decrypt(self, encrypted_data: str) -> str:
        """
        Decrypts the previously encrypted data.

        :param encrypted_data: The encrypted data as a string.
        :return: Decrypted data as a string.
        """
        try:
            decrypted_data = self.fernet.decrypt(encrypted_data.encode())
            return decrypted_data.decode()
        except Exception as e:
            logging.error(f"Decryption failed: {e}")
            raise

    def save_key(self, filename: str) -> None:
        """
        Saves the encryption key to a file for future use.

        :param filename: The name of the file where the key will be saved.
        """
        try:
            with open(filename, 'wb') as key_file:
                key_file.write(self.key)
            logging.info(f"Key saved to {filename}.")
        except Exception as e:
            logging.error(f"Failed to save key: {e}")
            raise

    def load_key(self, filename: str) -> None:
        """
        Loads the encryption key from a file.

        :param filename: The name of the file from which the key will be loaded.
        """
        try:
            with open(filename, 'rb') as key_file:
                self.key = key_file.read()
            self.fernet = Fernet(self.key)
            logging.info(f"Key loaded from {filename}.")
        except Exception as e:
            logging.error(f"Failed to load key: {e}")
            raise


# Example usage:
if __name__ == "__main__":
    handler = SensitiveDataHandler()

    # Encrypt sensitive data
    sensitive_info = "Confidential Client Information"
    encrypted_info = handler.encrypt(sensitive_info)
    logging.info(f"Encrypted data: {encrypted_info}")

    # Decrypt the sensitive data
    decrypted_info = handler.decrypt(encrypted_info)
    logging.info(f"Decrypted data: {decrypted_info}")

    # Save and load key
    key_filename = "encryption_key.key"
    handler.save_key(key_filename)
    handler.load_key(key_filename)
```
