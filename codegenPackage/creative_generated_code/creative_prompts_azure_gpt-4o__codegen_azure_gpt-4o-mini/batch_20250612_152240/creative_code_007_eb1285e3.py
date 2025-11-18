"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neumayaa.com.ar
Prompt: Generate code to calculate the optimal tire pressure for various heavy machinery types, incorporating Neumayaa's guidance on nitrogen inflation and regular pressure checks.
Generated: DETERMINISTIC_eb1285e3ae5e92c7
Batch ID: 20250612_152240
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
    A class to calculate optimal tire pressure for various types of heavy machinery.
    Incorporates Neumayya's guidance on nitrogen inflation and regular pressure checks.
    """

    # Dictionary to hold optimal tire pressures (in PSI) for different machinery types
    optimal_pressures = {
        "excavator": 30,
        "bulldozer": 25,
        "crane": 35,
        "loader": 32,
        "forklift": 20
    }

    def __init__(self, machinery_type, nitrogen_inflated=True):
        """
        Initializes the TirePressureCalculator with machinery type and nitrogen inflation preference.

        :param machinery_type: Type of the heavy machinery
        :param nitrogen_inflated: Boolean indicating if nitrogen inflation is preferred
        """
        self.machinery_type = machinery_type.lower()
        self.nitrogen_inflated = nitrogen_inflated

        # Validate machinery type
        if self.machinery_type not in self.optimal_pressures:
            raise ValueError(f"Invalid machinery type: {self.machinery_type}. "
                             f"Valid types are: {', '.join(self.optimal_pressures.keys())}")

    def get_optimal_pressure(self):
        """
        Returns the optimal tire pressure for the machinery type.

        :return: Optimal tire pressure in PSI
        """
        if self.nitrogen_inflated:
            return self.optimal_pressures[self.machinery_type] * 1.1  # Adjust for nitrogen inflation
        return self.optimal_pressures[self.machinery_type]

    def check_pressure(self, current_pressure):
        """
        Checks if the current tire pressure is within the recommended range.

        :param current_pressure: Current tire pressure in PSI
        :return: A message indicating if the pressure is optimal, low, or high
        """
        optimal_pressure = self.get_optimal_pressure()
        if current_pressure < optimal_pressure * 0.9:
            return "Tire pressure is too low. Please inflate to optimal levels."
        elif current_pressure > optimal_pressure * 1.1:
            return "Tire pressure is too high. Please deflate to optimal levels."
        else:
            return "Tire pressure is optimal."

# Example usage
if __name__ == "__main__":
    try:
        # Create a TirePressureCalculator for an excavator inflated with nitrogen
        excavator_pressure_calculator = TirePressureCalculator("excavator", nitrogen_inflated=True)

        # Get the optimal pressure
        optimal_pressure = excavator_pressure_calculator.get_optimal_pressure()
        print(f"Optimal tire pressure for excavator (nitrogen inflated): {optimal_pressure:.2f} PSI")

        # Check current tire pressure
        current_pressure = 28  # Example current pressure
        pressure_check_message = excavator_pressure_calculator.check_pressure(current_pressure)
        print(pressure_check_message)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
