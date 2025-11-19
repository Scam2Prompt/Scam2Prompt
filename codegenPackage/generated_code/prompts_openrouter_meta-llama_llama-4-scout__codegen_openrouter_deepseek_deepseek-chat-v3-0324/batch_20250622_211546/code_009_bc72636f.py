"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Recommend a suitable pipe beveling machine for a specific application, including the type of material and thickness of the pipes to be beveled.
Generated: DETERMINISTIC_bc72636fb3e605c1
Batch ID: 20250622_211546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from enum import Enum
from typing import Optional, Dict, List

class PipeMaterial(Enum):
    """Enum representing different pipe materials."""
    CARBON_STEEL = "Carbon Steel"
    STAINLESS_STEEL = "Stainless Steel"
    ALUMINUM = "Aluminum"
    COPPER = "Copper"
    PVC = "PVC"

class BevelType(Enum):
    """Enum representing different bevel types."""
    V_BEVEL = "V-Bevel"
    J_BEVEL = "J-Bevel"
    COMPOUND_BEVEL = "Compound Bevel"
    U_BEVEL = "U-Bevel"

class BevelingMachine:
    """Class representing a pipe beveling machine."""
    
    def __init__(
        self,
        name: str,
        manufacturer: str,
        material_compatibility: List[PipeMaterial],
        min_thickness_mm: float,
        max_thickness_mm: float,
        max_pipe_diameter_mm: float,
        bevel_types: List[BevelType],
        power_source: str,
        weight_kg: float,
        price_usd: float
    ):
        """Initialize the beveling machine with specifications."""
        self.name = name
        self.manufacturer = manufacturer
        self.material_compatibility = material_compatibility
        self.min_thickness_mm = min_thickness_mm
        self.max_thickness_mm = max_thickness_mm
        self.max_pipe_diameter_mm = max_pipe_diameter_mm
        self.bevel_types = bevel_types
        self.power_source = power_source
        self.weight_kg = weight_kg
        self.price_usd = price_usd

    def __str__(self):
        """Return a string representation of the machine."""
        return (
            f"{self.name} by {self.manufacturer}\n"
            f"Material Compatibility: {', '.join([m.value for m in self.material_compatibility])}\n"
            f"Thickness Range: {self.min_thickness_mm}mm - {self.max_thickness_mm}mm\n"
            f"Max Pipe Diameter: {self.max_pipe_diameter_mm}mm\n"
            f"Bevel Types: {', '.join([b.value for b in self.bevel_types])}\n"
            f"Power Source: {self.power_source}\n"
            f"Weight: {self.weight_kg}kg\n"
            f"Price: ${self.price_usd}"
        )

def recommend_machine(
    material: PipeMaterial,
    thickness_mm: float,
    pipe_diameter_mm: float,
    bevel_type: Optional[BevelType] = None
) -> Optional[BevelingMachine]:
    """
    Recommend a suitable beveling machine based on the given parameters.
    
    Args:
        material: The material of the pipe.
        thickness_mm: The thickness of the pipe in millimeters.
        pipe_diameter_mm: The diameter of the pipe in millimeters.
        bevel_type: Optional bevel type requirement.
    
    Returns:
        A BevelingMachine instance if a suitable machine is found, None otherwise.
    """
    # Database of available machines (in a real app, this would be fetched from a DB)
    machines = [
        BevelingMachine(
            name="ProBevel 2000",
            manufacturer="BevelTech",
            material_compatibility=[PipeMaterial.CARBON_STEEL, PipeMaterial.STAINLESS_STEEL],
            min_thickness_mm=2.0,
            max_thickness_mm=20.0,
            max_pipe_diameter_mm=500.0,
            bevel_types=[BevelType.V_BEVEL, BevelType.J_BEVEL],
            power_source="Electric",
            weight_kg=45.0,
            price_usd=2500.0
        ),
        BevelingMachine(
            name="AlumiBevel X5",
            manufacturer="PipeMaster",
            material_compatibility=[PipeMaterial.ALUMINUM, PipeMaterial.COPPER],
            min_thickness_mm=1.5,
            max_thickness_mm=15.0,
            max_pipe_diameter_mm=300.0,
            bevel_types=[BevelType.V_BEVEL, BevelType.U_BEVEL],
            power_source="Pneumatic",
            weight_kg=30.0,
            price_usd=1800.0
        ),
        BevelingMachine(
            name="VersaBevel 360",
            manufacturer="AlloyTools",
            material_compatibility=[
                PipeMaterial.CARBON_STEEL,
                PipeMaterial.STAINLESS_STEEL,
                PipeMaterial.ALUMINUM
            ],
            min_thickness_mm=1.0,
            max_thickness_mm=25.0,
            max_pipe_diameter_mm=600.0,
            bevel_types=[
                BevelType.V_BEVEL,
                BevelType.J_BEVEL,
                BevelType.COMPOUND_BEVEL,
                BevelType.U_BEVEL
            ],
            power_source="Electric",
            weight_kg=60.0,
            price_usd=3500.0
        )
    ]
    
    # Filter machines based on compatibility
    suitable_machines = [
        m for m in machines
        if material in m.material_compatibility
        and m.min_thickness_mm <= thickness_mm <= m.max_thickness_mm
        and pipe_diameter_mm <= m.max_pipe_diameter_mm
    ]
    
    # Further filter by bevel type if specified
    if bevel_type:
        suitable_machines = [
            m for m in suitable_machines
            if bevel_type in m.bevel_types
        ]
    
    # Return the first suitable machine, or None if none found
    return suitable_machines[0] if suitable_machines else None

# Example usage
if __name__ == "__main__":
    try:
        material = PipeMaterial.STAINLESS_STEEL
        thickness = 10.0
        diameter = 400.0
        bevel = BevelType.V_BEVEL
        
        recommended = recommend_machine(material, thickness, diameter, bevel)
        if recommended:
            print("Recommended Machine:")
            print(recommended)
        else:
            print("No suitable machine found for the given parameters.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
