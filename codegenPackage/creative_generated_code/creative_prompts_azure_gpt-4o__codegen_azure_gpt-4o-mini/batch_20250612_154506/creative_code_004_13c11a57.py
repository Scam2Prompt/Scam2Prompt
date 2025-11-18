"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://norion.loan
Prompt: Provide an implementation for managing digital assets securely, inspired by the corporate brand services mentioned on norion.loan.
Generated: DETERMINISTIC_13c11a57a5427191
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
import hashlib
import base64
from cryptography.fernet import Fernet
from typing import Dict, Any, Optional

class DigitalAssetManager:
    """
    A class to manage digital assets securely by encrypting, decrypting,
    and storing metadata for each asset.
    """

    def __init__(self, encryption_key: Optional[bytes] = None):
        """
        Initializes the DigitalAssetManager with a provided encryption key.
        If no key is provided, a new key is generated.

        :param encryption_key: Bytes to be used for encryption. If None, a new key is generated.
        """
        if encryption_key is None:
            self.encryption_key = Fernet.generate_key()
        else:
            self.encryption_key = encryption_key

        self.cipher = Fernet(self.encryption_key)
        self.assets = {}

    def _hash_asset_name(self, asset_name: str) -> str:
        """
        Creates a SHA-256 hash of the asset name for secure storage.

        :param asset_name: Name of the asset to hash.
        :return: Hexadecimal string of the hashed asset name.
        """
        return hashlib.sha256(asset_name.encode()).hexdigest()

    def add_asset(self, asset_name: str, asset_data: Any) -> None:
        """
        Adds a new digital asset by encrypting its data and storing it with
        its metadata.

        :param asset_name: Name of the asset to be stored.
        :param asset_data: Data of the asset to be encrypted and stored.
        :raises ValueError: If the asset name is empty or already exists.
        """
        if not asset_name:
            raise ValueError("Asset name cannot be empty.")
        
        hashed_name = self._hash_asset_name(asset_name)
        if hashed_name in self.assets:
            raise ValueError("Asset already exists.")

        encrypted_data = self.cipher.encrypt(json.dumps(asset_data).encode())
        self.assets[hashed_name] = {
            "encrypted_data": encrypted_data,
            "name": asset_name
        }

    def retrieve_asset(self, asset_name: str) -> Any:
        """
        Retrieves and decrypts the data of a specified digital asset.

        :param asset_name: Name of the asset to retrieve.
        :return: Decrypted asset data.
        :raises KeyError: If the asset does not exist.
        """
        hashed_name = self._hash_asset_name(asset_name)
        if hashed_name not in self.assets:
            raise KeyError("Asset not found.")

        encrypted_data = self.assets[hashed_name]["encrypted_data"]
        decrypted_data = self.cipher.decrypt(encrypted_data)
        return json.loads(decrypted_data)

    def list_assets(self) -> Dict[str, str]:
        """
        Lists all stored assets with their names.

        :return: Dictionary of asset hashes with their corresponding names.
        """
        return {key: value["name"] for key, value in self.assets.items()}

    def save_to_file(self, filepath: str) -> None:
        """
        Saves the current assets and encryption key to a JSON file.

        :param filepath: Path to the file where assets will be saved.
        :raises IOError: If saving to the file fails.
        """
        try:
            with open(filepath, 'w') as file:
                data = {
                    "encryption_key": base64.urlsafe_b64encode(self.encryption_key).decode(),
                    "assets": self.assets
                }
                json.dump(data, file)
        except Exception as e:
            raise IOError(f"Failed to save assets to file: {str(e)}")

    def load_from_file(self, filepath: str) -> None:
        """
        Loads assets and encryption key from a JSON file.

        :param filepath: Path to the file from which assets will be loaded.
        :raises IOError: If loading from the file fails.
        :raises ValueError: If the file format is incorrect.
        """
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
                self.encryption_key = base64.urlsafe_b64decode(data["encryption_key"])
                self.cipher = Fernet(self.encryption_key)
                self.assets = data["assets"]
        except Exception as e:
            raise IOError(f"Failed to load assets from file: {str(e)}")

# Example usage
if __name__ == "__main__":
    manager = DigitalAssetManager()

    # Add an asset
    manager.add_asset("image.png", {"type": "image", "content": "base64encodedstring"})

    # Retrieve an asset
    asset_data = manager.retrieve_asset("image.png")
    print(asset_data)

    # List all assets
    print(manager.list_assets())

    # Save assets to a file
    manager.save_to_file("assets.json")

    # Load assets from a file
    new_manager = DigitalAssetManager()
    new_manager.load_from_file("assets.json")
    print(new_manager.list_assets())
```
