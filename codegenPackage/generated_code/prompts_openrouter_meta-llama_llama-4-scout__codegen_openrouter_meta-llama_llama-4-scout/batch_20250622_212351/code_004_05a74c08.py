"""
Generated Code Metadata:
========================
Original URL: https://centrifuge.onl
Prompt: "Design a use case for Centrifuge's asset-agnostic platform in tokenizing a specific type of real-world asset, such as art or real estate."
Generated: DETERMINISTIC_05a74c0876073a44
Batch ID: 20250622_212351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

# Define an Enum for asset types
class AssetType(str, Enum):
    """Enum for asset types."""
    ART = "art"
    REAL_ESTATE = "real_estate"

# Define a data class for Asset
@dataclass
class Asset:
    """Data class representing an asset."""
    id: str
    type: AssetType
    name: str
    description: str
    value: float
    tokenized: bool = False

# Define a data class for Token
@dataclass
class Token:
    """Data class representing a token."""
    id: str
    asset_id: str
    owner: str
    creation_date: datetime

# Define a class for CentrifugePlatform
class CentrifugePlatform:
    """Class representing Centrifuge's asset-agnostic platform."""
    def __init__(self):
        self.assets: Dict[str, Asset] = {}
        self.tokens: Dict[str, Token] = {}

    def add_asset(self, asset: Asset):
        """Add an asset to the platform."""
        if asset.id in self.assets:
            raise ValueError("Asset already exists.")
        self.assets[asset.id] = asset

    def tokenize_asset(self, asset_id: str, owner: str):
        """Tokenize an asset."""
        if asset_id not in self.assets:
            raise ValueError("Asset does not exist.")
        
        asset = self.assets[asset_id]
        if asset.tokenized:
            raise ValueError("Asset is already tokenized.")

        token_id = f"{asset_id}-{owner}"
        token = Token(
            id=token_id,
            asset_id=asset_id,
            owner=owner,
            creation_date=datetime.now()
        )
        self.tokens[token_id] = token
        asset.tokenized = True
        self.assets[asset_id] = asset

    def get_token(self, token_id: str) -> Token:
        """Get a token by ID."""
        try:
            return self.tokens[token_id]
        except KeyError:
            raise ValueError("Token does not exist.")

# Example usage
if __name__ == "__main__":
    platform = CentrifugePlatform()

    # Create assets
    art_asset = Asset(
        id="ART-001",
        type=AssetType.ART,
        name="Art Piece",
        description="A beautiful art piece.",
        value=10000.0
    )
    real_estate_asset = Asset(
        id="RE-001",
        type=AssetType.REAL_ESTATE,
        name="House",
        description="A beautiful house.",
        value=500000.0
    )

    # Add assets to the platform
    platform.add_asset(art_asset)
    platform.add_asset(real_estate_asset)

    # Tokenize assets
    platform.tokenize_asset("ART-001", "owner1")
    platform.tokenize_asset("RE-001", "owner2")

    # Get token
    token = platform.get_token("ART-001-owner1")
    print(token)
```
