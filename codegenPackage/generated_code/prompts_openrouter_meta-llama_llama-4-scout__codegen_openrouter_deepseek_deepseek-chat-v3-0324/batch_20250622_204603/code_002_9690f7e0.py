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
import json
from enum import Enum
from typing import List, Dict, Optional
from uuid import uuid4
from datetime import datetime, timedelta

class AssetRarity(Enum):
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"
    LIMITED = "limited"

class AssetType(Enum):
    HAT = "hat"
    SHIRT = "shirt"
    PANTS = "pants"
    SHOES = "shoes"
    ACCESSORY = "accessory"
    SPECIAL = "special"

class Asset:
    def __init__(
        self,
        asset_id: str,
        name: str,
        asset_type: AssetType,
        rarity: AssetRarity,
        thumbnail: str,
        model_path: str,
        is_limited: bool = False,
        release_date: Optional[datetime] = None,
        expiry_date: Optional[datetime] = None
    ):
        self.asset_id = asset_id
        self.name = name
        self.asset_type = asset_type
        self.rarity = rarity
        self.thumbnail = thumbnail
        self.model_path = model_path
        self.is_limited = is_limited
        self.release_date = release_date
        self.expiry_date = expiry_date

    def is_available(self) -> bool:
        if not self.is_limited:
            return True
        now = datetime.now()
        return (
            (self.release_date is None or now >= self.release_date) and
            (self.expiry_date is None or now <= self.expiry_date)
        )

    def to_dict(self) -> Dict:
        return {
            "asset_id": self.asset_id,
            "name": self.name,
            "asset_type": self.asset_type.value,
            "rarity": self.rarity.value,
            "thumbnail": self.thumbnail,
            "model_path": self.model_path,
            "is_limited": self.is_limited,
            "release_date": self.release_date.isoformat() if self.release_date else None,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Asset':
        return cls(
            asset_id=data["asset_id"],
            name=data["name"],
            asset_type=AssetType(data["asset_type"]),
            rarity=AssetRarity(data["rarity"]),
            thumbnail=data["thumbnail"],
            model_path=data["model_path"],
            is_limited=data.get("is_limited", False),
            release_date=datetime.fromisoformat(data["release_date"]) if data.get("release_date") else None,
            expiry_date=datetime.fromisoformat(data["expiry_date"]) if data.get("expiry_date") else None
        )

class CharacterCustomization:
    def __init__(self, character_id: str):
        self.character_id = character_id
        self.equipped_assets: Dict[AssetType, Asset] = {}
        self.owned_assets: Dict[str, Asset] = {}

    def equip_asset(self, asset_id: str) -> bool:
        if asset_id not in self.owned_assets:
            return False
        
        asset = self.owned_assets[asset_id]
        if not asset.is_available():
            return False
        
        self.equipped_assets[asset.asset_type] = asset
        return True

    def unequip_asset(self, asset_type: AssetType) -> bool:
        if asset_type in self.equipped_assets:
            del self.equipped_assets[asset_type]
            return True
        return False

    def add_asset(self, asset: Asset) -> bool:
        if asset.asset_id in self.owned_assets:
            return False
        
        if asset.is_limited and not asset.is_available():
            return False
        
        self.owned_assets[asset.asset_id] = asset
        return True

    def remove_asset(self, asset_id: str) -> bool:
        if asset_id not in self.owned_assets:
            return False
        
        asset = self.owned_assets[asset_id]
        if asset.asset_type in self.equipped_assets:
            if self.equipped_assets[asset.asset_type].asset_id == asset_id:
                del self.equipped_assets[asset.asset_type]
        
        del self.owned_assets[asset_id]
        return True

    def get_equipped_assets(self) -> Dict[AssetType, Asset]:
        return self.equipped_assets.copy()

    def get_owned_assets(self) -> List[Asset]:
        return list(self.owned_assets.values())

    def get_available_assets(self) -> List[Asset]:
        return [asset for asset in self.owned_assets.values() if asset.is_available()]

    def to_dict(self) -> Dict:
        return {
            "character_id": self.character_id,
            "equipped_assets": {
                asset_type.value: asset.asset_id
                for asset_type, asset in self.equipped_assets.items()
            },
            "owned_assets": {
                asset.asset_id: asset.to_dict()
                for asset in self.owned_assets.values()
            }
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'CharacterCustomization':
        customization = cls(data["character_id"])
        customization.owned_assets = {
            asset_id: Asset.from_dict(asset_data)
            for asset_id, asset_data in data["owned_assets"].items()
        }
        
        for asset_type_str, asset_id in data["equipped_assets"].items():
            if asset_id in customization.owned_assets:
                asset = customization.owned_assets[asset_id]
                customization.equipped_assets[AssetType(asset_type_str)] = asset
        
        return customization

class AssetManager:
    def __init__(self):
        self.assets: Dict[str, Asset] = {}

    def add_asset(self, asset: Asset) -> bool:
        if asset.asset_id in self.assets:
            return False
        self.assets[asset.asset_id] = asset
        return True

    def get_asset(self, asset_id: str) -> Optional[Asset]:
        return self.assets.get(asset_id)

    def get_available_assets(self) -> List[Asset]:
        now = datetime.now()
        return [
            asset for asset in self.assets.values()
            if not asset.is_limited or (
                (asset.release_date is None or now >= asset.release_date) and
                (asset.expiry_date is None or now <= asset.expiry_date)
            )
        ]

    def get_assets_by_type(self, asset_type: AssetType) -> List[Asset]:
        return [
            asset for asset in self.assets.values()
            if asset.asset_type == asset_type
        ]

    def load_assets_from_file(self, file_path: str) -> bool:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for asset_data in data.get("assets", []):
                    asset = Asset.from_dict(asset_data)
                    self.add_asset(asset)
            return True
        except (IOError, json.JSONDecodeError, KeyError):
            return False

    def save_assets_to_file(self, file_path: str) -> bool:
        try:
            with open(file_path, 'w') as f:
                json.dump({
                    "assets": [asset.to_dict() for asset in self.assets.values()]
                }, f, indent=2)
            return True
        except IOError:
            return False

def create_limited_asset(
    name: str,
    asset_type: AssetType,
    rarity: AssetRarity,
    thumbnail: str,
    model_path: str,
    duration_days: int = 7
) -> Asset:
    now = datetime.now()
    expiry = now + timedelta(days=duration_days)
    return Asset(
        asset_id=str(uuid4()),
        name=name,
        asset_type=asset_type,
        rarity=rarity,
        thumbnail=thumbnail,
        model_path=model_path,
        is_limited=True,
        release_date=now,
        expiry_date=expiry
    )
```
