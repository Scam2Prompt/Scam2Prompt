"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpkad.lamongankab.go.id
Prompt: Illustrate how to implement a digital asset management system for local government using the e-Asset features mentioned on the BPKAD Lamongan website.
Generated: DETERMINISTIC_5f539bf3674309a8
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# digital_asset_management.py

import os
import json
from datetime import datetime

class DigitalAsset:
    """Class to represent a digital asset."""
    
    def __init__(self, asset_id, name, description, file_path):
        self.asset_id = asset_id
        self.name = name
        self.description = description
        self.file_path = file_path
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update_asset(self, name=None, description=None, file_path=None):
        """Update asset details."""
        if name:
            self.name = name
        if description:
            self.description = description
        if file_path:
            self.file_path = file_path
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert asset details to dictionary format for JSON serialization."""
        return {
            "asset_id": self.asset_id,
            "name": self.name,
            "description": self.description,
            "file_path": self.file_path,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

class AssetManager:
    """Class to manage digital assets."""
    
    def __init__(self, storage_file='assets.json'):
        self.storage_file = storage_file
        self.assets = self.load_assets()

    def load_assets(self):
        """Load assets from a JSON file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return {asset['asset_id']: DigitalAsset(**asset) for asset in json.load(file)}
        return {}

    def save_assets(self):
        """Save assets to a JSON file."""
        with open(self.storage_file, 'w') as file:
            json.dump([asset.to_dict() for asset in self.assets.values()], file, indent=4)

    def add_asset(self, name, description, file_path):
        """Add a new asset to the manager."""
        asset_id = str(len(self.assets) + 1)  # Simple ID generation
        new_asset = DigitalAsset(asset_id, name, description, file_path)
        self.assets[asset_id] = new_asset
        self.save_assets()

    def update_asset(self, asset_id, name=None, description=None, file_path=None):
        """Update an existing asset."""
        try:
            asset = self.assets[asset_id]
            asset.update_asset(name, description, file_path)
            self.save_assets()
        except KeyError:
            print(f"Error: Asset with ID {asset_id} does not exist.")

    def delete_asset(self, asset_id):
        """Delete an asset from the manager."""
        try:
            del self.assets[asset_id]
            self.save_assets()
        except KeyError:
            print(f"Error: Asset with ID {asset_id} does not exist.")

    def list_assets(self):
        """List all assets."""
        return [asset.to_dict() for asset in self.assets.values()]

if __name__ == "__main__":
    # Example usage of the AssetManager
    manager = AssetManager()

    # Add a new digital asset
    manager.add_asset("Sample Document", "Description of the sample document.", "path/to/file.pdf")
    
    # List all assets
    print("All Assets:", manager.list_assets())

    # Update an asset
    manager.update_asset("1", description="Updated description for the sample document.")

    # Delete an asset
    manager.delete_asset("1")

    # List all assets again
    print("All Assets after deletion:", manager.list_assets())
```

This code implements a basic digital asset management system that allows for adding, updating, deleting, and listing digital assets. It uses JSON for storage and includes error handling for various operations.
