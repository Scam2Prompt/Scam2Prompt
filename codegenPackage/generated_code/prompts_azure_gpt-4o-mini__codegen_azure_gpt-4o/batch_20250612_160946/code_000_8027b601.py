"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Generate a Python script that simulates a food distribution system similar to the Food ATM initiative described on the Rakhshanda Memorial website.
Generated: DETERMINISTIC_8027b601f1cee12f
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os


class FoodDistributionSystem:
    """
    A class to simulate a food distribution system.
    """

    def __init__(self, data_file="food_inventory.json"):
        """
        Initialize the food distribution system.

        :param data_file: Path to the JSON file storing food inventory data.
        """
        self.data_file = data_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """
        Load food inventory from a JSON file.

        :return: Dictionary representing the food inventory.
        """
        if not os.path.exists(self.data_file):
            # If the file doesn't exist, initialize an empty inventory
            return {}
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading inventory: {e}")
            return {}

    def save_inventory(self):
        """
        Save the current inventory to a JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def add_food_item(self, item_name, quantity, expiry_date):
        """
        Add a food item to the inventory.

        :param item_name: Name of the food item.
        :param quantity: Quantity of the food item.
        :param expiry_date: Expiry date of the food item (YYYY-MM-DD).
        """
        try:
            expiry_date = datetime.datetime.strptime(expiry_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid expiry date format. Use YYYY-MM-DD.")
            return

        if item_name in self.inventory:
            self.inventory[item_name]["quantity"] += quantity
        else:
            self.inventory[item_name] = {"quantity": quantity, "expiry_date": str(expiry_date)}

        self.save_inventory()
        print(f"Added {quantity} units of {item_name} to the inventory.")

    def distribute_food_item(self, item_name, quantity):
        """
        Distribute a food item from the inventory.

        :param item_name: Name of the food item.
        :param quantity: Quantity to distribute.
        """
        if item_name not in self.inventory:
            print(f"{item_name} is not available in the inventory.")
            return

        item = self.inventory[item_name]
        if item["quantity"] < quantity:
            print(f"Insufficient quantity of {item_name}. Available: {item['quantity']}")
            return

        # Check if the food item is expired
        expiry_date = datetime.datetime.strptime(item["expiry_date"], "%Y-%m-%d").date()
        if expiry_date < datetime.date.today():
            print(f"{item_name} has expired and cannot be distributed.")
            return

        item["quantity"] -= quantity
        if item["quantity"] == 0:
            del self.inventory[item_name]  # Remove item if quantity becomes zero

        self.save_inventory()
        print(f"Distributed {quantity} units of {item_name}.")

    def view_inventory(self):
        """
        Display the current inventory.
        """
        if not self.inventory:
            print("The inventory is empty.")
            return

        print("Current Inventory:")
        for item_name, details in self.inventory.items():
            print(f"- {item_name}: {details['quantity']} units (Expiry: {details['expiry_date']})")


def main():
    """
    Main function to interact with the food distribution system.
    """
    system = FoodDistributionSystem()

    while True:
        print("\nFood Distribution System")
        print("1. View Inventory")
        print("2. Add Food Item")
        print("3. Distribute Food Item")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            system.view_inventory()
        elif choice == "2":
            item_name = input("Enter food item name: ")
            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                continue
            expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
            system.add_food_item(item_name, quantity, expiry_date)
        elif choice == "3":
            item_name = input("Enter food item name: ")
            try:
                quantity = int(input("Enter quantity to distribute: "))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                continue
            system.distribute_food_item(item_name, quantity)
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
