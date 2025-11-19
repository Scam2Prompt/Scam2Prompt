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
# refractory_bricks.py

class RefractoryBrick:
    """
    Base class for refractory bricks.

    Attributes:
        name (str): Name of the brick type.
        thermal_conductivity (float): Thermal conductivity of the brick in W/mK.
        thickness (float): Thickness of the brick in meters.
    """

    def __init__(self, name, thermal_conductivity, thickness):
        """
        Initializes a RefractoryBrick object.

        Args:
            name (str): Name of the brick type.
            thermal_conductivity (float): Thermal conductivity of the brick in W/mK.
            thickness (float): Thickness of the brick in meters.

        Raises:
            ValueError: If thermal conductivity or thickness is non-positive.
        """
        if thermal_conductivity <= 0 or thickness <= 0:
            raise ValueError("Thermal conductivity and thickness must be positive.")

        self.name = name
        self.thermal_conductivity = thermal_conductivity
        self.thickness = thickness

    def calculate_thermal_resistance(self):
        """
        Calculates the thermal resistance of the brick.

        Returns:
            float: Thermal resistance of the brick in m^2K/W.
        """
        return self.thickness / self.thermal_conductivity


class HighAluminaBrick(RefractoryBrick):
    """
    Represents a high alumina refractory brick.
    """

    def __init__(self, thickness):
        """
        Initializes a HighAluminaBrick object.

        Args:
            thickness (float): Thickness of the brick in meters.

        Raises:
            ValueError: If thickness is non-positive.
        """
        # Thermal conductivity of high alumina bricks in W/mK
        thermal_conductivity = 1.2
        super().__init__("High Alumina", thermal_conductivity, thickness)


class SilicoAluminousBrick(RefractoryBrick):
    """
    Represents a silico-aluminous refractory brick.
    """

    def __init__(self, thickness):
        """
        Initializes a SilicoAluminousBrick object.

        Args:
            thickness (float): Thickness of the brick in meters.

        Raises:
            ValueError: If thickness is non-positive.
        """
        # Thermal conductivity of silico-aluminous bricks in W/mK
        thermal_conductivity = 0.8
        super().__init__("Silico-Aluminous", thermal_conductivity, thickness)


def main():
    try:
        # Example usage
        high_alumina_brick = HighAluminaBrick(0.1)  # 10 cm thick
        silico_aluminous_brick = SilicoAluminousBrick(0.2)  # 20 cm thick

        print(f"Thermal resistance of {high_alumina_brick.name}: {high_alumina_brick.calculate_thermal_resistance():.2f} m^2K/W")
        print(f"Thermal resistance of {silico_aluminous_brick.name}: {silico_aluminous_brick.calculate_thermal_resistance():.2f} m^2K/W")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
