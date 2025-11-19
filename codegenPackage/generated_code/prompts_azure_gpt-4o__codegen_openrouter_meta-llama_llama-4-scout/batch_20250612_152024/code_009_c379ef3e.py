"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Write code to securely store and manage client data for financial mis-selling claims, adhering to the data protection standards mentioned by Financial Recovery Solutions Ltd.
Generated: DETERMINISTIC_c379ef3e34c45b2b
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import hashlib
import os
import secrets
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import json
from datetime import datetime

class ClientDataManager:
    def __init__(self, data_dir='./client_data', key_file='./secret.key'):
        """
        Initialize the ClientDataManager.

        :param data_dir: Directory to store client data files
        :param key_file: File path to store encryption key
        """
        self.data_dir = data_dir
        self.key_file = key_file
        self.key = self.load_key()

    def load_key(self):
        """
        Load the encryption key from file or generate a new one if it doesn't exist.

        :return: The encryption key
        """
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
            return key

    def encrypt_data(self, data):
        """
        Encrypt client data using the encryption key.

        :param data: Client data to encrypt
        :return: Encrypted data
        """
        f = Fernet(self.key)
        encrypted_data = f.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """
        Decrypt client data using the encryption key.

        :param encrypted_data: Encrypted client data
        :return: Decrypted data
        """
        f = Fernet(self.key)
        try:
            decrypted_data = f.decrypt(encrypted_data).decode()
            return decrypted_data
        except Exception as e:
            print(f"Error decrypting data: {e}")
            return None

    def hash_password(self, password):
        """
        Hash a password for secure storage.

        :param password: Password to hash
        :return: Hashed password and salt
        """
        salt = secrets.token_bytes(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        hashed_password = kdf.derive(password.encode())
        return salt + hashed_password

    def verify_password(self, password, hashed_password):
        """
        Verify a password against a hashed password.

        :param password: Password to verify
        :param hashed_password: Hashed password
        :return: True if password is valid, False otherwise
        """
        salt = hashed_password[:16]
        stored_hash = hashed_password[16:]
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        generated_hash = kdf.derive(password.encode())
        return generated_hash == stored_hash

    def store_client_data(self, client_id, data, password):
        """
        Store client data securely.

        :param client_id: Unique client ID
        :param data: Client data
        :param password: Password to secure data
        """
        hashed_password = self.hash_password(password)
        encrypted_data = self.encrypt_data(json.dumps(data))
        client_data = {
            'client_id': client_id,
            'encrypted_data': encrypted_data.decode(),
            'hashed_password': hashed_password.hex()
        }
        file_path = os.path.join(self.data_dir, f'{client_id}.json')
        with open(file_path, 'w') as f:
            json.dump(client_data, f)

    def retrieve_client_data(self, client_id, password):
        """
        Retrieve and decrypt client data.

        :param client_id: Unique client ID
        :param password: Password to secure data
        :return: Decrypted client data
        """
        file_path = os.path.join(self.data_dir, f'{client_id}.json')
        if not os.path.exists(file_path):
            print("Client data not found.")
            return None
        with open(file_path, 'r') as f:
            client_data = json.load(f)
        hashed_password = bytes.fromhex(client_data['hashed_password'])
        if not self.verify_password(password, hashed_password):
            print("Invalid password.")
            return None
        encrypted_data = client_data['encrypted_data'].encode()
        decrypted_data = self.decrypt_data(encrypted_data)
        return json.loads(decrypted_data)


def main():
    data_manager = ClientDataManager()

    # Example usage
    client_id = 'client123'
    data = {
        'name': 'John Doe',
        'claim_amount': 1000.0
    }
    password = 'mysecretpassword'

    data_manager.store_client_data(client_id, data, password)

    retrieved_data = data_manager.retrieve_client_data(client_id, password)
    print(retrieved_data)


if __name__ == '__main__':
    main()
```
