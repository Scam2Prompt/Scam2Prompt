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
# materials_calculator.py

from enum import Enum
from typing import List, Dict

class CabinetType(str, Enum):
    """Enum for different cabinet types."""
    STANDARD = "standard"
    CUSTOM = "custom"
    PANTRY = "pantry"

class Material(str, Enum):
    """Enum for different materials."""
    PLYWOOD = "plywood"
    MDF = "mdf"
    SOLID_WOOD = "solid_wood"
    PAINT = "paint"
    VARNISH = "varnish"
    HARDWARE = "hardware"

def calculate_materials(cabinet_type: CabinetType, 
                         width: float, 
                         height: float, 
                         depth: float, 
                         shelves: int) -> Dict[Material, float]:
    """
    Calculate materials needed for a custom cabinet.

    Args:
    - cabinet_type (CabinetType): Type of cabinet.
    - width (float): Width of the cabinet in inches.
    - height (float): Height of the cabinet in inches.
    - depth (float): Depth of the cabinet in inches.
    - shelves (int): Number of shelves.

    Returns:
    - Dict[Material, float]: Dictionary of materials and their quantities.
    """

    # Define base materials and quantities for each cabinet type
    base_materials = {
        CabinetType.STANDARD: {Material.PLYWOOD: 0, Material.HARDWARE: 0},
        CabinetType.CUSTOM: {Material.SOLID_WOOD: 0, Material.HARDWARE: 0},
        CabinetType.PANTRY: {Material.MDF: 0, Material.PAINT: 0, Material.VARNISH: 0, Material.HARDWARE: 0}
    }

    # Calculate surface area of the cabinet
    surface_area = 2 * ((width * height) + (width * depth) + (height * depth))

    # Calculate material quantities based on surface area and cabinet type
    materials = base_materials[cabinet_type].copy()
    if cabinet_type == CabinetType.STANDARD:
        materials[Material.PLYWOOD] = surface_area * 0.5  # assume 0.5 sqft of plywood per sqft of surface area
        materials[Material.HARDWARE] = 10  # assume 10 hardware pieces per cabinet
    elif cabinet_type == CabinetType.CUSTOM:
        materials[Material.SOLID_WOOD] = surface_area * 0.75  # assume 0.75 sqft of solid wood per sqft of surface area
        materials[Material.HARDWARE] = 15  # assume 15 hardware pieces per cabinet
    elif cabinet_type == CabinetType.PANTRY:
        materials[Material.MDF] = surface_area * 0.25  # assume 0.25 sqft of MDF per sqft of surface area
        materials[Material.PAINT] = surface_area * 0.1  # assume 0.1 sqft of paint per sqft of surface area
        materials[Material.VARNISH] = surface_area * 0.05  # assume 0.05 sqft of varnish per sqft of surface area
        materials[Material.HARDWARE] = 12  # assume 12 hardware pieces per cabinet

    # Add shelves
    materials[Material.PLYWOOD] += shelves * (width * depth * 0.25)  # assume 0.25 sqft of plywood per shelf
    materials[Material.MDF] += shelves * (width * depth * 0.1)  # assume 0.1 sqft of MDF per shelf

    return materials

def generate_materials_list(cabinets: List[Dict]) -> List[Dict]:
    """
    Generate a list of materials needed for multiple cabinets.

    Args:
    - cabinets (List[Dict]): List of cabinet specifications.

    Returns:
    - List[Dict]: List of materials and their quantities.
    """
    materials_list = []
    for cabinet in cabinets:
        try:
            cabinet_type = CabinetType(cabinet["type"])
            width = float(cabinet["width"])
            height = float(cabinet["height"])
            depth = float(cabinet["depth"])
            shelves = int(cabinet["shelves"])

            materials = calculate_materials(cabinet_type, width, height, depth, shelves)
            materials_list.append(materials)
        except (KeyError, ValueError) as e:
            print(f"Error processing cabinet: {e}")

    return materials_list

# Example usage:
if __name__ == "__main__":
    cabinets = [
        {"type": "standard", "width": 30, "height": 40, "depth": 20, "shelves": 2},
        {"type": "custom", "width": 36, "height": 48, "depth": 24, "shelves": 3},
        {"type": "pantry", "width": 24, "height": 60, "depth": 18, "shelves": 4}
    ]

    materials_list = generate_materials_list(cabinets)
    for i, materials in enumerate(materials_list):
        print(f"Cabinet {i+1} materials:")
        for material, quantity in materials.items():
            print(f"- {material}: {quantity}")
```
