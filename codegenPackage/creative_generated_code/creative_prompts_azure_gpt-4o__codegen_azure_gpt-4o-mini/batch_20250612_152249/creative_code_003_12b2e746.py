"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramjiacro.com
Prompt: Write a program that calculates the production output of acrylic yarns based on machine efficiency and operating hours, using data inputs like yarn type and machinery specifications.
Generated: DETERMINISTIC_12b2e746741475e4
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class YarnProductionCalculator:
    """
    A class to calculate the production output of acrylic yarns based on machine efficiency and operating hours.
    """

    def __init__(self, yarn_type: str, machine_efficiency: float, operating_hours: float):
        """
        Initialize the calculator with yarn type, machine efficiency, and operating hours.

        :param yarn_type: Type of yarn (str)
        :param machine_efficiency: Efficiency of the machine (percentage as a float, e.g., 0.85 for 85%)
        :param operating_hours: Total operating hours (float)
        """
        self.yarn_type = yarn_type
        self.machine_efficiency = machine_efficiency
        self.operating_hours = operating_hours

        # Validate inputs
        self.validate_inputs()

    def validate_inputs(self):
        """
        Validate the inputs to ensure they are within acceptable ranges.
        """
        if not isinstance(self.yarn_type, str) or not self.yarn_type:
            raise ValueError("Yarn type must be a non-empty string.")
        if not (0 <= self.machine_efficiency <= 1):
            raise ValueError("Machine efficiency must be a float between 0 and 1.")
        if self.operating_hours < 0:
            raise ValueError("Operating hours must be a non-negative float.")

    def calculate_output(self, output_per_hour: float) -> float:
        """
        Calculate the total production output based on operating hours, machine efficiency, and output per hour.

        :param output_per_hour: Amount of yarn produced per hour (float)
        :return: Total production output (float)
        """
        if output_per_hour < 0:
            raise ValueError("Output per hour must be a non-negative value.")

        # Calculate total output
        total_output = output_per_hour * self.machine_efficiency * self.operating_hours
        return total_output

def main():
    """
    Main function to execute the yarn production calculation.
    """
    try:
        # Example inputs
        yarn_type = "Acrylic"
        machine_efficiency = 0.85  # 85%
        operating_hours = 10.0  # 10 hours
        output_per_hour = 50.0  # 50 units of yarn per hour

        # Create an instance of the calculator
        calculator = YarnProductionCalculator(yarn_type, machine_efficiency, operating_hours)

        # Calculate the production output
        total_output = calculator.calculate_output(output_per_hour)

        # Display the result
        print(f"Total production output for {yarn_type}: {total_output:.2f} units")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
