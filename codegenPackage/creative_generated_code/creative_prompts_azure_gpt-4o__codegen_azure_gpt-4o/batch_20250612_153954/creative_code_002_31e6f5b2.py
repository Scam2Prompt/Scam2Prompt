"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Generate code to calculate discounts on products like "Milly Mally Rowerek 5w1 Optimus Max Denim" and "Hulajnoga miejska Milly Mally Scooter Ultimate Pink," ensuring the final price reflects promotional offers.
Generated: DETERMINISTIC_31e6f5b2ccc847ef
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Product:
    """
    A class to represent a product.
    Attributes:
        name (str): The name of the product.
        original_price (float): The original price of the product.
        discount_percentage (float): The discount percentage to be applied.
    """
    def __init__(self, name, original_price, discount_percentage=0):
        self.name = name
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate_discounted_price(self):
        """
        Calculate the discounted price of the product based on its discount percentage.
        Returns:
            float: The final price of the product after applying the discount.
        """
        try:
            if self.discount_percentage < 0 or self.discount_percentage > 100:
                raise ValueError("Discount percentage must be between 0 and 100.")

            discount = (self.discount_percentage / 100) * self.original_price
            final_price = self.original_price - discount
            return round(final_price, 2)
        except Exception as e:
            logging.error(f"Error calculating discounted price for product '{self.name}': {e}")
            return None

def main():
    """
    Main function to handle product price calculations and output.
    """
    try:
        # Define products with their original prices and discount percentages
        products = [
            Product("Milly Mally Rowerek 5w1 Optimus Max Denim", 199.99, 20),
            Product("Hulajnoga miejska Milly Mally Scooter Ultimate Pink", 149.99, 15)
        ]

        # Calculate and display the final prices
        for product in products:
            final_price = product.calculate_discounted_price()
            if final_price is not None:
                print(f"Product: {product.name}")
                print(f"Original Price: ${product.original_price}")
                print(f"Discount Percentage: {product.discount_percentage}%")
                print(f"Final Price: ${final_price}\n")
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```
