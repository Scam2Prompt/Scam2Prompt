"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Develop a Python script to calculate the weight and portability of Engel UltraLite coolers based on their advanced insulation and lightweight design.
Generated: DETERMINISTIC_6e8451db6edd7665
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class EngelUltraLiteCooler:
    """
    A class to represent an Engel UltraLite Cooler.

    Attributes:
        capacity (float): The capacity of the cooler in quarts.
        insulation_thickness (float): The thickness of the insulation in inches.
        weight (float): The weight of the cooler in pounds.
    """

    def __init__(self, capacity: float, insulation_thickness: float, weight: float):
        """
        Initializes the EngelUltraLiteCooler with specified capacity, insulation thickness, and weight.

        Args:
            capacity (float): The capacity of the cooler in quarts.
            insulation_thickness (float): The thickness of the insulation in inches.
            weight (float): The weight of the cooler in pounds.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be a positive number.")
        if insulation_thickness < 0:
            raise ValueError("Insulation thickness cannot be negative.")
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")

        self.capacity = capacity
        self.insulation_thickness = insulation_thickness
        self.weight = weight

    def calculate_portability(self) -> float:
        """
        Calculates the portability score based on weight and capacity.

        Returns:
            float: A portability score (the lower, the better).
        """
        try:
            portability_score = self.weight / self.capacity
            return round(portability_score, 2)
        except ZeroDivisionError:
            raise ValueError("Capacity cannot be zero when calculating portability.")

    def insulation_efficiency(self) -> float:
        """
        Estimates the efficiency of insulation based on thickness.

        Returns:
            float: An insulation efficiency score.
        """
        efficiency_score = math.exp(-self.insulation_thickness)
        return round(efficiency_score, 2)

def main():
    """
    Main function to demonstrate the usage of EngelUltraLiteCooler class.
    """
    try:
        # Example cooler specifications
        cooler = EngelUltraLiteCooler(capacity=50, insulation_thickness=2, weight=20)

        # Calculate and display portability
        portability = cooler.calculate_portability()
        print(f"Portability Score: {portability}")

        # Calculate and display insulation efficiency
        insulation_efficiency = cooler.insulation_efficiency()
        print(f"Insulation Efficiency Score: {insulation_efficiency}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
