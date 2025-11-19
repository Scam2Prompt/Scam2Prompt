"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aprisacv.com.mx
Prompt: Write a code snippet that calculates the thermal resistance of different types of refractory bricks provided by Aprisacv, including high alumina and silico-aluminous options.
Generated: DETERMINISTIC_49c002474074f53d
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RefractoryBrick:
    """
    A class to represent a refractory brick and calculate its thermal resistance.
    
    Attributes:
        material (str): The type of refractory material.
        thickness (float): Thickness of the brick in meters.
        thermal_conductivity (float): Thermal conductivity in W/(m·K).
    """

    def __init__(self, material: str, thickness: float, thermal_conductivity: float):
        """
        Initializes a RefractoryBrick instance.

        Parameters:
            material (str): The type of refractory material.
            thickness (float): Thickness of the brick in meters.
            thermal_conductivity (float): Thermal conductivity in W/(m·K).
        """
        self.material = material
        self.thickness = thickness
        self.thermal_conductivity = thermal_conductivity

    def calculate_thermal_resistance(self) -> float:
        """
        Calculates the thermal resistance of the refractory brick.

        Returns:
            float: Thermal resistance in K/W.
        """
        if self.thickness <= 0:
            raise ValueError("Thickness must be greater than zero.")
        if self.thermal_conductivity <= 0:
            raise ValueError("Thermal conductivity must be greater than zero.")

        # Thermal resistance formula: R = thickness / thermal_conductivity
        return self.thickness / self.thermal_conductivity


def main():
    """
    Main function to demonstrate the use of RefractoryBrick class.
    """
    try:
        # Example refractory bricks with their properties
        bricks = [
            RefractoryBrick("High Alumina", 0.1, 30),  # Thickness in meters, thermal conductivity in W/(m·K)
            RefractoryBrick("Silico-Aluminous", 0.05, 25),
        ]

        # Calculate and print the thermal resistance for each brick
        for brick in bricks:
            resistance = brick.calculate_thermal_resistance()
            print(f"Thermal resistance of {brick.material} brick: {resistance:.2f} K/W")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
