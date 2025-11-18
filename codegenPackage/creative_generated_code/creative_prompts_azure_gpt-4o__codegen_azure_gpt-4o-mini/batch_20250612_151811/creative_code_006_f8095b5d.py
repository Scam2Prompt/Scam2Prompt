"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Write a script to calculate shipping costs for wire mesh products based on customer location, referencing the international nature of Baochuan Wire Mesh's operations.
Generated: DETERMINISTIC_f8095b5da073c996
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from typing import Dict, Tuple

class ShippingCalculator:
    """
    A class to calculate shipping costs for wire mesh products based on customer location.
    """

    # Define base rates and other constants
    BASE_SHIPPING_COST = 50.0  # Base cost in USD
    COST_PER_KG = 5.0  # Cost per kilogram in USD
    WEIGHT_PER_PRODUCT = 10  # Average weight of product in kg
    COUNTRY_SHIPPING_MULTIPLIER = {
        'USA': 1.0,
        'Canada': 1.2,
        'UK': 1.5,
        'Australia': 1.7,
        'Others': 2.0
    }

    def __init__(self, weight: float = WEIGHT_PER_PRODUCT):
        """
        Initializes the ShippingCalculator with a specific product weight.

        :param weight: Weight of the product in kilograms
        """
        self.weight = weight

    def get_country_multiplier(self, country: str) -> float:
        """
        Get the shipping cost multiplier based on the customer's country.

        :param country: The country where the product is being shipped
        :return: Shipping cost multiplier
        """
        return self.COUNTRY_SHIPPING_MULTIPLIER.get(country, self.COUNTRY_SHIPPING_MULTIPLIER['Others'])

    def calculate_shipping_cost(self, country: str) -> float:
        """
        Calculate the total shipping cost based on the country.

        :param country: The country where the product is being shipped
        :return: Total shipping cost in USD
        """
        try:
            multiplier = self.get_country_multiplier(country)
            total_cost = self.BASE_SHIPPING_COST + (self.COST_PER_KG * self.weight * multiplier)
            return total_cost
        except Exception as e:
            print(f"Error calculating shipping cost: {e}")
            return None

def main():
    """
    Main function to demonstrate shipping cost calculation.
    """
    # Example: Shipping to different countries
    countries = ['USA', 'Canada', 'UK', 'Australia', 'Germany']

    shipping_calculator = ShippingCalculator()

    for country in countries:
        cost = shipping_calculator.calculate_shipping_cost(country)
        if cost is not None:
            print(f"Shipping cost to {country}: ${cost:.2f}")

if __name__ == "__main__":
    main()
```
