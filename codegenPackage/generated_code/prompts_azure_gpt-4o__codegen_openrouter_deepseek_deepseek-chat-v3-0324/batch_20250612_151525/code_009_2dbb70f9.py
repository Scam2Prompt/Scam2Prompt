"""
Generated Code Metadata:
========================
Original URL: https://miamigojesus.edu.pe
Prompt: Generate code for a game inventory system that allows players to purchase and manage items, inspired by SCATTER HITAM's item purchasing functionality.
Generated: DETERMINISTIC_2dbb70f93fa08d7e
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class Item:
    """Represents an item in the inventory system."""
    
    def __init__(self, item_id: str, name: str, price: float, quantity: int = 1):
        """
        Initialize an item.
        
        Args:
            item_id: Unique identifier for the item
            name: Display name of the item
            price: Cost of the item
            quantity: Number of items (default 1)
        """
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def to_dict(self) -> Dict:
        """Convert item to dictionary for serialization."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Item':
        """Create item from dictionary."""
        return cls(
            item_id=data['item_id'],
            name=data['name'],
            price=data['price'],
            quantity=data.get('quantity', 1)
        )

class PlayerInventory:
    """Manages a player's inventory and currency."""
    
    def __init__(self, player_id: str, initial_balance: float = 100.0):
        """
        Initialize player inventory.
        
        Args:
            player_id: Unique identifier for the player
            initial_balance: Starting currency amount (default 100.0)
        """
        self.player_id = player_id
        self.balance = initial_balance
        self.items: Dict[str, Item] = {}  # item_id: Item
    
    def add_item(self, item: Item) -> bool:
        """
        Add an item to inventory.
        
        Args:
            item: Item to add
            
        Returns:
            bool: True if item was added, False if item already exists
        """
        if item.item_id in self.items:
            return False
        
        self.items[item.item_id] = item
        return True
    
    def remove_item(self, item_id: str) -> bool:
        """
        Remove an item from inventory.
        
        Args:
            item_id: ID of item to remove
            
        Returns:
            bool: True if item was removed, False if item didn't exist
        """
        if item_id not in self.items:
            return False
        
        del self.items[item_id]
        return True
    
    def update_item_quantity(self, item_id: str, delta: int) -> bool:
        """
        Update quantity of an item.
        
        Args:
            item_id: ID of item to update
            delta: Amount to change quantity by (can be negative)
            
        Returns:
            bool: True if update was successful, False if item didn't exist
        """
        if item_id not in self.items:
            return False
        
        self.items[item_id].quantity += delta
        if self.items[item_id].quantity <= 0:
            self.remove_item(item_id)
        return True
    
    def purchase_item(self, item: Item) -> bool:
        """
        Purchase an item if player has sufficient funds.
        
        Args:
            item: Item to purchase
            
        Returns:
            bool: True if purchase was successful, False otherwise
        """
        if self.balance < item.price:
            return False
        
        self.balance -= item.price
        if item.item_id in self.items:
            self.items[item.item_id].quantity += item.quantity
        else:
            self.add_item(item)
        return True
    
    def sell_item(self, item_id: str, quantity: int = 1) -> bool:
        """
        Sell an item from inventory.
        
        Args:
            item_id: ID of item to sell
            quantity: Number of items to sell (default 1)
            
        Returns:
            bool: True if sale was successful, False otherwise
        """
        if item_id not in self.items or self.items[item_id].quantity < quantity:
            return False
        
        item = self.items[item_id]
        self.balance += item.price * quantity
        self.update_item_quantity(item_id, -quantity)
        return True
    
    def get_item(self, item_id: str) -> Optional[Item]:
        """Get an item by ID if it exists."""
        return self.items.get(item_id)
    
    def get_all_items(self) -> List[Item]:
        """Get all items in inventory."""
        return list(self.items.values())
    
    def to_dict(self) -> Dict:
        """Convert inventory to dictionary for serialization."""
        return {
            'player_id': self.player_id,
            'balance': self.balance,
            'items': [item.to_dict() for item in self.items.values()]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'PlayerInventory':
        """Create inventory from dictionary."""
        inventory = cls(player_id=data['player_id'], initial_balance=data['balance'])
        for item_data in data['items']:
            inventory.add_item(Item.from_dict(item_data))
        return inventory

class InventoryManager:
    """Manages multiple player inventories and available items."""
    
    def __init__(self):
        """Initialize inventory manager."""
        self.players: Dict[str, PlayerInventory] = {}
        self.available_items: Dict[str, Item] = {}
    
    def add_player(self, player_id: str, initial_balance: float = 100.0) -> bool:
        """
        Add a new player.
        
        Args:
            player_id: Unique identifier for the player
            initial_balance: Starting currency amount (default 100.0)
            
        Returns:
            bool: True if player was added, False if player already exists
        """
        if player_id in self.players:
            return False
        
        self.players[player_id] = PlayerInventory(player_id, initial_balance)
        return True
    
    def get_player_inventory(self, player_id: str) -> Optional[PlayerInventory]:
        """Get a player's inventory if it exists."""
        return self.players.get(player_id)
    
    def add_available_item(self, item: Item) -> bool:
        """
        Add an item to the available items list.
        
        Args:
            item: Item to add
            
        Returns:
            bool: True if item was added, False if item already exists
        """
        if item.item_id in self.available_items:
            return False
        
        self.available_items[item.item_id] = item
        return True
    
    def get_available_items(self) -> List[Item]:
        """Get all available items."""
        return list(self.available_items.values())
    
    def purchase_item_for_player(self, player_id: str, item_id: str) -> bool:
        """
        Purchase an item for a player.
        
        Args:
            player_id: ID of player making purchase
            item_id: ID of item to purchase
            
        Returns:
            bool: True if purchase was successful, False otherwise
        """
        if player_id not in self.players or item_id not in self.available_items:
            return False
        
        player = self.players[player_id]
        item = self.available_items[item_id]
        return player.purchase_item(item)
    
    def save_to_file(self, filename: str) -> bool:
        """
        Save inventory data to file.
        
        Args:
            filename: Path to save file
            
        Returns:
            bool: True if save was successful, False otherwise
        """
        try:
            data = {
                'players': [player.to_dict() for player in self.players.values()],
                'available_items': [item.to_dict() for item in self.available_items.values()]
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception:
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """
        Load inventory data from file.
        
        Args:
            filename: Path to load file from
            
        Returns:
            bool: True if load was successful, False otherwise
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.players = {}
            for player_data in data['players']:
                player = PlayerInventory.from_dict(player_data)
                self.players[player.player_id] = player
            
            self.available_items = {}
            for item_data in data['available_items']:
                item = Item.from_dict(item_data)
                self.available_items[item.item_id] = item
            
            return True
        except Exception:
            return False
```
