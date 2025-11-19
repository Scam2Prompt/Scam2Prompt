"""
Generated Code Metadata:
========================
Original URL: https://cemnazmakine.com
Prompt: Generate a Python script to calculate the efficiency of a potato peeling machine, using parameters like capacity and technical specifications mentioned on the CEMNAZ Makine website.
Generated: DETERMINISTIC_dd7d78b936cc0eea
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# potato_peeler_efficiency_calculator.py

import math

class PotatoPeeler:
    def __init__(self, capacity, peeling_efficiency, peeling_speed, 
                 potato_size, peeling_thickness):
        """
        Initialize the PotatoPeeler class.

        Args:
            capacity (float): The capacity of the machine in kg/h.
            peeling_efficiency (float): The peeling efficiency of the machine in %.
            peeling_speed (float): The peeling speed of the machine in m/min.
            potato_size (float): The average size of the potatoes in cm.
            peeling_thickness (float): The peeling thickness in mm.
        """
        self.capacity = capacity
        self.peeling_efficiency = peeling_efficiency / 100  # Convert to decimal
        self.peeling_speed = peeling_speed
        self.potato_size = potato_size / 100  # Convert to meters
        self.peeling_thickness = peeling_thickness / 1000  # Convert to meters

    def calculate_efficiency(self):
        """
        Calculate the efficiency of the potato peeling machine.

        Returns:
            float: The efficiency of the machine in %.
        """
        # Theoretical peeling capacity in kg/h
        theoretical_capacity = self.capacity * self.peeling_efficiency

        # Actual peeling capacity in kg/h, considering peeling speed and potato size
        actual_capacity = theoretical_capacity * (self.peeling_speed / 60) * \
            (math.pi * (self.potato_size ** 2) / 4) / (self.peeling_thickness * self.capacity)

        # Efficiency calculation
        efficiency = (actual_capacity / self.capacity) * 100

        return efficiency


def main():
    try:
        # Technical specifications for CEMNAZ Makine potato peeler (example values)
        capacity = 2000  # kg/h
        peeling_efficiency = 95  # %
        peeling_speed = 10  # m/min
        potato_size = 5  # cm
        peeling_thickness = 2  # mm

        peeler = PotatoPeeler(capacity, peeling_efficiency, peeling_speed, 
                              potato_size, peeling_thickness)

        efficiency = peeler.calculate_efficiency()

        print(f"The efficiency of the potato peeling machine is: {efficiency:.2f}%")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
