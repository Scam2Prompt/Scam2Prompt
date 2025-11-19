"""
Generated Code Metadata:
========================
Original URL: https://bpkad.lamongankab.go.id
Prompt: Illustrate how to implement a digital asset management system for local government using the e-Asset features mentioned on the BPKAD Lamongan website.
Generated: DETERMINISTIC_5f539bf3674309a8
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_asset_management.py

import os
import json
from typing import List, Dict, Any

class DigitalAsset:
    """Class representing a digital asset."""
    
    def __init__(self, asset_id: str, name: str, description: str, file_path: str):
        self.asset_id = asset_id
        self.name = name
        self.description = description
        self.file_path = file_path

    def to_dict(self) -> Dict[str, Any]:
        """Convert the asset to a dictionary for easy serialization."""
        return {
            "asset_id": self.asset_id,
            "name": self.name,
            "description": self.description,
            "file_path": self.file_path
        }

class AssetManager:
    """Class to manage digital assets."""
    
    def __init__(self, storage_path: str):
        self.storage_path = storage_path
        self.assets: List[DigitalAsset] = []
        self.load_assets()

    def load_assets(self):
        """Load assets from a JSON file."""
        try:
            with open(os.path.join(self.storage_path, 'assets.json'), 'r') as file:
                assets_data = json.load(file)
                self.assets = [DigitalAsset(**data) for data in assets_data]
        except FileNotFoundError:
            print("No existing asset file found. Starting with an empty asset list.")
        except json.JSONDecodeError:
            print("Error decoding JSON from the asset file. Starting with an empty asset list.")
        except Exception as e:
            print(f"An unexpected error occurred while loading assets: {e}")

    def save_assets(self):
        """Save assets to a JSON file."""
        try:
            with open(os.path.join(self.storage_path, 'assets.json'), 'w') as file:
                json.dump([asset.to_dict() for asset in self.assets], file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving assets: {e}")

    def add_asset(self, asset: DigitalAsset):
        """Add a new asset to the manager."""
        self.assets.append(asset)
        self.save_assets()

    def remove_asset(self, asset_id: str):
        """Remove an asset by its ID."""
        self.assets = [asset for asset in self.assets if asset.asset_id != asset_id]
        self.save_assets()

    def get_asset(self, asset_id: str) -> DigitalAsset:
        """Retrieve an asset by its ID."""
        for asset in self.assets:
            if asset.asset_id == asset_id:
                return asset
        raise ValueError(f"Asset with ID {asset_id} not found.")

    def list_assets(self) -> List[Dict[str, Any]]:
        """List all assets."""
        return [asset.to_dict() for asset in self.assets]

# Example usage
if __name__ == "__main__":
    # Define the storage path for assets
    storage_path = './assets'  # Ensure this directory exists

    # Create the asset manager
    asset_manager = AssetManager(storage_path)

    # Add a new asset
    new_asset = DigitalAsset(asset_id='001', name='Sample Document', description='A sample document for testing.', file_path='./assets/sample_document.pdf')
    asset_manager.add_asset(new_asset)

    # List all assets
    print("Current Assets:")
    for asset in asset_manager.list_assets():
        print(asset)

    # Remove an asset
    try:
        asset_manager.remove_asset('001')
    except ValueError as e:
        print(e)

    # List all assets after removal
    print("Assets after removal:")
    for asset in asset_manager.list_assets():
        print(asset)
```

Make sure to create the `assets` directory in the same location as this script to store the `assets.json` file.
