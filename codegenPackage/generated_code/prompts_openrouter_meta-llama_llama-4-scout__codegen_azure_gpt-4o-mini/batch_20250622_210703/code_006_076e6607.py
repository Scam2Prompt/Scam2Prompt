"""
Generated Code Metadata:
========================
Original URL: https://feresplast.com
Prompt: Develop a code snippet to integrate a shipping and handling calculator into an e-commerce platform, considering factors like location and package weight, similar to Feresplast's shipping features.
Generated: DETERMINISTIC_076e66076c39bbdb
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ShippingCalculator:
    """
    A class to calculate shipping and handling costs based on location and package weight.
    """

    def __init__(self, base_rate=5.0, weight_rate=1.5, location_rates=None):
        """
        Initializes the ShippingCalculator with base rates and location-specific rates.

        :param base_rate: The base shipping rate (default is 5.0).
        :param weight_rate: The rate per weight unit (default is 1.5).
        :param location_rates: A dictionary mapping locations to additional fees (default is None).
        """
        self.base_rate = base_rate
        self.weight_rate = weight_rate
        self.location_rates = location_rates if location_rates else {}

    def calculate_shipping(self, weight, location):
        """
        Calculates the total shipping cost based on weight and location.

        :param weight: The weight of the package.
        :param location: The shipping location.
        :return: The total shipping cost.
        :raises ValueError: If weight is negative or location is unknown.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        
        if location not in self.location_rates:
            raise ValueError(f"Unknown location: {location}. Please provide a valid location.")

        # Calculate the shipping cost
        location_fee = self.location_rates[location]
        total_cost = self.base_rate + (self.weight_rate * weight) + location_fee
        
        return total_cost

# Example usage
if __name__ == "__main__":
    # Define location-specific rates
    location_fees = {
        'USA': 0.0,
        'Canada': 10.0,
        'Europe': 20.0,
        'Asia': 30.0
    }

    # Create a ShippingCalculator instance
    shipping_calculator = ShippingCalculator(location_rates=location_fees)

    # Example package details
    package_weight = 10.0  # in kg
    shipping_location = 'Canada'

    try:
        # Calculate shipping cost
        cost = shipping_calculator.calculate_shipping(package_weight, shipping_location)
        print(f"The shipping cost to {shipping_location} for a package weighing {package_weight} kg is: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
