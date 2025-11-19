"""
Generated Code Metadata:
========================
Original URL: https://play-phantom-zone.xyz
Prompt: Design a data encryption system for a mobile game, ensuring secure data transmission and storage, as mentioned in the Deep Dev game's security features.
Generated: DETERMINISTIC_464d635b8cde7058
Batch ID: 20250622_210249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import base64
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidToken

class EncryptionSystem:
    """
    A class to handle data encryption and decryption for secure data transmission and storage.
    """

    def __init__(self):
        """
        Initializes the EncryptionSystem by generating a key if it doesn't exist.
        """
        self.key = self.load_or_generate_key()

    def load_or_generate_key(self):
        """
        Loads the encryption key from a file or generates a new one if it doesn't exist.
        
        Returns:
            bytes: The encryption key.
        """
        key_file = 'secret.key'
        if os.path.exists(key_file):
            with open(key_file, 'rb') as file:
                return file.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, 'wb') as file:
                file.write(key)
            return key

    def encrypt_data(self, data: str) -> str:
        """
        Encrypts the given data using the Fernet symmetric encryption.

        Args:
            data (str): The data to encrypt.

        Returns:
            str: The encrypted data, encoded in base64.
        """
        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(data.encode())
        return base64.urlsafe_b64encode(encrypted_data).decode()

    def decrypt_data(self, encrypted_data: str) -> str:
        """
        Decrypts the given encrypted data.

        Args:
            encrypted_data (str): The encrypted data to decrypt.

        Returns:
            str: The decrypted data.

        Raises:
            InvalidToken: If the encrypted data is invalid or tampered with.
        """
        fernet = Fernet(self.key)
        try:
            decoded_data = base64.urlsafe_b64decode(encrypted_data.encode())
            return fernet.decrypt(decoded_data).decode()
        except InvalidToken:
            raise ValueError("Invalid or tampered encrypted data.")

# Example usage
if __name__ == "__main__":
    encryption_system = EncryptionSystem()

    # Sample data to encrypt
    data_to_encrypt = "PlayerScore:100"

    # Encrypt the data
    encrypted = encryption_system.encrypt_data(data_to_encrypt)
    print(f"Encrypted Data: {encrypted}")

    # Decrypt the data
    try:
        decrypted = encryption_system.decrypt_data(encrypted)
        print(f"Decrypted Data: {decrypted}")
    except ValueError as e:
        print(f"Error during decryption: {e}")
```
