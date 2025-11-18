"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miningbase.cloud
Prompt: Develop a script for secure data encryption in a cloud mining platform, referencing Bitspeed's encryption techniques for user security.
Generated: DETERMINISTIC_8c2241dfb6612db1
Batch ID: 20250612_154905
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
from base64 import urlsafe_b64encode, urlsafe_b64decode
import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SecureDataEncryption:
    def __init__(self):
        # Generate a new encryption key
        self.key = self.generate_key()
        self.cipher = Fernet(self.key)

    def generate_key(self):
        """Generates a secure encryption key and returns it encoded in URL-safe base64."""
        return urlsafe_b64encode(os.urandom(32))

    def encrypt_data(self, data: str) -> str:
        """Encrypts the provided data using the Fernet encryption method.

        Args:
            data (str): The plaintext data to encrypt.

        Returns:
            str: The encrypted data, encoded in URL-safe base64.
        """
        try:
            encrypted_data = self.cipher.encrypt(data.encode())
            logging.info("Data encryption successful.")
            return encrypted_data.decode()
        except Exception as e:
            logging.error(f"Encryption failed: {e}")
            raise RuntimeError("Encryption process encountered an error.")

    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypts the provided encrypted data.

        Args:
            encrypted_data (str): The encrypted data to decrypt.

        Returns:
            str: The decrypted plaintext data.
        """
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data.encode())
            logging.info("Data decryption successful.")
            return decrypted_data.decode()
        except Exception as e:
            logging.error(f"Decryption failed: {e}")
            raise RuntimeError("Decryption process encountered an error.")

    def save_key(self, file_path: str):
        """Saves the encryption key to a specified file.

        Args:
            file_path (str): The file path to save the encryption key.
        """
        try:
            with open(file_path, 'wb') as key_file:
                key_file.write(self.key)
                logging.info("Encryption key saved successfully.")
        except Exception as e:
            logging.error(f"Failed to save the encryption key: {e}")
            raise IOError("Could not save the encryption key.")

    def load_key(self, file_path: str):
        """Loads the encryption key from a specified file.

        Args:
            file_path (str): The file path from which to load the encryption key.
        """
        try:
            with open(file_path, 'rb') as key_file:
                self.key = key_file.read()
                self.cipher = Fernet(self.key)
                logging.info("Encryption key loaded successfully.")
        except Exception as e:
            logging.error(f"Failed to load the encryption key: {e}")
            raise IOError("Could not load the encryption key.")

# Example usage:
if __name__ == "__main__":
    try:
        encryption_service = SecureDataEncryption()
        
        # Encrypt a sample message
        original_message = "Secure data for cloud mining."
        encrypted_message = encryption_service.encrypt_data(original_message)
        print(f"Encrypted Message: {encrypted_message}")

        # Decrypt the message
        decrypted_message = encryption_service.decrypt_data(encrypted_message)
        print(f"Decrypted Message: {decrypted_message}")

        # Save the encryption key
        encryption_service.save_key("encryption_key.key")

        # Load the encryption key
        encryption_service.load_key("encryption_key.key")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
