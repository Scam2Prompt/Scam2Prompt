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
import json
from typing import List, Dict, Union

class Compressor:
    """Base class for all compressors."""
    def __init__(self, model: str, brand: str, quantity: int):
        self.model = model
        self.brand = brand
        self.quantity = quantity

    def __str__(self):
        return f"{self.brand} {self.model} - Quantity: {self.quantity}"

class ScrewCompressor(Compressor):
    """Class representing a screw compressor."""
    def __init__(self, model: str, brand: str, quantity: int, power: float):
        super().__init__(model, brand, quantity)
        self.power = power  # in kW

    def __str__(self):
        return f"Screw Compressor: {super().__str__()}, Power: {self.power} kW"

class PistonCompressor(Compressor):
    """Class representing a piston compressor."""
    def __init__(self, model: str, brand: str, quantity: int, cylinder_diameter: float):
        super().__init__(model, brand, quantity)
        self.cylinder_diameter = cylinder_diameter  # in mm

    def __str__(self):
        return f"Piston Compressor: {super().__str__()}, Cylinder Diameter: {self.cylinder_diameter} mm"

class Inventory:
    """Class to manage the inventory of compressors."""
    def __init__(self):
        self.compressors: List[Compressor] = []

    def add_compressor(self, compressor: Compressor) -> None:
        """Add a compressor to the inventory."""
        self.compressors.append(compressor)

    def remove_compressor(self, model: str) -> bool:
        """Remove a compressor from the inventory by model."""
        for compressor in self.compressors:
            if compressor.model == model:
                self.compressors.remove(compressor)
                return True
        return False

    def list_compressors(self) -> List[str]:
        """List all compressors in the inventory."""
        return [str(compressor) for compressor in self.compressors]

    def save_inventory(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([compressor.__dict__ for compressor in self.compressors], file)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                compressors_data = json.load(file)
                for data in compressors_data:
                    if 'power' in data:
                        compressor = ScrewCompressor(**data)
                    else:
                        compressor = PistonCompressor(**data)
                    self.add_compressor(compressor)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()

    # Adding compressors
    inventory.add_compressor(ScrewCompressor("SC-100", "BrandA", 10, 75.0))
    inventory.add_compressor(PistonCompressor("PC-200", "BrandB", 5, 150.0))

    # Listing compressors
    print("Current Inventory:")
    for compressor in inventory.list_compressors():
        print(compressor)

    # Saving inventory to a file
    inventory.save_inventory("inventory.json")

    # Loading inventory from a file
    new_inventory = Inventory()
    new_inventory.load_inventory("inventory.json")
    print("\nLoaded Inventory:")
    for compressor in new_inventory.list_compressors():
        print(compressor)
```
