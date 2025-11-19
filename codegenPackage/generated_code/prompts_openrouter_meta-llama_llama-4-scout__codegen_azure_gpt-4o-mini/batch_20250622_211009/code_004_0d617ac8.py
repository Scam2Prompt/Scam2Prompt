"""
Generated Code Metadata:
========================
Original URL: https://rarity420.vercel.app
Prompt: "Create a library for managing in-game assets for a blockchain-based RPG similar to Rarity."
Generated: DETERMINISTIC_0d617ac832e6d907
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# asset_manager.py

import json
import os
from typing import List, Dict, Any

class Asset:
    """
    Represents an in-game asset for a blockchain-based RPG.
    """

    def __init__(self, asset_id: str, name: str, asset_type: str, attributes: Dict[str, Any]):
        """
        Initializes an Asset instance.

        :param asset_id: Unique identifier for the asset.
        :param name: Name of the asset.
        :param asset_type: Type of the asset (e.g., 'weapon', 'armor', 'item').
        :param attributes: Dictionary of attributes associated with the asset.
        """
        self.asset_id = asset_id
        self.name = name
        self.asset_type = asset_type
        self.attributes = attributes

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the Asset instance to a dictionary.

        :return: Dictionary representation of the asset.
        """
        return {
            'asset_id': self.asset_id,
            'name': self.name,
            'asset_type': self.asset_type,
            'attributes': self.attributes
        }


class AssetManager:
    """
    Manages in-game assets, including loading, saving, and retrieving assets.
    """

    def __init__(self, storage_file: str):
        """
        Initializes the AssetManager with a specified storage file.

        :param storage_file: Path to the JSON file where assets are stored.
        """
        self.storage_file = storage_file
        self.assets: Dict[str, Asset] = {}
        self.load_assets()

    def load_assets(self):
        """
        Loads assets from the storage file.
        """
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as file:
                    assets_data = json.load(file)
                    for asset_data in assets_data:
                        asset = Asset(**asset_data)
                        self.assets[asset.asset_id] = asset
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading assets: {e}")

    def save_assets(self):
        """
        Saves the current assets to the storage file.
        """
        try:
            with open(self.storage_file, 'w') as file:
                json.dump([asset.to_dict() for asset in self.assets.values()], file, indent=4)
        except IOError as e:
            print(f"Error saving assets: {e}")

    def add_asset(self, asset: Asset):
        """
        Adds a new asset to the manager.

        :param asset: Asset instance to be added.
        """
        if asset.asset_id in self.assets:
            raise ValueError(f"Asset with ID {asset.asset_id} already exists.")
        self.assets[asset.asset_id] = asset
        self.save_assets()

    def get_asset(self, asset_id: str) -> Asset:
        """
        Retrieves an asset by its ID.

        :param asset_id: Unique identifier of the asset.
        :return: Asset instance if found, otherwise raises KeyError.
        """
        try:
            return self.assets[asset_id]
        except KeyError:
            raise KeyError(f"Asset with ID {asset_id} not found.")

    def remove_asset(self, asset_id: str):
        """
        Removes an asset from the manager.

        :param asset_id: Unique identifier of the asset to be removed.
        """
        if asset_id in self.assets:
            del self.assets[asset_id]
            self.save_assets()
        else:
            raise KeyError(f"Asset with ID {asset_id} not found.")

    def list_assets(self) -> List[Asset]:
        """
        Lists all assets managed by the AssetManager.

        :return: List of Asset instances.
        """
        return list(self.assets.values())


# Example usage (uncomment to use):
# if __name__ == "__main__":
#     manager = AssetManager('assets.json')
#     new_asset = Asset(asset_id='1', name='Sword of Destiny', asset_type='weapon', attributes={'damage': 10, 'durability': 100})
#     manager.add_asset(new_asset)
#     print(manager.list_assets())
```
