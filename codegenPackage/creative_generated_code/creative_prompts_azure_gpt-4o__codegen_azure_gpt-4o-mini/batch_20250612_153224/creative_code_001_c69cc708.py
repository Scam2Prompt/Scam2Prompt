"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atilumber.com
Prompt: Recommend APIs or libraries for managing timber inventory, including features for tracking softwood and hardwood types as outlined by Askar Trading International.
Generated: DETERMINISTIC_c69cc708c95c51aa
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# timber_inventory.py

import json
from typing import List, Dict, Union

class TimberInventory:
    """
    A class to manage timber inventory, including tracking of softwood and hardwood types.
    """

    def __init__(self):
        """Initialize an empty timber inventory."""
        self.inventory: Dict[str, Dict[str, Union[int, float]]] = {
            "softwood": {},
            "hardwood": {}
        }

    def add_timber(self, timber_type: str, species: str, quantity: int, price_per_unit: float) -> None:
        """
        Add timber species to the inventory.

        :param timber_type: Type of timber ('softwood' or 'hardwood').
        :param species: The species name of the timber.
        :param quantity: Quantity of timber to add.
        :param price_per_unit: Price per unit of the timber.
        :raises ValueError: If timber_type is not 'softwood' or 'hardwood'.
        """
        if timber_type not in self.inventory:
            raise ValueError("Invalid timber type. Must be 'softwood' or 'hardwood'.")

        if species in self.inventory[timber_type]:
            self.inventory[timber_type][species]['quantity'] += quantity
        else:
            self.inventory[timber_type][species] = {
                'quantity': quantity,
                'price_per_unit': price_per_unit
            }

    def remove_timber(self, timber_type: str, species: str, quantity: int) -> None:
        """
        Remove timber species from the inventory.

        :param timber_type: Type of timber ('softwood' or 'hardwood').
        :param species: The species name of the timber.
        :param quantity: Quantity of timber to remove.
        :raises ValueError: If the quantity exceeds what is available or if the timber type is invalid.
        """
        if timber_type not in self.inventory:
            raise ValueError("Invalid timber type. Must be 'softwood' or 'hardwood'.")

        if species not in self.inventory[timber_type]:
            raise ValueError(f"{species} not found in {timber_type} inventory.")

        if self.inventory[timber_type][species]['quantity'] < quantity:
            raise ValueError("Insufficient quantity to remove.")

        self.inventory[timber_type][species]['quantity'] -= quantity

        if self.inventory[timber_type][species]['quantity'] == 0:
            del self.inventory[timber_type][species]

    def get_inventory(self) -> Dict[str, Dict[str, Dict[str, Union[int, float]]]]:
        """
        Get the current inventory.

        :return: A dictionary containing the full inventory.
        """
        return self.inventory

    def save_inventory(self, filename: str) -> None:
        """
        Save the inventory to a JSON file.

        :param filename: The name of the file to save the inventory to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self, filename: str) -> None:
        """
        Load the inventory from a JSON file.

        :param filename: The name of the file to load the inventory from.
        :raises FileNotFoundError: If the file does not exist.
        """
        try:
            with open(filename, 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError as e:
            print(f"Error loading inventory: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file: {e}")

# Example usage:
if __name__ == "__main__":
    inventory = TimberInventory()
    inventory.add_timber('softwood', 'Pine', 50, 5.0)
    inventory.add_timber('hardwood', 'Oak', 30, 10.0)
    
    print("Current Inventory:", inventory.get_inventory())

    inventory.save_inventory('timber_inventory.json')
    inventory.load_inventory('timber_inventory.json')
    print("Loaded Inventory:", inventory.get_inventory())
```
