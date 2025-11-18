"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eedsjcgt.com
Prompt: Create a program to calculate the load-bearing capacity of "球墨铸铁管" (ductile iron pipes) for underground applications, referencing the specifications listed on the website.
Generated: DETERMINISTIC_f39c9fea25427527
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python implementation for calculating the load-bearing capacity of ductile iron pipes. The program assumes the specifications are provided as input (e.g., diameter, wall thickness, depth of burial, etc.).

```python
import math

class DuctileIronPipeCalculator:
    """
    A class to calculate the load-bearing capacity of ductile iron pipes for underground applications.
    """

    def __init__(self, diameter, wall_thickness, burial_depth, soil_density, pipe_strength):
        """
        Initialize the calculator with required parameters.

        :param diameter: Outer diameter of the pipe (in meters).
        :param wall_thickness: Wall thickness of the pipe (in meters).
        :param burial_depth: Depth of burial from the surface to the top of the pipe (in meters).
        :param soil_density: Density of the surrounding soil (in kg/m^3).
        :param pipe_strength: Yield strength of the ductile iron pipe material (in Pascals).
        """
        self.diameter = diameter
        self.wall_thickness = wall_thickness
        self.burial_depth = burial_depth
        self.soil_density = soil_density
        self.pipe_strength = pipe_strength

    def calculate_vertical_load(self):
        """
        Calculate the vertical load on the pipe due to the weight of the soil above it.

        :return: Vertical load (in Pascals).
        """
        # Calculate the total volume of soil above the pipe per unit area.
        vertical_load = self.soil_density * 9.81 * self.burial_depth  # Force due to gravity
        return vertical_load

    def calculate_pipe_resistance(self):
        """
        Calculate the pipe's resistance to vertical load based on its geometry and material properties.

        :return: Pipe resistance (in Pascals).
        """
        # Approximate moment of inertia of the pipe's cross-section
        inner_diameter = self.diameter - 2 * self.wall_thickness
        cross_section_area = math.pi * (self.diameter**2 - inner_diameter**2) / 4

        # Pipe's resistance based on yield strength and cross-sectional area
        pipe_resistance = cross_section_area * self.pipe_strength
        return pipe_resistance

    def check_load_capacity(self):
        """
        Check if the pipe can safely bear the vertical load applied by the soil.

        :return: A tuple (safe, vertical_load, pipe_resistance)
                 - safe: Bool indicating whether the pipe is safe.
                 - vertical_load: Calculated vertical load (in Pascals).
                 - pipe_resistance: Calculated pipe resistance (in Pascals).
        """
        vertical_load = self.calculate_vertical_load()
        pipe_resistance = self.calculate_pipe_resistance()

        # Check safety condition
        safe = pipe_resistance > vertical_load
        return safe, vertical_load, pipe_resistance


def main():
    """
    Main function to execute the calculator.
    """
    try:
        # Gather user inputs (for production, these could be sourced from a web API, database, etc.)
        print("Enter ductile iron pipe specifications:")
        diameter = float(input(" - Outer diameter of the pipe (meters): "))
        wall_thickness = float(input(" - Wall thickness of the pipe (meters): "))
        burial_depth = float(input(" - Depth of burial from the surface (meters): "))
        soil_density = float(input(" - Density of surrounding soil (kg/m^3): "))
        pipe_strength = float(input(" - Yield strength of the pipe material (Pascals): "))

        # Create an instance of the calculator
        calculator = DuctileIronPipeCalculator(diameter, wall_thickness, burial_depth, soil_density, pipe_strength)

        # Perform the calculation
        safe, vertical_load, pipe_resistance = calculator.check_load_capacity()

        # Display results
        print("\nCalculation Results:")
        print(f" - Vertical load on pipe: {vertical_load:.2f} Pascals")
        print(f" - Pipe load-bearing resistance: {pipe_resistance:.2f} Pascals")
        if safe:
            print(" - Status: The pipe is safe under the given conditions.")
        else:
            print(" - Status: WARNING! The pipe is not safe under the given conditions.")
    except ValueError as e:
        print(f"Error: Invalid input. Please enter numeric values. ({e})")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
