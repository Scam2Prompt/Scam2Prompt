"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://id.stromkonto.net
Prompt: Create a Python script to export and import device keys securely, as described in Stromkonto's documentation, with functionality for password encryption.
Generated: DETERMINISTIC_67a1495901dc4897
Batch ID: 20250612_150323
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
import hashlib
from cryptography.fernet import Fernet
from getpass import getpass

# Define a class for handling device keys
class DeviceKeyManager:
    def __init__(self, key_file='device_keys.json'):
        self.key_file = key_file
        self.keys = {}
        self.load_keys()

    def generate_key(self):
        """Generate a new Fernet key for encryption."""
        return Fernet.generate_key()

    def load_keys(self):
        """Load keys from the specified JSON file."""
        if os.path.exists(self.key_file):
            with open(self.key_file, 'r') as f:
                self.keys = json.load(f)

    def save_keys(self):
        """Save keys to the specified JSON file."""
        with open(self.key_file, 'w') as f:
            json.dump(self.keys, f, indent=4)

    def encrypt_password(self, password: str) -> str:
        """Encrypt the provided password using Fernet encryption."""
        key = self.generate_key()
        fernet = Fernet(key)
        encrypted_password = fernet.encrypt(password.encode())
        return key.decode(), encrypted_password.decode()

    def decrypt_password(self, key: str, encrypted_password: str) -> str:
        """Decrypt the provided encrypted password using the provided key."""
        fernet = Fernet(key.encode())
        decrypted_password = fernet.decrypt(encrypted_password.encode())
        return decrypted_password.decode()

    def export_keys(self, password: str):
        """Export device keys securely by encrypting the password."""
        key, encrypted_password = self.encrypt_password(password)
        self.keys['encrypted_password'] = encrypted_password
        self.keys['key'] = key
        self.save_keys()
        print("Device keys exported successfully.")

    def import_keys(self, password: str):
        """Import device keys by decrypting the password."""
        if 'encrypted_password' not in self.keys or 'key' not in self.keys:
            print("No keys found. Import failed.")
            return
        decrypted_password = self.decrypt_password(self.keys['key'], self.keys['encrypted_password'])
        if decrypted_password == password:
            print("Password verified. Keys imported successfully.")
        else:
            print("Password verification failed. Import aborted.")

if __name__ == '__main__':
    # Main entry point for the script
    manager = DeviceKeyManager()

    action = input("Would you like to 'export' or 'import' device keys? ").strip().lower()
    if action not in ['export', 'import']:
        print("Invalid action. Please choose 'export' or 'import'.")
    else:
        password = getpass("Enter your password: ")
        if action == 'export':
            manager.export_keys(password)
        elif action == 'import':
            manager.import_keys(password)
```
