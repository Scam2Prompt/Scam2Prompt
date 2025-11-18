"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftimus.com
Prompt: Write Python code to calculate the shipping cost for bulk orders of Himalayan salt products, considering weight and destination zones as described by Craftimus Industries.
Generated: DETERMINISTIC_8746b639f74cd79c
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShippingCostCalculator:
    """
    A class to calculate the shipping cost for bulk orders of Himalayan salt products.

    Attributes:
        base_rate (float): The base shipping rate per pound.
        zone_rates (dict): A dictionary mapping destination zones to their respective multipliers.
    """

    def __init__(self, base_rate: float):
        """
        Initializes the ShippingCostCalculator with a base shipping rate.

        Args:
            base_rate (float): The base shipping rate per pound.
        """
        if base_rate < 0:
            raise ValueError("Base rate must be a non-negative value.")
        self.base_rate = base_rate
        self.zone_rates = {
            'A': 1.0,  # Zone A multiplier
            'B': 1.5,  # Zone B multiplier
            'C': 2.0,  # Zone C multiplier
            'D': 2.5   # Zone D multiplier
        }

    def calculate_shipping_cost(self, weight: float, destination_zone: str) -> float:
        """
        Calculates the shipping cost based on the weight of the order and destination zone.

        Args:
            weight (float): The weight of the order in pounds.
            destination_zone (str): The destination zone (A, B, C, D).

        Returns:
            float: The total shipping cost.

        Raises:
            ValueError: If weight is negative or if the destination zone is invalid.
        """
        if weight < 0:
            raise ValueError("Weight must be a non-negative value.")
        
        if destination_zone not in self.zone_rates:
            raise ValueError("Invalid destination zone. Valid zones are: A, B, C, D.")

        # Calculate shipping cost
        multiplier = self.zone_rates[destination_zone]
        shipping_cost = self.base_rate * weight * multiplier
        return shipping_cost


if __name__ == "__main__":
    try:
        # Example usage
        base_rate_per_pound = 5.0  # Define the base rate for shipping
        calculator = ShippingCostCalculator(base_rate_per_pound)

        # Example order
        order_weight = 10.0  # Weight in pounds
        destination = 'B'    # Destination zone

        cost = calculator.calculate_shipping_cost(order_weight, destination)
        print(f"The shipping cost for {order_weight} lbs to zone {destination} is: ${cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
