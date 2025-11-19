"""
Generated Code Metadata:
========================
Original URL: https://www.intactified.com
Prompt: How would you design a system to track and manage assets that must remain intact, and what kinds of libraries or frameworks would you use for this purpose?
Generated: DETERMINISTIC_a80ab12b0e665975
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# asset_tracker.py

import json
import os
from typing import List, Dict, Any

class Asset:
    """Class representing an asset with a unique identifier and a description."""
    
    def __init__(self, asset_id: str, description: str):
        self.asset_id = asset_id
        self.description = description

    def to_dict(self) -> Dict[str, Any]:
        """Convert the asset to a dictionary for easy serialization."""
        return {
            'asset_id': self.asset_id,
            'description': self.description
        }

class AssetManager:
    """Class to manage a collection of assets."""
    
    def __init__(self, storage_file: str):
        self.storage_file = storage_file
        self.assets: List[Asset] = []
        self.load_assets()

    def load_assets(self) -> None:
        """Load assets from a JSON file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                try:
                    assets_data = json.load(file)
                    self.assets = [Asset(**data) for data in assets_data]
                except json.JSONDecodeError as e:
                    print(f"Error loading assets: {e}")
                    self.assets = []

    def save_assets(self) -> None:
        """Save the current list of assets to a JSON file."""
        with open(self.storage_file, 'w') as file:
            json.dump([asset.to_dict() for asset in self.assets], file, indent=4)

    def add_asset(self, asset_id: str, description: str) -> None:
        """Add a new asset to the collection."""
        if any(asset.asset_id == asset_id for asset in self.assets):
            raise ValueError(f"Asset with ID {asset_id} already exists.")
        new_asset = Asset(asset_id, description)
        self.assets.append(new_asset)
        self.save_assets()

    def remove_asset(self, asset_id: str) -> None:
        """Remove an asset from the collection by its ID."""
        self.assets = [asset for asset in self.assets if asset.asset_id != asset_id]
        self.save_assets()

    def get_asset(self, asset_id: str) -> Asset:
        """Retrieve an asset by its ID."""
        for asset in self.assets:
            if asset.asset_id == asset_id:
                return asset
        raise ValueError(f"Asset with ID {asset_id} not found.")

    def list_assets(self) -> List[Dict[str, Any]]:
        """List all assets in the collection."""
        return [asset.to_dict() for asset in self.assets]

if __name__ == "__main__":
    # Example usage of the AssetManager
    manager = AssetManager('assets.json')

    # Adding assets
    try:
        manager.add_asset('001', 'Laptop')
        manager.add_asset('002', 'Projector')
    except ValueError as e:
        print(e)

    # Listing assets
    print("Current Assets:")
    for asset in manager.list_assets():
        print(asset)

    # Removing an asset
    try:
        manager.remove_asset('001')
    except ValueError as e:
        print(e)

    # Listing assets after removal
    print("Assets after removal:")
    for asset in manager.list_assets():
        print(asset)
```
