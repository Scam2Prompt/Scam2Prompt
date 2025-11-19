"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Create a Python function to manage an inventory of airbrush equipment, including spray guns, compressors, and cleaning pots, as listed on AirstyleArt.
Generated: DETERMINISTIC_541614d5de6fc620
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class AirbrushInventory:
    """
    A class to manage an inventory of airbrush equipment including spray guns, compressors, and cleaning pots.
    """

    def __init__(self, inventory_file: str = "inventory.json"):
        """
        Initialize the inventory with a JSON file to persist data.
        
        Args:
            inventory_file (str): Path to the JSON file storing inventory data. Defaults to "inventory.json".
        """
        self.inventory_file = inventory_file
        self.inventory: Dict[str, Dict[str, Dict[str, int]]] = {
            "spray_guns": {},
            "compressors": {},
            "cleaning_pots": {}
        }
        self._load_inventory()

    def _load_inventory(self) -> None:
        """
        Load inventory data from the JSON file. If the file doesn't exist, initialize with empty inventory.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            self._save_inventory()
        except json.JSONDecodeError:
            raise ValueError("Inventory file is corrupted. Please check the file or provide a new one.")

    def _save_inventory(self) -> None:
        """
        Save the current inventory state to the JSON file.
        """
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_item(self, category: str, item_name: str, quantity: int, details: Optional[Dict] = None) -> None:
        """
        Add an item to the inventory or update its quantity if it already exists.
        
        Args:
            category (str): The category of the item (spray_guns, compressors, cleaning_pots).
            item_name (str): The name of the item to add.
            quantity (int): The quantity of the item to add.
            details (Optional[Dict]): Additional details about the item. Defaults to None.
        
        Raises:
            ValueError: If the category is invalid or quantity is negative.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Must be one of {list(self.inventory.keys())}")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        if item_name in self.inventory[category]:
            self.inventory[category][item_name]["quantity"] += quantity
            if details:
                self.inventory[category][item_name].update(details)
        else:
            if details is None:
                details = {}
            details["quantity"] = quantity
            self.inventory[category][item_name] = details

        self._save_inventory()

    def remove_item(self, category: str, item_name: str, quantity: int) -> None:
        """
        Remove a specified quantity of an item from the inventory.
        
        Args:
            category (str): The category of the item.
            item_name (str): The name of the item to remove.
            quantity (int): The quantity of the item to remove.
        
        Raises:
            ValueError: If the category or item doesn't exist, or quantity is invalid.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Must be one of {list(self.inventory.keys())}")
        if item_name not in self.inventory[category]:
            raise ValueError(f"Item {item_name} not found in category {category}.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if self.inventory[category][item_name]["quantity"] < quantity:
            raise ValueError(f"Insufficient quantity of {item_name} in inventory.")

        self.inventory[category][item_name]["quantity"] -= quantity
        if self.inventory[category][item_name]["quantity"] == 0:
            del self.inventory[category][item_name]
        self._save_inventory()

    def get_inventory(self, category: Optional[str] = None) -> Dict[str, Dict[str, int]]:
        """
        Retrieve the inventory for a specific category or all categories.
        
        Args:
            category (Optional[str]): The category to retrieve. If None, returns all categories.
        
        Returns:
            Dict[str, Dict[str, int]]: The inventory data.
        
        Raises:
            ValueError: If the category is invalid.
        """
        if category is None:
            return self.inventory
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Must be one of {list(self.inventory.keys())}")
        return {category: self.inventory[category]}

    def search_item(self, item_name: str) -> List[Dict[str, str]]:
        """
        Search for an item by name across all categories.
        
        Args:
            item_name (str): The name of the item to search for.
        
        Returns:
            List[Dict[str, str]]: A list of dictionaries containing category and item details.
        """
        results = []
        for category, items in self.inventory.items():
            if item_name in items:
                item_details = items[item_name].copy()
                item_details["category"] = category
                results.append(item_details)
        return results

# Example usage
if __name__ == "__main__":
    inventory = AirbrushInventory()
    
    # Add items to inventory
    inventory.add_item("spray_guns", "Iwata HP-CS", 5, {"nozzle_size": "0.35mm", "price": 149.99})
    inventory.add_item("compressors", "Master Airbrush TC-20", 3, {"tank": "1/5 gallon", "noise_level": "59dB"})
    inventory.add_item("cleaning_pots", "Master Airbrush Cleaning Pot", 10, {"capacity": "16oz"})
    
    # Remove items from inventory
    inventory.remove_item("spray_guns", "Iwata HP-CS", 2)
    
    # Get inventory
    print(inventory.get_inventory("spray_guns"))
    
    # Search item
    print(inventory.search_item("Master Airbrush"))
```
