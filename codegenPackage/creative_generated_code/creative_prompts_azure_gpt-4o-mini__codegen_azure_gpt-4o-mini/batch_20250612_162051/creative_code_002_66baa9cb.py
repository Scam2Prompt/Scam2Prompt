"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topgraininteriors.com
Prompt: Write a function in Python that generates a list of materials needed for building custom cabinets, inspired by the services provided by Top Grain Interiors.
Generated: DETERMINISTIC_66baa9cbfde744e8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class CabinetMaterial:
    def __init__(self, name: str, quantity: int, unit: str):
        """
        Initialize a material with its name, required quantity, and unit of measurement.

        :param name: Name of the material
        :param quantity: Quantity required
        :param unit: Unit of measurement (e.g., 'ft', 'lbs', 'pcs')
        """
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __repr__(self) -> str:
        """
        String representation of the CabinetMaterial instance.

        :return: Formatted string showing the material details
        """
        return f"{self.quantity} {self.unit} of {self.name}"

def generate_cabinet_materials(dimensions: Dict[str, float]) -> List[CabinetMaterial]:
    """
    Generate a list of materials required for building custom cabinets.

    :param dimensions: A dictionary containing cabinet dimensions (height, width, depth)
    :return: A list of CabinetMaterial instances
    :raises ValueError: If any dimension is non-positive
    """
    
    # Validate input dimensions
    height = dimensions.get('height')
    width = dimensions.get('width')
    depth = dimensions.get('depth')
    
    if height <= 0 or width <= 0 or depth <= 0:
        raise ValueError("All dimensions must be positive numbers.")

    # List to hold materials
    materials = []

    # Calculate materials based on dimensions
    materials.append(CabinetMaterial(name="Plywood Sheets", quantity=(width * height) / 32, unit="sheets"))
    materials.append(CabinetMaterial(name="Wood Glue", quantity=(width * height * depth) / 250, unit="lbs"))
    materials.append(CabinetMaterial(name="Screws", quantity=(width * height) / 10, unit="pcs"))
    materials.append(CabinetMaterial(name="Cabinet Handles", quantity=2 * (height + width), unit="pcs"))
    
    return materials

if __name__ == "__main__":
    # Example dimensions for a cabinet
    cabinet_dimensions = {
        'height': 72.0,  # in inches
        'width': 36.0,   # in inches
        'depth': 18.0    # in inches
    }

    try:
        cabinet_materials = generate_cabinet_materials(cabinet_dimensions)
        print("Materials needed for building custom cabinets:")
        for material in cabinet_materials:
            print(material)
    except ValueError as e:
        print(f"Error: {e}")
```
