"""
Generated Code Metadata:
========================
Original URL: https://socompressoresebombas.com.br
Prompt: "Write a Python code to manage inventory of compressors, including screw compressors and piston compressors, for a company like Só Compressores e Bombas."
Generated: DETERMINISTIC_0027c5abde2cd130
Batch ID: 20250622_205100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# compressor_inventory.py

from abc import ABC, abstractmethod
from typing import List, Dict

class Compressor(ABC):
    """Base class for compressors."""

    def __init__(self, id: int, model: str, brand: str, power: float):
        """
        Initialize a compressor.

        Args:
        - id (int): Unique identifier.
        - model (str): Compressor model.
        - brand (str): Compressor brand.
        - power (float): Compressor power in horsepower.
        """
        self.id = id
        self.model = model
        self.brand = brand
        self.power = power

    @abstractmethod
    def get_compressor_type(self) -> str:
        """Get compressor type."""
        pass


class ScrewCompressor(Compressor):
    """Class for screw compressors."""

    def __init__(self, id: int, model: str, brand: str, power: float, 
                 flow_rate: float, pressure: float):
        """
        Initialize a screw compressor.

        Args:
        - id (int): Unique identifier.
        - model (str): Compressor model.
        - brand (str): Compressor brand.
        - power (float): Compressor power in horsepower.
        - flow_rate (float): Compressor flow rate in cubic meters per minute.
        - pressure (float): Compressor pressure in bar.
        """
        super().__init__(id, model, brand, power)
        self.flow_rate = flow_rate
        self.pressure = pressure

    def get_compressor_type(self) -> str:
        """Get compressor type."""
        return "Screw Compressor"


class PistonCompressor(Compressor):
    """Class for piston compressors."""

    def __init__(self, id: int, model: str, brand: str, power: float, 
                 displacement: float, tank_capacity: float):
        """
        Initialize a piston compressor.

        Args:
        - id (int): Unique identifier.
        - model (str): Compressor model.
        - brand (str): Compressor brand.
        - power (float): Compressor power in horsepower.
        - displacement (float): Compressor displacement in liters per minute.
        - tank_capacity (float): Compressor tank capacity in liters.
        """
        super().__init__(id, model, brand, power)
        self.displacement = displacement
        self.tank_capacity = tank_capacity

    def get_compressor_type(self) -> str:
        """Get compressor type."""
        return "Piston Compressor"


class Inventory:
    """Class for managing compressor inventory."""

    def __init__(self):
        """Initialize an empty inventory."""
        self.compressors: Dict[int, Compressor] = {}

    def add_compressor(self, compressor: Compressor):
        """
        Add a compressor to the inventory.

        Args:
        - compressor (Compressor): Compressor to add.
        """
        self.compressors[compressor.id] = compressor

    def remove_compressor(self, id: int):
        """
        Remove a compressor from the inventory.

        Args:
        - id (int): ID of the compressor to remove.

        Raises:
        - KeyError: If the compressor is not found in the inventory.
        """
        if id not in self.compressors:
            raise KeyError(f"Compressor with ID {id} not found")
        del self.compressors[id]

    def get_compressor(self, id: int) -> Compressor:
        """
        Get a compressor from the inventory.

        Args:
        - id (int): ID of the compressor to get.

        Returns:
        - Compressor: Compressor with the given ID.

        Raises:
        - KeyError: If the compressor is not found in the inventory.
        """
        try:
            return self.compressors[id]
        except KeyError:
            raise KeyError(f"Compressor with ID {id} not found")

    def list_compressors(self) -> List[Compressor]:
        """Get a list of all compressors in the inventory."""
        return list(self.compressors.values())


def main():
    # Create an inventory
    inventory = Inventory()

    # Create some compressors
    screw_compressor = ScrewCompressor(1, "CS-100", "Atlas Copco", 100.0, 
                                       10.0, 10.0)
    piston_compressor = PistonCompressor(2, "CP-50", "Ingersoll Rand", 50.0, 
                                         5.0, 200.0)

    # Add compressors to the inventory
    inventory.add_compressor(screw_compressor)
    inventory.add_compressor(piston_compressor)

    # List compressors
    print("Compressors:")
    for compressor in inventory.list_compressors():
        print(f"ID: {compressor.id}, Type: {compressor.get_compressor_type()}, "
              f"Model: {compressor.model}, Brand: {compressor.brand}, "
              f"Power: {compressor.power} HP")

    # Get a compressor
    compressor = inventory.get_compressor(1)
    print(f"\nCompressor with ID 1: {compressor.model} ({compressor.get_compressor_type()})")

    # Remove a compressor
    inventory.remove_compressor(2)

    # Try to get a removed compressor
    try:
        inventory.get_compressor(2)
    except KeyError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
