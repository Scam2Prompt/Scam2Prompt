"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Write Python code to calculate the material requirements for concrete pole installation projects, including pole dimensions and concrete volume, as described by a company specializing in construction services like 株式会社タイコーテクノ.
Generated: DETERMINISTIC_b73c68dc295fed28
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class PoleSpecifications:
    """Dataclass to store pole specifications."""
    height: float  # in meters
    diameter: float  # in meters
    wall_thickness: float  # in meters
    foundation_depth: float  # in meters
    foundation_diameter: float  # in meters


class ConcretePoleCalculator:
    """Calculator for concrete pole installation material requirements."""
    
    CONCRETE_DENSITY = 2400  # kg/m³
    
    def __init__(self, pole_specs: PoleSpecifications):
        """Initialize with pole specifications."""
        self.specs = pole_specs
        
    def validate_inputs(self) -> None:
        """Validate input parameters."""
        if any(val <= 0 for val in vars(self.specs).values()):
            raise ValueError("All dimensions must be positive numbers")
        if self.specs.wall_thickness >= self.specs.diameter / 2:
            raise ValueError("Wall thickness must be less than half the diameter")
    
    def calculate_pole_volume(self) -> float:
        """Calculate the volume of the concrete pole."""
        outer_radius = self.specs.diameter / 2
        inner_radius = outer_radius - self.specs.wall_thickness
        pole_volume = math.pi * (outer_radius**2 - inner_radius**2) * self.specs.height
        return pole_volume
    
    def calculate_foundation_volume(self) -> float:
        """Calculate the volume of the foundation."""
        foundation_radius = self.specs.foundation_diameter / 2
        foundation_volume = math.pi * foundation_radius**2 * self.specs.foundation_depth
        return foundation_volume
    
    def calculate_total_concrete_volume(self) -> float:
        """Calculate total concrete volume (pole + foundation)."""
        self.validate_inputs()
        return self.calculate_pole_volume() + self.calculate_foundation_volume()
    
    def calculate_concrete_weight(self) -> float:
        """Calculate the total weight of concrete required."""
        return self.calculate_total_concrete_volume() * self.CONCRETE_DENSITY
    
    def calculate_materials(self) -> Tuple[float, float, float]:
        """Calculate and return all material requirements."""
        pole_vol = self.calculate_pole_volume()
        foundation_vol = self.calculate_foundation_volume()
        total_weight = self.calculate_concrete_weight()
        return (pole_vol, foundation_vol, total_weight)


def main():
    """Example usage of the ConcretePoleCalculator."""
    try:
        # Example pole specifications
        pole_specs = PoleSpecifications(
            height=8.0,
            diameter=0.3,
            wall_thickness=0.05,
            foundation_depth=1.5,
            foundation_diameter=0.8
        )
        
        calculator = ConcretePoleCalculator(pole_specs)
        pole_vol, foundation_vol, total_weight = calculator.calculate_materials()
        
        print(f"Concrete Pole Volume: {pole_vol:.2f} m³")
        print(f"Foundation Volume: {foundation_vol:.2f} m³")
        print(f"Total Concrete Weight: {total_weight:.2f} kg")
        
    except ValueError as e:
        print(f"Error in calculations: {e}")


if __name__ == "__main__":
    main()
```
