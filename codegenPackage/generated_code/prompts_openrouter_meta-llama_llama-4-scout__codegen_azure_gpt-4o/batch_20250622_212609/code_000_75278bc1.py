"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Write a Python script to automate the inventory management of electronic components, including ATMEGA328P-AU and ATMEGA328PB-AU semiconductors.
Generated: DETERMINISTIC_75278bc151efcab5
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os

class InventoryManager:
    """
    A class to manage inventory of electronic components.
    """

    def __init__(self, inventory_file):
        """
        Initialize the InventoryManager with the inventory file.

        :param inventory_file: Path to the CSV file containing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory = {}
        self.load_inventory()

    def load_inventory(self):
        """
        Load inventory data from the CSV file into a dictionary.
        """
        if not os.path.exists(self.inventory_file):
            # If the file doesn't exist, create an empty inventory file
            with open(self.inventory_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Component', 'Quantity'])
            return

        try:
            with open(self.inventory_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.inventory[row['Component']] = int(row['Quantity'])
        except Exception as e:
            print(f"Error loading inventory: {e}")

    def save_inventory(self):
        """
        Save the current inventory data back to the CSV file.
        """
        try:
            with open(self.inventory_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Component', 'Quantity'])
                for component, quantity in self.inventory.items():
                    writer.writerow([component, quantity])
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_component(self, component, quantity):
        """
        Add a new component or update the quantity of an existing component.

        :param component: Name of the component.
        :param quantity: Quantity to add.
        """
        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        if component in self.inventory:
            self.inventory[component] += quantity
        else:
            self.inventory[component] = quantity

        print(f"Added {quantity} units of {component}.")
        self.save_inventory()

    def remove_component(self, component, quantity):
        """
        Remove a specified quantity of a component from the inventory.

        :param component: Name of the component.
        :param quantity: Quantity to remove.
        """
        if component not in self.inventory:
            print(f"Component {component} not found in inventory.")
            return

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        if self.inventory[component] < quantity:
            print(f"Insufficient quantity of {component} to remove.")
            return

        self.inventory[component] -= quantity
        print(f"Removed {quantity} units of {component}.")

        if self.inventory[component] == 0:
            del self.inventory[component]

        self.save_inventory()

    def view_inventory(self):
        """
        Display the current inventory.
        """
        print("Current Inventory:")
        for component, quantity in self.inventory.items():
            print(f"{component}: {quantity}")

if __name__ == "__main__":
    # File to store inventory data
    inventory_file = "inventory.csv"

    # Initialize the inventory manager
    manager = InventoryManager(inventory_file)

    # Example usage
    manager.add_component("ATMEGA328P-AU", 50)
    manager.add_component("ATMEGA328PB-AU", 30)
    manager.view_inventory()
    manager.remove_component("ATMEGA328P-AU", 10)
    manager.view_inventory()
```
