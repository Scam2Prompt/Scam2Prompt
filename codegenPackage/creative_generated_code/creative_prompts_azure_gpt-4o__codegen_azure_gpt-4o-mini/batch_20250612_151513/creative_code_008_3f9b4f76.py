"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genopets.eu
Prompt: Suggest methods to securely store and manage user-generated game assets in a decentralized platform similar to Genopets.
Generated: DETERMINISTIC_3f9b4f7616a05308
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
import hashlib
from cryptography.fernet import Fernet
from typing import List, Dict, Any

class GameAssetManager:
    """
    A class to manage user-generated game assets with secure storage
    and retrieval mechanisms.
    """

    def __init__(self, storage_directory: str, encryption_key: bytes):
        """
        Initializes the GameAssetManager.

        :param storage_directory: Directory to store encrypted assets.
        :param encryption_key: Key for encrypting and decrypting files.
        """
        self.storage_directory = storage_directory
        self.cipher = Fernet(encryption_key)

        # Ensure the storage directory exists
        os.makedirs(self.storage_directory, exist_ok=True)

    def hash_asset_name(self, asset_name: str) -> str:
        """
        Creates a SHA-256 hash of the asset name for secure storage.

        :param asset_name: The name of the asset to hash.
        :return: Hexadecimal representation of the hash.
        """
        return hashlib.sha256(asset_name.encode()).hexdigest()

    def save_asset(self, asset_name: str, asset_data: Any) -> None:
        """
        Saves a user-generated asset securely by encrypting it.

        :param asset_name: The name of the asset to save.
        :param asset_data: The actual data of the asset to save.
        :raises OSError: If there is an error writing the file.
        """
        asset_hash = self.hash_asset_name(asset_name)
        asset_file_path = os.path.join(self.storage_directory, f"{asset_hash}.bin")

        # Convert asset data to JSON format and encrypt it
        asset_json = json.dumps(asset_data)
        encrypted_data = self.cipher.encrypt(asset_json.encode())

        try:
            with open(asset_file_path, 'wb') as asset_file:
                asset_file.write(encrypted_data)
        except OSError as e:
            print(f"Error saving asset {asset_name}: {e}")
            raise

    def load_asset(self, asset_name: str) -> Any:
        """
        Loads a user-generated asset by decrypting it.

        :param asset_name: The name of the asset to load.
        :return: The decrypted asset data.
        :raises FileNotFoundError: If the asset file does not exist.
        :raises ValueError: If decryption fails.
        """
        asset_hash = self.hash_asset_name(asset_name)
        asset_file_path = os.path.join(self.storage_directory, f"{asset_hash}.bin")

        try:
            with open(asset_file_path, 'rb') as asset_file:
                encrypted_data = asset_file.read()
                decrypted_data = self.cipher.decrypt(encrypted_data)
                return json.loads(decrypted_data.decode())
        except FileNotFoundError:
            print(f"Asset {asset_name} not found.")
            raise
        except (ValueError, json.JSONDecodeError) as e:
            print(f"Error loading asset {asset_name}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Generate a key and instantiate the manager
    key = Fernet.generate_key()  # Store this key securely
    manager = GameAssetManager(storage_directory='assets', encryption_key=key)

    # Save an example asset
    sample_asset = {'type': 'character', 'attributes': {'name': 'Hero', 'level': 5}}
    manager.save_asset(asset_name='hero_character', asset_data=sample_asset)

    # Load the asset back
    loaded_asset = manager.load_asset(asset_name='hero_character')
    print(loaded_asset)  # Output the loaded asset
```
