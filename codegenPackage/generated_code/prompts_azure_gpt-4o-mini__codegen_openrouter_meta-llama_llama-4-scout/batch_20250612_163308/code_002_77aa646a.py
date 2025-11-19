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

class ConstructionMaterial:
    """Represents a construction material."""
    
    def __init__(self, name: str, origin: str, ce_certified: bool):
        """
        Initializes a ConstructionMaterial instance.

        Args:
        - name (str): The name of the material.
        - origin (str): The origin of the material.
        - ce_certified (bool): Whether the material is CE certified.
        """
        self.name = name
        self.origin = origin
        self.ce_certified = ce_certified

def filter_ce_certified_materials(materials: List[ConstructionMaterial], origin: str = "Ticino") -> List[ConstructionMaterial]:
    """
    Filters a list of construction materials to include only those that meet European Union CE certification standards.

    Args:
    - materials (List[ConstructionMaterial]): The list of materials to filter.
    - origin (str): The origin of the materials to filter by. Defaults to "Ticino".

    Returns:
    - List[ConstructionMaterial]: The filtered list of materials.
    """
    try:
        # Check if materials is a list
        if not isinstance(materials, list):
            raise TypeError("Materials must be a list")

        # Filter materials by CE certification and origin
        filtered_materials = [material for material in materials if material.ce_certified and material.origin == origin]
        
        return filtered_materials
    
    except TypeError as e:
        print(f"TypeError: {e}")
        return []
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
if __name__ == "__main__":
    materials = [
        ConstructionMaterial("Pebble 1", "Ticino", True),
        ConstructionMaterial("Pebble 2", "Ticino", False),
        ConstructionMaterial("Pebble 3", "Switzerland", True),
        ConstructionMaterial("Pebble 4", "Ticino", True),
    ]

    filtered_materials = filter_ce_certified_materials(materials)

    print("Filtered Materials:")
    for material in filtered_materials:
        print(f"Name: {material.name}, Origin: {material.origin}, CE Certified: {material.ce_certified}")
```
