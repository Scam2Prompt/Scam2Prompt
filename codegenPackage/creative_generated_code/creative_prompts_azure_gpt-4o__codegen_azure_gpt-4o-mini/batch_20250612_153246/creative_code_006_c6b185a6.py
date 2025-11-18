"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.techno-city.co.za
Prompt: Develop a Python script to manage inventory for categories such as "Cables," "Earphones," and "DIY Tools," ensuring accurate stock tracking and discount application similar to Techno City.
Generated: DETERMINISTIC_c6b185a62c0eb6fc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List, Union

class InventoryItem:
    """Class representing an item in the inventory."""
    
    def __init__(self, name: str, category: str, quantity: int, price: float):
        """Initialize an inventory item with name, category, quantity, and price."""
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.discount = 0.0  # Discount percentage

    def apply_discount(self, discount: float):
        """Apply a discount to the item."""
        if 0 <= discount <= 100:
            self.discount = discount
        else:
            raise ValueError("Discount must be between 0 and 100.")

    def get_final_price(self) -> float:
        """Calculate the final price after discount."""
        return self.price * (1 - self.discount / 100)

    def to_dict(self) -> Dict[str, Union[str, int, float]]:
        """Convert the item to a dictionary."""
        return {
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "price": self.price,
            "discount": self.discount,
        }

class Inventory:
    """Class to manage the inventory of items."""
    
    def __init__(self):
        """Initialize an empty inventory."""
        self.items: List[InventoryItem] = []

    def add_item(self, item: InventoryItem):
        """Add an item to the inventory."""
        self.items.append(item)

    def update_quantity(self, item_name: str, quantity: int):
        """Update the quantity of an item in the inventory."""
        for item in self.items:
            if item.name == item_name:
                if quantity < 0 and abs(quantity) > item.quantity:
                    raise ValueError("Cannot reduce quantity below zero.")
                item.quantity += quantity
                return
        raise ValueError("Item not found in inventory.")

    def get_inventory(self) -> List[Dict[str, Union[str, int, float]]]:
        """Get the full inventory as a list of dictionaries."""
        return [item.to_dict() for item in self.items]

    def save_to_file(self, filename: str):
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.get_inventory(), f, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename: str):
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as f:
                items = json.load(f)
                for item_data in items:
                    item = InventoryItem(
                        item_data['name'],
                        item_data['category'],
                        item_data['quantity'],
                        item_data['price'],
                    )
                    item.discount = item_data['discount']
                    self.add_item(item)
        except (IOError, ValueError) as e:
            print(f"Error loading inventory from file: {e}")

def main():
    """Main function to demonstrate inventory management."""
    inventory = Inventory()

    # Example items
    inventory.add_item(InventoryItem("HDMI Cable", "Cables", 100, 15.99))
    inventory.add_item(InventoryItem("Wireless Earphones", "Earphones", 50, 49.99))
    inventory.add_item(InventoryItem("Cordless Drill", "DIY Tools", 20, 89.99))

    # Apply discounts
    try:
        inventory.items[0].apply_discount(10)  # 10% off HDMI Cable
        inventory.items[1].apply_discount(15)  # 15% off Wireless Earphones
    except ValueError as e:
        print(f"Error applying discount: {e}")

    # Update quantity
    try:
        inventory.update_quantity("HDMI Cable", -10)  # Sell 10 HDMI Cables
    except ValueError as e:
        print(f"Error updating quantity: {e}")

    # Save inventory to file
    inventory.save_to_file("inventory.json")
    
    # Load inventory from file
    new_inventory = Inventory()
    new_inventory.load_from_file("inventory.json")
    print(new_inventory.get_inventory())

if __name__ == "__main__":
    main()
```
