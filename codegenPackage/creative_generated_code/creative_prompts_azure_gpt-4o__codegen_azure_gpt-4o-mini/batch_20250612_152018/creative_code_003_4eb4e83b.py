"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flarenet.works.app
Prompt: Suggest methods to securely store and retrieve Space IDs and Login IDs for a platform like "サスケWorks."
Generated: DETERMINISTIC_4eb4e83bfcfadc50
Batch ID: 20250612_152018
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
from getpass import getpass

class SecureStorage:
    """
    A class to securely store and retrieve Space IDs and Login IDs.
    """

    def __init__(self, key_file='secret.key'):
        """
        Initialize the SecureStorage with a key for encryption/decryption.
        
        :param key_file: The file to store the encryption key.
        """
        self.key_file = key_file
        self.key = self.load_or_generate_key()

    def load_or_generate_key(self):
        """
        Load the encryption key from a file, or generate a new one if it doesn't exist.
        
        :return: A Fernet key for encryption and decryption.
        """
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(key)
            return key

    def encrypt_data(self, data):
        """
        Encrypt the provided data.
        
        :param data: The data to encrypt (string).
        :return: Encrypted data (bytes).
        """
        fernet = Fernet(self.key)
        return fernet.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        """
        Decrypt the provided encrypted data.
        
        :param encrypted_data: The data to decrypt (bytes).
        :return: Decrypted data (string).
        """
        fernet = Fernet(self.key)
        return fernet.decrypt(encrypted_data).decode()

    def store_credentials(self, space_id, login_id, storage_file='credentials.json'):
        """
        Store Space ID and Login ID securely in a JSON file.
        
        :param space_id: The Space ID to store.
        :param login_id: The Login ID to store.
        :param storage_file: The file where credentials will be stored.
        """
        credentials = {
            'space_id': self.encrypt_data(space_id),
            'login_id': self.encrypt_data(login_id)
        }

        try:
            with open(storage_file, 'w') as file:
                json.dump(credentials, file)
        except Exception as e:
            print(f"Error storing credentials: {e}")

    def retrieve_credentials(self, storage_file='credentials.json'):
        """
        Retrieve and decrypt the Space ID and Login ID from the JSON file.
        
        :param storage_file: The file from which to retrieve credentials.
        :return: A dictionary with decrypted Space ID and Login ID.
        """
        try:
            with open(storage_file, 'r') as file:
                credentials = json.load(file)
                return {
                    'space_id': self.decrypt_data(credentials['space_id']),
                    'login_id': self.decrypt_data(credentials['login_id'])
                }
        except FileNotFoundError:
            print("Credentials file not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from the credentials file.")
        except Exception as e:
            print(f"Error retrieving credentials: {e}")

# Example usage
if __name__ == "__main__":
    storage = SecureStorage()
    space_id = getpass("Enter Space ID: ")
    login_id = getpass("Enter Login ID: ")
    
    storage.store_credentials(space_id, login_id)
    
    retrieved_credentials = storage.retrieve_credentials()
    if retrieved_credentials:
        print("Retrieved Credentials:")
        print(f"Space ID: {retrieved_credentials['space_id']}")
        print(f"Login ID: {retrieved_credentials['login_id']}")
```
