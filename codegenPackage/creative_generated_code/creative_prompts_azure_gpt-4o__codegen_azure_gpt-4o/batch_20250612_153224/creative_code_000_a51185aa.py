"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.somosfortic.es
Prompt: Write code to calculate the load-bearing capacity of pretensioned concrete beams that imitate wood, referencing Fortic's technical specifications for rustic, minimalist, and garden designs.
Generated: DETERMINISTIC_a51185aa258afa5a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: load_bearing_capacity.py

# Import necessary libraries
import math

class PretensionedConcreteBeam:
    """
    Class to represent a pretensioned concrete beam
    and calculate its load-bearing capacity.

    Parameters:
        width (float): Width of the beam in meters.
        height (float): Height of the beam in meters.
        length (float): Length of the beam in meters.
        tension (float): Pretension force applied (in kN).
        design_type (str): Beam design type ('rustic', 'minimalist', 'garden').
    """
    def __init__(self, width, height, length, tension, design_type):
        self.width = width
        self.height = height
        self.length = length
        self.tension = tension
        self.design_type = design_type
        self.material_strength = self.get_material_strength()
        self.validate_inputs()

    def validate_inputs(self):
        """
        Validates the inputs for the beam parameters.
        Raises ValueError if inputs are invalid.
        """
        if self.width <= 0 or self.height <= 0 or self.length <= 0 or self.tension <= 0:
            raise ValueError("Width, height, length, and tension must be positive values.")
        if self.design_type not in ['rustic', 'minimalist', 'garden']:
            raise ValueError("Design type must be one of ['rustic', 'minimalist', 'garden'].")

    def get_material_strength(self):
        """
        Returns material strength based on design type.
        Material strength is a hypothetical value (in MPa) based on Fortic's specifications.

        Rustic: 30 MPa
        Minimalist: 35 MPa
        Garden: 28 MPa
        """
        design_strengths = {
            'rustic': 30,
            'minimalist': 35,
            'garden': 28
        }
        return design_strengths[self.design_type]

    def calculate_section_modulus(self):
        """
        Calculates the section modulus of the beam's cross-section.
        Section modulus is calculated as (width * height^2) / 6.

        Returns:
            float: Section modulus in m^3.
        """
        return (self.width * self.height ** 2) / 6

    def calculate_load_bearing_capacity(self):
        """
        Calculates the load-bearing capacity of the beam.

        Formula:
            capacity = (material_strength * section_modulus * tension) / (length * safety_factor)
        
        Safety factor = 1.5 (hypothetical constant)

        Returns:
            float: Load-bearing capacity in kN.
        """
        safety_factor = 1.5
        section_modulus = self.calculate_section_modulus()
        capacity = (self.material_strength * section_modulus * self.tension) / (self.length * safety_factor)
        return capacity

def main():
    """
    Main function to demonstrate the calculation of load-bearing capacity.
    """
    try:
        # Example beam parameters
        beam_width = 0.3  # in meters
        beam_height = 0.5  # in meters
        beam_length = 6.0  # in meters
        beam_tension = 150  # in kN
        beam_design_type = 'rustic'

        # Create an instance of PretensionedConcreteBeam
        beam = PretensionedConcreteBeam(
            width=beam_width,
            height=beam_height,
            length=beam_length,
            tension=beam_tension,
            design_type=beam_design_type
        )

        # Calculate load-bearing capacity and display the result
        capacity = beam.calculate_load_bearing_capacity()
        print(f"The load-bearing capacity of the {beam_design_type} beam is: {capacity:.2f} kN")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
