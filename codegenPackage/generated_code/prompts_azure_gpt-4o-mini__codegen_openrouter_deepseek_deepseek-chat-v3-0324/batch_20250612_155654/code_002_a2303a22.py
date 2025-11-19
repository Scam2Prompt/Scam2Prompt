"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasnft.org
Prompt: Generate code for creating and customizing digital assets in the Cornucopias game environment.
Generated: DETERMINISTIC_a2303a229c792426
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Union
from uuid import uuid4

class AssetType(Enum):
    """Enum representing different types of digital assets in Cornucopias."""
    CHARACTER = "character"
    VEHICLE = "vehicle"
    BUILDING = "building"
    WEAPON = "weapon"
    ITEM = "item"
    LAND = "land"

class Rarity(Enum):
    """Enum representing rarity levels of assets."""
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"

@dataclass
class Attribute:
    """Class representing an attribute of a digital asset."""
    name: str
    value: Union[int, float, str]
    display_name: Optional[str] = None
    is_hidden: bool = False

@dataclass
class AssetMetadata:
    """Class representing metadata for a digital asset."""
    name: str
    description: str
    image_url: str
    external_url: Optional[str] = None
    animation_url: Optional[str] = None

@dataclass
class DigitalAsset:
    """Main class representing a digital asset in Cornucopias."""
    asset_id: str = field(default_factory=lambda: str(uuid4()))
    asset_type: AssetType = AssetType.ITEM
    rarity: Rarity = Rarity.COMMON
    metadata: AssetMetadata = None
    attributes: List[Attribute] = field(default_factory=list)
    owner_id: Optional[str] = None
    is_tradable: bool = True
    is_soulbound: bool = False
    creation_timestamp: int = field(default_factory=lambda: int(time.time()))

    def add_attribute(self, attribute: Attribute) -> None:
        """Add an attribute to the asset."""
        self.attributes.append(attribute)

    def remove_attribute(self, attribute_name: str) -> bool:
        """Remove an attribute by name."""
        for i, attr in enumerate(self.attributes):
            if attr.name == attribute_name:
                self.attributes.pop(i)
                return True
        return False

    def update_attribute(self, attribute_name: str, new_value: Union[int, float, str]) -> bool:
        """Update an attribute's value."""
        for attr in self.attributes:
            if attr.name == attribute_name:
                attr.value = new_value
                return True
        return False

    def to_dict(self) -> Dict:
        """Convert the asset to a dictionary for serialization."""
        return {
            "asset_id": self.asset_id,
            "asset_type": self.asset_type.value,
            "rarity": self.rarity.value,
            "metadata": {
                "name": self.metadata.name,
                "description": self.metadata.description,
                "image_url": self.metadata.image_url,
                "external_url": self.metadata.external_url,
                "animation_url": self.metadata.animation_url
            },
            "attributes": [{
                "name": attr.name,
                "value": attr.value,
                "display_name": attr.display_name,
                "is_hidden": attr.is_hidden
            } for attr in self.attributes],
            "owner_id": self.owner_id,
            "is_tradable": self.is_tradable,
            "is_soulbound": self.is_soulbound,
            "creation_timestamp": self.creation_timestamp
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'DigitalAsset':
        """Create an asset from a dictionary."""
        metadata = AssetMetadata(
            name=data["metadata"]["name"],
            description=data["metadata"]["description"],
            image_url=data["metadata"]["image_url"],
            external_url=data["metadata"].get("external_url"),
            animation_url=data["metadata"].get("animation_url")
        )
        
        attributes = [
            Attribute(
                name=attr["name"],
                value=attr["value"],
                display_name=attr.get("display_name"),
                is_hidden=attr.get("is_hidden", False)
            ) for attr in data["attributes"]
        ]
        
        return cls(
            asset_id=data["asset_id"],
            asset_type=AssetType(data["asset_type"]),
            rarity=Rarity(data["rarity"]),
            metadata=metadata,
            attributes=attributes,
            owner_id=data.get("owner_id"),
            is_tradable=data.get("is_tradable", True),
            is_soulbound=data.get("is_soulbound", False),
            creation_timestamp=data.get("creation_timestamp", int(time.time()))
        )

    def save_to_file(self, file_path: str) -> None:
        """Save the asset to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump(self.to_dict(), f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save asset to file: {e}")

    @classmethod
    def load_from_file(cls, file_path: str) -> 'DigitalAsset':
        """Load an asset from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                return cls.from_dict(data)
        except IOError as e:
            raise IOError(f"Failed to load asset from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")

class AssetFactory:
    """Factory class for creating different types of assets."""
    
    @staticmethod
    def create_character(name: str, description: str, image_url: str, rarity: Rarity) -> DigitalAsset:
        """Create a character asset."""
        metadata = AssetMetadata(
            name=name,
            description=description,
            image_url=image_url
        )
        asset = DigitalAsset(
            asset_type=AssetType.CHARACTER,
            rarity=rarity,
            metadata=metadata
        )
        asset.add_attribute(Attribute("health", 100, "Health"))
        asset.add_attribute(Attribute("speed", 5, "Speed"))
        return asset

    @staticmethod
    def create_vehicle(name: str, description: str, image_url: str, rarity: Rarity) -> DigitalAsset:
        """Create a vehicle asset."""
        metadata = AssetMetadata(
            name=name,
            description=description,
            image_url=image_url
        )
        asset = DigitalAsset(
            asset_type=AssetType.VEHICLE,
            rarity=rarity,
            metadata=metadata
        )
        asset.add_attribute(Attribute("speed", 50, "Speed"))
        asset.add_attribute(Attribute("durability", 100, "Durability"))
        return asset

    @staticmethod
    def create_land(name: str, description: str, image_url: str, rarity: Rarity) -> DigitalAsset:
        """Create a land asset."""
        metadata = AssetMetadata(
            name=name,
            description=description,
            image_url=image_url
        )
        asset = DigitalAsset(
            asset_type=AssetType.LAND,
            rarity=rarity,
            metadata=metadata
        )
        asset.add_attribute(Attribute("size", 1000, "Size (sqm)"))
        asset.add_attribute(Attribute("coordinates", "0,0", "Coordinates", is_hidden=True))
        return asset

def validate_asset(asset: DigitalAsset) -> bool:
    """Validate that an asset has all required fields."""
    if not asset.metadata:
        raise ValueError("Asset must have metadata")
    if not asset.metadata.name:
        raise ValueError("Asset must have a name")
    if not asset.metadata.description:
        raise ValueError("Asset must have a description")
    if not asset.metadata.image_url:
        raise ValueError("Asset must have an image URL")
    return True
```
