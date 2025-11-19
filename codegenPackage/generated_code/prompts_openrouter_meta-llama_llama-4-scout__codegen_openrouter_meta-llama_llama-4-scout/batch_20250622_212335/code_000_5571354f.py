"""
Generated Code Metadata:
========================
Original URL: https://uniswop.shop
Prompt: Write a Python code snippet to implement a simple peer-to-peer marketplace platform, like UniSwop, that allows users to buy and sell items within a specific university community.
Generated: DETERMINISTIC_5571354f7757bf36
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# marketplace.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from uuid import uuid4

class ItemStatus(str, Enum):
    """Item status"""
    AVAILABLE = "available"
    SOLD = "sold"
    PENDING = "pending"

@dataclass
class Item:
    """Item data class"""
    id: str
    name: str
    description: str
    price: float
    status: ItemStatus = ItemStatus.AVAILABLE
    seller_id: str = None
    buyer_id: str = None

class User:
    """User class"""
    def __init__(self, id: str, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
        self.items: List[Item] = []

class Marketplace:
    """Marketplace class"""
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.items: Dict[str, Item] = {}

    def create_user(self, name: str, email: str) -> User:
        """Create a new user"""
        user_id = str(uuid4())
        user = User(user_id, name, email)
        self.users[user_id] = user
        return user

    def create_item(self, name: str, description: str, price: float, seller_id: str) -> Item:
        """Create a new item"""
        if seller_id not in self.users:
            raise ValueError("Seller not found")
        
        item_id = str(uuid4())
        item = Item(item_id, name, description, price, seller_id=seller_id)
        self.items[item_id] = item
        self.users[seller_id].items.append(item)
        return item

    def list_items(self) -> List[Item]:
        """List all available items"""
        return [item for item in self.items.values() if item.status == ItemStatus.AVAILABLE]

    def buy_item(self, item_id: str, buyer_id: str) -> Item:
        """Buy an item"""
        if item_id not in self.items:
            raise ValueError("Item not found")
        
        item = self.items[item_id]
        if item.status != ItemStatus.AVAILABLE:
            raise ValueError("Item is not available")
        
        if buyer_id not in self.users:
            raise ValueError("Buyer not found")
        
        item.status = ItemStatus.PENDING
        item.buyer_id = buyer_id
        return item

    def confirm_sale(self, item_id: str) -> Item:
        """Confirm a sale"""
        if item_id not in self.items:
            raise ValueError("Item not found")
        
        item = self.items[item_id]
        if item.status != ItemStatus.PENDING:
            raise ValueError("Item is not pending")
        
        item.status = ItemStatus.SOLD
        return item

    def cancel_sale(self, item_id: str) -> Item:
        """Cancel a sale"""
        if item_id not in self.items:
            raise ValueError("Item not found")
        
        item = self.items[item_id]
        if item.status != ItemStatus.PENDING:
            raise ValueError("Item is not pending")
        
        item.status = ItemStatus.AVAILABLE
        item.buyer_id = None
        return item

def main():
    marketplace = Marketplace()

    # Create users
    user1 = marketplace.create_user("John Doe", "john@example.com")
    user2 = marketplace.create_user("Jane Doe", "jane@example.com")

    # Create items
    item1 = marketplace.create_item("Laptop", "Used laptop", 500.0, user1.id)
    item2 = marketplace.create_item("Book", "Used book", 20.0, user2.id)

    # List items
    print("Available items:")
    for item in marketplace.list_items():
        print(f"{item.name}: ${item.price}")

    # Buy item
    bought_item = marketplace.buy_item(item1.id, user2.id)
    print(f"\nBought item: {bought_item.name}")

    # Confirm sale
    confirmed_item = marketplace.confirm_sale(item1.id)
    print(f"\nConfirmed sale: {confirmed_item.name}")

if __name__ == "__main__":
    main()
```
