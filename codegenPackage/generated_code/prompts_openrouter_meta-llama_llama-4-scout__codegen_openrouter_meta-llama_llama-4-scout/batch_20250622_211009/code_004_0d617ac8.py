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
# asset_library.py

from typing import Dict, List
from enum import Enum
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AssetType(str, Enum):
    """Enum for asset types."""
    ITEM = "item"
    CHARACTER = "character"
    SKIN = "skin"

class Asset:
    """Represents an in-game asset."""

    def __init__(self, 
                 asset_id: str, 
                 name: str, 
                 description: str, 
                 asset_type: AssetType, 
                 properties: Dict[str, str] = {}):
        """
        Initialize an Asset.

        Args:
        - asset_id (str): Unique identifier for the asset.
        - name (str): Name of the asset.
        - description (str): Description of the asset.
        - asset_type (AssetType): Type of the asset.
        - properties (Dict[str, str], optional): Additional properties of the asset. Defaults to {}.
        """
        self.asset_id = asset_id
        self.name = name
        self.description = description
        self.asset_type = asset_type
        self.properties = properties

    def to_dict(self) -> Dict:
        """Convert Asset to dictionary."""
        return {
            "asset_id": self.asset_id,
            "name": self.name,
            "description": self.description,
            "asset_type": self.asset_type.value,
            "properties": self.properties
        }

class AssetLibrary:
    """Manages in-game assets."""

    def __init__(self):
        """Initialize an empty AssetLibrary."""
        self.assets: Dict[str, Asset] = {}

    def add_asset(self, asset: Asset):
        """
        Add an asset to the library.

        Args:
        - asset (Asset): Asset to add.

        Raises:
        - ValueError: If an asset with the same ID already exists.
        """
        if asset.asset_id in self.assets:
            raise ValueError(f"Asset with ID {asset.asset_id} already exists.")
        self.assets[asset.asset_id] = asset
        logger.info(f"Added asset {asset.asset_id}")

    def get_asset(self, asset_id: str) -> Asset:
        """
        Get an asset by ID.

        Args:
        - asset_id (str): ID of the asset to retrieve.

        Returns:
        - Asset: The asset with the given ID.

        Raises:
        - ValueError: If the asset does not exist.
        """
        try:
            return self.assets[asset_id]
        except KeyError:
            raise ValueError(f"Asset with ID {asset_id} does not exist.")

    def update_asset(self, asset_id: str, **kwargs):
        """
        Update an asset's properties.

        Args:
        - asset_id (str): ID of the asset to update.
        - **kwargs: Properties to update.

        Raises:
        - ValueError: If the asset does not exist.
        """
        try:
            asset = self.assets[asset_id]
            for key, value in kwargs.items():
                setattr(asset, key, value)
            logger.info(f"Updated asset {asset_id}")
        except KeyError:
            raise ValueError(f"Asset with ID {asset_id} does not exist.")

    def delete_asset(self, asset_id: str):
        """
        Delete an asset from the library.

        Args:
        - asset_id (str): ID of the asset to delete.

        Raises:
        - ValueError: If the asset does not exist.
        """
        try:
            del self.assets[asset_id]
            logger.info(f"Deleted asset {asset_id}")
        except KeyError:
            raise ValueError(f"Asset with ID {asset_id} does not exist.")

    def to_json(self) -> str:
        """Convert the AssetLibrary to a JSON string."""
        assets_dict = [asset.to_dict() for asset in self.assets.values()]
        return json.dumps(assets_dict, indent=4)

def main():
    library = AssetLibrary()

    # Create assets
    sword = Asset(
        asset_id="sword_1",
        name="Dragon Slayer",
        description="A powerful sword.",
        asset_type=AssetType.ITEM,
        properties={"attack": "10", "rarity": "rare"}
    )

    character = Asset(
        asset_id="character_1",
        name="Warrior",
        description="A brave warrior.",
        asset_type=AssetType.CHARACTER,
        properties={"health": "100", "level": "1"}
    )

    # Add assets to library
    library.add_asset(sword)
    library.add_asset(character)

    # Print library as JSON
    print(library.to_json())

    # Get asset
    retrieved_sword = library.get_asset("sword_1")
    print(retrieved_sword.to_dict())

    # Update asset
    library.update_asset("sword_1", description="The most powerful sword.")
    updated_sword = library.get_asset("sword_1")
    print(updated_sword.to_dict())

    # Delete asset
    library.delete_asset("character_1")

if __name__ == "__main__":
    main()
```
