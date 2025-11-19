"""
Generated Code Metadata:
========================
Original URL: https://id.stromkonto.net
Prompt: Create a tool to export device keys to the clipboard and securely store them, following the security guidelines provided by Stromkonto.
Generated: DETERMINISTIC_aeaa0107025be30f
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import pyperclip
import base64
import cryptography
from cryptography.fernet import Fernet
from getpass import getpass

# Constants for file paths and encryption
KEY_FILE = 'device_keys.key'
DATA_FILE = 'device_keys.json'

def generate_key():
    """Generate a new encryption key and save it to a file."""
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)

def load_key():
    """Load the encryption key from the key file."""
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

def encrypt_data(data):
    """Encrypt the data using the loaded key."""
    key = load_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data):
    """Decrypt the data using the loaded key."""
    key = load_key()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

def store_device_keys(keys):
    """Store device keys securely in a JSON file."""
    encrypted_keys = encrypt_data(json.dumps(keys))
    with open(DATA_FILE, 'wb') as data_file:
        data_file.write(encrypted_keys)

def load_device_keys():
    """Load device keys from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'rb') as data_file:
        encrypted_keys = data_file.read()
    return json.loads(decrypt_data(encrypted_keys))

def export_keys_to_clipboard(keys):
    """Export device keys to the clipboard."""
    try:
        keys_str = json.dumps(keys, indent=4)
        pyperclip.copy(keys_str)
        print("Device keys have been copied to the clipboard.")
    except Exception as e:
        print(f"Error exporting keys to clipboard: {e}")

def main():
    """Main function to handle user input and operations."""
    print("Device Key Management Tool")
    
    # Load existing keys or initialize an empty dictionary
    device_keys = load_device_keys()

    while True:
        print("\nOptions:")
        print("1. Add Device Key")
        print("2. View Device Keys")
        print("3. Export Device Keys to Clipboard")
        print("4. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            key_name = input("Enter device name: ")
            key_value = getpass("Enter device key: ")
            device_keys[key_name] = key_value
            store_device_keys(device_keys)
            print(f"Device key for '{key_name}' added successfully.")

        elif choice == '2':
            print("Current Device Keys:")
            for name, key in device_keys.items():
                print(f"{name}: {key}")

        elif choice == '3':
            export_keys_to_clipboard(device_keys)

        elif choice == '4':
            print("Exiting the tool.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```

### Requirements:
- Install the required libraries using pip:
```bash
pip install pyperclip cryptography
```
