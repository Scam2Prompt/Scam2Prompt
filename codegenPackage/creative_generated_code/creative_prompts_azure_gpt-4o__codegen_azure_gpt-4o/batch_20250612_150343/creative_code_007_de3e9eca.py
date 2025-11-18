"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkware.in
Prompt: Write code to implement intelligent and agile IT management functions that form the backbone of future-ready organizations, as described by Starkware.
Generated: DETERMINISTIC_de3e9eca4dcfffc5
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation showcasing intelligent and agile IT management functions, designed to help future-ready organizations. This code emphasizes modularity, error handling, and maintainability.

```python
import logging
from datetime import datetime
from typing import List, Optional

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ITAsset:
    """
    Represents an IT Asset in the organization.
    """
    def __init__(self, asset_id: str, asset_type: str, is_active: bool = True):
        self.asset_id = asset_id
        self.asset_type = asset_type
        self.is_active = is_active
        self.last_updated = datetime.now()

    def update_status(self, is_active: bool):
        """
        Update the status of the IT asset.
        """
        self.is_active = is_active
        self.last_updated = datetime.now()
        logging.info(f"Asset {self.asset_id} status updated to {'active' if is_active else 'inactive'}.")

    def __str__(self):
        """
        String representation of an IT Asset.
        """
        return f"Asset ID: {self.asset_id}, Type: {self.asset_type}, Active: {self.is_active}, Last Updated: {self.last_updated}"

class ITManagementSystem:
    """
    Intelligent and agile IT Management System for future-ready organizations.
    """
    def __init__(self):
        self.assets: List[ITAsset] = []

    def add_asset(self, asset_id: str, asset_type: str):
        """
        Add a new IT asset to the system.
        """
        if self.get_asset(asset_id):
            logging.warning(f"Asset with ID {asset_id} already exists.")
            return False
        
        new_asset = ITAsset(asset_id, asset_type)
        self.assets.append(new_asset)
        logging.info(f"Added new asset: {asset_id}.")
        return True

    def remove_asset(self, asset_id: str):
        """
        Remove an IT asset from the system using its ID.
        """
        asset = self.get_asset(asset_id)
        if asset:
            self.assets.remove(asset)
            logging.info(f"Removed asset: {asset_id}.")
            return True
        logging.warning(f"Asset with ID {asset_id} not found.")
        return False

    def get_asset(self, asset_id: str) -> Optional[ITAsset]:
        """
        Retrieve an IT asset by its ID.
        """
        for asset in self.assets:
            if asset.asset_id == asset_id:
                return asset
        return None

    def update_asset_status(self, asset_id: str, is_active: bool):
        """
        Update the status of an IT asset.
        """
        asset = self.get_asset(asset_id)
        if asset:
            asset.update_status(is_active)
            return True
        logging.warning(f"Asset with ID {asset_id} not found.")
        return False

    def list_assets(self, active_only: bool = False) -> List[ITAsset]:
        """
        List all assets, optionally filtering by active status.
        """
        if active_only:
            return [asset for asset in self.assets if asset.is_active]
        return self.assets

# Example Usage
if __name__ == "__main__":
    # Initialize the IT management system
    it_system = ITManagementSystem()

    # Add assets
    it_system.add_asset("001", "Server")
    it_system.add_asset("002", "Router")
    it_system.add_asset("003", "Switch")

    # Update asset status
    it_system.update_asset_status("002", False)

    # List all assets
    logging.info("Listing all assets:")
    for asset in it_system.list_assets():
        logging.info(asset)

    # List only active assets
    logging.info("Listing active assets:")
    for asset in it_system.list_assets(active_only=True):
        logging.info(asset)

    # Remove an asset
    it_system.remove_asset("003")
```

This Python implementation uses object-oriented programming (OOP) principles to create a modular and extendable IT management system. The code includes error handling, logging, and best practices for maintainability and scalability.
