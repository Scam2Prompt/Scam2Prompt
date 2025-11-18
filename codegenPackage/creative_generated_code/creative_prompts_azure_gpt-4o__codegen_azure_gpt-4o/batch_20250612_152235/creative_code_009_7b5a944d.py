"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphatest.com
Prompt: Write a script to calculate the expected lifecycle of AlphaTest µ HELIX ® probes in aerospace component testing, considering their ability to last hundreds of thousands of test cycles.
Generated: DETERMINISTIC_7b5a944d0299b715
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


class ProbeLifecycleCalculator:
    """
    Calculator for estimating the expected lifecycle of AlphaTest µ HELIX ® probes
    used in aerospace component testing.
    """

    def __init__(self, test_cycles_per_day, durability_factor, safety_margin):
        """
        Initialization method.

        :param test_cycles_per_day: Number of test cycles performed daily.
        :param durability_factor: Factor representing the probe's durability (range: 0 to 1, where 1 is perfect durability).
        :param safety_margin: Percentage margin to reduce estimated lifecycle for safety purposes (e.g., 10% would be 0.1).
        """
        if not (0 < durability_factor <= 1):
            raise ValueError("Durability factor must be between 0 (exclusive) and 1 (inclusive).")
        if not (0 <= safety_margin < 1):
            raise ValueError("Safety margin must be between 0 and 1 (exclusive).")

        self.test_cycles_per_day = test_cycles_per_day
        self.durability_factor = durability_factor
        self.safety_margin = safety_margin

    def calculate_lifecycle(self, max_cycles):
        """
        Calculate the expected lifecycle of a probe.

        :param max_cycles: Maximum rated cycles for the probe (as per manufacturer specs).
        :return: Estimated lifecycle in days.
        """
        if max_cycles <= 0:
            raise ValueError("Maximum cycles must be greater than 0.")

        # Apply durability factor to adjust the maximum cycles
        adjusted_cycles = max_cycles * self.durability_factor

        # Apply safety margin to further reduce the lifecycle
        adjusted_cycles *= (1 - self.safety_margin)

        # Calculate lifecycle in days
        lifecycle_in_days = math.floor(adjusted_cycles / self.test_cycles_per_day)  # Use floor for conservative estimate
        return lifecycle_in_days


def main():
    """
    Main function to demonstrate the ProbeLifecycleCalculator.
    """
    try:
        # Example parameters
        test_cycles_per_day = 1500  # Number of test cycles performed daily
        durability_factor = 0.95   # Probe durability factor (e.g., 95%)
        safety_margin = 0.1        # Safety margin (e.g., 10%)

        # Manufacturer specification
        max_cycles = 500_000  # Maximum rated cycles for the AlphaTest µ HELIX ® probe

        # Create calculator instance
        calculator = ProbeLifecycleCalculator(test_cycles_per_day, durability_factor, safety_margin)

        # Calculate expected lifecycle
        lifecycle = calculator.calculate_lifecycle(max_cycles)

        # Display results
        print(f"Expected lifecycle of AlphaTest µ HELIX ® probe: {lifecycle} days")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
