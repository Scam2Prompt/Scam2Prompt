"""
Generated Code Metadata:
========================
Original URL: https://uniaircargo.id
Prompt: Generate a script to automate the calculation of ocean freight shipping costs based on Uniair Cargo's estimated timelines and cost-conscious business model.
Generated: DETERMINISTIC_5a06078726126743
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests

class OceanFreightCalculator:
    """
    A class to calculate ocean freight shipping costs based on Uniair Cargo's estimated timelines and cost model.
    """

    def __init__(self, base_rate, distance_rate, weight_rate):
        """
        Initializes the OceanFreightCalculator with base rates.

        :param base_rate: The base cost for shipping.
        :param distance_rate: Cost per distance unit (e.g., per mile or kilometer).
        :param weight_rate: Cost per weight unit (e.g., per kilogram or pound).
        """
        self.base_rate = base_rate
        self.distance_rate = distance_rate
        self.weight_rate = weight_rate

    def calculate_cost(self, distance, weight):
        """
        Calculates the total shipping cost based on distance and weight.

        :param distance: The distance to be shipped.
        :param weight: The weight of the cargo.
        :return: Total shipping cost.
        """
        if distance < 0 or weight < 0:
            raise ValueError("Distance and weight must be non-negative values.")

        cost = (self.base_rate +
                (self.distance_rate * distance) +
                (self.weight_rate * weight))
        return cost

    def get_estimated_time(self, distance):
        """
        Estimates the shipping time based on distance.

        :param distance: The distance to be shipped.
        :return: Estimated shipping time in days.
        """
        if distance < 0:
            raise ValueError("Distance must be a non-negative value.")

        # Assuming an average speed of 20 nautical miles per day
        average_speed = 20
        estimated_time = distance / average_speed
        return estimated_time

def main():
    """
    Main function to execute the ocean freight cost calculation.
    """
    # Example rates (these should be configured based on Uniair Cargo's pricing model)
    base_rate = 100.0  # Base shipping cost
    distance_rate = 2.0  # Cost per mile
    weight_rate = 0.5  # Cost per kilogram

    # Create an instance of the OceanFreightCalculator
    calculator = OceanFreightCalculator(base_rate, distance_rate, weight_rate)

    # Example input values
    distance = 1000  # Distance in miles
    weight = 500  # Weight in kilograms

    try:
        # Calculate the shipping cost
        cost = calculator.calculate_cost(distance, weight)
        print(f"Total shipping cost: ${cost:.2f}")

        # Get estimated shipping time
        estimated_time = calculator.get_estimated_time(distance)
        print(f"Estimated shipping time: {estimated_time:.2f} days")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
