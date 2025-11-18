"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://authorization-b6o.pages.dev
Prompt: Suggest cryptographic libraries that can enhance the security and confidentiality of user data in a system like SeedAim.
Generated: DETERMINISTIC_6bcf3cdacf732697
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for cryptography
from cryptography.fernet import Fernet
import os
import base64
import hashlib

class CryptographyUtility:
    """
    A utility class to handle encryption and decryption of user data
    using the Fernet symmetric encryption from the cryptography library.
    """

    def __init__(self):
        """
        Initializes the CryptographyUtility class by generating a key.
        The key is stored in the file system for later use.
        """
        self.key = self.generate_key()

    @staticmethod
    def generate_key():
        """
        Generates a new Fernet key and saves it to a key file.
        If the key file already exists, it retrieves the existing key.
        
        Returns:
            bytes: The base64 encoded key.
        """
        key_file = "secret.key"
        if os.path.exists(key_file):
            with open(key_file, "rb") as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, "wb") as key_file:
                key_file.write(key)
            return key

    def encrypt_data(self, data):
        """
        Encrypts the provided data using the Fernet key.

        Args:
            data (str): The plaintext data to be encrypted.
        
        Returns:
            str: The encrypted data in byte format, encoded in base64.
        """
        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data.decode()

    def decrypt_data(self, encrypted_data):
        """
        Decrypts the provided encrypted data using the Fernet key.

        Args:
            encrypted_data (str): The encrypted data in base64 format.
        
        Returns:
            str: The decrypted plaintext data.
        """
        fernet = Fernet(self.key)
        try:
            decrypted_data = fernet.decrypt(encrypted_data.encode())
            return decrypted_data.decode()
        except Exception as e:
            raise ValueError("Decryption failed: Invalid encrypted data.") from e

# Example usage
if __name__ == "__main__":
    # Create an instance of the CryptographyUtility
    crypto_util = CryptographyUtility()

    # Sample data to encrypt
    user_data = "Sensitive user information."

    # Encrypt the data
    encrypted = crypto_util.encrypt_data(user_data)
    print(f"Encrypted Data: {encrypted}")

    # Decrypt the data
    try:
        decrypted = crypto_util.decrypt_data(encrypted)
        print(f"Decrypted Data: {decrypted}")
    except ValueError as e:
        print(e)
```
