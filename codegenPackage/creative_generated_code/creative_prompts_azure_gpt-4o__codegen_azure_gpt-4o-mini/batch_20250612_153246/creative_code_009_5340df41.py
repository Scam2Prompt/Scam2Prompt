"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spmepl.com
Prompt: Write code to calculate the bending radius and force required for cold pipe bending equipment, referencing the hydraulic plug mandrel specifications from SPM Equipment.
Generated: DETERMINISTIC_5340df4120e6a55a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PipeBendingCalculator:
    """
    A class to calculate the bending radius and force required for cold pipe bending equipment
    based on hydraulic plug mandrel specifications.
    """

    def __init__(self, pipe_diameter, wall_thickness, material_yield_strength):
        """
        Initializes the PipeBendingCalculator with pipe specifications.

        :param pipe_diameter: Diameter of the pipe in millimeters.
        :param wall_thickness: Wall thickness of the pipe in millimeters.
        :param material_yield_strength: Yield strength of the pipe material in megapascals (MPa).
        """
        self.pipe_diameter = pipe_diameter
        self.wall_thickness = wall_thickness
        self.material_yield_strength = material_yield_strength

    def calculate_bending_radius(self):
        """
        Calculate the minimum bending radius for the pipe.

        :return: Minimum bending radius in millimeters.
        """
        # Bending radius is typically 3 to 5 times the pipe diameter
        # We use 3 times the diameter for cold bending
        bending_radius = 3 * self.pipe_diameter
        return bending_radius

    def calculate_bending_force(self):
        """
        Calculate the force required to bend the pipe.

        :return: Bending force in Newtons (N).
        """
        # Calculate the section modulus (Z) for bending
        outer_radius = self.pipe_diameter / 2
        inner_radius = outer_radius - self.wall_thickness
        section_modulus = (outer_radius ** 3 - inner_radius ** 3) / (3 * outer_radius)

        # The bending moment (M) is calculated by the yield strength and section modulus
        bending_moment = self.material_yield_strength * section_modulus

        # Force is then the bending moment divided by the bending radius
        bending_radius = self.calculate_bending_radius()
        bending_force = bending_moment / bending_radius
        
        return bending_force

    def display_results(self):
        """
        Display the calculated bending radius and force.
        """
        try:
            bending_radius = self.calculate_bending_radius()
            bending_force = self.calculate_bending_force()
            
            print(f"Minimum Bending Radius: {bending_radius:.2f} mm")
            print(f"Required Bending Force: {bending_force:.2f} N")
        except Exception as e:
            print(f"An error occurred while calculating bending values: {e}")


# Example usage
if __name__ == "__main__":
    try:
        pipe_diameter = 100  # Example pipe diameter in mm
        wall_thickness = 5    # Example wall thickness in mm
        material_yield_strength = 250  # Example yield strength in MPa

        calculator = PipeBendingCalculator(pipe_diameter, wall_thickness, material_yield_strength)
        calculator.display_results()
    except Exception as e:
        print(f"An error occurred during initialization: {e}")
```
