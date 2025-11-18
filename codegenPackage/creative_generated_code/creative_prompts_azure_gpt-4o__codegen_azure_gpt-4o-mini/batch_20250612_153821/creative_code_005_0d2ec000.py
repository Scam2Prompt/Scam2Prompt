"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twinpixt.com
Prompt: Provide a code snippet to securely store and retrieve cryptocurrency assets using TWINPIXT's encryption and storage systems.
Generated: DETERMINISTIC_0d2ec000ea4e786f
Batch ID: 20250612_153821
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

class CryptoAssetManager:
    def __init__(self, key_file='secret.key'):
        """Initialize the CryptoAssetManager with a key for encryption and decryption."""
        self.key_file = key_file
        self.key = self.load_or_generate_key()

    def load_or_generate_key(self):
        """Load the encryption key from a file, or generate a new key if it doesn't exist."""
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(key)
            return key

    def encrypt_data(self, data):
        """Encrypt the provided data using the encryption key."""
        fernet = Fernet(self.key)
        data_json = json.dumps(data).encode()  # Convert data to JSON string and encode
        encrypted_data = fernet.encrypt(data_json)
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """Decrypt the encrypted data using the encryption key."""
        fernet = Fernet(self.key)
        decrypted_data = fernet.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())  # Decode and convert back to JSON

    def store_assets(self, asset_name, asset_value):
        """Store a cryptocurrency asset securely."""
        try:
            # Encrypt asset value
            encrypted_value = self.encrypt_data({'name': asset_name, 'value': asset_value})
            # Store encrypted asset in a file
            with open(f"{asset_name}.encrypted", 'wb') as asset_file:
                asset_file.write(encrypted_value)
            print(f"Successfully stored asset: {asset_name}")
        except Exception as e:
            print(f"Error storing asset: {e}")

    def retrieve_assets(self, asset_name):
        """Retrieve a cryptocurrency asset securely."""
        try:
            # Read the encrypted asset from file
            with open(f"{asset_name}.encrypted", 'rb') as asset_file:
                encrypted_value = asset_file.read()
            # Decrypt the asset value
            asset_data = self.decrypt_data(encrypted_value)
            return asset_data
        except FileNotFoundError:
            print(f"Asset file not found: {asset_name}.encrypted")
        except Exception as e:
            print(f"Error retrieving asset: {e}")

# Example usage
if __name__ == "__main__":
    manager = CryptoAssetManager()
    manager.store_assets('Bitcoin', 0.5)
    asset_info = manager.retrieve_assets('Bitcoin')
    print(asset_info)  # Output: {'name': 'Bitcoin', 'value': 0.5}
```
