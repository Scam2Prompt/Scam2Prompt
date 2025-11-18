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
import re

class SledMeasurement:
    """Class to handle sled measurements for tractor pulling events based on regional guidelines."""

    def __init__(self, weight: float, length: float, width: float):
        """
        Initialize the sled measurement with weight, length, and width.

        Args:
            weight (float): The weight of the sled in kilograms.
            length (float): The length of the sled in meters.
            width (float): The width of the sled in meters.
        """
        self.weight = weight
        self.length = length
        self.width = width

    def validate_measurements(self):
        """Validate the sled measurements to ensure they are within acceptable ranges."""
        if self.weight <= 0:
            raise ValueError("Weight must be a positive value.")
        if self.length <= 0:
            raise ValueError("Length must be a positive value.")
        if self.width <= 0:
            raise ValueError("Width must be a positive value.")

    def calculate_total_weight(self, additional_weight: float = 0) -> float:
        """
        Calculate the total weight of the sled including any additional weight.

        Args:
            additional_weight (float): The additional weight to add (default is 0).

        Returns:
            float: The total weight of the sled.
        """
        return self.weight + additional_weight

    def calculate_area(self) -> float:
        """
        Calculate the area of the sled's surface.

        Returns:
            float: The area of the sled in square meters.
        """
        return self.length * self.width

    def display_measurements(self):
        """Display the sled measurements and calculated properties."""
        self.validate_measurements()
        total_weight = self.calculate_total_weight()
        area = self.calculate_area()

        print(f"Sled Measurements:")
        print(f" - Weight: {self.weight} kg")
        print(f" - Length: {self.length} m")
        print(f" - Width: {self.width} m")
        print(f" - Total Weight (including additional weight): {total_weight} kg")
        print(f" - Surface Area: {area:.2f} m²")


def main():
    """Main function to execute sled measurements calculation."""
    try:
        # Example sled measurements
        sled = SledMeasurement(weight=500, length=3.5, width=1.2)
        sled.display_measurements()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
