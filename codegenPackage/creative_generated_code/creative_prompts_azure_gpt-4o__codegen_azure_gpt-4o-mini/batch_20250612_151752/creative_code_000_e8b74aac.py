"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-pieces-service.fr
Prompt: Write a Python script to calculate inventory levels for an automotive parts store, including categories like "plaquettes de freins," "embrayage," and "batteries," as described on the Distribution Pièces Service website.
Generated: DETERMINISTIC_e8b74aac1fd06c48
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import Dict, List

# Configure logging to capture errors and info messages
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Inventory:
    def __init__(self):
        # Initialize inventory as an empty dictionary
        self.inventory: Dict[str, int] = {}

    def add_part(self, category: str, quantity: int) -> None:
        """
        Adds parts to the inventory.

        Args:
            category (str): The category of the automotive part.
            quantity (int): The quantity of the part to add.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity must be non-negative")
        
        if category in self.inventory:
            self.inventory[category] += quantity
        else:
            self.inventory[category] = quantity
        
        logging.info(f"Added {quantity} to {category}. Current inventory: {self.inventory[category]}")

    def remove_part(self, category: str, quantity: int) -> None:
        """
        Removes parts from the inventory.

        Args:
            category (str): The category of the automotive part.
            quantity (int): The quantity of the part to remove.

        Raises:
            ValueError: If the quantity is negative or exceeds available inventory.
        """
        if quantity < 0:
            raise ValueError("Quantity must be non-negative")
        
        if category not in self.inventory or self.inventory[category] < quantity:
            raise ValueError(f"Not enough inventory for {category}. Current stock: {self.inventory.get(category, 0)}")
        
        self.inventory[category] -= quantity
        
        logging.info(f"Removed {quantity} from {category}. Current inventory: {self.inventory[category]}")

    def get_inventory(self) -> Dict[str, int]:
        """Returns the current inventory levels."""
        return self.inventory

    def save_inventory(self, filename: str) -> None:
        """
        Saves the current inventory to a JSON file.

        Args:
            filename (str): The name of the file to save the inventory.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.inventory, file)
            logging.info(f"Inventory saved to {filename} successfully.")
        except IOError as e:
            logging.error(f"Error saving inventory to {filename}: {e}")

    def load_inventory(self, filename: str) -> None:
        """
        Loads inventory from a JSON file.

        Args:
            filename (str): The name of the file to load the inventory from.
        """
        try:
            with open(filename, 'r') as file:
                self.inventory = json.load(file)
            logging.info(f"Inventory loaded from {filename} successfully.")
        except IOError as e:
            logging.error(f"Error loading inventory from {filename}: {e}")
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from {filename}: {e}")

def main():
    # Create an instance of the Inventory class
    inventory = Inventory()
    
    # Example usage of the inventory management
    try:
        # Adding parts to inventory
        inventory.add_part("plaquettes de freins", 50)
        inventory.add_part("embrayage", 30)
        inventory.add_part("batteries", 20)

        # Removing parts from inventory
        inventory.remove_part("plaquettes de freins", 10)
        
        # Display current inventory
        print("Current Inventory Levels:", inventory.get_inventory())

        # Save inventory to file
        inventory.save_inventory("inventory.json")

        # Load inventory from file
        inventory.load_inventory("inventory.json")

    except ValueError as e:
        logging.error(f"Value error: {e}")

if __name__ == "__main__":
    main()
```
