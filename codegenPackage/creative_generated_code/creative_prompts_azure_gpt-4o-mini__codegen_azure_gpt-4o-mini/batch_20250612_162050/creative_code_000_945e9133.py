"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birlikjenerator.com
Prompt: Write a Python script to calculate the optimal generator size based on power and location assessment as described on the Birlik Jeneratör website.
Generated: DETERMINISTIC_945e9133da05dff1
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class GeneratorSizeCalculator:
    """
    A class to calculate the optimal generator size based on power requirements
    and location assessment factors.
    """

    def __init__(self, power_requirement_kw, location_factor):
        """
        Initializes the generator size calculator with power requirements and location factor.

        :param power_requirement_kw: Required power in kilowatts (kW)
        :param location_factor: Factor based on location assessment (0 <= location_factor <= 1)
        """
        if power_requirement_kw <= 0:
            raise ValueError("Power requirement must be greater than zero.")
        if not (0 <= location_factor <= 1):
            raise ValueError("Location factor must be between 0 and 1.")
        
        self.power_requirement_kw = power_requirement_kw
        self.location_factor = location_factor
        self.optimal_size_kw = None

    def calculate_optimal_size(self):
        """
        Calculates the optimal generator size using the power requirement and location factor.

        :return: The optimal generator size in kilowatts (kW)
        """
        # Adjust power requirement based on location factor
        adjusted_power = self.power_requirement_kw / (1 - self.location_factor)
        self.optimal_size_kw = math.ceil(adjusted_power)

        return self.optimal_size_kw

    def display_optimal_size(self):
        """
        Displays the optimal generator size.
        """
        if self.optimal_size_kw is None:
            raise RuntimeError("Optimal size has not been calculated. Call calculate_optimal_size() first.")

        print(f"The optimal generator size is: {self.optimal_size_kw} kW")


def main():
    """
    Main entry point of the script. Gets user input and calculates the optimal generator size.
    """
    try:
        power_requirement = float(input("Enter the power requirement in kW: "))
        location_factor = float(input("Enter the location factor (0 to 1): "))

        # Create an instance of the calculator
        calculator = GeneratorSizeCalculator(power_requirement, location_factor)

        # Calculate the optimal generator size
        optimal_size = calculator.calculate_optimal_size()

        # Display the result
        calculator.display_optimal_size()

    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
