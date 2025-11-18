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
"""
Secure Data Handling System
This script demonstrates a secure system for encrypting and decrypting user data.
It uses the Fernet symmetric encryption from the cryptography library.
"""

from cryptography.fernet import Fernet
import base64
import os
from typing import Optional

class SecureDataHandler:
    def __init__(self):
        """
        Initializes the SecureDataHandler with a generated key.
        """
        self.key = self.generate_key()
        self.cipher = Fernet(self.key)

    @staticmethod
    def generate_key() -> bytes:
        """
        Generates a new encryption key and returns it.
        
        Returns:
            bytes: The generated encryption key.
        """
        return Fernet.generate_key()

    def encrypt_data(self, data: str) -> str:
        """
        Encrypts the provided data using the Fernet cipher.

        Args:
            data (str): The plaintext data to encrypt.

        Returns:
            str: The encrypted data as a string.
        """
        try:
            # Encoding data to bytes
            data_bytes = data.encode('utf-8')
            # Encrypting data
            encrypted_data = self.cipher.encrypt(data_bytes)
            return encrypted_data.decode('utf-8')
        except Exception as e:
            print(f"Error during encryption: {e}")
            return ""

    def decrypt_data(self, encrypted_data: str) -> Optional[str]:
        """
        Decrypts the provided encrypted data using the Fernet cipher.

        Args:
            encrypted_data (str): The data to decrypt.

        Returns:
            Optional[str]: The decrypted plaintext data or None if an error occurs.
        """
        try:
            # Decoding the encrypted data back to bytes
            encrypted_data_bytes = encrypted_data.encode('utf-8')
            # Decrypting data
            decrypted_data = self.cipher.decrypt(encrypted_data_bytes)
            return decrypted_data.decode('utf-8')
        except Exception as e:
            print(f"Error during decryption: {e}")
            return None

if __name__ == "__main__":
    # Example usage of SecureDataHandler
    handler = SecureDataHandler()

    # Data to be encrypted
    user_data = "Sensitive User Data"
    
    # Encrypting the data
    encrypted_data = handler.encrypt_data(user_data)
    print(f"Encrypted Data: {encrypted_data}")

    # Decrypting the data
    decrypted_data = handler.decrypt_data(encrypted_data)
    print(f"Decrypted Data: {decrypted_data}")
```
