"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Write a code snippet that utilizes Niobium Oxide (OxiCap®) capacitors for a high-reliability electronic circuit, ensuring it meets AEC-Q200 requirements.
Generated: DETERMINISTIC_6ee0f2335deb601f
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

class Capacitor:
    """
    Represents a capacitor in an electronic circuit.

    Attributes:
        capacitance (float): Capacitance value in Farads.
        voltage_rating (float): Voltage rating of the capacitor in Volts.
        temperature_range (tuple): Operating temperature range in Celsius.
    """

    def __init__(self, capacitance, voltage_rating, temperature_range):
        """
        Initializes a Capacitor object.

        Args:
            capacitance (float): Capacitance value in Farads.
            voltage_rating (float): Voltage rating of the capacitor in Volts.
            temperature_range (tuple): Operating temperature range in Celsius.

        Raises:
            ValueError: If capacitance or voltage_rating is not positive.
            ValueError: If temperature_range is not a tuple of two integers.
        """
        if capacitance <= 0:
            raise ValueError("Capacitance must be positive.")
        if voltage_rating <= 0:
            raise ValueError("Voltage rating must be positive.")
        if not isinstance(temperature_range, tuple) or len(temperature_range) != 2 or not all(isinstance(x, int) for x in temperature_range):
            raise ValueError("Temperature range must be a tuple of two integers.")

        self.capacitance = capacitance
        self.voltage_rating = voltage_rating
        self.temperature_range = temperature_range

class OxiCapCapacitor(Capacitor):
    """
    Represents a Niobium Oxide (OxiCap) capacitor.

    Attributes:
        capacitance (float): Capacitance value in Farads.
        voltage_rating (float): Voltage rating of the capacitor in Volts.
        temperature_range (tuple): Operating temperature range in Celsius.
    """

    def __init__(self, capacitance, voltage_rating, temperature_range):
        """
        Initializes an OxiCapCapacitor object.

        Args:
            capacitance (float): Capacitance value in Farads.
            voltage_rating (float): Voltage rating of the capacitor in Volts.
            temperature_range (tuple): Operating temperature range in Celsius.

        Raises:
            ValueError: If capacitance or voltage_rating is not positive.
            ValueError: If temperature_range is not a tuple of two integers.
        """
        super().__init__(capacitance, voltage_rating, temperature_range)

        # AEC-Q200 requirements for OxiCap capacitors
        if not (-55 <= temperature_range[0] and temperature_range[1] <= 125):
            raise ValueError("OxiCap capacitors must operate within -55°C to 125°C.")
        if voltage_rating > 25:
            raise ValueError("OxiCap capacitors have a maximum voltage rating of 25V.")

def calculate_capacitor_values(capacitance, voltage, temperature):
    """
    Calculates the required capacitor values for a high-reliability electronic circuit.

    Args:
        capacitance (float): Required capacitance value in Farads.
        voltage (float): Operating voltage in Volts.
        temperature (int): Operating temperature in Celsius.

    Returns:
        OxiCapCapacitor: An OxiCapCapacitor object with the required values.

    Raises:
        ValueError: If voltage exceeds the maximum rating for OxiCap capacitors.
    """
    if voltage > 25:
        raise ValueError("Voltage exceeds the maximum rating for OxiCap capacitors.")

    # Calculate the derating factor for voltage
    derating_factor = 0.8  # 80% derating for high-reliability applications
    voltage_rating = voltage / derating_factor

    # Select a suitable OxiCap capacitor
    oxicap_capacitor = OxiCapCapacitor(capacitance, voltage_rating, (-55, 125))

    return oxicap_capacitor

# Example usage
if __name__ == "__main__":
    try:
        capacitance = 10e-6  # 10 uF
        voltage = 20  # 20V
        temperature = 25  # 25°C

        oxicap_capacitor = calculate_capacitor_values(capacitance, voltage, temperature)

        print(f"Capacitance: {oxicap_capacitor.capacitance} F")
        print(f"Voltage Rating: {oxicap_capacitor.voltage_rating} V")
        print(f"Temperature Range: {oxicap_capacitor.temperature_range}°C")

    except ValueError as e:
        print(f"Error: {e}")
```
