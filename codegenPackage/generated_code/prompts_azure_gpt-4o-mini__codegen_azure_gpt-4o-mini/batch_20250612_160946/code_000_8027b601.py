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
import random
from typing import List, Dict

class FoodItem:
    """Class representing a food item in the distribution system."""
    
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (Quantity: {self.quantity})"

class FoodATM:
    """Class representing a Food ATM that distributes food items."""
    
    def __init__(self):
        self.inventory: List[FoodItem] = []

    def add_food_item(self, food_item: FoodItem):
        """Add a food item to the ATM's inventory."""
        self.inventory.append(food_item)
        print(f"Added {food_item} to the inventory.")

    def distribute_food(self, requested_item: str, requested_quantity: int) -> Dict[str, str]:
        """Distribute food items based on user request."""
        for item in self.inventory:
            if item.name.lower() == requested_item.lower():
                if item.quantity >= requested_quantity:
                    item.quantity -= requested_quantity
                    return {
                        "status": "success",
                        "message": f"Distributed {requested_quantity} of {item.name}.",
                        "remaining_quantity": item.quantity
                    }
                else:
                    return {
                        "status": "error",
                        "message": f"Insufficient quantity of {item.name}. Available: {item.quantity}."
                    }
        return {
            "status": "error",
            "message": f"{requested_item} not found in inventory."
        }

    def display_inventory(self):
        """Display the current inventory of the Food ATM."""
        if not self.inventory:
            print("The inventory is empty.")
            return
        print("Current Inventory:")
        for item in self.inventory:
            print(item)

def main():
    """Main function to simulate the food distribution system."""
    food_atm = FoodATM()

    # Adding food items to the ATM
    food_items = [
        FoodItem("Rice", 100),
        FoodItem("Pasta", 50),
        FoodItem("Canned Beans", 75),
        FoodItem("Vegetable Oil", 30),
        FoodItem("Sugar", 20)
    ]

    for item in food_items:
        food_atm.add_food_item(item)

    # Display current inventory
    food_atm.display_inventory()

    # Simulate user requests
    requests = [
        ("Rice", 20),
        ("Pasta", 60),
        ("Sugar", 10),
        ("Canned Beans", 80),
        ("Flour", 5)  # Item not in inventory
    ]

    for requested_item, requested_quantity in requests:
        result = food_atm.distribute_food(requested_item, requested_quantity)
        print(result["message"])

    # Final inventory display
    food_atm.display_inventory()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
