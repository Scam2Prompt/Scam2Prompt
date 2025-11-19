"""
Generated Code Metadata:
========================
Original URL: https://galopinautomobile.fr
Prompt: Write a Python script to create an inventory management system for a luxury car dealership like Galopin Automobile.
Generated: DETERMINISTIC_d1f11029f2d1e10e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class InventoryManagementSystem:
    """
    A class to manage the inventory of a luxury car dealership.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initializes the inventory management system.

        :param inventory_file: Path to the inventory file (default: inventory.json)
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """
        Loads the inventory from a JSON file.

        :return: A dictionary representing the inventory.
        """
        try:
            with open(self.inventory_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, initialize an empty inventory
            return {}
        except json.JSONDecodeError:
            # Handle corrupted JSON file
            print("Error: Inventory file is corrupted. Initializing empty inventory.")
            return {}

    def save_inventory(self):
        """
        Saves the current inventory to a JSON file.
        """
        try:
            with open(self.inventory_file, "w") as file:
                json.dump(self.inventory, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save inventory. {e}")

    def add_car(self, car_id, make, model, year, price, quantity):
        """
        Adds a new car to the inventory.

        :param car_id: Unique identifier for the car.
        :param make: Car manufacturer.
        :param model: Car model.
        :param year: Manufacturing year.
        :param price: Price of the car.
        :param quantity: Number of cars available.
        """
        if car_id in self.inventory:
            print(f"Error: Car with ID {car_id} already exists in the inventory.")
            return

        self.inventory[car_id] = {
            "make": make,
            "model": model,
            "year": year,
            "price": price,
            "quantity": quantity
        }
        self.save_inventory()
        print(f"Car {make} {model} added successfully.")

    def update_car(self, car_id, **kwargs):
        """
        Updates the details of an existing car in the inventory.

        :param car_id: Unique identifier for the car.
        :param kwargs: Key-value pairs of attributes to update.
        """
        if car_id not in self.inventory:
            print(f"Error: Car with ID {car_id} does not exist in the inventory.")
            return

        self.inventory[car_id].update(kwargs)
        self.save_inventory()
        print(f"Car with ID {car_id} updated successfully.")

    def remove_car(self, car_id):
        """
        Removes a car from the inventory.

        :param car_id: Unique identifier for the car.
        """
        if car_id not in self.inventory:
            print(f"Error: Car with ID {car_id} does not exist in the inventory.")
            return

        del self.inventory[car_id]
        self.save_inventory()
        print(f"Car with ID {car_id} removed successfully.")

    def view_inventory(self):
        """
        Displays the current inventory in a readable format.
        """
        if not self.inventory:
            print("Inventory is empty.")
            return

        print("Current Inventory:")
        for car_id, details in self.inventory.items():
            print(f"ID: {car_id}")
            print(f"  Make: {details['make']}")
            print(f"  Model: {details['model']}")
            print(f"  Year: {details['year']}")
            print(f"  Price: ${details['price']}")
            print(f"  Quantity: {details['quantity']}")
            print("-" * 20)

    def search_car(self, car_id):
        """
        Searches for a car in the inventory by its ID.

        :param car_id: Unique identifier for the car.
        """
        if car_id not in self.inventory:
            print(f"Error: Car with ID {car_id} does not exist in the inventory.")
            return

        details = self.inventory[car_id]
        print(f"Car Details (ID: {car_id}):")
        print(f"  Make: {details['make']}")
        print(f"  Model: {details['model']}")
        print(f"  Year: {details['year']}")
        print(f"  Price: ${details['price']}")
        print(f"  Quantity: {details['quantity']}")


# Example usage
if __name__ == "__main__":
    # Initialize the inventory management system
    ims = InventoryManagementSystem()

    # Add cars to the inventory
    ims.add_car("001", "Rolls-Royce", "Phantom", 2023, 450000, 2)
    ims.add_car("002", "Bentley", "Continental GT", 2022, 250000, 3)

    # View the inventory
    ims.view_inventory()

    # Update a car's details
    ims.update_car("001", price=460000, quantity=1)

    # Search for a car
    ims.search_car("001")

    # Remove a car from the inventory
    ims.remove_car("002")

    # View the inventory again
    ims.view_inventory()
```
