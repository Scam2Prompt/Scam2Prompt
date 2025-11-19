"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Create a roadmap for expanding staking asset support in a DeFi platform, inspired by Tenderize's multi-asset support feature.
Generated: DETERMINISTIC_0bddc546b76733ee
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_roadmap.py

from typing import Dict, List
from enum import Enum

class StakingAssetStatus(Enum):
    """Enum for staking asset status"""
    SUPPORTED = 1
    UNSUPPORTED = 2
    PENDING = 3

class StakingAsset:
    """Class representing a staking asset"""
    def __init__(self, asset_id: str, name: str, status: StakingAssetStatus):
        """
        Initialize a staking asset

        Args:
        - asset_id (str): Unique ID of the asset
        - name (str): Name of the asset
        - status (StakingAssetStatus): Status of the asset
        """
        self.asset_id = asset_id
        self.name = name
        self.status = status

class StakingRoadmap:
    """Class representing the staking roadmap"""
    def __init__(self):
        """Initialize the staking roadmap"""
        self.assets: Dict[str, StakingAsset] = {}
        self.supported_assets: List[str] = []

    def add_asset(self, asset: StakingAsset):
        """
        Add a staking asset to the roadmap

        Args:
        - asset (StakingAsset): Asset to add
        """
        self.assets[asset.asset_id] = asset

    def update_asset_status(self, asset_id: str, status: StakingAssetStatus):
        """
        Update the status of a staking asset

        Args:
        - asset_id (str): ID of the asset to update
        - status (StakingAssetStatus): New status of the asset

        Raises:
        - ValueError: If the asset ID does not exist
        """
        if asset_id not in self.assets:
            raise ValueError("Asset ID does not exist")
        self.assets[asset_id].status = status

    def support_asset(self, asset_id: str):
        """
        Support a staking asset

        Args:
        - asset_id (str): ID of the asset to support

        Raises:
        - ValueError: If the asset ID does not exist or is already supported
        """
        if asset_id not in self.assets:
            raise ValueError("Asset ID does not exist")
        if asset_id in self.supported_assets:
            raise ValueError("Asset is already supported")
        self.supported_assets.append(asset_id)
        self.update_asset_status(asset_id, StakingAssetStatus.SUPPORTED)

    def get_supported_assets(self) -> List[StakingAsset]:
        """
        Get a list of supported staking assets

        Returns:
        - List[StakingAsset]: List of supported assets
        """
        return [self.assets[asset_id] for asset_id in self.supported_assets]

def main():
    # Example usage
    roadmap = StakingRoadmap()

    asset1 = StakingAsset("asset1", "Asset 1", StakingAssetStatus.PENDING)
    asset2 = StakingAsset("asset2", "Asset 2", StakingAssetStatus.UNSUPPORTED)

    roadmap.add_asset(asset1)
    roadmap.add_asset(asset2)

    roadmap.support_asset("asset1")

    supported_assets = roadmap.get_supported_assets()

    for asset in supported_assets:
        print(f"Supported Asset: {asset.name} ({asset.asset_id}) - {asset.status.name}")

if __name__ == "__main__":
    main()
```
