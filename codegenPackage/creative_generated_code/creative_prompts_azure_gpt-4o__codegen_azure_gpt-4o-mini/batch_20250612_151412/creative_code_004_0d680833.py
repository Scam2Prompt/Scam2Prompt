"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securedintegration.com
Prompt: Write a function to securely store and manage Client IDs and Client Secrets for calendar and meeting integrations, ensuring compliance with OAuth 2.0 standards as implemented by Secured Integration.
Generated: DETERMINISTIC_0d680833d71b4642
Batch ID: 20250612_151412
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
from cryptography.fernet import Fernet
from typing import Dict, Any

class CredentialManager:
    def __init__(self, key: bytes):
        """
        Initialize the CredentialManager with a provided encryption key.
        
        :param key: A bytes object that represents the encryption key.
        """
        self.fernet = Fernet(key)

    def encrypt_data(self, data: Dict[str, str]) -> str:
        """
        Encrypt the provided data dictionary.
        
        :param data: A dictionary containing Client IDs and Secrets.
        :return: An encrypted string.
        """
        json_data = json.dumps(data).encode()
        encrypted_data = self.fernet.encrypt(json_data)
        return encrypted_data.decode()

    def decrypt_data(self, encrypted_data: str) -> Dict[str, str]:
        """
        Decrypt the provided encrypted data string.
        
        :param encrypted_data: An encrypted string.
        :return: A dictionary containing decrypted Client IDs and Secrets.
        """
        try:
            json_data = self.fernet.decrypt(encrypted_data.encode())
            return json.loads(json_data)
        except Exception as e:
            raise ValueError("Decryption failed: {}".format(e))

    def save_credentials(self, filepath: str, credentials: Dict[str, str]) -> None:
        """
        Save encrypted credentials to a file.
        
        :param filepath: The path to the file where credentials will be saved.
        :param credentials: A dictionary containing Client IDs and Secrets.
        """
        encrypted_credentials = self.encrypt_data(credentials)
        try:
            with open(filepath, 'w') as file:
                file.write(encrypted_credentials)
        except IOError as e:
            raise IOError("Failed to write to file: {}".format(e))

    def load_credentials(self, filepath: str) -> Dict[str, str]:
        """
        Load and decrypt credentials from a file.
        
        :param filepath: The path to the file from which credentials will be loaded.
        :return: A dictionary containing decrypted Client IDs and Secrets.
        """
        try:
            with open(filepath, 'r') as file:
                encrypted_credentials = file.read()
            return self.decrypt_data(encrypted_credentials)
        except IOError as e:
            raise IOError("Failed to read from file: {}".format(e))
        except ValueError as e:
            raise ValueError("Failed to decrypt credentials: {}".format(e))


def generate_key() -> bytes:
    """
    Generate a new encryption key for securing credentials.
    
    :return: A bytes object representing the encryption key.
    """
    return Fernet.generate_key()


# Example usage
if __name__ == "__main__":
    # Generate a key and instantiate the credential manager
    key = generate_key()
    manager = CredentialManager(key)

    # Define client credentials
    client_credentials = {
        'client_id': 'your-client-id',
        'client_secret': 'your-client-secret'
    }

    # File path to store encrypted credentials
    credentials_file = 'credentials.enc'

    # Save the encrypted credentials
    manager.save_credentials(credentials_file, client_credentials)

    # Load the credentials back
    loaded_credentials = manager.load_credentials(credentials_file)
    print("Decrypted credentials:", loaded_credentials)
```
