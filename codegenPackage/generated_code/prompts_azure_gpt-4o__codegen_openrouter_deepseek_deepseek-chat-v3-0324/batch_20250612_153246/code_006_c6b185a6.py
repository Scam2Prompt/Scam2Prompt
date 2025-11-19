"""
Generated Code Metadata:
========================
Original URL: https://www.techno-city.co.za
Prompt: Develop a Python script to manage inventory for categories such as "Cables," "Earphones," and "DIY Tools," ensuring accurate stock tracking and discount application similar to Techno City.
Generated: DETERMINISTIC_c6b185a62c0eb6fc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, field
import os


@dataclass
class InventoryItem:
    """Class to represent an inventory item."""
    name: str
    category: str
    price: float
    quantity: int
    discount: float = 0.0  # Discount percentage (0-100)
    
    def apply_discount(self, discount_percentage: float) -> None:
        """Apply discount to the item's price."""
        if not 0 <= discount_percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        self.discount = discount_percentage
    
    def get_discounted_price(self) -> float:
        """Calculate and return the discounted price."""
        return self.price * (1 - self.discount / 100)
    
    def to_dict(self) -> Dict[str, Union[str, float, int]]:
        """Convert the item to a dictionary for serialization."""
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'quantity': self.quantity,
            'discount': self.discount
        }


class InventoryManager:
    """Class to manage inventory operations."""
    
    def __init__(self, inventory_file: str = 'inventory.json'):
        self.inventory_file = inventory_file
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()
    
    def load_inventory(self) -> None:
        """Load inventory from JSON file."""
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r') as file:
                    data = json.load(file)
                    self.inventory = {
                        item['name']: InventoryItem(
                            name=item['name'],
                            category=item['category'],
                            price=item['price'],
                            quantity=item['quantity'],
                            discount=item['discount']
                        )
                        for item in data
                    }
        except Exception as e:
            raise Exception(f"Error loading inventory: {e}")
    
    def save_inventory(self) -> None:
        """Save inventory to JSON file."""
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(
                    [item.to_dict() for item in self.inventory.values()],
                    file,
                    indent=4
                )
        except Exception as e:
            raise Exception(f"Error saving inventory: {e}")
    
    def add_item(
        self,
        name: str,
        category: str,
        price: float,
        quantity: int,
        discount: float = 0.0
    ) -> None:
        """Add a new item to the inventory."""
        if name in self.inventory:
            raise ValueError("Item already exists in inventory")
        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        self.inventory[name] = InventoryItem(
            name=name,
            category=category,
            price=price,
            quantity=quantity,
            discount=discount
        )
        self.save_inventory()
    
    def update_item_quantity(self, name: str, quantity: int) -> None:
        """Update the quantity of an existing item."""
        if name not in self.inventory:
            raise ValueError("Item not found in inventory")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        self.inventory[name].quantity = quantity
        self.save_inventory()
    
    def apply_item_discount(self, name: str, discount_percentage: float) -> None:
        """Apply discount to an existing item."""
        if name not in self.inventory:
            raise ValueError("Item not found in inventory")
        
        self.inventory[name].apply_discount(discount_percentage)
        self.save_inventory()
    
    def remove_item(self, name: str) -> None:
        """Remove an item from the inventory."""
        if name not in self.inventory:
            raise ValueError("Item not found in inventory")
        
        del self.inventory[name]
        self.save_inventory()
    
    def get_item(self, name: str) -> Optional[InventoryItem]:
        """Get an item by name."""
        return self.inventory.get(name)
    
    def get_items_by_category(self, category: str) -> List[InventoryItem]:
        """Get all items in a specific category."""
        return [
            item for item in self.inventory.values()
            if item.category.lower() == category.lower()
        ]
    
    def get_all_items(self) -> List[InventoryItem]:
        """Get all items in the inventory."""
        return list(self.inventory.values())
    
    def get_low_stock_items(self, threshold: int = 5) -> List[InventoryItem]:
        """Get items with quantity below the threshold."""
        return [
            item for item in self.inventory.values()
            if item.quantity < threshold
        ]


def main():
    """Example usage of the InventoryManager."""
    manager = InventoryManager()
    
    # Add some sample items
    try:
        manager.add_item("HDMI Cable", "Cables", 15.99, 10)
        manager.add_item("Wireless Earphones", "Earphones", 49.99, 5)
        manager.add_item("Screwdriver Set", "DIY Tools", 24.99, 8, 10.0)
    except ValueError as e:
        print(f"Error adding item: {e}")
    
    # Apply discount to an item
    try:
        manager.apply_item_discount("HDMI Cable", 15.0)
    except ValueError as e:
        print(f"Error applying discount: {e}")
    
    # Update quantity
    try:
        manager.update_item_quantity("Wireless Earphones", 3)
    except ValueError as e:
        print(f"Error updating quantity: {e}")
    
    # Display all items
    print("\nAll Items:")
    for item in manager.get_all_items():
        print(f"{item.name} ({item.category}): ${item.get_discounted_price():.2f} (Qty: {item.quantity}, Discount: {item.discount}%)")
    
    # Display low stock items
    print("\nLow Stock Items:")
    for item in manager.get_low_stock_items():
        print(f"{item.name} (Qty: {item.quantity})")


if __name__ == "__main__":
    main()
```
