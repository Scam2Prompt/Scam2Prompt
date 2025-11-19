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
import uuid
from typing import List, Dict, Optional

class Item:
    """Class representing an item for sale in the marketplace."""
    
    def __init__(self, name: str, description: str, price: float, seller: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the item
        self.name = name
        self.description = description
        self.price = price
        self.seller = seller
        self.is_sold = False

    def __repr__(self):
        return f"Item({self.name}, {self.price}, Seller: {self.seller}, Sold: {self.is_sold})"


class Marketplace:
    """Class representing the peer-to-peer marketplace."""
    
    def __init__(self):
        self.items: List[Item] = []  # List to store items for sale

    def add_item(self, name: str, description: str, price: float, seller: str) -> Item:
        """Add a new item to the marketplace."""
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        item = Item(name, description, price, seller)
        self.items.append(item)
        return item

    def list_items(self) -> List[Dict]:
        """List all available items in the marketplace."""
        return [vars(item) for item in self.items if not item.is_sold]

    def buy_item(self, item_id: str, buyer: str) -> Optional[str]:
        """Purchase an item from the marketplace."""
        for item in self.items:
            if item.id == item_id:
                if item.is_sold:
                    return "Item has already been sold."
                item.is_sold = True
                return f"{buyer} successfully purchased {item.name}."
        return "Item not found."

    def find_item(self, item_id: str) -> Optional[Item]:
        """Find an item by its ID."""
        for item in self.items:
            if item.id == item_id:
                return item
        return None


# Example usage
if __name__ == "__main__":
    marketplace = Marketplace()
    
    # Adding items to the marketplace
    try:
        item1 = marketplace.add_item("Laptop", "Dell XPS 13", 800.00, "Alice")
        item2 = marketplace.add_item("Textbook", "Introduction to Algorithms", 50.00, "Bob")
        
        print("Items for sale:")
        print(marketplace.list_items())
        
        # Buying an item
        purchase_message = marketplace.buy_item(item1.id, "Charlie")
        print(purchase_message)
        
        print("Items for sale after purchase:")
        print(marketplace.list_items())
        
    except ValueError as e:
        print(f"Error: {e}")
```
