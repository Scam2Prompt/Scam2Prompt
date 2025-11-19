"""
Generated Code Metadata:
========================
Original URL: https://moontropica.pages.dev
Prompt: Generate code for a character customization system in a game like Moon Tropica, with options for wearables and limited edition assets.
Generated: DETERMINISTIC_9690f7e03372bd8c
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# character_customization.py

from enum import Enum
from typing import List, Dict

class WearableType(Enum):
    """Enum for wearable types."""
    HAT = 1
    SHIRT = 2
    PANTS = 3
    SHOES = 4

class LimitedEditionAssetType(Enum):
    """Enum for limited edition asset types."""
    EMOTE = 1
    PET = 2
    BACKGROUND = 3

class Wearable:
    """Class representing a wearable item."""
    def __init__(self, id: int, name: str, wearable_type: WearableType, description: str):
        """
        Initialize a wearable item.

        Args:
        id (int): Unique identifier for the wearable.
        name (str): Name of the wearable.
        wearable_type (WearableType): Type of wearable.
        description (str): Description of the wearable.
        """
        self.id = id
        self.name = name
        self.wearable_type = wearable_type
        self.description = description

class LimitedEditionAsset:
    """Class representing a limited edition asset."""
    def __init__(self, id: int, name: str, asset_type: LimitedEditionAssetType, description: str):
        """
        Initialize a limited edition asset.

        Args:
        id (int): Unique identifier for the asset.
        name (str): Name of the asset.
        asset_type (LimitedEditionAssetType): Type of asset.
        description (str): Description of the asset.
        """
        self.id = id
        self.name = name
        self.asset_type = asset_type
        self.description = description

class Character:
    """Class representing a character."""
    def __init__(self, id: int, name: str):
        """
        Initialize a character.

        Args:
        id (int): Unique identifier for the character.
        name (str): Name of the character.
        """
        self.id = id
        self.name = name
        self.wearables: Dict[WearableType, Wearable] = {}
        self.limited_edition_assets: List[LimitedEditionAsset] = []

    def add_wearable(self, wearable: Wearable):
        """
        Add a wearable to the character.

        Args:
        wearable (Wearable): Wearable to add.

        Raises:
        ValueError: If the wearable type is already occupied.
        """
        if wearable.wearable_type in self.wearables:
            raise ValueError("Wearable type already occupied")
        self.wearables[wearable.wearable_type] = wearable

    def remove_wearable(self, wearable_type: WearableType):
        """
        Remove a wearable from the character.

        Args:
        wearable_type (WearableType): Type of wearable to remove.

        Raises:
        KeyError: If the wearable type is not found.
        """
        if wearable_type not in self.wearables:
            raise KeyError("Wearable type not found")
        del self.wearables[wearable_type]

    def add_limited_edition_asset(self, asset: LimitedEditionAsset):
        """
        Add a limited edition asset to the character.

        Args:
        asset (LimitedEditionAsset): Asset to add.

        Raises:
        ValueError: If the asset is already owned.
        """
        if asset in self.limited_edition_assets:
            raise ValueError("Asset already owned")
        self.limited_edition_assets.append(asset)

    def remove_limited_edition_asset(self, asset_id: int):
        """
        Remove a limited edition asset from the character.

        Args:
        asset_id (int): ID of the asset to remove.

        Raises:
        ValueError: If the asset is not found.
        """
        self.limited_edition_assets = [asset for asset in self.limited_edition_assets if asset.id != asset_id]

def main():
    # Create wearables
    hat = Wearable(1, "Cool Hat", WearableType.HAT, "A cool hat")
    shirt = Wearable(2, "Awesome Shirt", WearableType.SHIRT, "An awesome shirt")

    # Create limited edition assets
    emote = LimitedEditionAsset(1, "Happy Emote", LimitedEditionAssetType.EMOTE, "A happy emote")
    pet = LimitedEditionAsset(2, "Cute Pet", LimitedEditionAssetType.PET, "A cute pet")

    # Create character
    character = Character(1, "John Doe")

    # Add wearables
    character.add_wearable(hat)
    character.add_wearable(shirt)

    # Add limited edition assets
    character.add_limited_edition_asset(emote)
    character.add_limited_edition_asset(pet)

    # Print character information
    print(f"Character Name: {character.name}")
    print("Wearables:")
    for wearable_type, wearable in character.wearables.items():
        print(f"- {wearable_type.name}: {wearable.name}")
    print("Limited Edition Assets:")
    for asset in character.limited_edition_assets:
        print(f"- {asset.name}")

if __name__ == "__main__":
    main()
```
