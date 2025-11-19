"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: Generate code for calculating the efficiency of a CCHP (Combined Cooling, Heat, and Power) system, incorporating the technical specifications provided by پایش نیرو.
Generated: DETERMINISTIC_eef76eb55f66ea97
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CCHPEfficiencyCalculator:
    """
    A class to calculate the efficiency of a Combined Cooling, Heat, and Power (CCHP) system.
    """

    def __init__(self, electrical_output, thermal_output, cooling_output, fuel_input):
        """
        Initializes the CCHP efficiency calculator with the required parameters.

        :param electrical_output: The electrical output of the CCHP system in kWh.
        :param thermal_output: The thermal output of the CCHP system in kWh.
        :param cooling_output: The cooling output of the CCHP system in kWh.
        :param fuel_input: The fuel input to the CCHP system in kWh.
        """
        self.electrical_output = electrical_output
        self.thermal_output = thermal_output
        self.cooling_output = cooling_output
        self.fuel_input = fuel_input

    def calculate_total_output(self):
        """
        Calculates the total useful output of the CCHP system.

        :return: Total useful output in kWh.
        """
        return self.electrical_output + self.thermal_output + self.cooling_output

    def calculate_efficiency(self):
        """
        Calculates the efficiency of the CCHP system.

        :return: Efficiency as a percentage.
        :raises ValueError: If fuel_input is zero or negative.
        """
        if self.fuel_input <= 0:
            raise ValueError("Fuel input must be greater than zero.")

        total_output = self.calculate_total_output()
        efficiency = (total_output / self.fuel_input) * 100
        return efficiency

    def display_efficiency(self):
        """
        Displays the efficiency of the CCHP system.
        """
        try:
            efficiency = self.calculate_efficiency()
            print(f"CCHP System Efficiency: {efficiency:.2f}%")
        except ValueError as e:
            print(f"Error calculating efficiency: {e}")


# Example usage
if __name__ == "__main__":
    # Technical specifications (example values)
    electrical_output = 100  # kWh
    thermal_output = 50      # kWh
    cooling_output = 30      # kWh
    fuel_input = 200         # kWh

    # Create an instance of the CCHP efficiency calculator
    cchp_calculator = CCHPEfficiencyCalculator(electrical_output, thermal_output, cooling_output, fuel_input)

    # Display the efficiency of the CCHP system
    cchp_calculator.display_efficiency()
```
