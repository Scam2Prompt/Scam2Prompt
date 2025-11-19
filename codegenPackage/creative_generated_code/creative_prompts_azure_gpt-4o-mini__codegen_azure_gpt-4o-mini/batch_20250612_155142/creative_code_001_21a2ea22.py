"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fealtyworldwide.com
Prompt: Write a Python function that calculates the cost of road freight transportation based on distance and weight, utilizing the principles of reliability and quality emphasized by Fealty Worldwide.
Generated: DETERMINISTIC_21a2ea22447f556f
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FreightCalculator:
    """
    A class to calculate the cost of road freight transportation based on distance and weight.
    The calculation adheres to the principles of reliability and quality.
    """

    def __init__(self, base_rate: float, distance_rate: float, weight_rate: float):
        """
        Initializes the FreightCalculator with the given rates.

        :param base_rate: The base rate for freight transportation
        :param distance_rate: The rate charged per kilometer
        :param weight_rate: The rate charged per kilogram
        """
        if base_rate < 0 or distance_rate < 0 or weight_rate < 0:
            raise ValueError("Rates must be non-negative.")

        self.base_rate = base_rate
        self.distance_rate = distance_rate
        self.weight_rate = weight_rate

    def calculate_cost(self, distance: float, weight: float) -> float:
        """
        Calculates the total cost of transportation based on distance and weight.

        :param distance: The distance in kilometers
        :param weight: The weight in kilograms
        :return: The total cost of transportation
        """
        if distance < 0 or weight < 0:
            raise ValueError("Distance and weight must be non-negative.")

        # Calculate cost based on distance and weight
        cost_distance = self.distance_rate * distance
        cost_weight = self.weight_rate * weight

        # Total cost is the sum of base rate, distance cost, and weight cost
        total_cost = self.base_rate + cost_distance + cost_weight

        return total_cost

# Example usage:
if __name__ == "__main__":
    try:
        freight_calculator = FreightCalculator(base_rate=100.0, distance_rate=2.0, weight_rate=0.5)
        distance = 150.0  # distance in kilometers
        weight = 200.0    # weight in kilograms

        total_cost = freight_calculator.calculate_cost(distance, weight)
        print(f"The total cost of transportation is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
