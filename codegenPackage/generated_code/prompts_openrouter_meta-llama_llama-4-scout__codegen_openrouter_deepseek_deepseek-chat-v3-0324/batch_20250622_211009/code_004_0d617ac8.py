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
# SPDX-License-Identifier: MIT
"""
Blockchain RPG Asset Management Library

This library provides functionality to manage in-game assets for a blockchain-based RPG.
It includes classes for characters, items, and asset storage with blockchain integration.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Union
import json
import hashlib
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound


class AssetType(Enum):
    """Enumeration of asset types in the game."""
    CHARACTER = "character"
    ITEM = "item"
    CURRENCY = "currency"
    SKILL = "skill"


class Rarity(Enum):
    """Enumeration of rarity levels for game assets."""
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"


@dataclass
class GameAsset:
    """Base class for all in-game assets."""
    asset_id: str
    name: str
    asset_type: AssetType
    rarity: Rarity
    metadata: Dict = field(default_factory=dict)

    def __post_init__(self):
        """Validate asset data after initialization."""
        if not self.asset_id:
            raise ValueError("Asset ID cannot be empty")
        if not self.name:
            raise ValueError("Asset name cannot be empty")

    def to_dict(self) -> Dict:
        """Convert asset to dictionary representation."""
        return {
            "asset_id": self.asset_id,
            "name": self.name,
            "asset_type": self.asset_type.value,
            "rarity": self.rarity.value,
            "metadata": self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'GameAsset':
        """Create asset from dictionary representation."""
        return cls(
            asset_id=data["asset_id"],
            name=data["name"],
            asset_type=AssetType(data["asset_type"]),
            rarity=Rarity(data["rarity"]),
            metadata=data.get("metadata", {})
        )


@dataclass
class Character(GameAsset):
    """Class representing a game character."""
    level: int = 1
    experience: int = 0
    attributes: Dict[str, int] = field(default_factory=dict)
    inventory: List[str] = field(default_factory=list)

    def __post_init__(self):
        """Validate character data after initialization."""
        super().__post_init__()
        if self.level < 1:
            raise ValueError("Level must be at least 1")
        if self.experience < 0:
            raise ValueError("Experience cannot be negative")

    def to_dict(self) -> Dict:
        """Convert character to dictionary representation."""
        base_dict = super().to_dict()
        base_dict.update({
            "level": self.level,
            "experience": self.experience,
            "attributes": self.attributes,
            "inventory": self.inventory
        })
        return base_dict

    @classmethod
    def from_dict(cls, data: Dict) -> 'Character':
        """Create character from dictionary representation."""
        return cls(
            asset_id=data["asset_id"],
            name=data["name"],
            asset_type=AssetType(data["asset_type"]),
            rarity=Rarity(data["rarity"]),
            metadata=data.get("metadata", {}),
            level=data["level"],
            experience=data["experience"],
            attributes=data.get("attributes", {}),
            inventory=data.get("inventory", [])
        )


@dataclass
class Item(GameAsset):
    """Class representing a game item."""
    quantity: int = 1
    equippable: bool = False
    equipped: bool = False

    def __post_init__(self):
        """Validate item data after initialization."""
        super().__post_init__()
        if self.quantity < 1:
            raise ValueError("Quantity must be at least 1")

    def to_dict(self) -> Dict:
        """Convert item to dictionary representation."""
        base_dict = super().to_dict()
        base_dict.update({
            "quantity": self.quantity,
            "equippable": self.equippable,
            "equipped": self.equipped
        })
        return base_dict

    @classmethod
    def from_dict(cls, data: Dict) -> 'Item':
        """Create item from dictionary representation."""
        return cls(
            asset_id=data["asset_id"],
            name=data["name"],
            asset_type=AssetType(data["asset_type"]),
            rarity=Rarity(data["rarity"]),
            metadata=data.get("metadata", {}),
            quantity=data["quantity"],
            equippable=data.get("equippable", False),
            equipped=data.get("equipped", False)
        )


class AssetManager:
    """Main class for managing game assets with blockchain integration."""

    def __init__(self, web3_provider: str, contract_address: str, contract_abi: str):
        """
        Initialize the AssetManager with blockchain connection.

        Args:
            web3_provider: URL of the Ethereum node provider
            contract_address: Address of the smart contract
            contract_abi: ABI of the smart contract
        """
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum node")

        self.contract_address = contract_address
        self.contract = self.web3.eth.contract(
            address=contract_address,
            abi=json.loads(contract_abi)
        )
        self.assets: Dict[str, GameAsset] = {}

    def add_asset(self, asset: GameAsset) -> str:
        """
        Add an asset to the local manager.

        Args:
            asset: The game asset to add

        Returns:
            The asset ID of the added asset
        """
        if asset.asset_id in self.assets:
            raise ValueError(f"Asset with ID {asset.asset_id} already exists")
        self.assets[asset.asset_id] = asset
        return asset.asset_id

    def get_asset(self, asset_id: str) -> Optional[GameAsset]:
        """
        Retrieve an asset by ID.

        Args:
            asset_id: The ID of the asset to retrieve

        Returns:
            The asset if found, None otherwise
        """
        return self.assets.get(asset_id)

    def remove_asset(self, asset_id: str) -> bool:
        """
        Remove an asset from the local manager.

        Args:
            asset_id: The ID of the asset to remove

        Returns:
            True if the asset was removed, False if not found
        """
        if asset_id in self.assets:
            del self.assets[asset_id]
            return True
        return False

    def mint_asset(self, asset: GameAsset, private_key: str) -> str:
        """
        Mint a new asset on the blockchain.

        Args:
            asset: The asset to mint
            private_key: The private key for the transaction

        Returns:
            Transaction hash of the mint operation
        """
        account = self.web3.eth.account.from_key(private_key)
        tx_data = asset.to_dict()

        try:
            tx = self.contract.functions.mint(
                account.address,
                asset.asset_id,
                json.dumps(tx_data)
            ).build_transaction({
                'from': account.address,
                'nonce': self.web3.eth.get_transaction_count(account.address),
                'gas': 2000000,
                'gasPrice': self.web3.to_wei('50', 'gwei')
            })

            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except ContractLogicError as e:
            raise ValueError(f"Contract error: {e}") from e
        except Exception as e:
            raise RuntimeError(f"Failed to mint asset: {e}") from e

    def get_asset_from_blockchain(self, asset_id: str) -> Optional[GameAsset]:
        """
        Retrieve an asset from the blockchain.

        Args:
            asset_id: The ID of the asset to retrieve

        Returns:
            The asset if found, None otherwise
        """
        try:
            asset_data = self.contract.functions.getAsset(asset_id).call()
            if not asset_data:
                return None

            asset_dict = json.loads(asset_data)
            asset_type = AssetType(asset_dict["asset_type"])

            if asset_type == AssetType.CHARACTER:
                return Character.from_dict(asset_dict)
            elif asset_type == AssetType.ITEM:
                return Item.from_dict(asset_dict)
            else:
                return GameAsset.from_dict(asset_dict)
        except ContractLogicError:
            return None
        except Exception as e:
            raise RuntimeError(f"Failed to fetch asset: {e}") from e

    def transfer_asset(self, asset_id: str, to_address: str, private_key: str) -> str:
        """
        Transfer an asset to another address on the blockchain.

        Args:
            asset_id: The ID
