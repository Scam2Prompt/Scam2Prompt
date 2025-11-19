"""
Generated Code Metadata:
========================
Original URL: https://ratnarajfoods.in
Prompt: Write a Python code snippet to manage inventory for a spice manufacturing company like Ratnaraj Foods, including classes for different types of spices.
Generated: DETERMINISTIC_4c848361ff52e0d6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

from abc import ABC, abstractmethod
from typing import Dict, List

class Spice(ABC):
    """Base class for all spices."""

    def __init__(self, name: str, quantity: int, price: float):
        """
        Initialize a spice.

        Args:
        - name (str): Name of the spice.
        - quantity (int): Quantity of the spice in stock.
        - price (float): Price of the spice per unit.
        """
        self.name = name
        self.quantity = quantity
        self.price = price

    @abstractmethod
    def get_details(self) -> Dict:
        """Get details of the spice."""
        pass


class PowderSpice(Spice):
    """Class for powder spices."""

    def __init__(self, name: str, quantity: int, price: float, mesh_size: int):
        """
        Initialize a powder spice.

        Args:
        - name (str): Name of the spice.
        - quantity (int): Quantity of the spice in stock.
        - price (float): Price of the spice per unit.
        - mesh_size (int): Mesh size of the powder spice.
        """
        super().__init__(name, quantity, price)
        self.mesh_size = mesh_size

    def get_details(self) -> Dict:
        """Get details of the powder spice."""
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "mesh_size": self.mesh_size,
            "type": "Powder"
        }


class WholeSpice(Spice):
    """Class for whole spices."""

    def __init__(self, name: str, quantity: int, price: float, origin: str):
        """
        Initialize a whole spice.

        Args:
        - name (str): Name of the spice.
        - quantity (int): Quantity of the spice in stock.
        - price (float): Price of the spice per unit.
        - origin (str): Origin of the whole spice.
        """
        super().__init__(name, quantity, price)
        self.origin = origin

    def get_details(self) -> Dict:
        """Get details of the whole spice."""
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "origin": self.origin,
            "type": "Whole"
        }


class Inventory:
    """Class to manage inventory."""

    def __init__(self):
        """Initialize an empty inventory."""
        self.spices: List[Spice] = []

    def add_spice(self, spice: Spice):
        """
        Add a spice to the inventory.

        Args:
        - spice (Spice): Spice to add.
        """
        self.spices.append(spice)

    def remove_spice(self, name: str):
        """
        Remove a spice from the inventory.

        Args:
        - name (str): Name of the spice to remove.

        Raises:
        - ValueError: If the spice is not found in the inventory.
        """
        for spice in self.spices:
            if spice.name == name:
                self.spices.remove(spice)
                return
        raise ValueError("Spice not found in the inventory.")

    def update_quantity(self, name: str, quantity: int):
        """
        Update the quantity of a spice in the inventory.

        Args:
        - name (str): Name of the spice to update.
        - quantity (int): New quantity of the spice.

        Raises:
        - ValueError: If the spice is not found in the inventory.
        """
        for spice in self.spices:
            if spice.name == name:
                spice.quantity = quantity
                return
        raise ValueError("Spice not found in the inventory.")

    def get_spice_details(self, name: str) -> Dict:
        """
        Get details of a spice in the inventory.

        Args:
        - name (str): Name of the spice.

        Returns:
        - Dict: Details of the spice.

        Raises:
        - ValueError: If the spice is not found in the inventory.
        """
        for spice in self.spices:
            if spice.name == name:
                return spice.get_details()
        raise ValueError("Spice not found in the inventory.")

    def display_inventory(self):
        """Display all spices in the inventory."""
        for spice in self.spices:
            print(spice.get_details())


def main():
    # Create an inventory
    inventory = Inventory()

    # Create spices
    turmeric = PowderSpice("Turmeric", 100, 5.99, 200)
    cinnamon = WholeSpice("Cinnamon", 50, 3.99, "Sri Lanka")

    # Add spices to the inventory
    inventory.add_spice(turmeric)
    inventory.add_spice(cinnamon)

    # Display inventory
    print("Inventory:")
    inventory.display_inventory()

    # Update quantity
    inventory.update_quantity("Turmeric", 80)

    # Get spice details
    print("\nTurmeric Details:")
    print(inventory.get_spice_details("Turmeric"))

    # Remove spice
    inventory.remove_spice("Cinnamon")

    # Display updated inventory
    print("\nUpdated Inventory:")
    inventory.display_inventory()


if __name__ == "__main__":
    main()
```
