"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-t.com
Prompt: Create a library function that calculates the material requirements for concrete pole construction based on project specifications.
Generated: DETERMINISTIC_b140dc1c81bd3cb0
Batch ID: 20250612_135230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: concrete_pole_calculator.py

class ConcretePoleCalculator:
    """
    A library to calculate material requirements for concrete pole construction
    based on project specifications.
    """

    def __init__(self):
        """
        Initializes the calculator with default material densities and ratios.
        """
        # Densities and ratios are in units assumed standard for concrete calculations
        self.concrete_density = 2400  # kg/m³ (average concrete density)
        self.steel_density = 7850  # kg/m³ (average steel density)
        self.reinforcement_ratio = 0.05  # Steel reinforcement as a percentage of concrete volume

    def calculate_materials(self, pole_height, pole_diameter, reinforcement_percentage=None):
        """
        Calculates the material requirements for a single concrete pole.

        Parameters:
            pole_height (float): Height of the pole in meters.
            pole_diameter (float): Diameter of the pole in meters.
            reinforcement_percentage (float, optional): Percentage of concrete volume to be replaced
                                                        with steel reinforcement. Defaults to
                                                        self.reinforcement_ratio.

        Returns:
            dict: A dictionary containing the required quantities of concrete and steel in kilograms.

        Raises:
            ValueError: If any of the input parameters are invalid.
        """
        # Input validation
        if pole_height <= 0:
            raise ValueError("Pole height must be a positive number.")
        if pole_diameter <= 0:
            raise ValueError("Pole diameter must be a positive number.")
        if reinforcement_percentage is not None and (reinforcement_percentage < 0 or reinforcement_percentage > 1):
            raise ValueError("Reinforcement percentage must be between 0 and 1.")

        # Use the default reinforcement percentage if not provided
        reinforcement_percentage = reinforcement_percentage or self.reinforcement_ratio

        # Calculate the volume of the pole (assumed cylindrical shape)
        import math
        radius = pole_diameter / 2
        pole_volume = math.pi * (radius ** 2) * pole_height  # Volume in cubic meters

        # Calculate material requirements
        concrete_volume = pole_volume * (1 - reinforcement_percentage)
        steel_volume = pole_volume * reinforcement_percentage

        # Convert volumes to weights based on densities
        concrete_weight = concrete_volume * self.concrete_density
        steel_weight = steel_volume * self.steel_density

        # Return the material requirements as a dictionary
        return {
            "concrete_weight_kg": round(concrete_weight, 2),
            "steel_weight_kg": round(steel_weight, 2)
        }

# Example usage:
if __name__ == "__main__":
    try:
        calculator = ConcretePoleCalculator()
        pole_specs = {
            "pole_height": 6,  # meters
            "pole_diameter": 0.3,  # meters
            "reinforcement_percentage": 0.07  # optional, overrides default
        }
        materials = calculator.calculate_materials(**pole_specs)
        print(f"Material requirements: {materials}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
