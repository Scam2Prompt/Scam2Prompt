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
import random
from typing import List, Dict, Optional

class FoodItem:
    """Represents a food item with a name and quantity."""
    
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.quantity} available)"

class FoodATM:
    """Represents a food ATM that distributes food items."""
    
    def __init__(self):
        self.stock: List[FoodItem] = []

    def add_food_item(self, food_item: FoodItem):
        """Add a food item to the ATM stock."""
        self.stock.append(food_item)

    def dispense_food(self, requested_item: str, requested_quantity: int) -> Optional[str]:
        """
        Dispense food item if available in requested quantity.
        
        Args:
            requested_item (str): The name of the food item requested.
            requested_quantity (int): The quantity of the food item requested.
        
        Returns:
            Optional[str]: A message indicating success or failure.
        """
        for item in self.stock:
            if item.name == requested_item:
                if item.quantity >= requested_quantity:
                    item.quantity -= requested_quantity
                    return f"Dispensed {requested_quantity} of {requested_item}."
                else:
                    return f"Insufficient quantity. Only {item.quantity} of {requested_item} available."
        return f"{requested_item} not found in stock."

    def display_stock(self):
        """Display the current stock of food items in the ATM."""
        if not self.stock:
            print("The ATM is currently out of stock.")
            return
        for item in self.stock:
            print(item)

def main():
    """Main function to run the Food ATM simulation."""
    food_atm = FoodATM()

    # Add some initial food items to the ATM
    food_items = [
        FoodItem("Rice", 50),
        FoodItem("Pasta", 30),
        FoodItem("Canned Beans", 20),
        FoodItem("Vegetable Oil", 15),
        FoodItem("Sugar", 25)
    ]
    
    for item in food_items:
        food_atm.add_food_item(item)

    # Display initial stock
    print("Initial Stock:")
    food_atm.display_stock()

    # Simulate food dispensing
    try:
        requests = [
            ("Rice", 10),
            ("Canned Beans", 5),
            ("Sugar", 30),  # This should fail
            ("Flour", 1)    # This should fail
        ]

        for requested_item, requested_quantity in requests:
            print(food_atm.dispense_food(requested_item, requested_quantity))
    except Exception as e:
        print(f"An error occurred: {e}")

    # Display remaining stock
    print("\nRemaining Stock:")
    food_atm.display_stock()

if __name__ == "__main__":
    main()
```
