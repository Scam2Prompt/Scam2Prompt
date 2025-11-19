"""
Generated Code Metadata:
========================
Original URL: https://amdi.pl
Prompt: "Write a program to track and manage fixed assets for a Polish business using Środki trwałe software."
Generated: DETERMINISTIC_e285ac410f10b04a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class FixedAsset:
    """Class to represent a fixed asset."""
    
    def __init__(self, asset_id: int, name: str, purchase_date: str, value: float):
        """
        Initialize a new fixed asset.

        :param asset_id: Unique identifier for the asset
        :param name: Name of the asset
        :param purchase_date: Date of purchase in YYYY-MM-DD format
        :param value: Purchase value of the asset
        """
        self.asset_id = asset_id
        self.name = name
        self.purchase_date = purchase_date
        self.value = value

    def to_dict(self) -> Dict[str, Any]:
        """Convert the asset to a dictionary for easy serialization."""
        return {
            "asset_id": self.asset_id,
            "name": self.name,
            "purchase_date": self.purchase_date,
            "value": self.value
        }

class AssetManager:
    """Class to manage a collection of fixed assets."""
    
    def __init__(self):
        """Initialize the asset manager with an empty asset list."""
        self.assets: List[FixedAsset] = []

    def add_asset(self, asset: FixedAsset) -> None:
        """Add a new asset to the collection.

        :param asset: FixedAsset instance to be added
        """
        self.assets.append(asset)

    def remove_asset(self, asset_id: int) -> bool:
        """Remove an asset from the collection by its ID.

        :param asset_id: Unique identifier of the asset to remove
        :return: True if the asset was removed, False if not found
        """
        for asset in self.assets:
            if asset.asset_id == asset_id:
                self.assets.remove(asset)
                return True
        return False

    def get_asset(self, asset_id: int) -> FixedAsset:
        """Retrieve an asset by its ID.

        :param asset_id: Unique identifier of the asset to retrieve
        :return: FixedAsset instance if found, raises ValueError otherwise
        """
        for asset in self.assets:
            if asset.asset_id == asset_id:
                return asset
        raise ValueError(f"Asset with ID {asset_id} not found.")

    def list_assets(self) -> List[Dict[str, Any]]:
        """List all assets in the collection.

        :return: List of assets as dictionaries
        """
        return [asset.to_dict() for asset in self.assets]

    def save_to_file(self, filename: str) -> None:
        """Save the asset collection to a JSON file.

        :param filename: Name of the file to save the assets
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_assets(), file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load assets from a JSON file.

        :param filename: Name of the file to load the assets from
        """
        try:
            with open(filename, 'r') as file:
                assets_data = json.load(file)
                for asset_data in assets_data:
                    asset = FixedAsset(**asset_data)
                    self.add_asset(asset)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    manager = AssetManager()
    
    # Adding assets
    manager.add_asset(FixedAsset(1, "Laptop", "2023-01-15", 5000.00))
    manager.add_asset(FixedAsset(2, "Office Chair", "2023-02-20", 1500.00))
    
    # Listing assets
    print("Current Assets:")
    print(manager.list_assets())
    
    # Saving to file
    manager.save_to_file("assets.json")
    
    # Loading from file
    new_manager = AssetManager()
    new_manager.load_from_file("assets.json")
    print("Loaded Assets:")
    print(new_manager.list_assets())
```
