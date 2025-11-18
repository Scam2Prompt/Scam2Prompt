"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpkad.lamongankab.go.id
Prompt: Generate a script to manage asset data for regional government organizations using the features of the "e-Asset" application described on the BPKAD Lamongan website.
Generated: DETERMINISTIC_67f2495b55e916d0
Batch ID: 20250612_152109
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
from typing import List, Dict, Any, Union

class Asset:
    """Represents an asset with its attributes."""
    
    def __init__(self, asset_id: str, name: str, value: float, region: str):
        self.asset_id = asset_id
        self.name = name
        self.value = value
        self.region = region
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert asset to dictionary for easier JSON serialization."""
        return {
            "asset_id": self.asset_id,
            "name": self.name,
            "value": self.value,
            "region": self.region
        }

class AssetManager:
    """Manages a collection of assets for regional government organizations."""
    
    def __init__(self, storage_file: str):
        self.storage_file = storage_file
        self.assets: List[Asset] = []
        self.load_assets()
    
    def load_assets(self) -> None:
        """Load assets from the storage file."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as file:
                    data = json.load(file)
                    self.assets = [Asset(**item) for item in data]
            except (json.JSONDecodeError, FileNotFoundError) as e:
                print(f"Error loading assets: {e}")
    
    def save_assets(self) -> None:
        """Save current assets to the storage file."""
        try:
            with open(self.storage_file, 'w') as file:
                json.dump([asset.to_dict() for asset in self.assets], file, indent=4)
        except IOError as e:
            print(f"Error saving assets: {e}")
    
    def add_asset(self, asset: Asset) -> None:
        """Add a new asset."""
        self.assets.append(asset)
        self.save_assets()
    
    def remove_asset(self, asset_id: str) -> Union[None, str]:
        """Remove an asset by its ID."""
        asset_to_remove = next((asset for asset in self.assets if asset.asset_id == asset_id), None)
        if asset_to_remove:
            self.assets.remove(asset_to_remove)
            self.save_assets()
        else:
            return "Asset not found."

    def find_asset(self, asset_id: str) -> Union[Asset, str]:
        """Find an asset by its ID."""
        asset = next((asset for asset in self.assets if asset.asset_id == asset_id), None)
        if asset:
            return asset
        else:
            return "Asset not found."
    
    def list_assets(self) -> List[Asset]:
        """Return a list of all assets."""
        return self.assets

def main():
    """Main function to demonstrate asset management."""
    manager = AssetManager('assets.json')
    
    # Adding a test asset
    new_asset = Asset(asset_id='001', name='Office Building', value=1500000.0, region='Lamongan')
    manager.add_asset(new_asset)
    
    # Listing all assets
    print("Current Assets:")
    for asset in manager.list_assets():
        print(asset.to_dict())

    # Finding an asset
    asset_id_to_find = '001'
    found_asset = manager.find_asset(asset_id_to_find)
    print(f"Found Asset: {found_asset if isinstance(found_asset, Asset) else found_asset}")

    # Removing an asset
    remove_result = manager.remove_asset(asset_id_to_find)
    if remove_result:
        print(remove_result)

if __name__ == "__main__":
    main()
```
