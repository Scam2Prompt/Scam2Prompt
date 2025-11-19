"""
Generated Code Metadata:
========================
Original URL: https://ton.orgusdcs.top
Prompt: Write a Python script to manage an e-commerce store's inventory, including track cycling products like chainsets, wheels, and tires.
Generated: DETERMINISTIC_739ea786163276f6
Batch ID: 20250622_212649
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional

class InventoryItem:
    """Represents an item in the inventory."""
    
    def __init__(self, product_id: str, name: str, category: str, price: float, quantity: int):
        """Initialize an inventory item.
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            category: Category of the product (e.g., chainset, wheel, tire)
            price: Price of the product
            quantity: Available quantity in stock
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
    
    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for serialization."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'quantity': self.quantity
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'InventoryItem':
        """Create an InventoryItem from a dictionary."""
        return cls(
            product_id=data['product_id'],
            name=data['name'],
            category=data['category'],
            price=data['price'],
            quantity=data['quantity']
        )

class InventoryManager:
    """Manages the inventory of cycling products."""
    
    def __init__(self, file_path: str = 'inventory.json'):
        """Initialize the inventory manager.
        
        Args:
            file_path: Path to the JSON file storing inventory data
        """
        self.file_path = file_path
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()
    
    def load_inventory(self) -> None:
        """Load inventory data from the JSON file."""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as file:
                    data = json.load(file)
                    self.inventory = {
                        item_id: InventoryItem.from_dict(item_data)
                        for item_id, item_data in data.items()
                    }
        except Exception as e:
            print(f"Error loading inventory: {e}")
            self.inventory = {}
    
    def save_inventory(self) -> None:
        """Save inventory data to the JSON file."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump(
                    {item_id: item.to_dict() for item_id, item in self.inventory.items()},
                    file,
                    indent=2
                )
        except Exception as e:
            print(f"Error saving inventory: {e}")
    
    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory.
        
        Args:
            item: InventoryItem to add
        """
        if item.product_id in self.inventory:
            raise ValueError(f"Product with ID {item.product_id} already exists")
        self.inventory[item.product_id] = item
        self.save_inventory()
    
    def update_item(self, product_id: str, quantity: Optional[int] = None, price: Optional[float] = None) -> None:
        """Update an existing item's quantity and/or price.
        
        Args:
            product_id: ID of the product to update
            quantity: New quantity (optional)
            price: New price (optional)
        """
        if product_id not in self.inventory:
            raise ValueError(f"Product with ID {product_id} not found")
        
        item = self.inventory[product_id]
        if quantity is not None:
            item.quantity = quantity
        if price is not None:
            item.price = price
        
        self.save_inventory()
    
    def remove_item(self, product_id: str) -> None:
        """Remove an item from the inventory.
        
        Args:
            product_id: ID of the product to remove
        """
        if product_id not in self.inventory:
            raise ValueError(f"Product with ID {product_id} not found")
        del self.inventory[product_id]
        self.save_inventory()
    
    def get_item(self, product_id: str) -> InventoryItem:
        """Get an item by its product ID.
        
        Args:
            product_id: ID of the product to retrieve
        """
        if product_id not in self.inventory:
            raise ValueError(f"Product with ID {product_id} not found")
        return self.inventory[product_id]
    
    def list_items(self, category: Optional[str] = None) -> List[InventoryItem]:
        """List all items, optionally filtered by category.
        
        Args:
            category: Category to filter by (optional)
        """
        if category:
            return [item for item in self.inventory.values() if item.category == category]
        return list(self.inventory.values())
    
    def check_stock(self, product_id: str, quantity: int) -> bool:
        """Check if sufficient stock is available.
        
        Args:
            product_id: ID of the product to check
            quantity: Quantity needed
        """
        item = self.get_item(product_id)
        return item.quantity >= quantity
    
    def process_sale(self, product_id: str, quantity: int) -> None:
        """Process a sale by reducing inventory quantity.
        
        Args:
            product_id: ID of the product sold
            quantity: Quantity sold
        """
        if not self.check_stock(product_id, quantity):
            raise ValueError("Insufficient stock")
        item = self.get_item(product_id)
        item.quantity -= quantity
        self.save_inventory()

def main():
    """Example usage of the InventoryManager."""
    manager = InventoryManager()
    
    # Add some sample products
    try:
        manager.add_item(InventoryItem(
            product_id="CS-100",
            name="Shimano Ultegra Chainset",
            category="chainset",
            price=199.99,
            quantity=10
        ))
        
        manager.add_item(InventoryItem(
            product_id="WH-200",
            name="Mavic Cosmic Wheelset",
            category="wheel",
            price=899.99,
            quantity=5
        ))
        
        manager.add_item(InventoryItem(
            product_id="TR-300",
            name="Continental Grand Prix 5000",
            category="tire",
            price=49.99,
            quantity=20
        ))
    except ValueError as e:
        print(f"Error adding items: {e}")
    
    # List all wheels
    print("Available wheels:")
    for item in manager.list_items(category="wheel"):
        print(f"{item.name} - ${item.price} ({item.quantity} in stock)")
    
    # Process a sale
    try:
        manager.process_sale("TR-300", 2)
        print("Sale processed successfully")
    except ValueError as e:
        print(f"Error processing sale: {e}")

if __name__ == "__main__":
    main()
```
