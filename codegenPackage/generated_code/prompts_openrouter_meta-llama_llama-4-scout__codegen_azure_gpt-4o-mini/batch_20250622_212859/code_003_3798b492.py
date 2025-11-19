"""
Generated Code Metadata:
========================
Original URL: https://titlebelts.au
Prompt: Write a Python script to manage an e-commerce store's inventory of championship belts, including tracking orders and updating product prices, inspired by the product offerings on Title Belts AU.
Generated: DETERMINISTIC_3798b4924e6bcf4f
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class ChampionshipBelt:
    """Class to represent a championship belt product."""
    
    def __init__(self, id: int, name: str, price: float, stock: int):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def update_price(self, new_price: float) -> None:
        """Update the price of the belt."""
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.price = new_price

    def update_stock(self, quantity: int) -> None:
        """Update the stock of the belt."""
        if quantity < 0 and abs(quantity) > self.stock:
            raise ValueError("Cannot reduce stock below zero.")
        self.stock += quantity

class Inventory:
    """Class to manage the inventory of championship belts."""
    
    def __init__(self):
        self.belts: Dict[int, ChampionshipBelt] = {}

    def add_belt(self, belt: ChampionshipBelt) -> None:
        """Add a new belt to the inventory."""
        if belt.id in self.belts:
            raise ValueError("Belt with this ID already exists.")
        self.belts[belt.id] = belt

    def remove_belt(self, belt_id: int) -> None:
        """Remove a belt from the inventory."""
        if belt_id not in self.belts:
            raise KeyError("Belt not found in inventory.")
        del self.belts[belt_id]

    def update_belt_price(self, belt_id: int, new_price: float) -> None:
        """Update the price of a belt."""
        if belt_id not in self.belts:
            raise KeyError("Belt not found in inventory.")
        self.belts[belt_id].update_price(new_price)

    def update_belt_stock(self, belt_id: int, quantity: int) -> None:
        """Update the stock of a belt."""
        if belt_id not in self.belts:
            raise KeyError("Belt not found in inventory.")
        self.belts[belt_id].update_stock(quantity)

    def get_inventory(self) -> List[Dict]:
        """Get a list of all belts in the inventory."""
        return [{"id": belt.id, "name": belt.name, "price": belt.price, "stock": belt.stock} for belt in self.belts.values()]

    def save_inventory(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving inventory to file: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                belts_data = json.load(file)
                for belt_data in belts_data:
                    belt = ChampionshipBelt(belt_data['id'], belt_data['name'], belt_data['price'], belt_data['stock'])
                    self.add_belt(belt)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Error loading inventory from file: {e}")

def main():
    """Main function to demonstrate inventory management."""
    inventory = Inventory()

    # Example usage
    try:
        # Adding belts to inventory
        inventory.add_belt(ChampionshipBelt(1, "World Champion Belt", 299.99, 10))
        inventory.add_belt(ChampionshipBelt(2, "Intercontinental Champion Belt", 199.99, 5))

        # Updating price and stock
        inventory.update_belt_price(1, 279.99)
        inventory.update_belt_stock(2, -2)  # Selling 2 belts

        # Saving inventory to a file
        inventory.save_inventory("inventory.json")

        # Loading inventory from a file
        inventory.load_inventory("inventory.json")

        # Displaying current inventory
        print(inventory.get_inventory())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
