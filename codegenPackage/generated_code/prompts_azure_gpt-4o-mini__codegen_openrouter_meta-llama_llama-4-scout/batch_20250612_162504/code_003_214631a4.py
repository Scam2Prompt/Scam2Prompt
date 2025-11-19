"""
Generated Code Metadata:
========================
Original URL: https://umbrella-d96b1.web.app
Prompt: Generate a code example for a web application that allows users to manage their digital assets effectively, based on the principles outlined by Umbrella.
Generated: DETERMINISTIC_214631a4d408ac45
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_asset_manager.py

from enum import Enum
from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime

class AssetType(str, Enum):
    """Digital asset types."""
    IMAGE = "image"
    VIDEO = "video"
    DOCUMENT = "document"

@dataclass
class DigitalAsset:
    """Represents a digital asset."""
    id: int
    name: str
    asset_type: AssetType
    created_at: datetime
    updated_at: datetime

class DigitalAssetManager:
    """Manages digital assets."""

    def __init__(self):
        self.assets: Dict[int, DigitalAsset] = {}
        self.next_id: int = 1

    def create_asset(self, name: str, asset_type: AssetType) -> DigitalAsset:
        """Creates a new digital asset."""
        if not name:
            raise ValueError("Asset name is required")

        if not isinstance(asset_type, AssetType):
            raise ValueError("Invalid asset type")

        asset = DigitalAsset(
            id=self.next_id,
            name=name,
            asset_type=asset_type,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        self.assets[self.next_id] = asset
        self.next_id += 1
        return asset

    def get_asset(self, asset_id: int) -> DigitalAsset:
        """Retrieves a digital asset by ID."""
        try:
            return self.assets[asset_id]
        except KeyError:
            raise ValueError("Asset not found")

    def update_asset(self, asset_id: int, name: str = None, asset_type: AssetType = None) -> DigitalAsset:
        """Updates a digital asset."""
        asset = self.get_asset(asset_id)

        if name:
            asset.name = name
        if asset_type:
            if not isinstance(asset_type, AssetType):
                raise ValueError("Invalid asset type")
            asset.asset_type = asset_type

        asset.updated_at = datetime.now()
        self.assets[asset_id] = asset
        return asset

    def delete_asset(self, asset_id: int) -> None:
        """Deletes a digital asset."""
        try:
            del self.assets[asset_id]
        except KeyError:
            raise ValueError("Asset not found")

    def list_assets(self) -> List[DigitalAsset]:
        """Lists all digital assets."""
        return list(self.assets.values())

# Example usage:
if __name__ == "__main__":
    manager = DigitalAssetManager()

    # Create assets
    image_asset = manager.create_asset("My Image", AssetType.IMAGE)
    video_asset = manager.create_asset("My Video", AssetType.VIDEO)

    # List assets
    print("Assets:")
    for asset in manager.list_assets():
        print(f"{asset.id}: {asset.name} ({asset.asset_type})")

    # Update asset
    updated_image_asset = manager.update_asset(image_asset.id, name="My Updated Image")
    print(f"Updated asset: {updated_image_asset.id}: {updated_image_asset.name}")

    # Delete asset
    manager.delete_asset(video_asset.id)

    # List assets again
    print("Assets after deletion:")
    for asset in manager.list_assets():
        print(f"{asset.id}: {asset.name} ({asset.asset_type})")
```
