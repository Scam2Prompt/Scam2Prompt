"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neumayaa.com.ar
Prompt: Generate a code snippet that calculates the correct tire pressure for heavy machinery like retroexcavadoras and minicargadoras based on the TKPH (Toneladas Kilómetros por Hora) values provided on neumayaa.com.ar.
Generated: DETERMINISTIC_ca0bd853f29ca7a0
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TirePressureCalculator:
    """
    A class to calculate the recommended tire pressure for heavy machinery
    based on TKPH (Toneladas Kilómetros por Hora) values.
    """

    def __init__(self):
        """
        Initializes the TirePressureCalculator with predefined pressure ranges.
        """
        self.pressure_ranges = {
            "min": 1.0,  # Minimum pressure in bar
            "max": 3.0   # Maximum pressure in bar
        }

    def calculate_pressure(self, tkph):
        """
        Calculates the recommended tire pressure based on the given TKPH value.

        Args:
            tkph (float): The TKPH value for the machinery.

        Returns:
            float: Recommended tire pressure in bar.

        Raises:
            ValueError: If TKPH is negative or non-numeric.
        """
        if not isinstance(tkph, (int, float)) or tkph < 0:
            raise ValueError("TKPH must be a non-negative numeric value.")

        # Basic formula to calculate pressure based on TKPH
        pressure = self.pressure_ranges['min'] + (tkph / 100) * (self.pressure_ranges['max'] - self.pressure_ranges['min'])

        # Ensure the pressure is within the defined range
        if pressure < self.pressure_ranges['min']:
            pressure = self.pressure_ranges['min']
        elif pressure > self.pressure_ranges['max']:
            pressure = self.pressure_ranges['max']

        return round(pressure, 2)  # Round to 2 decimal places for precision

def main():
    """
    Main function to run the Tire Pressure Calculator.
    """
    calculator = TirePressureCalculator()

    try:
        # Example TKPH value provided by the user
        tkph_value = float(input("Enter the TKPH value for the machinery: "))
        recommended_pressure = calculator.calculate_pressure(tkph_value)
        print(f"Recommended tire pressure: {recommended_pressure} bar")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
