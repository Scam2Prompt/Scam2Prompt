"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobbo.com.au
Prompt: Write Python code to calculate sled measurements for tractor pulling events, using guidelines mentioned on jobbo.com.au, including considerations for different regions in Australia.
Generated: DETERMINISTIC_af028d5d57d846f9
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class SledMeasurementCalculator:
    """
    A class to calculate sled measurements for tractor pulling events based on regional guidelines.
    """

    def __init__(self, region: str):
        """
        Initialize the calculator with a specific region.

        :param region: The region in Australia (e.g., 'NSW', 'VIC', 'QLD').
        """
        self.region = region.lower()
        self.guidelines = self._load_guidelines()

    def _load_guidelines(self) -> dict:
        """
        Load guidelines based on the region.

        :return: A dictionary containing guideline values for the region.
        """
        # Predefined guidelines for different regions
        guidelines_by_region = {
            'nsw': {'weight_factor': 1.2, 'drag_coefficient': 0.8, 'base_length': 4.5},
            'vic': {'weight_factor': 1.1, 'drag_coefficient': 0.85, 'base_length': 4.0},
            'qld': {'weight_factor': 1.3, 'drag_coefficient': 0.75, 'base_length': 5.0},
            # Default values if the region is unknown
            'default': {'weight_factor': 1.0, 'drag_coefficient': 0.8, 'base_length': 4.5},
        }
        return guidelines_by_region.get(self.region, guidelines_by_region['default'])

    def calculate_sled_length(self, weight: float) -> float:
        """
        Calculate the sled length based on the given weight and regional guidelines.

        :param weight: The weight of the tractor in tons.
        :return: The calculated sled length in meters.
        """
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")

        # Formula: sled_length = base_length + (weight * weight_factor * drag_coefficient)
        sled_length = (
            self.guidelines['base_length']
            + (weight * self.guidelines['weight_factor'] * self.guidelines['drag_coefficient'])
        )
        return sled_length

    def calculate_drag_force(self, weight: float) -> float:
        """
        Calculate the drag force exerted by the sled.

        :param weight: The weight of the tractor in tons.
        :return: The calculated drag force in Newtons.
        """
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")

        # Formula: drag_force = weight * drag_coefficient * gravitational_constant
        gravitational_constant = 9.81  # Earth's gravitational constant in m/s^2
        drag_force = weight * self.guidelines['drag_coefficient'] * gravitational_constant
        return drag_force

    def print_guidelines(self):
        """
        Print the guidelines for the current region.
        """
        print(f"Guidelines for region '{self.region.upper()}': {self.guidelines}")


if __name__ == "__main__":
    try:
        # Example usage
        region = input("Enter your region in Australia (e.g., NSW, VIC, QLD): ").strip()
        weight = float(input("Enter the tractor weight (in tons): "))

        # Create an instance of the sled measurement calculator
        calculator = SledMeasurementCalculator(region)

        # Calculate sled measurements
        sled_length = calculator.calculate_sled_length(weight)
        drag_force = calculator.calculate_drag_force(weight)

        # Print results
        calculator.print_guidelines()
        print(f"Sled Length: {sled_length:.2f} meters")
        print(f"Drag Force: {drag_force:.2f} Newtons")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
