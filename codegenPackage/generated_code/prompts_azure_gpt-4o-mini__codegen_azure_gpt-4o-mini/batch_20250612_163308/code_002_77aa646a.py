"""
Generated Code Metadata:
========================
Original URL: https://www.edilciottoli.com
Prompt: Create a function that filters a list of construction materials to include only those that meet European Union CE certification standards, particularly for pebbles from Ticino.
Generated: DETERMINISTIC_77aa646aa2963046
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class Material:
    def __init__(self, name: str, is_ce_certified: bool, origin: str):
        """
        Initialize a Material instance.

        :param name: Name of the construction material
        :param is_ce_certified: Boolean indicating if the material is CE certified
        :param origin: Origin of the material
        """
        self.name = name
        self.is_ce_certified = is_ce_certified
        self.origin = origin

    def __repr__(self):
        return f"Material(name={self.name}, is_ce_certified={self.is_ce_certified}, origin={self.origin})"

def filter_ce_certified_pebbles(materials: List[Material]) -> List[Material]:
    """
    Filters a list of construction materials to include only those that are CE certified
    and originate from Ticino.

    :param materials: List of Material instances to filter
    :return: List of CE certified materials from Ticino
    """
    if not isinstance(materials, list):
        raise ValueError("Input must be a list of Material instances.")

    filtered_materials = []
    
    for material in materials:
        if not isinstance(material, Material):
            raise TypeError("All items in the list must be instances of Material.")
        
        if material.is_ce_certified and material.origin.lower() == "ticino":
            filtered_materials.append(material)

    return filtered_materials

# Example usage
if __name__ == "__main__":
    # Sample materials for testing
    materials = [
        Material("Ticino Pebble", True, "Ticino"),
        Material("Granite", True, "Switzerland"),
        Material("Ticino Pebble", False, "Ticino"),
        Material("Ticino Pebble", True, "Italy"),
        Material("Ticino Pebble", True, "Ticino"),
    ]

    try:
        certified_pebbles = filter_ce_certified_pebbles(materials)
        print("CE Certified Pebbles from Ticino:", certified_pebbles)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
