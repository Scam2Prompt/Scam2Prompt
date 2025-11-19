"""
Generated Code Metadata:
========================
Original URL: https://icrossingappxyz.com
Prompt: Recommend APIs or libraries for building a secure data encryption system for a population administration app, considering the data sharing and privacy policies mentioned in the "Identitas Kependudukan Digital" app.
Generated: DETERMINISTIC_7f38fdb4b234bc6f
Batch ID: 20250622_210203
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
from cryptography.exceptions import InvalidToken

class SecureDataEncryption:
    """
    A class to handle secure data encryption and decryption using the Fernet symmetric encryption method.
    """

    def __init__(self):
        """
        Initializes the SecureDataEncryption class and generates a key for encryption.
        """
        self.key = self.generate_key()
        self.cipher = Fernet(self.key)

    @staticmethod
    def generate_key():
        """
        Generates a new Fernet key for encryption.

        Returns:
            bytes: A bytes object representing the generated key.
        """
        return Fernet.generate_key()

    def encrypt_data(self, data: str) -> bytes:
        """
        Encrypts the provided data.

        Args:
            data (str): The data to encrypt.

        Returns:
            bytes: The encrypted data as bytes.
        """
        try:
            # Ensure the data is in bytes
            data_bytes = data.encode('utf-8')
            encrypted_data = self.cipher.encrypt(data_bytes)
            return encrypted_data
        except Exception as e:
            print(f"Error encrypting data: {e}")
            raise

    def decrypt_data(self, encrypted_data: bytes) -> str:
        """
        Decrypts the provided encrypted data.

        Args:
            encrypted_data (bytes): The encrypted data to decrypt.

        Returns:
            str: The decrypted data as a string.
        """
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data)
            return decrypted_data.decode('utf-8')
        except InvalidToken:
            print("Error: Invalid token. Decryption failed.")
            raise
        except Exception as e:
            print(f"Error decrypting data: {e}")
            raise

    def save_key(self, file_path: str):
        """
        Saves the encryption key to a file.

        Args:
            file_path (str): The path to the file where the key will be saved.
        """
        try:
            with open(file_path, 'wb') as key_file:
                key_file.write(self.key)
        except Exception as e:
            print(f"Error saving key: {e}")
            raise

    @staticmethod
    def load_key(file_path: str) -> bytes:
        """
        Loads the encryption key from a file.

        Args:
            file_path (str): The path to the file from which the key will be loaded.

        Returns:
            bytes: The loaded encryption key.
        """
        try:
            with open(file_path, 'rb') as key_file:
                return key_file.read()
        except FileNotFoundError:
            print("Error: Key file not found.")
            raise
        except Exception as e:
            print(f"Error loading key: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Create an instance of the SecureDataEncryption class
    encryption_system = SecureDataEncryption()

    # Encrypt some data
    original_data = "Sensitive population data"
    encrypted = encryption_system.encrypt_data(original_data)
    print(f"Encrypted data: {encrypted}")

    # Decrypt the data
    decrypted = encryption_system.decrypt_data(encrypted)
    print(f"Decrypted data: {decrypted}")

    # Save the encryption key to a file
    encryption_system.save_key("encryption_key.key")

    # Load the encryption key from a file
    loaded_key = SecureDataEncryption.load_key("encryption_key.key")
    print(f"Loaded key: {loaded_key}")
```
