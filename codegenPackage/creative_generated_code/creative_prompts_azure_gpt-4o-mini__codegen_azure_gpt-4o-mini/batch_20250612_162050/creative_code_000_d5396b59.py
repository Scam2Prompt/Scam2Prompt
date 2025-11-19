"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingoficecream.com
Prompt: Generate a Python script to simulate an ice cream truck inventory management system for a snow cone truck.
Generated: DETERMINISTIC_d5396b59319004f0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class IceCreamTruckInventory:
    """
    A class to manage the inventory of an ice cream truck, specifically 
    for snow cones.
    """

    def __init__(self):
        """Initialize the inventory with a default set of flavors."""
        self.inventory = {
            "flavors": {},
            "total_sales": 0.0
        }

    def add_flavor(self, flavor: str, quantity: int) -> None:
        """
        Add a new flavor to the inventory with an initial quantity.
        
        Args:
            flavor (str): The name of the flavor to add.
            quantity (int): The initial quantity of the flavor.
        
        Raises:
            ValueError: If the quantity is less than zero or the flavor already exists.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if flavor in self.inventory["flavors"]:
            raise ValueError(f"Flavor '{flavor}' already exists in inventory.")
        
        self.inventory["flavors"][flavor] = quantity

    def sell_flavor(self, flavor: str, quantity: int) -> None:
        """
        Sell a specified quantity of a flavor from the inventory.

        Args:
            flavor (str): The name of the flavor to sell.
            quantity (int): The quantity to sell.

        Raises:
            ValueError: If the flavor does not exist or there is insufficient stock.
        """
        if flavor not in self.inventory["flavors"]:
            raise ValueError(f"Flavor '{flavor}' does not exist in inventory.")

        if self.inventory["flavors"][flavor] < quantity:
            raise ValueError(f"Insufficient stock for '{flavor}'. Available: {self.inventory['flavors'][flavor]}")

        # Deduct the sold quantity from the inventory
        self.inventory["flavors"][flavor] -= quantity
        # Assuming a fixed price of $2.00 per snow cone sold
        self.inventory["total_sales"] += 2.00 * quantity

    def restock_flavor(self, flavor: str, quantity: int) -> None:
        """
        Restock an existing flavor in the inventory.

        Args:
            flavor (str): The name of the flavor to restock.
            quantity (int): The quantity to add to the stock.

        Raises:
            ValueError: If the quantity is less than zero or the flavor does not exist.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if flavor not in self.inventory["flavors"]:
            raise ValueError(f"Flavor '{flavor}' does not exist in inventory.")

        self.inventory["flavors"][flavor] += quantity

    def get_inventory(self) -> dict:
        """Return the current inventory."""
        return self.inventory

    def save_inventory(self, filename: str) -> None:
        """
        Save the current inventory to a JSON file.

        Args:
            filename (str): The name of the file to save the inventory to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.inventory, file)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory(self, filename: str) -> None:
        """
        Load inventory from a JSON file.

        Args:
            filename (str): The name of the file to load the inventory from.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(filename, 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error: File '{filename}' contains invalid JSON.")

# Example usage:
if __name__ == "__main__":
    try:
        truck_inventory = IceCreamTruckInventory()
        truck_inventory.add_flavor("Blue Raspberry", 50)
        truck_inventory.add_flavor("Cherry", 30)
        
        truck_inventory.sell_flavor("Blue Raspberry", 5)
        truck_inventory.restock_flavor("Cherry", 20)

        print(truck_inventory.get_inventory())
        
        truck_inventory.save_inventory("inventory.json")
        truck_inventory.load_inventory("inventory.json")
        
        print(truck_inventory.get_inventory())
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
