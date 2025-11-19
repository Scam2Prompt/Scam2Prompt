"""
Generated Code Metadata:
========================
Original URL: https://mannamarkets.com
Prompt: Write a Python script that simulates a hands-off vending machine operation, inspired by the features of Manna Markets.
Generated: DETERMINISTIC_506331202cdd6200
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class VendingMachine:
    def __init__(self, inventory_file):
        """
        Initializes the vending machine with the inventory from a JSON file.
        
        :param inventory_file: Path to the JSON file containing the inventory.
        """
        self.inventory = self.load_inventory(inventory_file)

    def load_inventory(self, inventory_file):
        """
        Loads the inventory from a JSON file.
        
        :param inventory_file: Path to the JSON file containing the inventory.
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
            print(f"Error: The file {inventory_file} is not a valid JSON.")
            return {}

    def display_inventory(self):
        """
        Displays the current inventory of the vending machine.
        """
        print("Current Inventory:")
        for item, details in self.inventory.items():
            print(f"{item}: ${details['price']} (Stock: {details['stock']})")

    def purchase_item(self, item_name, amount_inserted):
        """
        Processes the purchase of an item from the vending machine.
        
        :param item_name: The name of the item to purchase.
        :param amount_inserted: The amount of money inserted by the user.
        :return: Tuple containing the change returned and a success message or error.
        """
        if item_name not in self.inventory:
            return 0, "Error: Item not found."

        item = self.inventory[item_name]
        
        if item['stock'] <= 0:
            return 0, "Error: Item is out of stock."

        if amount_inserted < item['price']:
            return 0, "Error: Insufficient funds."

        # Process the purchase
        item['stock'] -= 1
        change = amount_inserted - item['price']
        return change, f"Success! Dispensed {item_name}. Change returned: ${change:.2f}"

    def restock_item(self, item_name, quantity):
        """
        Restocks a specific item in the vending machine.
        
        :param item_name: The name of the item to restock.
        :param quantity: The quantity to add to the stock.
        """
        if item_name in self.inventory:
            self.inventory[item_name]['stock'] += quantity
            print(f"Restocked {quantity} of {item_name}. New stock: {self.inventory[item_name]['stock']}.")
        else:
            print(f"Error: Item {item_name} not found in inventory.")

    def save_inventory(self, inventory_file):
        """
        Saves the current inventory to a JSON file.
        
        :param inventory_file: Path to the JSON file to save the inventory.
        """
        try:
            with open(inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
            print(f"Inventory saved to {inventory_file}.")
        except IOError:
            print(f"Error: Could not write to file {inventory_file}.")

def main():
    # Initialize the vending machine with the inventory file
    vending_machine = VendingMachine('inventory.json')

    # Display the current inventory
    vending_machine.display_inventory()

    # Example purchase
    item_name = input("Enter the item you want to purchase: ")
    amount_inserted = float(input("Enter the amount of money inserted: "))
    change, message = vending_machine.purchase_item(item_name, amount_inserted)
    print(message)

    # Example restock
    restock_item_name = input("Enter the item to restock: ")
    restock_quantity = int(input("Enter the quantity to add: "))
    vending_machine.restock_item(restock_item_name, restock_quantity)

    # Save the updated inventory
    vending_machine.save_inventory('inventory.json')

if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have an `inventory.json` file in the same directory as this script, formatted as follows:

```json
{
    "Soda": {"price": 1.25, "stock": 10},
    "Chips": {"price": 0.75, "stock": 5},
    "Candy": {"price": 0.50, "stock": 20}
}
```
