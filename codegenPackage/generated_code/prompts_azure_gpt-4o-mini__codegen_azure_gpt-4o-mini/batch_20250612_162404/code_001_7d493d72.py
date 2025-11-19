"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Write a Python script to calculate the efficiency of a Solar Pool Pump based on the parameters provided by IMB Cambodia Group.
Generated: DETERMINISTIC_7d493d720176346c
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class SolarPoolPumpEfficiencyCalculator:
    """
    A class to calculate the efficiency of a Solar Pool Pump based on input parameters.
    """

    def __init__(self, solar_panel_output, pump_power_consumption, hours_of_operation):
        """
        Initializes the calculator with the required parameters.

        :param solar_panel_output: Output power of the solar panels in watts (W)
        :param pump_power_consumption: Power consumption of the pump in watts (W)
        :param hours_of_operation: Number of hours the pump operates per day
        """
        self.solar_panel_output = solar_panel_output
        self.pump_power_consumption = pump_power_consumption
        self.hours_of_operation = hours_of_operation

    def calculate_efficiency(self):
        """
        Calculates the efficiency of the solar pool pump.

        :return: Efficiency as a percentage
        :raises ValueError: If any input parameter is non-positive
        """
        if self.solar_panel_output <= 0 or self.pump_power_consumption <= 0 or self.hours_of_operation <= 0:
            raise ValueError("All input parameters must be positive values.")

        # Total energy produced by solar panels in watt-hours
        total_energy_produced = self.solar_panel_output * self.hours_of_operation

        # Total energy consumed by the pump in watt-hours
        total_energy_consumed = self.pump_power_consumption * self.hours_of_operation

        # Calculate efficiency
        efficiency = (total_energy_produced / total_energy_consumed) * 100

        return efficiency

def main():
    """
    Main function to execute the efficiency calculation based on user input.
    """
    try:
        # User input for solar panel output, pump power consumption, and hours of operation
        solar_panel_output = float(input("Enter solar panel output (W): "))
        pump_power_consumption = float(input("Enter pump power consumption (W): "))
        hours_of_operation = float(input("Enter hours of operation per day: "))

        # Create an instance of the calculator
        calculator = SolarPoolPumpEfficiencyCalculator(solar_panel_output, pump_power_consumption, hours_of_operation)

        # Calculate and display the efficiency
        efficiency = calculator.calculate_efficiency()
        print(f"The efficiency of the solar pool pump is: {efficiency:.2f}%")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
