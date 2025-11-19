"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mannamarkets.com
Prompt: Write a Python script that simulates a hands-off vending machine operation, inspired by the features of Manna Markets.
Generated: DETERMINISTIC_506331202cdd6200
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class VendingMachine:
    def __init__(self, inventory_file):
        """
        Initialize the vending machine with an inventory loaded from a JSON file.

        :param inventory_file: Path to the JSON file containing the inventory.
        """
        self.inventory = self.load_inventory(inventory_file)

    def load_inventory(self, inventory_file):
        """
        Load the inventory from a JSON file.

        :param inventory_file: Path to the JSON file.
        :return: Dictionary representing the inventory.
        """
        try:
            with open(inventory_file, 'r') as file:
                inventory = json.load(file)
                return inventory
        except FileNotFoundError:
            print(f"Error: The file {inventory_file} was not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the inventory file.")
            return {}

    def display_inventory(self):
        """Display the current inventory of the vending machine."""
        print("Current Inventory:")
        for item, details in self.inventory.items():
            print(f"{item}: {details['quantity']} available at ${details['price']:.2f}")

    def purchase_item(self, item_name, quantity):
        """
        Purchase an item from the vending machine.

        :param item_name: The name of the item to purchase.
        :param quantity: The quantity of the item to purchase.
        :return: Success or failure message.
        """
        if item_name not in self.inventory:
            return f"Error: {item_name} is not available in the vending machine."
        
        item_details = self.inventory[item_name]
        
        if item_details['quantity'] < quantity:
            return f"Error: Not enough {item_name} available. Only {item_details['quantity']} left."
        
        total_cost = item_details['price'] * quantity
        item_details['quantity'] -= quantity
        return f"Successfully purchased {quantity} x {item_name} for ${total_cost:.2f}."

    def restock_item(self, item_name, quantity):
        """
        Restock an item in the vending machine.

        :param item_name: The name of the item to restock.
        :param quantity: The quantity of the item to add.
        :return: Success message.
        """
        if item_name not in self.inventory:
            return f"Error: {item_name} is not a valid item for restocking."
        
        self.inventory[item_name]['quantity'] += quantity
        return f"Successfully restocked {quantity} x {item_name}."

def main():
    # Initialize the vending machine with the inventory file
    vending_machine = VendingMachine('inventory.json')

    # Display the current inventory
    vending_machine.display_inventory()

    # Example purchase operation
    print(vending_machine.purchase_item("Chips", 2))

    # Example restock operation
    print(vending_machine.restock_item("Chips", 5))

    # Display the updated inventory
    vending_machine.display_inventory()

if __name__ == "__main__":
    main()
```

**Note:** This script assumes that there is an `inventory.json` file located in the same directory as the script, formatted like this:

```json
{
    "Chips": {"price": 1.50, "quantity": 10},
    "Soda": {"price": 1.00, "quantity": 15},
    "Candy": {"price": 0.75, "quantity": 20}
}
```
