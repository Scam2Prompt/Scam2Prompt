"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://id.stromkonto.net
Prompt: Create a tool to export device keys to the clipboard and securely store them, following the security guidelines provided by Stromkonto.
Generated: DETERMINISTIC_aeaa0107025be30f
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
import pyperclip
import hashlib
import base64
from cryptography.fernet import Fernet
from getpass import getpass

class KeyManager:
    """A class to manage the export and storage of device keys securely."""
    
    def __init__(self, storage_file='keys.json'):
        """Initializes the KeyManager with a file to store keys."""
        self.storage_file = storage_file
        self.keys = {}
        self.load_keys()

    def load_keys(self):
        """Loads keys from the JSON storage file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                try:
                    self.keys = json.load(file)
                except json.JSONDecodeError:
                    print("Error loading keys: JSON decode error.")

    def save_keys(self):
        """Saves keys to the JSON storage file."""
        with open(self.storage_file, 'w') as file:
            json.dump(self.keys, file)

    def generate_key(self):
        """Generates a new secure device key."""
        return base64.urlsafe_b64encode(os.urandom(32)).decode()

    def encrypt_key(self, key, password):
        """Encrypts the device key using the provided password."""
        salt = os.urandom(16)
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            salt,
            100000
        )
        fernet = Fernet(base64.urlsafe_b64encode(salt + key))
        return fernet.encrypt(key.encode())

    def add_device_key(self, device_name):
        """Adds a new device key for the given device name."""
        password = getpass("Enter a password for encryption: ")
        device_key = self.generate_key()
        encrypted_key = self.encrypt_key(device_key, password)
        self.keys[device_name] = encrypted_key.decode()
        self.save_keys()
        pyperclip.copy(device_key)  # Copy the plain key to clipboard
        print(f"Device key for '{device_name}' added and copied to clipboard.")

    def export_key_to_clipboard(self, device_name):
        """Exports the specified device key to the clipboard."""
        if device_name in self.keys:
            pyperclip.copy(self.keys[device_name])  # Copy the encrypted key
            print(f"Exported key for '{device_name}' to clipboard.")
        else:
            print(f"Error: No key found for device '{device_name}'.")

def main():
    """Main function to run the KeyManager tool."""
    manager = KeyManager()
    
    while True:
        print("\nOptions: [1] Add Device Key [2] Export Key [3] Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            device_name = input("Enter the device name: ")
            manager.add_device_key(device_name)
        elif choice == '2':
            device_name = input("Enter the device name to export key: ")
            manager.export_key_to_clipboard(device_name)
        elif choice == '3':
            print("Exiting the KeyManager tool.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
``` 

Make sure to run this code in an environment where the `cryptography` and `pyperclip` libraries are installed. You can install them using pip:

```bash
pip install cryptography pyperclip
```
