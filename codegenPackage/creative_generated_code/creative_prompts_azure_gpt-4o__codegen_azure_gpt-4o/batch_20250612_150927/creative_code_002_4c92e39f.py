"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Generate code to calculate shipping costs for an online store in Ukraine, using product categories such as "снаряжение для дайвинга," "одежда для зимней рыбалки," and "туристическое снаряжение," as outlined on acula.com.ua.
Generated: DETERMINISTIC_4c92e39fb83484a0
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shipping_calculator.py

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ShippingCalculator:
    """
    This class calculates shipping costs for an online store in Ukraine based on product category.
    """

    # Shipping cost rates per category (in UAH)
    SHIPPING_RATES = {
        "снаряжение для дайвинга": 150,      # Diving gear
        "одежда для зимней рыбалки": 100,   # Winter fishing clothing
        "туристическое снаряжение": 200     # Tourist equipment
    }

    DEFAULT_SHIPPING_COST = 120  # Default shipping cost for unknown categories

    def __init__(self):
        pass

    def calculate_shipping_cost(self, category: str, weight: float) -> float:
        """
        Calculate the shipping cost based on the product category and weight.

        Args:
            category (str): The category of the product.
            weight (float): The weight of the product in kilograms.

        Returns:
            float: The calculated shipping cost in UAH.

        Raises:
            ValueError: If the weight is less than or equal to zero.
        """
        if weight <= 0:
            logging.error("Invalid weight provided. Weight must be greater than zero.")
            raise ValueError("Weight must be greater than zero.")

        # Get the base shipping cost for the specified category
        base_cost = self.SHIPPING_RATES.get(category, self.DEFAULT_SHIPPING_COST)
        logging.info(f"Base shipping cost for category '{category}': {base_cost} UAH")

        # Calculate the final cost (base cost + weight factor)
        # Assuming an additional 10 UAH charge per kilogram
        final_cost = base_cost + (10 * weight)
        logging.info(f"Final shipping cost calculated: {final_cost} UAH")

        return final_cost


if __name__ == "__main__":
    # Example usage of the ShippingCalculator class
    calculator = ShippingCalculator()

    try:
        # Define inputs
        product_category = "туристическое снаряжение"
        product_weight = 5.5  # in kilograms

        # Calculate shipping cost
        shipping_cost = calculator.calculate_shipping_cost(product_category, product_weight)

        # Print the calculated shipping cost
        print(f"Shipping cost for '{product_category}' with weight {product_weight} kg: {shipping_cost} UAH")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        logging.exception("An unexpected error occurred.")
```
