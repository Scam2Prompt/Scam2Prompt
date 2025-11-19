"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Generate code to calculate the optimal drilling angle and depth for a geotechnical survey, referencing the types of drilling work described by URANPRES.
Generated: DETERMINISTIC_eb77f7904744fa40
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class DrillingParameters:
    """
    Class to hold drilling parameters.
    """

    def __init__(self, rock_type, hole_diameter, hole_depth, water_table_depth):
        """
        Initialize drilling parameters.

        Args:
            rock_type (str): Type of rock (e.g., 'soil', 'sedimentary', 'igneous', 'metamorphic').
            hole_diameter (float): Diameter of the hole in meters.
            hole_depth (float): Desired depth of the hole in meters.
            water_table_depth (float): Depth to the water table in meters.
        """
        self.rock_type = rock_type
        self.hole_diameter = hole_diameter
        self.hole_depth = hole_depth
        self.water_table_depth = water_table_depth


class DrillingAngleCalculator:
    """
    Class to calculate optimal drilling angle.
    """

    def __init__(self, drilling_parameters):
        """
        Initialize drilling angle calculator.

        Args:
            drilling_parameters (DrillingParameters): Drilling parameters.
        """
        self.drilling_parameters = drilling_parameters

    def calculate_optimal_angle(self):
        """
        Calculate optimal drilling angle based on rock type.

        Returns:
            float: Optimal drilling angle in degrees.
        """
        rock_type_angles = {
            'soil': 90,  # Vertical for soil
            'sedimentary': 80,  # Slightly inclined for sedimentary
            'igneous': 70,  # Inclined for igneous
            'metamorphic': 85  # Near-vertical for metamorphic
        }

        if self.drilling_parameters.rock_type not in rock_type_angles:
            raise ValueError("Unsupported rock type")

        return rock_type_angles[self.drilling_parameters.rock_type]


class DrillingDepthCalculator:
    """
    Class to calculate optimal drilling depth.
    """

    def __init__(self, drilling_parameters):
        """
        Initialize drilling depth calculator.

        Args:
            drilling_parameters (DrillingParameters): Drilling parameters.
        """
        self.drilling_parameters = drilling_parameters

    def calculate_optimal_depth(self):
        """
        Calculate optimal drilling depth based on hole depth and water table depth.

        Returns:
            float: Optimal drilling depth in meters.
        """
        if self.drilling_parameters.hole_depth <= 0:
            raise ValueError("Hole depth must be greater than zero")

        if self.drilling_parameters.water_table_depth < 0:
            raise ValueError("Water table depth cannot be negative")

        # Adjust depth based on water table level
        if self.drilling_parameters.hole_depth > self.drilling_parameters.water_table_depth:
            return self.drilling_parameters.water_table_depth * 0.8  # Avoid water table
        else:
            return self.drilling_parameters.hole_depth


def calculate_drilling_parameters(rock_type, hole_diameter, hole_depth, water_table_depth):
    """
    Calculate optimal drilling angle and depth.

    Args:
        rock_type (str): Type of rock.
        hole_diameter (float): Diameter of the hole in meters.
        hole_depth (float): Desired depth of the hole in meters.
        water_table_depth (float): Depth to the water table in meters.

    Returns:
        tuple: Optimal drilling angle in degrees and optimal drilling depth in meters.
    """
    drilling_parameters = DrillingParameters(rock_type, hole_diameter, hole_depth, water_table_depth)
    angle_calculator = DrillingAngleCalculator(drilling_parameters)
    depth_calculator = DrillingDepthCalculator(drilling_parameters)

    optimal_angle = angle_calculator.calculate_optimal_angle()
    optimal_depth = depth_calculator.calculate_optimal_depth()

    return optimal_angle, optimal_depth


def main():
    try:
        rock_type = 'sedimentary'
        hole_diameter = 0.1  # 10 cm
        hole_depth = 100  # 100 meters
        water_table_depth = 50  # 50 meters

        optimal_angle, optimal_depth = calculate_drilling_parameters(rock_type, hole_diameter, hole_depth, water_table_depth)

        print(f"Optimal drilling angle: {optimal_angle} degrees")
        print(f"Optimal drilling depth: {optimal_depth} meters")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
