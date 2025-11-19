"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinsup.blogspot.com
Prompt: Construct a library recommendation for managing shoe inventory data, specifically for the types listed on the Raila Sapatos em Geral website.
Generated: DETERMINISTIC_5905d61e1a843ca9
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class Shoe:
    """
    Represents a shoe in the inventory.

    Attributes:
        shoe_id (int): Unique identifier for the shoe.
        name (str): Name of the shoe.
        size (float): Size of the shoe.
        quantity (int): Available quantity in inventory.
        price (float): Price of the shoe.
    """
    def __init__(self, shoe_id: int, name: str, size: float, quantity: int, price: float):
        self.shoe_id = shoe_id
        self.name = name
        self.size = size
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict:
        """Convert the shoe object to a dictionary."""
        return {
            "shoe_id": self.shoe_id,
            "name": self.name,
            "size": self.size,
            "quantity": self.quantity,
            "price": self.price
        }

class ShoeInventory:
    """
    Class to manage a shoe inventory.

    Attributes:
        shoes (List[Shoe]): List of shoes in the inventory.
    """
    def __init__(self):
        self.shoes: List[Shoe] = []

    def add_shoe(self, shoe: Shoe) -> None:
        """Add a new shoe to the inventory.

        Args:
            shoe (Shoe): The shoe object to add.
        """
        self.shoes.append(shoe)

    def remove_shoe(self, shoe_id: int) -> Optional[Shoe]:
        """Remove a shoe from the inventory by its ID.

        Args:
            shoe_id (int): The ID of the shoe to remove.

        Returns:
            Optional[Shoe]: The removed shoe object, or None if not found.
        """
        for shoe in self.shoes:
            if shoe.shoe_id == shoe_id:
                self.shoes.remove(shoe)
                return shoe
        return None

    def update_shoe_quantity(self, shoe_id: int, quantity: int) -> bool:
        """Update the quantity of a shoe in the inventory.

        Args:
            shoe_id (int): The ID of the shoe to update.
            quantity (int): The new quantity.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        for shoe in self.shoes:
            if shoe.shoe_id == shoe_id:
                shoe.quantity = quantity
                return True
        return False

    def get_inventory(self) -> List[Dict]:
        """Get the current inventory as a list of dictionaries.

        Returns:
            List[Dict]: List of shoe dictionaries.
        """
        return [shoe.to_dict() for shoe in self.shoes]

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file.

        Args:
            filename (str): The filename to save to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load inventory from a JSON file.

        Args:
            filename (str): The filename to load from.
        """
        try:
            with open(filename, 'r') as file:
                inventory_data = json.load(file)
                for shoe_data in inventory_data:
                    shoe = Shoe(**shoe_data)
                    self.add_shoe(shoe)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file {filename}: {e}")
```
