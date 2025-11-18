"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socrates-gm.com
Prompt: Recommend a library for implementing secure offline access to the Socrates GM portal, ensuring no compromise on information security.
Generated: DETERMINISTIC_84e5cb99de5fa5d1
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import cryptography
from cryptography.fernet import Fernet
import os

class SecureOfflineAccess:
    """
    A class to implement secure offline access using encryption.
    This ensures data is encrypted before saving locally and decrypted during access.
    """

    def __init__(self, key_file="encryption_key.key"):
        """
        Initialize the SecureOfflineAccess class.

        :param key_file: Path to the encryption key file. Default is 'encryption_key.key'.
        """
        self.key_file = key_file
        self.key = self.load_or_generate_key()

    def load_or_generate_key(self):
        """
        Load an existing encryption key if available, or generate a new one.

        :return: Encryption key.
        """
        if os.path.exists(self.key_file):
            # Load existing encryption key
            with open(self.key_file, "rb") as key_file:
                return key_file.read()
        else:
            # Generate a new encryption key
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as key_file:
                key_file.write(key)
            return key

    def encrypt_data(self, data):
        """
        Encrypt the data using the encryption key.

        :param data: Data to be encrypted (string).
        :return: Encrypted data (bytes).
        """
        try:
            fernet = Fernet(self.key)
            encrypted_data = fernet.encrypt(data.encode())
            return encrypted_data
        except Exception as e:
            raise ValueError(f"Error encrypting data: {e}")

    def decrypt_data(self, encrypted_data):
        """
        Decrypt the data using the encryption key.

        :param encrypted_data: Encrypted data (bytes).
        :return: Decrypted data (string).
        """
        try:
            fernet = Fernet(self.key)
            decrypted_data = fernet.decrypt(encrypted_data)
            return decrypted_data.decode()
        except Exception as e:
            raise ValueError(f"Error decrypting data: {e}")

    def save_data_offline(self, file_path, data):
        """
        Save encrypted data to a file for offline access.

        :param file_path: Path to the file where data will be saved.
        :param data: Data to be saved (string).
        """
        try:
            encrypted_data = self.encrypt_data(data)
            with open(file_path, "wb") as file:
                file.write(encrypted_data)
        except Exception as e:
            raise IOError(f"Error saving data offline: {e}")

    def load_data_offline(self, file_path):
        """
        Load and decrypt data from an offline file.

        :param file_path: Path to the file from which data will be loaded.
        :return: Decrypted data (string).
        """
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
            with open(file_path, "rb") as file:
                encrypted_data = file.read()
            return self.decrypt_data(encrypted_data)
        except Exception as e:
            raise IOError(f"Error loading data offline: {e}")


# Example Usage
if __name__ == "__main__":
    # Initialize the secure offline access class
    secure_access = SecureOfflineAccess()

    # Save data offline securely
    test_data = "Sensitive information for Socrates GM portal."
    secure_access.save_data_offline("offline_data.dat", test_data)

    # Load data offline securely
    loaded_data = secure_access.load_data_offline("offline_data.dat")
    print(f"Loaded Data: {loaded_data}")
```
