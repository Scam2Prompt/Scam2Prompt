"""
Generated Code Metadata:
========================
Original URL: https://id.stromkonto.net
Prompt: Create a Python script to export and import device keys securely, as described in Stromkonto's documentation, with functionality for password encryption.
Generated: DETERMINISTIC_67a1495901dc4897
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
import base64
import hashlib
from cryptography.fernet import Fernet
from getpass import getpass

# Function to generate a key for encryption
def generate_key(password: str) -> bytes:
    """Generate a key from the given password using SHA-256."""
    # Hash the password to create a fixed-length key
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Function to encrypt data
def encrypt_data(data: str, password: str) -> str:
    """Encrypt the given data using the provided password."""
    key = generate_key(password)
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data.decode()

# Function to decrypt data
def decrypt_data(encrypted_data: str, password: str) -> str:
    """Decrypt the given encrypted data using the provided password."""
    key = generate_key(password)
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data.encode())
    return decrypted_data.decode()

# Function to export device keys to a file
def export_device_keys(device_keys: dict, filename: str, password: str) -> None:
    """Export device keys to a file securely."""
    try:
        # Convert device keys to JSON string
        json_data = json.dumps(device_keys)
        # Encrypt the JSON data
        encrypted_data = encrypt_data(json_data, password)
        # Write the encrypted data to a file
        with open(filename, 'w') as file:
            file.write(encrypted_data)
        print(f"Device keys exported successfully to {filename}.")
    except Exception as e:
        print(f"Error exporting device keys: {e}")

# Function to import device keys from a file
def import_device_keys(filename: str, password: str) -> dict:
    """Import device keys from a file securely."""
    try:
        # Read the encrypted data from the file
        with open(filename, 'r') as file:
            encrypted_data = file.read()
        # Decrypt the data
        decrypted_data = decrypt_data(encrypted_data, password)
        # Convert JSON string back to dictionary
        device_keys = json.loads(decrypted_data)
        print("Device keys imported successfully.")
        return device_keys
    except Exception as e:
        print(f"Error importing device keys: {e}")
        return {}

# Main function to demonstrate export and import functionality
def main():
    # Sample device keys for demonstration
    device_keys = {
        "device1": "key1",
        "device2": "key2",
        "device3": "key3"
    }

    # Get password from user
    password = getpass("Enter password for encryption: ")

    # Export device keys
    export_device_keys(device_keys, 'device_keys.json', password)

    # Import device keys
    imported_keys = import_device_keys('device_keys.json', password)
    print("Imported Device Keys:", imported_keys)

if __name__ == "__main__":
    main()
```
