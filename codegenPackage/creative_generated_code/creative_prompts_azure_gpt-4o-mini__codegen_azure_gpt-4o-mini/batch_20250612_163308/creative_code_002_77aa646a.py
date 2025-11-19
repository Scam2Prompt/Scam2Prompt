"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.edilciottoli.com
Prompt: Create a function that filters a list of construction materials to include only those that meet European Union CE certification standards, particularly for pebbles from Ticino.
Generated: DETERMINISTIC_77aa646aa2963046
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class Material:
    def __init__(self, name: str, is_ce_certified: bool, origin: str):
        """
        Initialize a Material instance.
        
        :param name: Name of the construction material
        :param is_ce_certified: Boolean indicating CE certification status
        :param origin: Geographic origin of the material
        """
        self.name = name
        self.is_ce_certified = is_ce_certified
        self.origin = origin

    def __repr__(self):
        return f"Material(name={self.name}, is_ce_certified={self.is_ce_certified}, origin={self.origin})"


def filter_ce_certified_pebbles(materials: List[Material]) -> List[Material]:
    """
    Filters a list of materials to include only those that are CE certified 
    and specifically pebbles from Ticino.
    
    :param materials: A list of Material instances to filter
    :return: A list of Material instances that are CE certified pebbles from Ticino
    """
    if not isinstance(materials, list):
        raise ValueError("Input must be a list of Material instances.")
    
    filtered_materials = [
        material for material in materials 
        if material.is_ce_certified and material.origin.lower() == "ticino"
    ]
    
    return filtered_materials


# Example usage:
if __name__ == "__main__":
    # Sample list of construction materials
    materials_list = [
        Material(name="Ticino Pebbles", is_ce_certified=True, origin="Ticino"),
        Material(name="Granite", is_ce_certified=True, origin="Italy"),
        Material(name="Ticino Pebbles", is_ce_certified=False, origin="Ticino"),
        Material(name="River Stones", is_ce_certified=True, origin="Ticino"),
    ]

    # Filter materials
    try:
        ce_certified_pebbles = filter_ce_certified_pebbles(materials_list)
        print("CE Certified Pebbles from Ticino:")
        for pebble in ce_certified_pebbles:
            print(pebble)
    except ValueError as e:
        print(f"Error: {e}")
```
