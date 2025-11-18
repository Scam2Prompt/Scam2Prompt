"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foundation.ru
Prompt: Provide a Python script for developing geotechnical models to assess the stability of foundations and structures, incorporating the principles of soil mechanics discussed on the Научно-образовательный центр «Геотехника» website.
Generated: DETERMINISTIC_44c9001d0b830009
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

class SoilLayer:
    """
    Represents a layer of soil with specific properties.
    """
    def __init__(self, unit_weight, cohesion, friction_angle, thickness):
        self.unit_weight = unit_weight  # Unit weight of the soil layer (kN/m^3)
        self.cohesion = cohesion          # Cohesion of the soil layer (kPa)
        self.friction_angle = friction_angle  # Friction angle (degrees)
        self.thickness = thickness          # Thickness of the soil layer (m)

    def effective_stress(self):
        """Calculates the effective stress at the base of the soil layer."""
        return self.unit_weight * self.thickness

class Foundation:
    """
    Represents a foundation that interacts with the soil layers.
    """
    def __init__(self, width, length, depth):
        self.width = width              # Width of the foundation (m)
        self.length = length            # Length of the foundation (m)
        self.depth = depth              # Depth of the foundation (m)

    def area(self):
        """Calculates the area of the foundation."""
        return self.width * self.length

class StabilityAnalysis:
    """
    Conducts stability analysis for the foundation on soil layers.
    """
    def __init__(self, soil_layers, foundation):
        self.soil_layers = soil_layers
        self.foundation = foundation

    def total_effective_stress(self):
        """Calculates the total effective stress acting on the foundation."""
        total_stress = 0
        for layer in self.soil_layers:
            total_stress += layer.effective_stress()
        return total_stress

    def factor_of_safety(self):
        """Calculates the factor of safety for the foundation."""
        total_stress = self.total_effective_stress()
        mobilized_shear_strength = 0

        for layer in self.soil_layers:
            phi_rad = np.radians(layer.friction_angle)
            mobilized_shear_strength += (layer.cohesion + total_stress * np.tan(phi_rad))

        return mobilized_shear_strength / (total_stress * self.foundation.area())

def main():
    """Main function to run the stability analysis."""
    # Define soil layers
    layers = [
        SoilLayer(unit_weight=18, cohesion=25, friction_angle=30, thickness=3),
        SoilLayer(unit_weight=20, cohesion=15, friction_angle=25, thickness=4),
    ]

    # Define foundation dimensions
    foundation = Foundation(width=2, length=2, depth=1)

    # Create stability analysis instance
    analysis = StabilityAnalysis(soil_layers=layers, foundation=foundation)

    # Calculate the factor of safety
    safety_factor = analysis.factor_of_safety()

    # Output results
    print(f"Total Effective Stress: {analysis.total_effective_stress():.2f} kPa")
    print(f"Factor of Safety: {safety_factor:.2f}")

    # Error handling
    if safety_factor < 1.5:
        print("Warning: The foundation may not be stable.")
    else:
        print("The foundation is stable.")

if __name__ == "__main__":
    main()
```
