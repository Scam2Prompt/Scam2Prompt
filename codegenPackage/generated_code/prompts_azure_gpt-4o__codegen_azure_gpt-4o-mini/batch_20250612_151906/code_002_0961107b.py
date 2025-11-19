"""
Generated Code Metadata:
========================
Original URL: https://conficarnesdelvalle.com
Prompt: Generate a Python script to simulate basic POS operations, such as sales tracking and inventory management, for a business like Conficarnes del Valle.
Generated: DETERMINISTIC_0961107b5aba8d2f
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount: int):
        """Update the quantity of the item."""
        if self.quantity + amount < 0:
            raise ValueError("Insufficient stock to complete the operation.")
        self.quantity += amount

    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }

class Inventory:
    """Class to manage the inventory of items."""
    
    def __init__(self):
        self.items: Dict[str, InventoryItem] = {}

    def add_item(self, name: str, price: float, quantity: int):
        """Add a new item to the inventory."""
        if name in self.items:
            raise ValueError("Item already exists in inventory.")
        self.items[name] = InventoryItem(name, price, quantity)

    def update_item_quantity(self, name: str, amount: int):
        """Update the quantity of an existing item."""
        if name not in self.items:
            raise ValueError("Item not found in inventory.")
        self.items[name].update_quantity(amount)

    def get_inventory(self) -> List[Dict]:
        """Get a list of all items in the inventory."""
        return [item.to_dict() for item in self.items.values()]

    def save_to_file(self, filename: str):
        """Save the inventory to a JSON file."""
        with open(filename, 'w') as file:
            json.dump(self.get_inventory(), file)

    def load_from_file(self, filename: str):
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                for item in items:
                    self.add_item(item['name'], item['price'], item['quantity'])
        except FileNotFoundError:
            print("File not found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the file format.")

class POS:
    """Class to handle point of sale operations."""
    
    def __init__(self, inventory: Inventory):
        self.inventory = inventory
        self.sales: List[Dict] = []

    def make_sale(self, item_name: str, quantity: int):
        """Process a sale for a given item and quantity."""
        if item_name not in self.inventory.items:
            raise ValueError("Item not found in inventory.")
        item = self.inventory.items[item_name]
        if item.quantity < quantity:
            raise ValueError("Insufficient stock for sale.")
        
        item.update_quantity(-quantity)
        sale_record = {
            'item': item_name,
            'quantity': quantity,
            'total_price': item.price * quantity
        }
        self.sales.append(sale_record)

    def get_sales_report(self) -> List[Dict]:
        """Get a report of all sales made."""
        return self.sales

def main():
    """Main function to run the POS system."""
    inventory = Inventory()
    pos = POS(inventory)

    # Load inventory from file if it exists
    inventory.load_from_file('inventory.json')

    # Example operations
    try:
        inventory.add_item('Beef', 10.0, 50)
        inventory.add_item('Chicken', 8.0, 30)
        pos.make_sale('Beef', 5)
        pos.make_sale('Chicken', 2)

        # Print sales report
        print("Sales Report:", pos.get_sales_report())

        # Save inventory to file
        inventory.save_to_file('inventory.json')

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
