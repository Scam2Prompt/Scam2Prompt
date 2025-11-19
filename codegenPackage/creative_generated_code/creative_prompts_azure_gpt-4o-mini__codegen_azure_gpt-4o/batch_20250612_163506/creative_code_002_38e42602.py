"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brandforlessegy.com
Prompt: Create a code snippet that utilizes Brandforlessegy's pricing data to calculate discounts for items on sale, specifically for products like the BOSS T-shirt.
Generated: DETERMINISTIC_38e42602a693ccbd
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class DiscountCalculator:
    """
    A class to calculate discounts for items using pricing data.
    """
    def __init__(self, pricing_data):
        """
        Initializes the DiscountCalculator with pricing data.

        :param pricing_data: A dictionary containing product pricing information.
        """
        if not isinstance(pricing_data, dict):
            raise ValueError("Pricing data must be a dictionary.")
        self.pricing_data = pricing_data

    def calculate_discount(self, product_name, sale_percentage):
        """
        Calculates the discounted price for a given product.

        :param product_name: The name of the product.
        :param sale_percentage: The percentage of the discount to apply.
        :return: The discounted price or None if the product is not found.
        """
        if product_name not in self.pricing_data:
            print(f"Error: Product '{product_name}' not found in pricing data.")
            return None

        try:
            original_price = self.pricing_data[product_name]
            if not isinstance(original_price, (int, float)) or original_price < 0:
                raise ValueError(f"Invalid price for product '{product_name}'.")
            if not 0 <= sale_percentage <= 100:
                raise ValueError(f"Sale percentage must be between 0 and 100.")

            # Calculate the discounted price
            discount_amount = original_price * (sale_percentage / 100)
            discounted_price = original_price - discount_amount
            return round(discounted_price, 2)  # Round to 2 decimal places for clarity

        except Exception as e:
            print(f"An error occurred while calculating the discount: {e}")
            return None


# Example usage:
if __name__ == "__main__":
    # Sample pricing data (you can replace this with Brandforlessegy's pricing data)
    pricing_data_json = '''
    {
        "BOSS T-shirt": 50.0,
        "Adidas Shoes": 120.0,
        "Nike Cap": 30.0
    }
    '''

    try:
        # Parse the pricing data
        pricing_data = json.loads(pricing_data_json)

        # Initialize the discount calculator
        discount_calculator = DiscountCalculator(pricing_data)

        # Calculate discount for BOSS T-shirt
        product_name = "BOSS T-shirt"
        sale_percentage = 20  # 20% off
        discounted_price = discount_calculator.calculate_discount(product_name, sale_percentage)

        if discounted_price is not None:
            print(f"The discounted price for '{product_name}' is: ${discounted_price}")

    except json.JSONDecodeError as e:
        print(f"Error parsing pricing data: {e}")
```
