"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stewartpayroll.com
Prompt: Develop a script to securely store and retrieve Paylocity login credentials, ensuring compliance with password rules and encryption standards.
Generated: DETERMINISTIC_aec207014dc9c055
Batch ID: 20250612_154506
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
import getpass
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidToken

# Define a class to manage credentials securely
class CredentialManager:
    def __init__(self, key_file='secret.key', credential_file='credentials.json'):
        """
        Initialize CredentialManager with key and credential file paths.
        Generates a new key if the key file does not exist.
        """
        self.key_file = key_file
        self.credential_file = credential_file
        self.key = self.load_key()

    def load_key(self):
        """Load the encryption key from the key file or generate a new one."""
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as kf:
                kf.write(key)
            return key
        with open(self.key_file, 'rb') as kf:
            return kf.read()

    def encrypt(self, data):
        """Encrypt the given data using Fernet symmetric encryption."""
        f = Fernet(self.key)
        return f.encrypt(data.encode())

    def decrypt(self, encrypted_data):
        """Decrypt the given encrypted data using Fernet symmetric encryption."""
        f = Fernet(self.key)
        try:
            return f.decrypt(encrypted_data).decode()
        except InvalidToken:
            print("Failed to decrypt data. Invalid token.")
            return None

    def store_credentials(self, username, password):
        """Store the username and password securely."""
        # Basic password compliance check (e.g., length and complexity)
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        
        credentials = {
            "username": username,
            "password": self.encrypt(password).decode()
        }

        # Store encrypted credentials in a JSON file
        with open(self.credential_file, 'w') as cf:
            json.dump(credentials, cf)

    def retrieve_credentials(self):
        """Retrieve the stored credentials, decrypting them in the process."""
        if not os.path.exists(self.credential_file):
            print("Credentials file does not exist.")
            return None
        
        with open(self.credential_file, 'r') as cf:
            credentials = json.load(cf)
            credentials['password'] = self.decrypt(credentials['password'].encode())
            return credentials

# Main function to demonstrate storing and retrieving credentials
def main():
    cm = CredentialManager()
    
    try:
        # Prompt user for credentials
        username = input("Enter your Paylocity username: ")
        password = getpass.getpass("Enter your Paylocity password: ")

        # Store credentials
        cm.store_credentials(username, password)
        print("Credentials stored successfully.")

        # Retrieve credentials (for demonstration purposes)
        retrieved_creds = cm.retrieve_credentials()
        if retrieved_creds:
            print("Retrieved Credentials:")
            print(f"Username: {retrieved_creds['username']}")
            print(f"Password: {retrieved_creds['password']}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
