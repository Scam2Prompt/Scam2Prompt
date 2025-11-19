"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Generate a Python script to calculate the total weight and quantity of stainless steel screws based on the specifications provided by APN Hardware.
Generated: DETERMINISTIC_4d60e82f9fa42bda
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# stainless_steel_screw_calculator.py

class Screw:
    def __init__(self, diameter: float, length: float, weight_per_unit: float, quantity: int):
        """
        Initialize a Screw instance.

        :param diameter: Diameter of the screw in millimeters
        :param length: Length of the screw in millimeters
        :param weight_per_unit: Weight of a single screw in grams
        :param quantity: Number of screws
        """
        self.diameter = diameter
        self.length = length
        self.weight_per_unit = weight_per_unit
        self.quantity = quantity

    def total_weight(self) -> float:
        """
        Calculate the total weight of the screws.

        :return: Total weight in grams
        """
        return self.weight_per_unit * self.quantity

    def total_quantity(self) -> int:
        """
        Get the total quantity of screws.

        :return: Total quantity of screws
        """
        return self.quantity


def main():
    try:
        # Example specifications for stainless steel screws
        screw_diameter = 4.0  # in mm
        screw_length = 25.0    # in mm
        screw_weight_per_unit = 5.0  # in grams
        screw_quantity = 100   # total number of screws

        # Create a Screw instance
        screw = Screw(screw_diameter, screw_length, screw_weight_per_unit, screw_quantity)

        # Calculate total weight and quantity
        total_weight = screw.total_weight()
        total_quantity = screw.total_quantity()

        # Display the results
        print(f"Total Quantity of Screws: {total_quantity}")
        print(f"Total Weight of Screws: {total_weight:.2f} grams")

    except ValueError as e:
        print(f"Value error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
