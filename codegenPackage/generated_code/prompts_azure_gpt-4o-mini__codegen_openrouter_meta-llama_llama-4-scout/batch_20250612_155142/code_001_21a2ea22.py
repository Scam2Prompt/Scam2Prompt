"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: Write a Python function that calculates the cost of road freight transportation based on distance and weight, utilizing the principles of reliability and quality emphasized by Fealty Worldwide.
Generated: DETERMINISTIC_21a2ea22447f556f
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Freight Transportation Cost Calculator

This module provides a function to calculate the cost of road freight transportation
based on distance and weight, following the principles of reliability and quality.

Author: [Your Name]
Date: [Today's Date]
"""

class FreightCalculator:
    def __init__(self, base_rate_per_km, base_rate_per_ton):
        """
        Initializes the FreightCalculator with base rates.

        Args:
            base_rate_per_km (float): Base rate per kilometer.
            base_rate_per_ton (float): Base rate per ton.
        """
        self.base_rate_per_km = base_rate_per_km
        self.base_rate_per_ton = base_rate_per_ton

    def calculate_cost(self, distance_in_km, weight_in_tons):
        """
        Calculates the cost of road freight transportation.

        Args:
            distance_in_km (float): Distance to be traveled in kilometers.
            weight_in_tons (float): Weight of the cargo in tons.

        Returns:
            float: The calculated cost.

        Raises:
            ValueError: If distance or weight is negative.
        """
        if distance_in_km < 0 or weight_in_tons < 0:
            raise ValueError("Distance and weight must be non-negative.")

        # Calculate the cost based on distance and weight
        distance_cost = distance_in_km * self.base_rate_per_km
        weight_cost = weight_in_tons * self.base_rate_per_ton
        total_cost = distance_cost + weight_cost

        return total_cost


def main():
    try:
        # Example usage
        calculator = FreightCalculator(base_rate_per_km=1.5, base_rate_per_ton=2.0)
        distance_in_km = 100
        weight_in_tons = 5
        cost = calculator.calculate_cost(distance_in_km, weight_in_tons)
        print(f"The cost of transporting {weight_in_tons} tons over {distance_in_km} km is: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
