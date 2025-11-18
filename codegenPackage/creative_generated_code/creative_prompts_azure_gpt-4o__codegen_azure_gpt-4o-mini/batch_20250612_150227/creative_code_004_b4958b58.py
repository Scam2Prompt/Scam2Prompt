"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worfluxai.com
Prompt: Suggest Python libraries for implementing secure data storage and encryption, as highlighted in WorfluxAI's emphasis on "Datensicherheit rund um die Uhr."
Generated: DETERMINISTIC_b4958b5877c7def6
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# secure_storage.py

"""
This module provides a simple interface for secure data storage 
and encryption using the `cryptography` library. It allows users 
to securely store and retrieve sensitive information, ensuring 
data confidentiality and integrity.
"""

import os
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidToken

class SecureStorage:
    """
    A class to handle secure storage and encryption of sensitive data.
    """

    def __init__(self, key_file='secret.key'):
        """
        Initializes the SecureStorage instance.

        Parameters:
        key_file (str): The filename where the encryption key will be stored.
        """
        self.key_file = key_file
        self.key = self.load_key()

    def load_key(self):
        """
        Loads the encryption key from the specified key file or generates 
        a new key if the file does not exist.

        Returns:
        bytes: The encryption key.
        """
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as key_file:
                return key_file.read()
        else:
            # Generate a new key and save it to the key file
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(key)
            return key

    def encrypt_data(self, data: str) -> bytes:
        """
        Encrypts the given data using the stored encryption key.

        Parameters:
        data (str): The data to be encrypted.

        Returns:
        bytes: The encrypted data.
        """
        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data: bytes) -> str:
        """
        Decrypts the given encrypted data using the stored encryption key.

        Parameters:
        encrypted_data (bytes): The data to be decrypted.

        Returns:
        str: The decrypted data.
        
        Raises:
        InvalidToken: If the decryption fails due to an invalid token.
        """
        fernet = Fernet(self.key)
        try:
            decrypted_data = fernet.decrypt(encrypted_data)
            return decrypted_data.decode()
        except InvalidToken as e:
            raise ValueError("Invalid token! Decryption failed.") from e

if __name__ == "__main__":
    # Example usage of SecureStorage class
    storage = SecureStorage()

    # Encrypting data
    sensitive_data = "This is a secret!"
    encrypted = storage.encrypt_data(sensitive_data)
    print(f"Encrypted data: {encrypted}")

    # Decrypting data
    try:
        decrypted = storage.decrypt_data(encrypted)
        print(f"Decrypted data: {decrypted}")
    except ValueError as e:
        print(e)
```

### Requirements
To run the above code, make sure to install the `cryptography` library:

```bash
pip install cryptography
```
