"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eedsjcgt.com
Prompt: Write Python code to calculate the stress tolerance of seamless steel pipes based on their diameter and wall thickness, referencing specifications for "无缝钢管" from the website.
Generated: DETERMINISTIC_6a55a05c8490441e
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class SeamlessSteelPipeStressCalculator:
    """
    A class to calculate the stress tolerance of seamless steel pipes based on diameter and wall thickness.
    """

    def __init__(self, diameter_mm: float, wall_thickness_mm: float, material_strength_mpa: float):
        """
        Initialize the calculator with pipe dimensions and material strength.

        :param diameter_mm: External diameter of the pipe in millimeters (mm).
        :param wall_thickness_mm: Wall thickness of the pipe in millimeters (mm).
        :param material_strength_mpa: Material strength in megapascals (MPa).
        """
        self.diameter_mm = diameter_mm
        self.wall_thickness_mm = wall_thickness_mm
        self.material_strength_mpa = material_strength_mpa

        # Validate input parameters
        self._validate_inputs()

    def _validate_inputs(self):
        """
        Validate the input parameters to ensure they are physically meaningful values.
        """
        if self.diameter_mm <= 0:
            raise ValueError("Diameter must be a positive value.")
        if self.wall_thickness_mm <= 0:
            raise ValueError("Wall thickness must be a positive value.")
        if self.wall_thickness_mm >= (self.diameter_mm / 2):
            raise ValueError("Wall thickness must be less than half of the diameter.")
        if self.material_strength_mpa <= 0:
            raise ValueError("Material strength must be a positive value.")

    def calculate_stress_tolerance(self) -> float:
        """
        Calculate the stress tolerance of the pipe based on its dimensions and material strength.

        The calculation uses the formula for hoop stress in a thin-walled pressure vessel:
        stress_tolerance = (material_strength * wall_thickness) / diameter

        :return: Stress tolerance in megapascals (MPa).
        """
        # Calculate stress tolerance
        stress_tolerance = (self.material_strength_mpa * self.wall_thickness_mm) / self.diameter_mm
        return stress_tolerance

if __name__ == "__main__":
    # Example usage:
    try:
        # Input parameters (user could specify these dynamically)
        diameter = 100.0  # in mm
        wall_thickness = 10.0  # in mm
        material_strength = 400.0  # in MPa

        # Create a calculator instance
        calculator = SeamlessSteelPipeStressCalculator(diameter, wall_thickness, material_strength)

        # Calculate stress tolerance
        stress_tolerance = calculator.calculate_stress_tolerance()

        # Output the result
        print(f"Stress tolerance of the pipe: {stress_tolerance:.2f} MPa")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
