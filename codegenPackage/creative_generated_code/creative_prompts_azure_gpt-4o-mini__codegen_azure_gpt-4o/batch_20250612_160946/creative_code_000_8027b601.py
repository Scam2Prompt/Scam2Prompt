"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rakhshandamemorial.org
Prompt: Generate a Python script that simulates a food distribution system similar to the Food ATM initiative described on the Rakhshanda Memorial website.
Generated: DETERMINISTIC_8027b601f1cee12f
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class FoodItem:
    """
    Represents a food item in the system.
    Attributes:
        name (str): Name of the food item.
        quantity (int): Quantity available for distribution.
        expiry_date (datetime.date): Expiry date of the food item.
    """
    def __init__(self, name, quantity, expiry_date):
        self.name = name
        self.quantity = quantity
        self.expiry_date = expiry_date

    def is_expired(self):
        """
        Check if the food item is expired.
        Returns:
            bool: True if expired, False otherwise.
        """
        return datetime.date.today() > self.expiry_date


class FoodATM:
    """
    Simulates a Food ATM system.
    Attributes:
        inventory (list): List of FoodItem objects available for distribution.
    """
    def __init__(self):
        self.inventory = []

    def add_food_item(self, name, quantity, expiry_date):
        """
        Adds a food item to the inventory.
        Args:
            name (str): Name of the food item.
            quantity (int): Quantity of the food item.
            expiry_date (str): Expiry date in YYYY-MM-DD format.
        """
        try:
            expiry_date_obj = datetime.datetime.strptime(expiry_date, "%Y-%m-%d").date()
            food_item = FoodItem(name, quantity, expiry_date_obj)
            self.inventory.append(food_item)
            print(f"Added {quantity} of {name} to inventory.")
        except ValueError:
            print("Error: Invalid expiry date format. Use YYYY-MM-DD.")

    def distribute_food(self, name, requested_quantity):
        """
        Distributes food to a user.
        Args:
            name (str): Name of the food item requested.
            requested_quantity (int): Quantity requested by the user.
        """
        for food_item in self.inventory:
            if food_item.name == name:
                if food_item.is_expired():
                    print(f"Error: {name} is expired and cannot be distributed.")
                    return
                if food_item.quantity >= requested_quantity:
                    food_item.quantity -= requested_quantity
                    print(f"Distributed {requested_quantity} of {name}.")
                    return
                else:
                    print(f"Error: Insufficient quantity of {name}. Only {food_item.quantity} available.")
                    return
        print(f"Error: {name} not found in inventory.")

    def check_inventory(self):
        """
        Prints the current inventory status.
        """
        print("\nCurrent Inventory:")
        for food_item in self.inventory:
            status = "Expired" if food_item.is_expired() else "Available"
            print(f"{food_item.name} - Quantity: {food_item.quantity}, Expiry Date: {food_item.expiry_date}, Status: {status}")


# Example usage of the FoodATM system
if __name__ == "__main__":
    food_atm = FoodATM()

    # Adding food items to the inventory
    food_atm.add_food_item("Rice", 100, "2023-12-31")
    food_atm.add_food_item("Beans", 50, "2023-10-15")
    food_atm.add_food_item("Bread", 20, "2023-10-01")  # Assume bread is already expired

    # Checking inventory
    food_atm.check_inventory()

    # Distributing food
    food_atm.distribute_food("Rice", 20)
    food_atm.distribute_food("Bread", 5)  # Attempt to distribute expired item
    food_atm.distribute_food("Beans", 60)  # Request more than available quantity

    # Checking inventory after distribution
    food_atm.check_inventory()
```
