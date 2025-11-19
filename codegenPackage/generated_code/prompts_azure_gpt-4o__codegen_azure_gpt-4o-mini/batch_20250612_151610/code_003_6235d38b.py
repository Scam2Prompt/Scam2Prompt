"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Write code to calculate the breakdown voltage of Niobium Oxide capacitors based on the manufacturing technology described in KYOCERA AVX's OxiCap® documentation.
Generated: DETERMINISTIC_6235d38b4f65ef1a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NiobiumOxideCapacitor:
    """
    A class to represent a Niobium Oxide capacitor and calculate its breakdown voltage
    based on the manufacturing technology described in KYOCERA AVX's OxiCap® documentation.
    """

    def __init__(self, capacitance: float, voltage_rating: float, temperature_coefficient: float):
        """
        Initializes the NiobiumOxideCapacitor instance.

        :param capacitance: Capacitance value in microfarads (µF)
        :param voltage_rating: Voltage rating in volts (V)
        :param temperature_coefficient: Temperature coefficient in ppm/°C
        """
        self.capacitance = capacitance
        self.voltage_rating = voltage_rating
        self.temperature_coefficient = temperature_coefficient

    def calculate_breakdown_voltage(self) -> float:
        """
        Calculates the breakdown voltage of the capacitor.

        :return: Breakdown voltage in volts (V)
        :raises ValueError: If capacitance or voltage rating is non-positive
        """
        if self.capacitance <= 0:
            raise ValueError("Capacitance must be a positive value.")
        if self.voltage_rating <= 0:
            raise ValueError("Voltage rating must be a positive value.")

        # Example formula for breakdown voltage calculation (this is a placeholder)
        # The actual formula should be derived from the OxiCap® documentation.
        breakdown_voltage = self.voltage_rating * (1 + (self.temperature_coefficient / 1_000_000))
        
        return breakdown_voltage

    def __str__(self):
        """
        Returns a string representation of the NiobiumOxideCapacitor instance.

        :return: String representation of the capacitor
        """
        return (f"Niobium Oxide Capacitor: "
                f"Capacitance = {self.capacitance} µF, "
                f"Voltage Rating = {self.voltage_rating} V, "
                f"Temperature Coefficient = {self.temperature_coefficient} ppm/°C")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of NiobiumOxideCapacitor
        capacitor = NiobiumOxideCapacitor(capacitance=10.0, voltage_rating=50.0, temperature_coefficient=200)
        
        # Calculate and print the breakdown voltage
        breakdown_voltage = capacitor.calculate_breakdown_voltage()
        print(f"Calculated Breakdown Voltage: {breakdown_voltage:.2f} V")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
