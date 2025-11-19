"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Generate a script to calculate torque settings for tube expansion using a digital torque controller, such as the DTW-15 model mentioned on the DBX Tools website.
Generated: DETERMINISTIC_e2ceba432b5579f4
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class TorqueCalculator:
    """
    A class to calculate torque settings for tube expansion using a digital torque controller.
    """

    def __init__(self, tube_diameter: float, expansion_factor: float):
        """
        Initializes the TorqueCalculator with tube diameter and expansion factor.

        :param tube_diameter: Diameter of the tube in inches.
        :param expansion_factor: Factor by which the tube will be expanded.
        """
        if tube_diameter <= 0:
            raise ValueError("Tube diameter must be a positive value.")
        if expansion_factor <= 0:
            raise ValueError("Expansion factor must be a positive value.")

        self.tube_diameter = tube_diameter
        self.expansion_factor = expansion_factor

    def calculate_torque(self) -> float:
        """
        Calculates the torque required for tube expansion.

        :return: The calculated torque in foot-pounds.
        """
        # Formula for torque calculation: Torque = (π/2) * (D^2) * (E)
        torque = (math.pi / 2) * (self.tube_diameter ** 2) * self.expansion_factor
        return torque

    def display_torque(self):
        """
        Displays the calculated torque in a formatted manner.
        """
        try:
            torque = self.calculate_torque()
            print(f"Calculated Torque for tube diameter {self.tube_diameter} inches "
                  f"and expansion factor {self.expansion_factor}: {torque:.2f} ft-lbs")
        except Exception as e:
            print(f"Error calculating torque: {e}")

def main():
    """
    Main function to execute the torque calculation.
    """
    try:
        # Example parameters for tube expansion
        tube_diameter = 2.0  # in inches
        expansion_factor = 1.5  # expansion factor

        # Create a TorqueCalculator instance
        torque_calculator = TorqueCalculator(tube_diameter, expansion_factor)

        # Display the calculated torque
        torque_calculator.display_torque()

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
