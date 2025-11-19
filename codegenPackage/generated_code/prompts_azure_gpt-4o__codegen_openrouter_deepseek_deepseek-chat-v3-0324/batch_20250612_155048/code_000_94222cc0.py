"""
Generated Code Metadata:
========================
Original URL: https://cm-canada.ca
Prompt: Write Python code to calculate the load capacity of anchors based on specifications provided by Apeanchor™ products from CM-Canada's construction materials catalog.
Generated: DETERMINISTIC_94222cc063203834
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Apeanchor™ Load Capacity Calculator

This script calculates the load capacity of Apeanchor™ products based on specifications
from CM-Canada's construction materials catalog. It supports various anchor types and
materials, with validation for input parameters.

Error handling is included for invalid inputs and edge cases.
"""

from enum import Enum
from typing import Optional, Union

class AnchorType(Enum):
    """Enumeration of supported Apeanchor™ product types."""
    WEDGE = "Wedge"
    SLEEVE = "Sleeve"
    DROP_IN = "Drop-in"
    CONCRETE_SCREW = "Concrete Screw"

class Material(Enum):
    """Enumeration of supported anchor materials."""
    CARBON_STEEL = "Carbon Steel"
    STAINLESS_STEEL = "Stainless Steel"
    ZINC_PLATED = "Zinc Plated"

class LoadDirection(Enum):
    """Enumeration of load direction types."""
    TENSION = "Tension"
    SHEAR = "Shear"

# Material strength properties (MPa)
MATERIAL_PROPERTIES = {
    Material.CARBON_STEEL: {"tensile_strength": 400, "shear_strength": 240},
    Material.STAINLESS_STEEL: {"tensile_strength": 500, "shear_strength": 300},
    Material.ZINC_PLATED: {"tensile_strength": 350, "shear_strength": 210},
}

# Anchor type coefficients
ANCHOR_COEFFICIENTS = {
    AnchorType.WEDGE: {"tension": 1.2, "shear": 1.0},
    AnchorType.SLEEVE: {"tension": 1.0, "shear": 1.1},
    AnchorType.DROP_IN: {"tension": 0.9, "shear": 0.8},
    AnchorType.CONCRETE_SCREW: {"tension": 1.3, "shear": 1.2},
}

def calculate_load_capacity(
    anchor_type: AnchorType,
    material: Material,
    diameter: float,
    embedment_depth: float,
    load_direction: LoadDirection,
    concrete_strength: Optional[float] = 25.0,
    safety_factor: float = 4.0
) -> Union[float, str]:
    """
    Calculate the load capacity of an Apeanchor™ product.

    Args:
        anchor_type: Type of anchor (Wedge, Sleeve, etc.)
        material: Material of the anchor
        diameter: Diameter of the anchor in mm
        embedment_depth: Embedment depth in mm
        load_direction: Tension or Shear load
        concrete_strength: Concrete compressive strength in MPa (default: 25.0)
        safety_factor: Safety factor (default: 4.0)

    Returns:
        Load capacity in kN or error message if validation fails
    """
    try:
        # Input validation
        if diameter <= 0:
            return "Diameter must be positive"
        if embedment_depth <= 0:
            return "Embedment depth must be positive"
        if concrete_strength <= 0:
            return "Concrete strength must be positive"
        if safety_factor <= 0:
            return "Safety factor must be positive"

        # Get material properties
        material_props = MATERIAL_PROPERTIES.get(material)
        if not material_props:
            return "Invalid material specified"

        # Get anchor coefficients
        anchor_coeffs = ANCHOR_COEFFICIENTS.get(anchor_type)
        if not anchor_coeffs:
            return "Invalid anchor type specified"

        # Calculate base capacity based on material strength
        if load_direction == LoadDirection.TENSION:
            strength = material_props["tensile_strength"]
            coefficient = anchor_coeffs["tension"]
        else:
            strength = material_props["shear_strength"]
            coefficient = anchor_coeffs["shear"]

        # Cross-sectional area in mm²
        area = 3.14159 * (diameter / 2) ** 2

        # Base capacity calculation (N)
        base_capacity = strength * area * coefficient

        # Concrete strength adjustment
        concrete_factor = min(1.0, (concrete_strength / 25.0) ** 0.5)

        # Embedment depth adjustment
        embedment_factor = min(1.0, embedment_depth / (5 * diameter))

        # Final capacity calculation (kN)
        capacity = (base_capacity * concrete_factor * embedment_factor) / (safety_factor * 1000)

        return round(capacity, 2)

    except Exception as e:
        return f"Error in calculation: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Example calculation
    capacity = calculate_load_capacity(
        anchor_type=AnchorType.WEDGE,
        material=Material.CARBON_STEEL,
        diameter=10.0,
        embedment_depth=50.0,
        load_direction=LoadDirection.TENSION,
        concrete_strength=30.0,
        safety_factor=4.0
    )
    print(f"Calculated load capacity: {capacity} kN")
```
