"""
Generated Code Metadata:
========================
Original URL: https://telltak.com
Prompt: Write a Python code snippet to manage an e-commerce inventory of mobile phone accessories, including products like LDNIO cables and SODO headphones.
Generated: DETERMINISTIC_b391393cc004203d
Batch ID: 20250622_205236
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

class InventoryItem:
    """
    Represents an item in the inventory with its properties.
    """
    def __init__(self, product_id: str, name: str, category: str, price: float, quantity: int):
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

class InventoryManager:
    """
    Manages the inventory of mobile phone accessories.
    """
    def __init__(self, inventory_file: str = 'inventory.json'):
        self.inventory_file = inventory_file
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()

    def load_inventory(self) -> None:
        """Load inventory from JSON file."""
        try:
            with open(self.inventory_file, 'r') as file:
                data = json.load(file)
                for item_data in data.values():
                    item = InventoryItem(
                        product_id=item_data['product_id'],
                        name=item_data['name'],
                        category=item_data['category'],
                        price=item_data['price'],
                        quantity=item_data['quantity']
                    )
                    self.inventory[item.product_id] = item
        except FileNotFoundError:
            # Initialize empty inventory if file doesn't exist
            self.save_inventory()
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in inventory file.")

    def save_inventory(self) -> None:
        """Save inventory to JSON file."""
        inventory_data = {k: v.to_dict() for k, v in self.inventory.items()}
        with open(self.inventory_file, 'w') as file:
            json.dump(inventory_data, file, indent=4)

    def add_item(self, product_id: str, name: str, category: str, price: float, quantity: int) -> None:
        """Add a new item to the inventory."""
        if product_id in self.inventory:
            raise ValueError(f"Product with ID {product_id} already exists.")
        if price <= 0:
            raise ValueError("Price must be greater than 0.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        self.inventory[product_id] = InventoryItem(product_id, name, category, price, quantity)
        self.save_inventory()

    def update_item_quantity(self, product_id: str, quantity_change: int) -> None:
        """Update the quantity of an existing item."""
        if product_id not in self.inventory:
            raise ValueError(f"Product with ID {product_id} not found.")
        
        new_quantity = self.inventory[product_id].quantity + quantity_change
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        self.inventory[product_id].quantity = new_quantity
        self.save_inventory()

    def remove_item(self, product_id: str) -> None:
        """Remove an item from the inventory."""
        if product_id not in self.inventory:
            raise ValueError(f"Product with ID {product_id} not found.")
        
        del self.inventory[product_id]
        self.save_inventory()

    def get_item(self, product_id: str) -> Optional[InventoryItem]:
        """Get an item by its product ID."""
        return self.inventory.get(product_id)

    def list_items(self, category: Optional[str] = None) -> List[InventoryItem]:
        """List all items, optionally filtered by category."""
        if category:
            return [item for item in self.inventory.values() if item.category == category]
        return list(self.inventory.values())

    def get_inventory_value(self) -> float:
        """Calculate the total value of the inventory."""
        return sum(item.price * item.quantity for item in self.inventory.values())

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add sample products
    try:
        manager.add_item("LDNIO001", "LDNIO USB-C Cable", "Cables", 12.99, 50)
        manager.add_item("SODO001", "SODO Wireless Headphones", "Headphones", 59.99, 30)
    except ValueError as e:
        print(f"Error adding items: {e}")

    # List all items
    print("Current Inventory:")
    for item in manager.list_items():
        print(f"{item.product_id}: {item.name} - ${item.price} - Qty: {item.quantity}")

    # Get inventory value
    print(f"\nTotal Inventory Value: ${manager.get_inventory_value():.2f}")
```
