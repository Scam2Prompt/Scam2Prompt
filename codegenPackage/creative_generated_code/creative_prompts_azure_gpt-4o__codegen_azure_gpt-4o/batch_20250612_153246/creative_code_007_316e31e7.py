"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aulaferretera.com
Prompt: Create a Python program to manage inventory and sales in a hardware store, referencing the "Guía Completa: Cómo Gestionar y Operar una Ferretería – Desde Cero hasta el Éxito" from Aula Ferretera.
Generated: DETERMINISTIC_316e31e7b55088be
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
import os


class HardwareStore:
    def __init__(self, inventory_file='inventory.json', sales_file='sales.json'):
        """
        Initialize the hardware store with inventory and sales files.

        Args:
            inventory_file (str): The path to the inventory file.
            sales_file (str): The path to the sales file.
        """
        self.inventory_file = inventory_file
        self.sales_file = sales_file
        self.inventory = {}
        self.sales = []

        # Load inventory and sales data from files if they exist
        self._load_data()

    def _load_data(self):
        """Load inventory and sales data from JSON files."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as f:
                self.inventory = json.load(f)
        else:
            self.inventory = {}

        if os.path.exists(self.sales_file):
            with open(self.sales_file, 'r') as f:
                self.sales = json.load(f)
        else:
            self.sales = []

    def _save_inventory(self):
        """Save inventory data to the JSON file."""
        try:
            with open(self.inventory_file, 'w') as f:
                json.dump(self.inventory, f, indent=4)
        except Exception as e:
            print(f"Error saving inventory data: {e}")

    def _save_sales(self):
        """Save sales data to the JSON file."""
        try:
            with open(self.sales_file, 'w') as f:
                json.dump(self.sales, f, indent=4)
        except Exception as e:
            print(f"Error saving sales data: {e}")

    def add_item(self, item_name, quantity, price):
        """
        Add or update an item in the inventory.

        Args:
            item_name (str): Name of the item.
            quantity (int): Quantity of the item.
            price (float): Price of the item.
        """
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
            self.inventory[item_name]['price'] = price
        else:
            self.inventory[item_name] = {'quantity': quantity, 'price': price}
        self._save_inventory()
        print(f"Added/Updated item: {item_name}")

    def sell_item(self, item_name, quantity):
        """
        Sell an item, updating inventory and logging the sale.

        Args:
            item_name (str): Name of the item.
            quantity (int): Quantity to sell.
        """
        if item_name not in self.inventory:
            print(f"Error: {item_name} not found in inventory.")
            return

        if self.inventory[item_name]['quantity'] < quantity:
            print(f"Error: Not enough stock of {item_name}. Available: {self.inventory[item_name]['quantity']}")
            return

        # Update inventory
        self.inventory[item_name]['quantity'] -= quantity
        self._save_inventory()

        # Log the sale
        sale_record = {
            'item_name': item_name,
            'quantity': quantity,
            'total_price': self.inventory[item_name]['price'] * quantity
        }
        self.sales.append(sale_record)
        self._save_sales()
        print(f"Sold {quantity} units of {item_name}.")

    def view_inventory(self):
        """Display the current inventory."""
        print("Current Inventory:")
        for item, details in self.inventory.items():
            print(f"- {item}: {details['quantity']} units at ${details['price']:.2f} each")

    def view_sales(self):
        """Display the sales records."""
        print("Sales Records:")
        for sale in self.sales:
            print(f"- {sale['quantity']} units of {sale['item_name']} sold for ${sale['total_price']:.2f}")


# Example usage
if __name__ == '__main__':
    store = HardwareStore()

    # Add items to inventory
    store.add_item("Hammer", 50, 9.99)
    store.add_item("Wrench", 30, 12.49)

    # View inventory
    store.view_inventory()

    # Sell items
    store.sell_item("Hammer", 10)
    store.sell_item("Wrench", 5)

    # View updated inventory
    store.view_inventory()

    # View sales records
    store.view_sales()
```
