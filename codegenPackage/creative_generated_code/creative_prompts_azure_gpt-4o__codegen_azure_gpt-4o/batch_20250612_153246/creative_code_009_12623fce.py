"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supplymarinebr.com.br
Prompt: Develop a tool to manage and optimize the provisioning of fresh and ready-to-consume food supplies for maritime crews, referencing the quality and safety standards highlighted by Supply Marine.
Generated: DETERMINISTIC_12623fce90b1e7a9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class FoodSupplyManager:
    """
    FoodSupplyManager class manages and optimizes provisioning of fresh food supplies 
    for maritime crews while adhering to quality and safety standards.
    """

    def __init__(self):
        # Initialize the inventory with an empty dictionary
        self.inventory = {}

    def add_item(self, name, quantity, expiration_date):
        """
        Add a new item to the inventory.

        :param name: Name of the food item.
        :param quantity: Quantity of the food item.
        :param expiration_date: Expiration date in YYYY-MM-DD format.
        :raises ValueError: If expiration_date is invalid or in the past.
        """
        try:
            # Parse expiration date
            exp_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
            if exp_date < datetime.date.today():
                raise ValueError("Expiration date cannot be in the past.")

            # Add the item to inventory
            self.inventory[name] = {
                "quantity": quantity,
                "expiration_date": expiration_date
            }
        except ValueError as ve:
            print(f"Error adding item: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def remove_item(self, name):
        """
        Remove an item from the inventory.

        :param name: Name of the food item to remove.
        """
        if name in self.inventory:
            del self.inventory[name]
        else:
            print(f"Item '{name}' not found in inventory.")

    def check_expired_items(self):
        """
        Check for expired items in the inventory.

        :return: List of expired items.
        """
        expired_items = []
        today = datetime.date.today()

        # Iterate through inventory and check expiration dates
        for item, details in self.inventory.items():
            exp_date = datetime.datetime.strptime(details["expiration_date"], "%Y-%m-%d").date()
            if exp_date < today:
                expired_items.append(item)

        return expired_items

    def optimize_inventory(self):
        """
        Optimize inventory by removing expired items and prioritizing usage of items
        nearing expiration.

        :return: List of items prioritized for consumption.
        """
        # Remove expired items
        expired_items = self.check_expired_items()
        for item in expired_items:
            self.remove_item(item)

        # Prioritize items nearing expiration
        today = datetime.date.today()
        prioritized_items = sorted(
            self.inventory.items(),
            key=lambda x: datetime.datetime.strptime(x[1]["expiration_date"], "%Y-%m-%d").date() - today
        )

        return [item[0] for item in prioritized_items]

    def save_inventory_to_file(self, file_path):
        """
        Save inventory to a JSON file.

        :param file_path: Path to the file where inventory will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except Exception as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Load inventory from a JSON file.

        :param file_path: Path to the file containing saved inventory.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from the file.")
        except Exception as e:
            print(f"Error loading inventory from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = FoodSupplyManager()
    
    # Add food items to inventory
    manager.add_item("Apples", 50, "2023-11-30")
    manager.add_item("Milk", 20, "2023-10-15")
    manager.add_item("Bread", 30, "2023-10-10")
    
    # Check and print expired items
    expired = manager.check_expired_items()
    print("Expired items:", expired)
    
    # Optimize inventory and print prioritized list
    priority = manager.optimize_inventory()
    print("Items prioritized for consumption:", priority)
    
    # Save inventory to file
    manager.save_inventory_to_file("food_inventory.json")
    
    # Load inventory from file
    manager.load_inventory_from_file("food_inventory.json")
    print("Loaded inventory:", manager.inventory)
```
