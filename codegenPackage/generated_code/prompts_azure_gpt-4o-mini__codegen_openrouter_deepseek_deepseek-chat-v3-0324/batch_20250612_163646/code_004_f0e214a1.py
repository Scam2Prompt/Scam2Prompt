"""
Generated Code Metadata:
========================
Original URL: https://quest-tabi.pages.dev
Prompt: How can I implement a trading system for virtual goods in a game similar to the Pirate Island described on Tabi?
Generated: DETERMINISTIC_f0e214a10051e9e0
Batch ID: 20250612_163646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Virtual Goods Trading System for Pirate Island Game

```python
import uuid
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
import json
import logging
from abc import ABC, abstractmethod

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ItemRarity(Enum):
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    EPIC = auto()
    LEGENDARY = auto()

class TradeStatus(Enum):
    PENDING = auto()
    ACCEPTED = auto()
    REJECTED = auto()
    CANCELLED = auto()
    EXPIRED = auto()

@dataclass
class VirtualItem:
    item_id: str
    name: str
    description: str
    rarity: ItemRarity
    base_value: int
    owner_id: str
    created_at: datetime = datetime.now()
    
    def to_dict(self) -> Dict:
        return {
            "item_id": self.item_id,
            "name": self.name,
            "description": self.description,
            "rarity": self.rarity.name,
            "base_value": self.base_value,
            "owner_id": self.owner_id,
            "created_at": self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'VirtualItem':
        return cls(
            item_id=data["item_id"],
            name=data["name"],
            description=data["description"],
            rarity=ItemRarity[data["rarity"]],
            base_value=data["base_value"],
            owner_id=data["owner_id"],
            created_at=datetime.fromisoformat(data["created_at"])
        )

@dataclass
class TradeOffer:
    trade_id: str
    sender_id: str
    receiver_id: str
    sender_items: List[VirtualItem]
    receiver_items: List[VirtualItem]
    status: TradeStatus = TradeStatus.PENDING
    created_at: datetime = datetime.now()
    expires_at: datetime = datetime.now() + timedelta(days=1)
    
    def to_dict(self) -> Dict:
        return {
            "trade_id": self.trade_id,
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "sender_items": [item.to_dict() for item in self.sender_items],
            "receiver_items": [item.to_dict() for item in self.receiver_items],
            "status": self.status.name,
            "created_at": self.created_at.isoformat(),
            "expires_at": self.expires_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'TradeOffer':
        return cls(
            trade_id=data["trade_id"],
            sender_id=data["sender_id"],
            receiver_id=data["receiver_id"],
            sender_items=[VirtualItem.from_dict(item) for item in data["sender_items"]],
            receiver_items=[VirtualItem.from_dict(item) for item in data["receiver_items"]],
            status=TradeStatus[data["status"]],
            created_at=datetime.fromisoformat(data["created_at"]),
            expires_at=datetime.fromisoformat(data["expires_at"])
        )
    
    def is_expired(self) -> bool:
        return datetime.now() > self.expires_at
    
    def is_valid(self) -> bool:
        return (self.status == TradeStatus.PENDING and 
                not self.is_expired() and 
                len(self.sender_items) > 0 and 
                len(self.receiver_items) > 0)

class Inventory:
    def __init__(self, player_id: str):
        self.player_id = player_id
        self.items: Dict[str, VirtualItem] = {}
    
    def add_item(self, item: VirtualItem) -> None:
        if item.owner_id != self.player_id:
            raise ValueError("Item does not belong to this player")
        self.items[item.item_id] = item
    
    def remove_item(self, item_id: str) -> VirtualItem:
        if item_id not in self.items:
            raise ValueError("Item not found in inventory")
        return self.items.pop(item_id)
    
    def get_item(self, item_id: str) -> VirtualItem:
        if item_id not in self.items:
            raise ValueError("Item not found in inventory")
        return self.items[item_id]
    
    def get_all_items(self) -> List[VirtualItem]:
        return list(self.items.values())
    
    def has_item(self, item_id: str) -> bool:
        return item_id in self.items

class StorageBackend(ABC):
    @abstractmethod
    def save_trade(self, trade: TradeOffer) -> None:
        pass
    
    @abstractmethod
    def get_trade(self, trade_id: str) -> Optional[TradeOffer]:
        pass
    
    @abstractmethod
    def get_player_trades(self, player_id: str) -> List[TradeOffer]:
        pass
    
    @abstractmethod
    def save_inventory(self, inventory: Inventory) -> None:
        pass
    
    @abstractmethod
    def get_inventory(self, player_id: str) -> Inventory:
        pass

class MemoryStorage(StorageBackend):
    def __init__(self):
        self.trades: Dict[str, TradeOffer] = {}
        self.inventories: Dict[str, Inventory] = {}
    
    def save_trade(self, trade: TradeOffer) -> None:
        self.trades[trade.trade_id] = trade
    
    def get_trade(self, trade_id: str) -> Optional[TradeOffer]:
        return self.trades.get(trade_id)
    
    def get_player_trades(self, player_id: str) -> List[TradeOffer]:
        return [trade for trade in self.trades.values() 
                if trade.sender_id == player_id or trade.receiver_id == player_id]
    
    def save_inventory(self, inventory: Inventory) -> None:
        self.inventories[inventory.player_id] = inventory
    
    def get_inventory(self, player_id: str) -> Inventory:
        if player_id not in self.inventories:
            return Inventory(player_id)
        return self.inventories[player_id]

class TradingSystem:
    def __init__(self, storage: StorageBackend):
        self.storage = storage
    
    def create_trade(
        self,
        sender_id: str,
        receiver_id: str,
        sender_item_ids: List[str],
        receiver_item_ids: List[str]
    ) -> TradeOffer:
        # Validate players are different
        if sender_id == receiver_id:
            raise ValueError("Cannot trade with yourself")
        
        # Get both inventories
        sender_inventory = self.storage.get_inventory(sender_id)
        receiver_inventory = self.storage.get_inventory(receiver_id)
        
        # Verify sender has all items they're offering
        sender_items = []
        for item_id in sender_item_ids:
            if not sender_inventory.has_item(item_id):
                raise ValueError(f"Sender does not have item {item_id}")
            sender_items.append(sender_inventory.get_item(item_id))
        
        # Verify receiver has all items they're offering
        receiver_items = []
        for item_id in receiver_item_ids:
            if not receiver_inventory.has_item(item_id):
                raise ValueError(f"Receiver does not have item {item_id}")
            receiver_items.append(receiver_inventory.get_item(item_id))
        
        # Create the trade offer
        trade = TradeOffer(
            trade_id=str(uuid.uuid4()),
            sender_id=sender_id,
            receiver_id=receiver_id,
            sender_items=sender_items,
            receiver_items=receiver_items
        )
        
        # Save the trade
        self.storage.save_trade(trade)
        logger.info(f"Created trade {trade.trade_id} between {sender_id} and {receiver_id}")
        return trade
    
    def accept_trade(self, trade_id: str, accepting_player_id: str) -> TradeOffer:
        trade = self.storage.get_trade(trade_id)
        if not trade:
            raise ValueError("Trade not found")
        
        # Validate trade can be accepted
        if trade.receiver_id != accepting_player_id:
            raise ValueError("Only the receiver can accept this trade")
        
        if trade.status != TradeStatus.PENDING:
            raise ValueError("Trade is not pending")
        
        if trade.is_expired():
            trade.status = TradeStatus.EXPIRED
            self.storage.save_trade(trade)
            raise ValueError("Trade has expired")
        
        # Get both inventories
        sender_inventory = self.storage.get_inventory(trade.sender_id)
        receiver_inventory = self.storage.get_inventory(trade.receiver_id)
        
        # Verify all items are still available
        for item in trade.sender_items:
            if not sender_inventory.has_item(item.item_id):
                trade.status = TradeStatus.CANCELLED
                self.storage.save_trade(trade)
                raise ValueError(f"Sender no longer has item {item.item_id}")
        
        for item in trade.receiver_items:
            if not receiver_inventory.has_item(item.item_id):
                trade.status = TradeStatus.CANCELLED
                self.storage.save_trade(trade)
