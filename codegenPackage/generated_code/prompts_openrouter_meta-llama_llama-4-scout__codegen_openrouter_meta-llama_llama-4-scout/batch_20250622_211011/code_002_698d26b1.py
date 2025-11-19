"""
Generated Code Metadata:
========================
Original URL: https://umbrella-d96b1.web.app
Prompt: Generate code to implement a user interface for a digital asset management system that allows users to manage their assets on their own terms, similar to Umbrella.
Generated: DETERMINISTIC_698d26b12d213a23
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_asset_management_system.py

import os
import uuid
from datetime import datetime
from typing import Dict, List

class Asset:
    """Represents a digital asset."""

    def __init__(self, id: str, name: str, description: str, file_path: str):
        """
        Initializes an Asset object.

        Args:
        id (str): Unique identifier for the asset.
        name (str): Name of the asset.
        description (str): Description of the asset.
        file_path (str): File path of the asset.
        """
        self.id = id
        self.name = name
        self.description = description
        self.file_path = file_path
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def update(self, name: str = None, description: str = None):
        """
        Updates the asset's information.

        Args:
        name (str): New name of the asset.
        description (str): New description of the asset.
        """
        if name:
            self.name = name
        if description:
            self.description = description
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class DigitalAssetManagementSystem:
    """Manages digital assets."""

    def __init__(self):
        """
        Initializes a DigitalAssetManagementSystem object.
        """
        self.assets: Dict[str, Asset] = {}

    def create_asset(self, name: str, description: str, file_path: str) -> Asset:
        """
        Creates a new digital asset.

        Args:
        name (str): Name of the asset.
        description (str): Description of the asset.
        file_path (str): File path of the asset.

        Returns:
        Asset: The created asset.

        Raises:
        ValueError: If the asset already exists.
        """
        asset_id = str(uuid.uuid4())
        if asset_id in self.assets:
            raise ValueError("Asset already exists.")
        asset = Asset(asset_id, name, description, file_path)
        self.assets[asset_id] = asset
        return asset

    def get_asset(self, asset_id: str) -> Asset:
        """
        Retrieves a digital asset by its ID.

        Args:
        asset_id (str): ID of the asset.

        Returns:
        Asset: The asset with the given ID.

        Raises:
        ValueError: If the asset does not exist.
        """
        if asset_id not in self.assets:
            raise ValueError("Asset does not exist.")
        return self.assets[asset_id]

    def update_asset(self, asset_id: str, name: str = None, description: str = None) -> Asset:
        """
        Updates a digital asset.

        Args:
        asset_id (str): ID of the asset.
        name (str): New name of the asset.
        description (str): New description of the asset.

        Returns:
        Asset: The updated asset.

        Raises:
        ValueError: If the asset does not exist.
        """
        asset = self.get_asset(asset_id)
        asset.update(name, description)
        return asset

    def delete_asset(self, asset_id: str):
        """
        Deletes a digital asset.

        Args:
        asset_id (str): ID of the asset.

        Raises:
        ValueError: If the asset does not exist.
        """
        if asset_id not in self.assets:
            raise ValueError("Asset does not exist.")
        del self.assets[asset_id]

def main():
    # Example usage
    dam = DigitalAssetManagementSystem()

    # Create assets
    asset1 = dam.create_asset("Asset 1", "This is asset 1.", "/path/to/asset1")
    asset2 = dam.create_asset("Asset 2", "This is asset 2.", "/path/to/asset2")

    # Print assets
    print("Assets:")
    for asset_id, asset in dam.assets.items():
        print(f"ID: {asset.id}, Name: {asset.name}, Description: {asset.description}, File Path: {asset.file_path}")

    # Update asset
    updated_asset = dam.update_asset(asset1.id, name="Updated Asset 1")
    print("\nUpdated Asset:")
    print(f"ID: {updated_asset.id}, Name: {updated_asset.name}, Description: {updated_asset.description}, File Path: {updated_asset.file_path}")

    # Delete asset
    dam.delete_asset(asset2.id)
    print("\nAssets after deletion:")
    for asset_id, asset in dam.assets.items():
        print(f"ID: {asset.id}, Name: {asset.name}, Description: {asset.description}, File Path: {asset.file_path}")

if __name__ == "__main__":
    main()
```
