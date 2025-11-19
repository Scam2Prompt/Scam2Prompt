"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: "Design a workbench with 5 drawers and a 1.5-meter length, using DKP Sac material and electrostatically powder-coated, provide technical specifications."
Generated: DETERMINISTIC_6a738d8877058b2f
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List

class Material(Enum):
    """Enum for different materials."""
    DKP_SAC = "DKP Sac"

class Finish(Enum):
    """Enum for different finishes."""
    ELECTROSTATIC_POWDER_COATED = "Electrostatically Powder-Coated"

@dataclass
class Drawer:
    """Class to represent a drawer."""
    width: float
    height: float
    depth: float

@dataclass
class Workbench:
    """Class to represent a workbench."""
    length: float
    material: Material
    finish: Finish
    drawers: List[Drawer]

    def __post_init__(self):
        """Validate workbench properties."""
        if self.length <= 0:
            raise ValueError("Length must be greater than zero.")
        if not self.drawers:
            raise ValueError("At least one drawer is required.")

    def get_technical_specifications(self):
        """Generate technical specifications for the workbench."""
        specs = f"Workbench Length: {self.length} meters\n"
        specs += f"Material: {self.material.value}\n"
        specs += f"Finish: {self.finish.value}\n"
        specs += "Drawers:\n"
        for i, drawer in enumerate(self.drawers):
            specs += f"  Drawer {i+1}: {drawer.width} x {drawer.height} x {drawer.depth} meters\n"
        return specs

def create_workbench(length: float, material: Material, finish: Finish, num_drawers: int) -> Workbench:
    """Create a workbench with specified properties."""
    try:
        drawers = [Drawer(0.5, 0.2, 0.6) for _ in range(num_drawers)]
        workbench = Workbench(length, material, finish, drawers)
        return workbench
    except Exception as e:
        print(f"Error creating workbench: {str(e)}")
        return None

def main():
    workbench = create_workbench(1.5, Material.DKP_SAC, Finish.ELECTROSTATIC_POWDER_COATED, 5)
    if workbench:
        print(workbench.get_technical_specifications())

if __name__ == "__main__":
    main()
```
