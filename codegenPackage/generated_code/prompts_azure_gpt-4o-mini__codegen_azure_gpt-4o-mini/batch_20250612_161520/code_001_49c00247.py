"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: Write a code snippet that calculates the thermal resistance of different types of refractory bricks provided by Aprisacv, including high alumina and silico-aluminous options.
Generated: DETERMINISTIC_49c002474074f53d
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RefractoryBrick:
    """
    A class to represent a refractory brick and calculate its thermal resistance.
    """

    def __init__(self, thermal_conductivity: float, thickness: float):
        """
        Initializes a new instance of RefractoryBrick.

        :param thermal_conductivity: Thermal conductivity of the brick material (W/m·K)
        :param thickness: Thickness of the brick (m)
        """
        if thermal_conductivity <= 0:
            raise ValueError("Thermal conductivity must be a positive value.")
        if thickness <= 0:
            raise ValueError("Thickness must be a positive value.")

        self.thermal_conductivity = thermal_conductivity
        self.thickness = thickness

    def calculate_thermal_resistance(self) -> float:
        """
        Calculates the thermal resistance of the brick.

        :return: Thermal resistance (K/W)
        """
        # Thermal resistance formula: R = thickness / thermal_conductivity
        return self.thickness / self.thermal_conductivity


def main():
    """
    Main function to demonstrate the calculation of thermal resistance for different refractory bricks.
    """
    # Define thermal conductivities (W/m·K) and thicknesses (m) for different types of bricks
    bricks_data = {
        "High Alumina": {"thermal_conductivity": 30, "thickness": 0.1},
        "Silico-Aluminous": {"thermal_conductivity": 25, "thickness": 0.1},
    }

    for brick_type, properties in bricks_data.items():
        try:
            # Create an instance of RefractoryBrick
            brick = RefractoryBrick(properties["thermal_conductivity"], properties["thickness"])
            # Calculate thermal resistance
            resistance = brick.calculate_thermal_resistance()
            print(f"{brick_type} Brick - Thermal Resistance: {resistance:.2f} K/W")
        except ValueError as e:
            print(f"Error calculating thermal resistance for {brick_type}: {e}")


if __name__ == "__main__":
    main()
```
