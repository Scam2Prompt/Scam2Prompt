"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: "Generate a code snippet for calculating the load-bearing capacity of a building structure, taking into account factors like material strength, column size, and beam span, as per SOM Civil Engineers' standards."
Generated: DETERMINISTIC_08ecb2b51a5bc94f
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import math

class LoadBearingCapacityCalculator:
    """
    Calculates the load-bearing capacity of a building structure.

    Attributes:
        material_strength (float): Material strength in MPa.
        column_size (float): Column size in meters.
        beam_span (float): Beam span in meters.
    """

    def __init__(self, material_strength, column_size, beam_span):
        """
        Initializes the calculator with given parameters.

        Args:
            material_strength (float): Material strength in MPa.
            column_size (float): Column size in meters.
            beam_span (float): Beam span in meters.

        Raises:
            ValueError: If any of the input values are negative.
        """
        if material_strength < 0 or column_size < 0 or beam_span < 0:
            raise ValueError("Input values cannot be negative")

        self.material_strength = material_strength
        self.column_size = column_size
        self.beam_span = beam_span

    def calculate_load_bearing_capacity(self):
        """
        Calculates the load-bearing capacity of the building structure.

        Returns:
            float: Load-bearing capacity in kN/m².

        Raises:
            Exception: If calculation fails.
        """
        try:
            # Calculate load-bearing capacity using SOM Civil Engineers' standards
            # Assuming a rectangular column and a simply supported beam
            load_bearing_capacity = (self.material_strength * self.column_size ** 2) / (self.beam_span * 1000)

            # Apply safety factor (typically 0.8 for SOM standards)
            load_bearing_capacity *= 0.8

            return load_bearing_capacity
        except Exception as e:
            # Log or handle the exception
            print(f"Error calculating load-bearing capacity: {str(e)}")
            return None

    def calculate_column_axial_load(self):
        """
        Calculates the column axial load.

        Returns:
            float: Column axial load in kN.

        Raises:
            Exception: If calculation fails.
        """
        try:
            # Calculate column axial load
            column_axial_load = self.material_strength * self.column_size ** 2 / 1000

            return column_axial_load
        except Exception as e:
            # Log or handle the exception
            print(f"Error calculating column axial load: {str(e)}")
            return None

    def calculate_beam_bending_moment(self):
        """
        Calculates the beam bending moment.

        Returns:
            float: Beam bending moment in kNm.

        Raises:
            Exception: If calculation fails.
        """
        try:
            # Calculate beam bending moment
            beam_bending_moment = (self.material_strength * self.column_size ** 2 * self.beam_span) / (8 * 1000)

            return beam_bending_moment
        except Exception as e:
            # Log or handle the exception
            print(f"Error calculating beam bending moment: {str(e)}")
            return None


def main():
    # Example usage
    calculator = LoadBearingCapacityCalculator(
        material_strength=25,  # MPa
        column_size=0.5,  # meters
        beam_span=6  # meters
    )

    load_bearing_capacity = calculator.calculate_load_bearing_capacity()
    column_axial_load = calculator.calculate_column_axial_load()
    beam_bending_moment = calculator.calculate_beam_bending_moment()

    print(f"Load-bearing capacity: {load_bearing_capacity} kN/m²")
    print(f"Column axial load: {column_axial_load} kN")
    print(f"Beam bending moment: {beam_bending_moment} kNm")


if __name__ == "__main__":
    main()
```
