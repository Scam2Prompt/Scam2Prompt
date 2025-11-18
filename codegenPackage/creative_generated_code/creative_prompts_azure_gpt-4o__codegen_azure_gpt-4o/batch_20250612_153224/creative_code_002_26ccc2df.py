"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karenfixing.com
Prompt: Generate code to model the structural behavior of "قلاب فوقانی سرامیک تک" in a 3D CAD software, using the technical details provided by Karen Fixing.
Generated: DETERMINISTIC_26ccc2dfea354567
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class CeramicHook:
    """
    Class to model the structural behavior of a ceramic upper hook in a 3D CAD software.
    This uses the technical details provided by Karen Fixing.
    """

    def __init__(self, width, height, depth, material_properties):
        """
        Initialize the hook object with its dimensions and material properties.

        :param width: Width of the hook (mm)
        :param height: Height of the hook (mm)
        :param depth: Depth of the hook (mm)
        :param material_properties: Dictionary containing material properties such as density and tensile strength
        """
        self.width = width
        self.height = height
        self.depth = depth
        self.material_properties = material_properties
        self.validate_properties()

    def validate_properties(self):
        """
        Validate dimensions and material properties for correctness.
        Raises ValueError if any property is invalid.
        """
        if self.width <= 0 or self.height <= 0 or self.depth <= 0:
            raise ValueError("Dimensions must be positive numbers.")
        if not all(key in self.material_properties for key in ["density", "tensile_strength"]):
            raise ValueError("Material properties must include 'density' and 'tensile_strength'.")
        if self.material_properties["density"] <= 0 or self.material_properties["tensile_strength"] <= 0:
            raise ValueError("Material properties must be positive values.")

    def calculate_volume(self):
        """
        Calculate the volume of the hook based on its dimensions.

        :return: Volume in cubic millimeters
        """
        return self.width * self.height * self.depth

    def calculate_weight(self):
        """
        Calculate the weight of the hook based on its volume and material density.

        :return: Weight in grams
        """
        volume_mm3 = self.calculate_volume()
        density_g_per_mm3 = self.material_properties["density"] / 1000
        return volume_mm3 * density_g_per_mm3

    def stress_analysis(self, applied_force):
        """
        Calculate the stress experienced by the hook given an applied force.

        :param applied_force: Force applied to the hook (N)
        :return: Stress in MPa
        """
        # Assume the cross-sectional area is width * depth (simplified model)
        cross_section_area_mm2 = self.width * self.depth
        cross_section_area_m2 = cross_section_area_mm2 / 1e6  # Convert mm² to m²
        stress_mpa = applied_force / cross_section_area_m2 / 1e6  # Convert to MPa
        return stress_mpa

    def is_safe(self, applied_force):
        """
        Determine if the hook is safe under a given applied force.

        :param applied_force: Force applied to the hook (N)
        :return: True if the hook is safe, False otherwise
        """
        stress_mpa = self.stress_analysis(applied_force)
        return stress_mpa <= self.material_properties["tensile_strength"]

# Example usage
if __name__ == "__main__":
    try:
        # Define dimensions and material properties
        hook_dimensions = {"width": 50, "height": 100, "depth": 20}  # in mm
        material_props = {"density": 2.4, "tensile_strength": 50}  # density in g/cm³, tensile strength in MPa

        # Create CeramicHook object
        ceramic_hook = CeramicHook(
            width=hook_dimensions["width"],
            height=hook_dimensions["height"],
            depth=hook_dimensions["depth"],
            material_properties=material_props
        )

        # Calculate volume and weight
        print(f"Volume: {ceramic_hook.calculate_volume()} mm³")
        print(f"Weight: {ceramic_hook.calculate_weight():.2f} g")

        # Perform stress analysis
        applied_force = 2000  # Force in Newtons
        stress = ceramic_hook.stress_analysis(applied_force)
        print(f"Stress under applied force: {stress:.2f} MPa")

        # Check if hook is safe
        if ceramic_hook.is_safe(applied_force):
            print("The hook is structurally safe under the applied force.")
        else:
            print("Warning: The hook may fail under the applied force.")

    except ValueError as e:
        print(f"Error: {e}")
```
