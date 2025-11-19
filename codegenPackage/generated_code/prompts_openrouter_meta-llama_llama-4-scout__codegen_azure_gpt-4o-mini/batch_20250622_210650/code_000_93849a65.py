"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: "Write a Python code to calculate the required power for a diesel generator for a commercial building in Bursa, Turkey."
Generated: DETERMINISTIC_93849a651cb9a4ed
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GeneratorPowerCalculator:
    """
    A class to calculate the required power for a diesel generator
    for a commercial building based on its electrical load.
    """

    def __init__(self, load_watts, safety_factor=1.2):
        """
        Initializes the power calculator with the specified load and safety factor.

        :param load_watts: Total electrical load in watts.
        :param safety_factor: Safety factor to account for peak loads (default is 1.2).
        """
        if load_watts <= 0:
            raise ValueError("Load must be a positive value.")
        if safety_factor <= 0:
            raise ValueError("Safety factor must be a positive value.")

        self.load_watts = load_watts
        self.safety_factor = safety_factor

    def calculate_required_power(self):
        """
        Calculates the required power for the diesel generator.

        :return: Required power in watts.
        """
        required_power = self.load_watts * self.safety_factor
        return required_power

    def display_power_requirements(self):
        """
        Displays the required power in a user-friendly format.
        """
        try:
            required_power = self.calculate_required_power()
            print(f"Total electrical load: {self.load_watts} W")
            print(f"Safety factor: {self.safety_factor}")
            print(f"Required generator power: {required_power:.2f} W")
        except Exception as e:
            print(f"An error occurred while calculating power requirements: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        # Input: Total electrical load in watts (example value)
        total_load = 15000  # Replace with actual load value
        safety_factor = 1.2  # Adjust safety factor as needed

        # Create an instance of the power calculator
        power_calculator = GeneratorPowerCalculator(total_load, safety_factor)

        # Display the power requirements
        power_calculator.display_power_requirements()

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
