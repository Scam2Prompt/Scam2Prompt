"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homlukkkkkkkkh.pages.dev
Prompt: Generate a Python script to calculate shipping costs for Condi Shop orders based on product weight and delivery location, referencing categories like "Disposable baking molds" and "Gift packaging."
Generated: DETERMINISTIC_54b48a65c1a02f2a
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ShippingCalculator:
    """
    A class to calculate shipping costs for Condi Shop orders.
    """

    # Shipping rates per weight category (in kg)
    SHIPPING_RATES = {
        "local": {  # Rates for local delivery
            "0-1": 5.00,
            "1-5": 10.00,
            "5-10": 15.00,
            "10+": 20.00,
        },
        "national": {  # Rates for national delivery
            "0-1": 10.00,
            "1-5": 20.00,
            "5-10": 30.00,
            "10+": 40.00,
        },
    }

    def __init__(self, delivery_location: str):
        """
        Initializes the ShippingCalculator with the specified delivery location.
        
        :param delivery_location: The delivery location (local or national).
        """
        if delivery_location.lower() not in self.SHIPPING_RATES:
            raise ValueError("Invalid delivery location. Choose 'local' or 'national'.")
        self.delivery_location = delivery_location.lower()

    def calculate_cost(self, product_weight: float) -> float:
        """
        Calculates the shipping cost based on product weight and delivery location.

        :param product_weight: The weight of the product in kilograms.
        :return: The calculated shipping cost.
        :raises ValueError: If product_weight is negative.
        """
        if product_weight < 0:
            raise ValueError("Product weight cannot be negative.")

        # Determine the applicable weight category for pricing
        if product_weight <= 1:
            weight_category = "0-1"
        elif product_weight <= 5:
            weight_category = "1-5"
        elif product_weight <= 10:
            weight_category = "5-10"
        else:
            weight_category = "10+"

        # Retrieve the shipping cost based on delivery location and weight category
        cost = self.SHIPPING_RATES[self.delivery_location].get(weight_category)
        return cost if cost is not None else 0.0


def main():
    """
    Main function to execute the shipping cost calculation.
    """
    try:
        # Sample weights for demonstration purposes
        products = [
            {"name": "Disposable baking molds", "weight": 2.5},
            {"name": "Gift packaging", "weight": 0.5},
            {"name": "Large baking tray", "weight": 12.0},
        ]

        # Set delivery location
        delivery_location = "national"  # Can be 'local' or 'national'
        calculator = ShippingCalculator(delivery_location)

        # Calculate and display shipping costs for each product
        for product in products:
            shipping_cost = calculator.calculate_cost(product["weight"])
            print(f"Shipping cost for {product['name']} (weight: {product['weight']}kg): ${shipping_cost:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
