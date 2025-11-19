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
from cryptography.fernet import Fernet

class DataEncryptor:
    """
    A class to encrypt and decrypt data using symmetric encryption.
    This class uses the Fernet symmetric encryption provided by the 
    cryptography library.
    """

    def __init__(self):
        """Initialize the DataEncryptor and generate a key."""
        self.key = self.generate_key()
        self.cipher = Fernet(self.key)

    @staticmethod
    def generate_key():
        """
        Generate a new Fernet key.
        
        Returns:
            bytes: A base64-encoded 32-byte key.
        """
        return Fernet.generate_key()

    def encrypt(self, data: str) -> bytes:
        """
        Encrypt the provided data.

        Args:
            data (str): The plaintext data to encrypt.

        Returns:
            bytes: The encrypted data as bytes.
        """
        try:
            # Ensure the data is bytes before encryption
            data_bytes = data.encode('utf-8')
            encrypted_data = self.cipher.encrypt(data_bytes)
            return encrypted_data
        except Exception as e:
            raise RuntimeError("Encryption failed: {}".format(e))

    def decrypt(self, encrypted_data: bytes) -> str:
        """
        Decrypt the provided encrypted data.

        Args:
            encrypted_data (bytes): The encrypted data to decrypt.

        Returns:
            str: The decrypted plaintext data.
        """
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data)
            return decrypted_data.decode('utf-8')
        except Exception as e:
            raise RuntimeError("Decryption failed: {}".format(e))

    def save_key(self, file_path: str):
        """
        Save the encryption key to a file.

        Args:
            file_path (str): The file path to save the key.
        """
        try:
            with open(file_path, 'wb') as key_file:
                key_file.write(self.key)
        except IOError as e:
            raise RuntimeError("Failed to save key: {}".format(e))

    @staticmethod
    def load_key(file_path: str) -> bytes:
        """
        Load the encryption key from a file.

        Args:
            file_path (str): The file path to load the key from.

        Returns:
            bytes: The loaded encryption key.
        """
        try:
            with open(file_path, 'rb') as key_file:
                return key_file.read()
        except IOError as e:
            raise RuntimeError("Failed to load key: {}".format(e))


# Example usage
if __name__ == "__main__":
    encryptor = DataEncryptor()
    
    # Save the encryption key to a file
    encryptor.save_key('encryption_key.key')

    # Encrypt customer data
    customer_data = "Customer Name: John Doe, Email: john@example.com"
    encrypted_data = encryptor.encrypt(customer_data)
    print("Encrypted data:", encrypted_data)

    # Decrypt the data
    decrypted_data = encryptor.decrypt(encrypted_data)
    print("Decrypted data:", decrypted_data)
```
