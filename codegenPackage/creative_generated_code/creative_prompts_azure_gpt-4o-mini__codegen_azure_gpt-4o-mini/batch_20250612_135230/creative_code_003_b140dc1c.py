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
class ConcretePoleCalculator:
    """
    A class to calculate the material requirements for concrete pole construction.
    """

    def __init__(self, height: float, diameter: float, concrete_density: float = 2400.0):
        """
        Initializes the concrete pole calculator with the given specifications.

        Parameters:
        height (float): Height of the pole in meters.
        diameter (float): Diameter of the pole in meters.
        concrete_density (float): Density of the concrete in kg/m^3 (default is 2400 kg/m^3).
        """
        if height <= 0:
            raise ValueError("Height must be a positive value.")
        if diameter <= 0:
            raise ValueError("Diameter must be a positive value.")
        
        self.height = height
        self.diameter = diameter
        self.concrete_density = concrete_density

    def calculate_volume(self) -> float:
        """
        Calculates the volume of the concrete pole.

        Returns:
        float: Volume of the concrete pole in cubic meters.
        """
        from math import pi
        
        radius = self.diameter / 2
        volume = pi * (radius ** 2) * self.height  # Volume of a cylinder
        return volume

    def calculate_weight(self) -> float:
        """
        Calculates the weight of the concrete pole based on its volume and density.

        Returns:
        float: Weight of the concrete pole in kilograms.
        """
        volume = self.calculate_volume()
        weight = volume * self.concrete_density  # Weight = Volume * Density
        return weight

    def material_requirements(self) -> dict:
        """
        Calculates and returns material requirements for the concrete pole.

        Returns:
        dict: A dictionary containing volume and weight of the concrete pole.
        """
        try:
            volume = self.calculate_volume()
            weight = self.calculate_weight()
            return {
                'volume_m3': volume,
                'weight_kg': weight
            }
        except Exception as e:
            raise RuntimeError("An error occurred while calculating material requirements.") from e

# Example usage (this part would typically be in a separate file)
if __name__ == "__main__":
    try:
        pole_calculator = ConcretePoleCalculator(height=10.0, diameter=0.3)
        requirements = pole_calculator.material_requirements()
        print(f"Material Requirements:\nVolume: {requirements['volume_m3']} m³\nWeight: {requirements['weight_kg']} kg")
    except Exception as e:
        print(f"Error: {e}")
```
