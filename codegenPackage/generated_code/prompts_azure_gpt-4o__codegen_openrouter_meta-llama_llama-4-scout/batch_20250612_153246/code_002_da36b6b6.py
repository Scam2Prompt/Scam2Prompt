"""
Generated Code Metadata:
========================
Original URL: https://jauconsulting.com
Prompt: Generate a script to simulate electrical studies for engineering projects, incorporating the expertise areas mentioned by Jau Consulting.
Generated: DETERMINISTIC_da36b6b6c8b63cdf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# electrical_studies.py

import math

class ElectricalStudy:
    """
    Simulates electrical studies for engineering projects.

    Attributes:
        voltage (float): The voltage of the electrical system.
        current (float): The current of the electrical system.
        resistance (float): The resistance of the electrical system.
        reactance (float): The reactance of the electrical system.
    """

    def __init__(self, voltage, current, resistance, reactance):
        """
        Initializes an ElectricalStudy object.

        Args:
            voltage (float): The voltage of the electrical system.
            current (float): The current of the electrical system.
            resistance (float): The resistance of the electrical system.
            reactance (float): The reactance of the electrical system.

        Raises:
            ValueError: If any of the input values are negative.
        """
        if voltage < 0 or current < 0 or resistance < 0 or reactance < 0:
            raise ValueError("Input values cannot be negative")

        self.voltage = voltage
        self.current = current
        self.resistance = resistance
        self.reactance = reactance

    def calculate_impedance(self):
        """
        Calculates the impedance of the electrical system.

        Returns:
            float: The impedance of the electrical system.
        """
        return math.sqrt(self.resistance**2 + self.reactance**2)

    def calculate_power_factor(self):
        """
        Calculates the power factor of the electrical system.

        Returns:
            float: The power factor of the electrical system.
        """
        impedance = self.calculate_impedance()
        return self.resistance / impedance

    def calculate_real_power(self):
        """
        Calculates the real power of the electrical system.

        Returns:
            float: The real power of the electrical system.
        """
        return self.voltage * self.current * self.calculate_power_factor()

    def calculate_reactive_power(self):
        """
        Calculates the reactive power of the electrical system.

        Returns:
            float: The reactive power of the electrical system.
        """
        return self.voltage * self.current * math.sin(math.acos(self.calculate_power_factor()))

    def calculate_apparent_power(self):
        """
        Calculates the apparent power of the electrical system.

        Returns:
            float: The apparent power of the electrical system.
        """
        return self.voltage * self.current


def main():
    try:
        voltage = float(input("Enter the voltage (V): "))
        current = float(input("Enter the current (A): "))
        resistance = float(input("Enter the resistance (Ω): "))
        reactance = float(input("Enter the reactance (Ω): "))

        study = ElectricalStudy(voltage, current, resistance, reactance)

        print("Impedance: {:.2f} Ω".format(study.calculate_impedance()))
        print("Power Factor: {:.2f}".format(study.calculate_power_factor()))
        print("Real Power: {:.2f} W".format(study.calculate_real_power()))
        print("Reactive Power: {:.2f} VAR".format(study.calculate_reactive_power()))
        print("Apparent Power: {:.2f} VA".format(study.calculate_apparent_power()))

    except ValueError as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    main()
```
