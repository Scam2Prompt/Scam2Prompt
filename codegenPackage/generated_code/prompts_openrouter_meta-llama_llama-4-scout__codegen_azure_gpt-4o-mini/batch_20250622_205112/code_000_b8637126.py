"""
Generated Code Metadata:
========================
Original URL: https://opticalize.com
Prompt: Write a Python script to manage an inventory of eyeglasses and sunglasses for an optical store like Optic Alizé, including frames for men, women, and children.
Generated: DETERMINISTIC_b8637126d51c9bd7
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, item_id: int, category: str, gender: str, brand: str, price: float, quantity: int):
        self.item_id = item_id
        self.category = category  # 'eyeglasses' or 'sunglasses'
        self.gender = gender      # 'men', 'women', or 'children'
        self.brand = brand
        self.price = price
        self.quantity = quantity

    def to_dict(self) -> Dict[str, Any]:
        """Convert the inventory item to a dictionary."""
        return {
            "item_id": self.item_id,
            "category": self.category,
            "gender": self.gender,
            "brand": self.brand,
            "price": self.price,
            "quantity": self.quantity
        }

class Inventory:
    """Class to manage the inventory of eyeglasses and sunglasses."""
    
    def __init__(self):
        self.items: List[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        self.items.append(item)

    def remove_item(self, item_id: int) -> None:
        """Remove an item from the inventory by item_id."""
        self.items = [item for item in self.items if item.item_id != item_id]

    def update_item(self, item_id: int, quantity: int) -> None:
        """Update the quantity of an existing item."""
        for item in self.items:
            if item.item_id == item_id:
                item.quantity = quantity
                return
        raise ValueError(f"Item with ID {item_id} not found.")

    def get_item(self, item_id: int) -> InventoryItem:
        """Retrieve an item from the inventory by item_id."""
        for item in self.items:
            if item.item_id == item_id:
                return item
        raise ValueError(f"Item with ID {item_id} not found.")

    def list_items(self) -> List[Dict[str, Any]]:
        """List all items in the inventory."""
        return [item.to_dict() for item in self.items]

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_items(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items_data = json.load(file)
                self.items = [InventoryItem(**item) for item in items_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

def main():
    """Main function to demonstrate inventory management."""
    inventory = Inventory()

    # Example items
    inventory.add_item(InventoryItem(1, 'eyeglasses', 'men', 'Ray-Ban', 150.00, 10))
    inventory.add_item(InventoryItem(2, 'sunglasses', 'women', 'Gucci', 200.00, 5))
    inventory.add_item(InventoryItem(3, 'eyeglasses', 'children', 'Disney', 50.00, 20))

    # List all items
    print("Current Inventory:")
    for item in inventory.list_items():
        print(item)

    # Update an item
    try:
        inventory.update_item(1, 8)  # Update quantity of item with ID 1
    except ValueError as e:
        print(e)

    # Save inventory to file
    inventory.save_to_file('inventory.json')

    # Load inventory from file
    new_inventory = Inventory()
    new_inventory.load_from_file('inventory.json')
    print("Loaded Inventory from file:")
    for item in new_inventory.list_items():
        print(item)

if __name__ == "__main__":
    main()
```
