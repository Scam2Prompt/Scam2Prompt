"""
Generated Code Metadata:
========================
Original URL: https://topgraininteriors.com
Prompt: Write a function in Python that generates a list of materials needed for building custom cabinets, inspired by the services provided by Top Grain Interiors.
Generated: DETERMINISTIC_66baa9cbfde744e8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class CabinetMaterialGenerator:
    """
    A class to generate a list of materials needed for building custom cabinets.
    """

    def __init__(self):
        # Initialize the materials dictionary with default values
        self.materials: Dict[str, float] = {
            "Plywood": 0.0,
            "Hardwood": 0.0,
            "Wood Glue": 0.0,
            "Screws": 0.0,
            "Cabinet Hinges": 0.0,
            "Drawer Slides": 0.0,
            "Finish (Paint/Stain)": 0.0,
            "Handles/Knobs": 0.0,
            "Sandpaper": 0.0,
            "Veneer": 0.0
        }

    def set_material_quantity(self, material: str, quantity: float) -> None:
        """
        Set the quantity for a specific material.

        :param material: The name of the material.
        :param quantity: The quantity of the material needed.
        :raises ValueError: If the material is not recognized or quantity is negative.
        """
        if material not in self.materials:
            raise ValueError(f"Material '{material}' is not recognized.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        self.materials[material] = quantity

    def generate_material_list(self) -> List[Dict[str, float]]:
        """
        Generate a list of materials with their quantities.

        :return: A list of dictionaries containing materials and their quantities.
        """
        material_list = []
        for material, quantity in self.materials.items():
            if quantity > 0:  # Only include materials with a positive quantity
                material_list.append({material: quantity})
        return material_list

    def display_material_list(self) -> None:
        """
        Display the list of materials in a readable format.
        """
        material_list = self.generate_material_list()
        if not material_list:
            print("No materials needed.")
            return
        
        print("Materials needed for building custom cabinets:")
        for item in material_list:
            for material, quantity in item.items():
                print(f"{material}: {quantity}")

# Example usage
if __name__ == "__main__":
    try:
        cabinet_generator = CabinetMaterialGenerator()
        cabinet_generator.set_material_quantity("Plywood", 5.0)
        cabinet_generator.set_material_quantity("Hardwood", 2.0)
        cabinet_generator.set_material_quantity("Wood Glue", 1.0)
        cabinet_generator.set_material_quantity("Screws", 100.0)
        cabinet_generator.set_material_quantity("Cabinet Hinges", 10.0)
        cabinet_generator.set_material_quantity("Drawer Slides", 4.0)
        cabinet_generator.set_material_quantity("Finish (Paint/Stain)", 1.0)
        cabinet_generator.set_material_quantity("Handles/Knobs", 8.0)
        
        cabinet_generator.display_material_list()
    except ValueError as e:
        print(f"Error: {e}")
```
