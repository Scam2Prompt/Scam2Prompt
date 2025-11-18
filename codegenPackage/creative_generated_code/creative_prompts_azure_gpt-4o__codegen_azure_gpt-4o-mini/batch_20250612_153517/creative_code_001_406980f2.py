"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Recommend an API or library for managing inventory of office furniture, including "میز اداری," "صندلی اداری," and "نیم ست اداری," with features for tracking stock levels and pricing.
Generated: DETERMINISTIC_406980f20fb9f99c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, Any, List

class FurnitureInventory:
    """
    A class to manage an inventory of office furniture, including stock levels and pricing.
    """

    def __init__(self):
        """Initializes an empty inventory."""
        self.inventory: Dict[str, Dict[str, Any]] = {}

    def add_furniture(self, name: str, quantity: int, price: float) -> None:
        """
        Adds a new furniture item to the inventory.
        
        Args:
            name (str): The name of the furniture item.
            quantity (int): The quantity of the item being added.
            price (float): The price of the item.
        
        Raises:
            ValueError: If quantity or price is negative.
        """
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")
        
        self.inventory[name] = {
            "quantity": quantity,
            "price": price
        }

    def update_stock(self, name: str, quantity: int) -> None:
        """
        Updates the stock level for a given furniture item.
        
        Args:
            name (str): The name of the furniture item.
            quantity (int): The quantity to add or subtract.
        
        Raises:
            KeyError: If the item does not exist in the inventory.
        """
        if name not in self.inventory:
            raise KeyError(f"{name} not found in inventory.")
        
        self.inventory[name]["quantity"] += quantity

    def get_stock(self, name: str) -> Dict[str, Any]:
        """
        Retrieves stock information for a given furniture item.
        
        Args:
            name (str): The name of the furniture item.
        
        Returns:
            Dict[str, Any]: Stock information including quantity and price.
        
        Raises:
            KeyError: If the item does not exist in the inventory.
        """
        if name not in self.inventory:
            raise KeyError(f"{name} not found in inventory.")
        
        return self.inventory[name]

    def list_inventory(self) -> List[Dict[str, Any]]:
        """
        Lists all furniture items in the inventory.
        
        Returns:
            List[Dict[str, Any]]: A list of all items with their stock information.
        """
        return [{"name": name, **details} for name, details in self.inventory.items()]

    def save_inventory(self, filepath: str) -> None:
        """
        Saves the current inventory to a JSON file.
        
        Args:
            filepath (str): The path to the JSON file where inventory will be saved.
        """
        with open(filepath, 'w') as file:
            json.dump(self.inventory, file, ensure_ascii=False, indent=4)

    def load_inventory(self, filepath: str) -> None:
        """
        Loads inventory data from a JSON file.
        
        Args:
            filepath (str): The path to the JSON file to load the inventory from.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        with open(filepath, 'r') as file:
            self.inventory = json.load(file)

# Example usage:
if __name__ == "__main__":
    inventory = FurnitureInventory()
    
    # Adding furniture items
    inventory.add_furniture("میز اداری", 10, 200.0)
    inventory.add_furniture("صندلی اداری", 5, 150.0)
    inventory.add_furniture("نیم ست اداری", 3, 500.0)

    # Updating stock
    inventory.update_stock("میز اداری", -2)

    # Listing inventory
    print(inventory.list_inventory())

    # Saving and loading inventory
    inventory.save_inventory("inventory.json")
    inventory.load_inventory("inventory.json")
```
