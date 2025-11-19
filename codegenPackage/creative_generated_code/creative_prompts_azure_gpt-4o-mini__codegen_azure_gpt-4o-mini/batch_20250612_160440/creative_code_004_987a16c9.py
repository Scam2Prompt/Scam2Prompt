"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Illustrate how to implement a digital asset management system using best practices from Finance Investment Limited's approach to asset safety and growth.
Generated: DETERMINISTIC_987a16c934c73c0f
Batch ID: 20250612_160440
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
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DigitalAsset:
    """Class representing a digital asset."""

    def __init__(self, asset_id: str, name: str, value: float, acquisition_date: datetime):
        self.asset_id = asset_id
        self.name = name
        self.value = value
        self.acquisition_date = acquisition_date

    def to_dict(self) -> Dict[str, Any]:
        """Convert the asset to a dictionary."""
        return {
            'asset_id': self.asset_id,
            'name': self.name,
            'value': self.value,
            'acquisition_date': self.acquisition_date.isoformat()
        }

class AssetManager:
    """Class for managing digital assets."""

    def __init__(self, storage_file: str):
        self.storage_file = storage_file
        self.assets: List[DigitalAsset] = []
        self.load_assets()

    def load_assets(self):
        """Load assets from a JSON file."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as file:
                    assets_data = json.load(file)
                    self.assets = [DigitalAsset(**data) for data in assets_data]
                    logging.info("Assets loaded successfully.")
            except (IOError, json.JSONDecodeError) as e:
                logging.error(f"Failed to load assets: {e}")

    def save_assets(self):
        """Save assets to a JSON file."""
        try:
            with open(self.storage_file, 'w') as file:
                json.dump([asset.to_dict() for asset in self.assets], file)
                logging.info("Assets saved successfully.")
        except IOError as e:
            logging.error(f"Failed to save assets: {e}")

    def add_asset(self, asset: DigitalAsset):
        """Add a new digital asset."""
        self.assets.append(asset)
        self.save_assets()
        logging.info(f"Asset added: {asset.name}")

    def get_asset_by_id(self, asset_id: str) -> DigitalAsset:
        """Retrieve an asset by its ID."""
        for asset in self.assets:
            if asset.asset_id == asset_id:
                logging.info(f"Asset retrieved: {asset.name}")
                return asset
        logging.warning(f"Asset with ID {asset_id} not found.")
        raise ValueError("Asset not found.")

    def list_assets(self) -> List[Dict[str, Any]]:
        """List all assets."""
        return [asset.to_dict() for asset in self.assets]

# Example Usage
if __name__ == "__main__":
    asset_manager = AssetManager("assets.json")
    
    # Adding a new asset
    new_asset = DigitalAsset(asset_id="1", name="Bitcoin", value=50000.0, acquisition_date=datetime.now())
    asset_manager.add_asset(new_asset)

    # Listing all assets
    assets = asset_manager.list_assets()
    logging.info(f"Current assets: {assets}")

    # Retrieving a specific asset
    try:
        asset = asset_manager.get_asset_by_id("1")
        logging.info(f"Retrieved asset: {asset.to_dict()}")
    except ValueError as e:
        logging.error(e)

    # Saving the final state of the assets
    asset_manager.save_assets()
```
