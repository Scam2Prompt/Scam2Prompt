"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Design a flexible shaft and brush system for tube cleaning in a sugar mill, including specifications for air-driven motors and straight tube cleaning kits.
Generated: DETERMINISTIC_98ae9a95ec739f4f
Batch ID: 20250622_211546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tube_cleaning_system.py

class FlexibleShaft:
    """
    Represents a flexible shaft for tube cleaning in a sugar mill.
    """

    def __init__(self, length: float, diameter: float, material: str):
        """
        Initializes a FlexibleShaft object.

        Args:
            length (float): The length of the shaft in meters.
            diameter (float): The diameter of the shaft in millimeters.
            material (str): The material of the shaft (e.g., steel, stainless steel).
        """
        self.length = length
        self.diameter = diameter
        self.material = material

    def __str__(self):
        return f"Flexible Shaft - Length: {self.length}m, Diameter: {self.diameter}mm, Material: {self.material}"


class Brush:
    """
    Represents a brush for tube cleaning in a sugar mill.
    """

    def __init__(self, diameter: float, bristle_type: str, bristle_length: float):
        """
        Initializes a Brush object.

        Args:
            diameter (float): The diameter of the brush in millimeters.
            bristle_type (str): The type of bristles (e.g., nylon, steel).
            bristle_length (float): The length of the bristles in millimeters.
        """
        self.diameter = diameter
        self.bristle_type = bristle_type
        self.bristle_length = bristle_length

    def __str__(self):
        return f"Brush - Diameter: {self.diameter}mm, Bristle Type: {self.bristle_type}, Bristle Length: {self.bristle_length}mm"


class AirDrivenMotor:
    """
    Represents an air-driven motor for tube cleaning in a sugar mill.
    """

    def __init__(self, power: float, speed: int, air_pressure: float):
        """
        Initializes an AirDrivenMotor object.

        Args:
            power (float): The power of the motor in horsepower.
            speed (int): The speed of the motor in revolutions per minute.
            air_pressure (float): The required air pressure in bar.
        """
        self.power = power
        self.speed = speed
        self.air_pressure = air_pressure

    def __str__(self):
        return f"Air-Driven Motor - Power: {self.power}hp, Speed: {self.speed}rpm, Air Pressure: {self.air_pressure}bar"


class StraightTubeCleaningKit:
    """
    Represents a straight tube cleaning kit for tube cleaning in a sugar mill.
    """

    def __init__(self, tube_diameter: float, tube_length: float, flexible_shaft: FlexibleShaft, brush: Brush):
        """
        Initializes a StraightTubeCleaningKit object.

        Args:
            tube_diameter (float): The diameter of the tube in millimeters.
            tube_length (float): The length of the tube in meters.
            flexible_shaft (FlexibleShaft): The flexible shaft to use.
            brush (Brush): The brush to use.
        """
        self.tube_diameter = tube_diameter
        self.tube_length = tube_length
        self.flexible_shaft = flexible_shaft
        self.brush = brush

    def __str__(self):
        return (
            f"Straight Tube Cleaning Kit - Tube Diameter: {self.tube_diameter}mm, Tube Length: {self.tube_length}m\n"
            f"{self.flexible_shaft}\n"
            f"{self.brush}"
        )


def main():
    try:
        # Create a flexible shaft
        flexible_shaft = FlexibleShaft(length=5.0, diameter=10.0, material="stainless steel")

        # Create a brush
        brush = Brush(diameter=10.0, bristle_type="nylon", bristle_length=50.0)

        # Create an air-driven motor
        air_driven_motor = AirDrivenMotor(power=1.5, speed=1000, air_pressure=6.0)

        # Create a straight tube cleaning kit
        straight_tube_cleaning_kit = StraightTubeCleaningKit(
            tube_diameter=50.0, tube_length=10.0, flexible_shaft=flexible_shaft, brush=brush
        )

        # Print the specifications
        print("Flexible Shaft:")
        print(flexible_shaft)
        print("\nBrush:")
        print(brush)
        print("\nAir-Driven Motor:")
        print(air_driven_motor)
        print("\nStraight Tube Cleaning Kit:")
        print(straight_tube_cleaning_kit)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
