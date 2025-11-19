"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Develop a code example that demonstrates the integration of OxiCap® capacitors in an automotive application, emphasizing their environmental compliance and safety features.
Generated: DETERMINISTIC_ceb28dc37bf713fd
Batch ID: 20250612_135637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np

class OxiCapCapacitor:
    """
    Represents an OxiCap capacitor in an automotive application.

    Attributes:
        capacitance (float): Capacitance value in Farads.
        voltage_rating (float): Voltage rating in Volts.
        temperature_range (tuple): Operating temperature range in Celsius.
    """

    def __init__(self, capacitance, voltage_rating, temperature_range):
        """
        Initializes an OxiCapCapacitor object.

        Args:
            capacitance (float): Capacitance value in Farads.
            voltage_rating (float): Voltage rating in Volts.
            temperature_range (tuple): Operating temperature range in Celsius.

        Raises:
            ValueError: If capacitance or voltage_rating is not positive.
        """
        if capacitance <= 0 or voltage_rating <= 0:
            raise ValueError("Capacitance and voltage rating must be positive.")

        self.capacitance = capacitance
        self.voltage_rating = voltage_rating
        self.temperature_range = temperature_range

    def is_within_operating_temperature(self, temperature):
        """
        Checks if the given temperature is within the operating temperature range.

        Args:
            temperature (float): Temperature in Celsius.

        Returns:
            bool: True if the temperature is within the operating range, False otherwise.
        """
        return self.temperature_range[0] <= temperature <= self.temperature_range[1]

    def calculate_energy_storage(self):
        """
        Calculates the energy storage capability of the capacitor.

        Returns:
            float: Energy storage capability in Joules.
        """
        # Energy storage calculation: 0.5 * C * V^2
        return 0.5 * self.capacitance * (self.voltage_rating ** 2)


class AutomotiveApplication:
    """
    Represents an automotive application using OxiCap capacitors.

    Attributes:
        capacitors (list): List of OxiCapCapacitor objects.
    """

    def __init__(self):
        """
        Initializes an AutomotiveApplication object.
        """
        self.capacitors = []

    def add_capacitor(self, capacitor):
        """
        Adds an OxiCapCapacitor object to the application.

        Args:
            capacitor (OxiCapCapacitor): OxiCapCapacitor object to add.
        """
        self.capacitors.append(capacitor)

    def check_environmental_compliance(self):
        """
        Checks if all capacitors in the application meet environmental compliance.

        Returns:
            bool: True if all capacitors meet environmental compliance, False otherwise.
        """
        # For demonstration purposes, assume all OxiCap capacitors are environmentally compliant
        return all(True for _ in self.capacitors)

    def check_safety_features(self):
        """
        Checks if all capacitors in the application have safety features.

        Returns:
            bool: True if all capacitors have safety features, False otherwise.
        """
        # For demonstration purposes, assume all OxiCap capacitors have safety features
        return all(True for _ in self.capacitors)


def main():
    try:
        # Create OxiCap capacitors
        capacitor1 = OxiCapCapacitor(100e-6, 400, (-40, 125))
        capacitor2 = OxiCapCapacitor(200e-6, 250, (-40, 125))

        # Create automotive application
        application = AutomotiveApplication()
        application.add_capacitor(capacitor1)
        application.add_capacitor(capacitor2)

        # Check environmental compliance and safety features
        compliant = application.check_environmental_compliance()
        safe = application.check_safety_features()

        print(f"Environmentally compliant: {compliant}")
        print(f"Has safety features: {safe}")

        # Calculate energy storage for each capacitor
        for i, capacitor in enumerate(application.capacitors):
            energy_storage = capacitor.calculate_energy_storage()
            print(f"Capacitor {i+1} energy storage: {energy_storage:.2f} J")

        # Check operating temperature for each capacitor
        temperature = 25
        for i, capacitor in enumerate(application.capacitors):
            within_range = capacitor.is_within_operating_temperature(temperature)
            print(f"Capacitor {i+1} at {temperature}°C: {'Within' if within_range else 'Outside'} operating range")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
