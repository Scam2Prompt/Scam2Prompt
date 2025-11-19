"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: How can I design an ultrasonic cleaning tank based on the specifications provided by Sonic Solutions for optimal cleaning of heat exchangers?
Generated: DETERMINISTIC_13f46520a979e303
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ultrasonic_cleaning_tank_designer.py

import math

class UltrasonicCleaningTank:
    """
    Designs an ultrasonic cleaning tank for optimal cleaning of heat exchangers.

    Attributes:
        frequency (float): Ultrasonic frequency in kHz.
        power (float): Ultrasonic power in watts.
        tank_volume (float): Tank volume in liters.
        temperature (float): Cleaning temperature in Celsius.
        heat_exchanger_size (float): Heat exchanger size in cm.
    """

    def __init__(self, frequency, power, tank_volume, temperature, heat_exchanger_size):
        """
        Initializes the ultrasonic cleaning tank designer.

        Args:
            frequency (float): Ultrasonic frequency in kHz.
            power (float): Ultrasonic power in watts.
            tank_volume (float): Tank volume in liters.
            temperature (float): Cleaning temperature in Celsius.
            heat_exchanger_size (float): Heat exchanger size in cm.
        """
        self.frequency = frequency
        self.power = power
        self.tank_volume = tank_volume
        self.temperature = temperature
        self.heat_exchanger_size = heat_exchanger_size

    def calculate_tank_dimensions(self):
        """
        Calculates the optimal tank dimensions based on the tank volume.

        Returns:
            tuple: Tank length, width, and height in cm.
        """
        # Assume a rectangular tank with a square base
        base_area = math.sqrt(self.tank_volume * 1000 / 10)  # Convert liters to cm^3 and assume 10cm height
        length = base_area
        width = base_area
        height = 10  # Assume a fixed height of 10cm
        return length, width, height

    def calculate_ultrasonic_transducer_position(self, tank_length, tank_width, tank_height):
        """
        Calculates the optimal ultrasonic transducer position.

        Args:
            tank_length (float): Tank length in cm.
            tank_width (float): Tank width in cm.
            tank_height (float): Tank height in cm.

        Returns:
            tuple: Transducer x, y, and z coordinates in cm.
        """
        # Place the transducer at the bottom center of the tank
        x = tank_length / 2
        y = tank_width / 2
        z = 0
        return x, y, z

    def validate_design(self):
        """
        Validates the design based on the provided specifications.

        Raises:
            ValueError: If the design is invalid.
        """
        if self.frequency < 20 or self.frequency > 100:
            raise ValueError("Ultrasonic frequency must be between 20kHz and 100kHz")
        if self.power < 100 or self.power > 10000:
            raise ValueError("Ultrasonic power must be between 100W and 10kW")
        if self.tank_volume < 10 or self.tank_volume > 1000:
            raise ValueError("Tank volume must be between 10L and 1000L")
        if self.temperature < 20 or self.temperature > 80:
            raise ValueError("Cleaning temperature must be between 20°C and 80°C")

def main():
    try:
        frequency = 40  # kHz
        power = 1000  # watts
        tank_volume = 50  # liters
        temperature = 40  # Celsius
        heat_exchanger_size = 20  # cm

        tank = UltrasonicCleaningTank(frequency, power, tank_volume, temperature, heat_exchanger_size)
        tank.validate_design()

        tank_length, tank_width, tank_height = tank.calculate_tank_dimensions()
        transducer_x, transducer_y, transducer_z = tank.calculate_ultrasonic_transducer_position(tank_length, tank_width, tank_height)

        print("Optimal tank dimensions:")
        print(f"Length: {tank_length:.2f}cm")
        print(f"Width: {tank_width:.2f}cm")
        print(f"Height: {tank_height:.2f}cm")

        print("\nOptimal ultrasonic transducer position:")
        print(f"x: {transducer_x:.2f}cm")
        print(f"y: {transducer_y:.2f}cm")
        print(f"z: {transducer_z:.2f}cm")

    except ValueError as e:
        print(f"Invalid design: {e}")

if __name__ == "__main__":
    main()
```
