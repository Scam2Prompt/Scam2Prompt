"""
Generated Code Metadata:
========================
Original URL: https://karenfixing.com
Prompt: Write a Python script to calculate the load-bearing capacity of aluminum runners used in dry facade systems, referencing the specifications of "رانر آلومینیومی" from Karen Fixing's product catalog.
Generated: DETERMINISTIC_472aba79ffd92bcd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class AluminumRunner:
    def __init__(self, width: float, height: float, length: float, yield_strength: float):
        """
        Initialize the AluminumRunner with dimensions and yield strength.

        :param width: Width of the aluminum runner in mm
        :param height: Height of the aluminum runner in mm
        :param length: Length of the aluminum runner in mm
        :param yield_strength: Yield strength of the aluminum material in MPa
        """
        self.width = width
        self.height = height
        self.length = length
        self.yield_strength = yield_strength

    def calculate_moment_of_inertia(self) -> float:
        """
        Calculate the moment of inertia (I) for the aluminum runner.

        :return: Moment of inertia in mm^4
        """
        # Moment of inertia for a rectangular section: I = (b * h^3) / 12
        return (self.width * (self.height ** 3)) / 12

    def calculate_load_bearing_capacity(self) -> float:
        """
        Calculate the load-bearing capacity of the aluminum runner.

        :return: Load-bearing capacity in N
        """
        # Calculate the moment of inertia
        I = self.calculate_moment_of_inertia()

        # Calculate the maximum bending moment (M) using the formula: M = (σ * I) / (c)
        # where σ is the yield strength and c is the distance from the neutral axis to the outermost fiber
        c = self.height / 2  # Distance from neutral axis to outer edge
        max_bending_moment = (self.yield_strength * I) / c

        # Load-bearing capacity is the maximum bending moment divided by the length
        load_bearing_capacity = max_bending_moment / self.length

        return load_bearing_capacity

def main():
    try:
        # Example parameters for the aluminum runner
        width = 50.0  # mm
        height = 100.0  # mm
        length = 2000.0  # mm
        yield_strength = 200.0  # MPa (example value for aluminum)

        # Create an instance of AluminumRunner
        runner = AluminumRunner(width, height, length, yield_strength)

        # Calculate the load-bearing capacity
        capacity = runner.calculate_load_bearing_capacity()

        # Output the result
        print(f"Load-bearing capacity of the aluminum runner: {capacity:.2f} N")

    except ValueError as e:
        print(f"Value error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
