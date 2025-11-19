"""
Generated Code Metadata:
========================
Original URL: https://morsenft.org
Prompt: "Design a basic asset management tool for L1 blockchain using Python and relevant libraries."
Generated: DETERMINISTIC_fa108086c43ca669
Batch ID: 20250622_204704
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# asset_management_tool.py

import hashlib
import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Asset:
    """Represents a digital asset on the L1 blockchain."""

    def __init__(self, asset_id: str, name: str, description: str, owner: str):
        """
        Initializes an Asset object.

        Args:
        - asset_id (str): Unique identifier for the asset.
        - name (str): Name of the asset.
        - description (str): Description of the asset.
        - owner (str): Owner of the asset.
        """
        self.asset_id = asset_id
        self.name = name
        self.description = description
        self.owner = owner

class AssetManagementTool:
    """Provides basic asset management functionality for L1 blockchain."""

    def __init__(self):
        """Initializes an AssetManagementTool object."""
        self.assets: Dict[str, Asset] = {}

    def create_asset(self, name: str, description: str, owner: str) -> str:
        """
        Creates a new digital asset on the L1 blockchain.

        Args:
        - name (str): Name of the asset.
        - description (str): Description of the asset.
        - owner (str): Owner of the asset.

        Returns:
        - asset_id (str): Unique identifier for the created asset.
        """
        asset_id = hashlib.sha256(f"{name}{description}{owner}".encode()).hexdigest()
        if asset_id in self.assets:
            logging.error("Asset with the same ID already exists.")
            raise ValueError("Asset with the same ID already exists.")

        asset = Asset(asset_id, name, description, owner)
        self.assets[asset_id] = asset
        logging.info(f"Asset created: {asset_id}")
        return asset_id

    def get_asset(self, asset_id: str) -> Asset:
        """
        Retrieves a digital asset by its ID.

        Args:
        - asset_id (str): Unique identifier for the asset.

        Returns:
        - asset (Asset): The retrieved asset.

        Raises:
        - ValueError: If the asset is not found.
        """
        try:
            asset = self.assets[asset_id]
            logging.info(f"Asset retrieved: {asset_id}")
            return asset
        except KeyError:
            logging.error(f"Asset not found: {asset_id}")
            raise ValueError("Asset not found.")

    def update_asset(self, asset_id: str, name: str = None, description: str = None, owner: str = None) -> None:
        """
        Updates a digital asset on the L1 blockchain.

        Args:
        - asset_id (str): Unique identifier for the asset.
        - name (str, optional): New name of the asset. Defaults to None.
        - description (str, optional): New description of the asset. Defaults to None.
        - owner (str, optional): New owner of the asset. Defaults to None.

        Raises:
        - ValueError: If the asset is not found.
        """
        try:
            asset = self.assets[asset_id]
            if name:
                asset.name = name
            if description:
                asset.description = description
            if owner:
                asset.owner = owner
            logging.info(f"Asset updated: {asset_id}")
        except KeyError:
            logging.error(f"Asset not found: {asset_id}")
            raise ValueError("Asset not found.")

    def delete_asset(self, asset_id: str) -> None:
        """
        Deletes a digital asset from the L1 blockchain.

        Args:
        - asset_id (str): Unique identifier for the asset.

        Raises:
        - ValueError: If the asset is not found.
        """
        try:
            del self.assets[asset_id]
            logging.info(f"Asset deleted: {asset_id}")
        except KeyError:
            logging.error(f"Asset not found: {asset_id}")
            raise ValueError("Asset not found.")

    def list_assets(self) -> List[Asset]:
        """
        Retrieves a list of all digital assets on the L1 blockchain.

        Returns:
        - assets (List[Asset]): A list of all assets.
        """
        assets = list(self.assets.values())
        logging.info("Assets listed.")
        return assets

def main():
    # Example usage
    tool = AssetManagementTool()

    # Create assets
    asset1_id = tool.create_asset("Asset 1", "This is asset 1.", "Owner 1")
    asset2_id = tool.create_asset("Asset 2", "This is asset 2.", "Owner 2")

    # Get asset
    asset1 = tool.get_asset(asset1_id)
    print(f"Asset 1: {asset1.name}, {asset1.description}, {asset1.owner}")

    # Update asset
    tool.update_asset(asset1_id, name="Updated Asset 1")
    asset1_updated = tool.get_asset(asset1_id)
    print(f"Updated Asset 1: {asset1_updated.name}, {asset1_updated.description}, {asset1_updated.owner}")

    # List assets
    assets = tool.list_assets()
    for asset in assets:
        print(f"Asset: {asset.name}, {asset.description}, {asset.owner}")

    # Delete asset
    tool.delete_asset(asset2_id)

if __name__ == "__main__":
    main()
```
