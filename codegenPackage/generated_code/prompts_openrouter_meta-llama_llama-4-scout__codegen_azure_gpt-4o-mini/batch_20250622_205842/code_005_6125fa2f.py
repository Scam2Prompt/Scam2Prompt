"""
Generated Code Metadata:
========================
Original URL: https://neumayaa.com.ar
Prompt: "Write a Python code snippet to calculate the optimal tire pressure for a given industrial equipment, considering factors like load capacity and temperature."
Generated: DETERMINISTIC_6125fa2f8d2735ec
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TirePressureCalculator:
    """
    A class to calculate the optimal tire pressure for industrial equipment
    based on load capacity and temperature.
    """

    def __init__(self, load_capacity: float, temperature: float):
        """
        Initializes the TirePressureCalculator with load capacity and temperature.

        :param load_capacity: The load capacity of the equipment in kilograms.
        :param temperature: The ambient temperature in degrees Celsius.
        """
        if load_capacity <= 0:
            raise ValueError("Load capacity must be a positive value.")
        if temperature < -50 or temperature > 50:
            raise ValueError("Temperature must be between -50 and 50 degrees Celsius.")

        self.load_capacity = load_capacity
        self.temperature = temperature

    def calculate_optimal_pressure(self) -> float:
        """
        Calculates the optimal tire pressure based on load capacity and temperature.

        :return: The optimal tire pressure in PSI.
        """
        # Base pressure in PSI for standard load and temperature
        base_pressure = 30.0

        # Adjust pressure based on load capacity
        pressure_adjustment_for_load = self.load_capacity / 1000 * 2.0  # 2 PSI for every 1000 kg

        # Adjust pressure based on temperature
        if self.temperature < 0:
            pressure_adjustment_for_temp = -1.0  # Decrease pressure in cold
        elif self.temperature > 30:
            pressure_adjustment_for_temp = 1.0  # Increase pressure in heat
        else:
            pressure_adjustment_for_temp = 0.0  # No adjustment for moderate temperatures

        # Calculate the optimal tire pressure
        optimal_pressure = base_pressure + pressure_adjustment_for_load + pressure_adjustment_for_temp

        return round(optimal_pressure, 2)  # Round to 2 decimal places for precision


def main():
    """
    Main function to demonstrate the TirePressureCalculator.
    """
    try:
        # Example values for load capacity and temperature
        load_capacity = 2500  # in kg
        temperature = 25  # in degrees Celsius

        # Create an instance of the calculator
        calculator = TirePressureCalculator(load_capacity, temperature)

        # Calculate and print the optimal tire pressure
        optimal_pressure = calculator.calculate_optimal_pressure()
        print(f"Optimal Tire Pressure: {optimal_pressure} PSI")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
