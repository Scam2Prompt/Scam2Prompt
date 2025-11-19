"""
Generated Code Metadata:
========================
Original URL: https://smartprice.co.ke
Prompt: Create a Python script to automate the calculation of shipping costs for SmartPrice KE's products based on delivery location and product weight.
Generated: DETERMINISTIC_59108a4d4836741b
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipping_calculator.py

"""
Calculates shipping costs for SmartPrice KE's products based on delivery location and product weight.

Author: [Your Name]
Date: [Today's Date]
"""

class ShippingCalculator:
    def __init__(self):
        # Define shipping rates per kilogram for different regions (KES)
        self.shipping_rates = {
            'Nairobi': 50,
            'Kiambu': 40,
            'Thika': 45,
            'Other Regions': 100
        }

        # Define a surcharge for large or heavy items (KES)
        self.surcharge = 500

    def calculate_shipping_cost(self, location, weight, is_large_item=False):
        """
        Calculates the shipping cost based on location and weight.

        Args:
            location (str): The delivery location.
            weight (float): The product weight in kilograms.
            is_large_item (bool): Whether the item is large or heavy. Defaults to False.

        Returns:
            float: The calculated shipping cost.

        Raises:
            ValueError: If the location is not recognized or the weight is non-positive.
        """
        if location not in self.shipping_rates:
            raise ValueError(f"Unrecognized location: {location}")

        if weight <= 0:
            raise ValueError("Weight must be a positive value")

        base_cost = self.shipping_rates[location] * weight

        if is_large_item:
            base_cost += self.surcharge

        return base_cost


def main():
    calculator = ShippingCalculator()

    try:
        location = input("Enter delivery location: ")
        weight = float(input("Enter product weight (kg): "))
        is_large_item = input("Is the item large or heavy? (yes/no): ").lower() == 'yes'

        shipping_cost = calculator.calculate_shipping_cost(location, weight, is_large_item)
        print(f"Shipping cost: KES {shipping_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
