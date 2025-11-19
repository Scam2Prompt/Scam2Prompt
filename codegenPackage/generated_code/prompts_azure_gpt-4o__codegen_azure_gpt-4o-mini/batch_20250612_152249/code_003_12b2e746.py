"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Write a program that calculates the production output of acrylic yarns based on machine efficiency and operating hours, using data inputs like yarn type and machinery specifications.
Generated: DETERMINISTIC_12b2e746741475e4
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class YarnProductionCalculator:
    """
    A class to calculate the production output of acrylic yarns based on machine efficiency and operating hours.
    """

    def __init__(self, yarn_type, machine_efficiency, operating_hours):
        """
        Initializes the YarnProductionCalculator with yarn type, machine efficiency, and operating hours.

        :param yarn_type: str - The type of yarn (e.g., 'Acrylic')
        :param machine_efficiency: float - The efficiency of the machine (0 to 1)
        :param operating_hours: float - The number of hours the machine operates
        """
        self.yarn_type = yarn_type
        self.machine_efficiency = self.validate_efficiency(machine_efficiency)
        self.operating_hours = self.validate_operating_hours(operating_hours)

    @staticmethod
    def validate_efficiency(efficiency):
        """
        Validates the machine efficiency value.

        :param efficiency: float - The efficiency to validate
        :return: float - The validated efficiency
        :raises ValueError: If efficiency is not between 0 and 1
        """
        if not (0 <= efficiency <= 1):
            raise ValueError("Machine efficiency must be between 0 and 1.")
        return efficiency

    @staticmethod
    def validate_operating_hours(hours):
        """
        Validates the operating hours value.

        :param hours: float - The hours to validate
        :return: float - The validated operating hours
        :raises ValueError: If hours is negative
        """
        if hours < 0:
            raise ValueError("Operating hours cannot be negative.")
        return hours

    def calculate_output(self):
        """
        Calculates the production output based on machine efficiency and operating hours.

        :return: float - The total production output in kilograms
        """
        # Assuming a constant production rate per hour for acrylic yarn
        production_rate_per_hour = self.get_production_rate()
        total_output = production_rate_per_hour * self.machine_efficiency * self.operating_hours
        return total_output

    def get_production_rate(self):
        """
        Retrieves the production rate based on the yarn type.

        :return: float - The production rate in kilograms per hour
        :raises ValueError: If the yarn type is not recognized
        """
        production_rates = {
            'Acrylic': 50.0,  # Example production rate for acrylic yarn
            'Wool': 40.0,
            'Cotton': 45.0
        }
        if self.yarn_type not in production_rates:
            raise ValueError(f"Unrecognized yarn type: {self.yarn_type}")
        return production_rates[self.yarn_type]

def main():
    """
    Main function to execute the yarn production calculation.
    """
    try:
        # Example inputs
        yarn_type = 'Acrylic'
        machine_efficiency = 0.85  # 85% efficiency
        operating_hours = 8  # 8 hours of operation

        # Create a YarnProductionCalculator instance
        calculator = YarnProductionCalculator(yarn_type, machine_efficiency, operating_hours)

        # Calculate and print the production output
        output = calculator.calculate_output()
        print(f"Total production output for {yarn_type} yarn: {output:.2f} kg")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
