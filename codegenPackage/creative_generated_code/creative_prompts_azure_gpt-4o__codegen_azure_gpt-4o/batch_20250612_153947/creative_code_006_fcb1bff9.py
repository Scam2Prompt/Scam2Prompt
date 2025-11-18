"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medebooks.shop
Prompt: Write a script to manage and display discounted prices for products, ensuring discounts are applied dynamically based on the original price, as seen on medebooks.shop.
Generated: DETERMINISTIC_fcb1bff9494a9ddd
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to manage and display dynamically discounted prices for products

import logging

# Configure logging for the script
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define a Product class to manage product details
class Product:
    """
    A class to represent a product with its name, original price, and discounted price.
    """
    def __init__(self, name, original_price):
        """
        Initialize the Product object with name and original price.

        :param name: str - Name of the product
        :param original_price: float - Original price of the product
        """
        self.name = name
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        self.original_price = original_price
        self.discounted_price = None

    def apply_discount(self, discount_rate):
        """
        Apply a discount to the product's original price and calculate the discounted price.

        :param discount_rate: float - Discount rate as a percentage (e.g., 20 for 20%)
        """
        if not (0 <= discount_rate <= 100):
            raise ValueError("Discount rate must be between 0 and 100.")
        self.discounted_price = round(self.original_price * (1 - discount_rate / 100), 2)

    def display(self):
        """
        Display product details including discounted price.
        """
        print(f"Product: {self.name}")
        print(f"Original Price: ${self.original_price:.2f}")
        if self.discounted_price is not None:
            print(f"Discounted Price: ${self.discounted_price:.2f}")
        else:
            print("No discount applied.")

# Function to manage a list of products and apply discounts
def manage_products():
    """
    Manage a list of products, apply discounts, and display results.
    """
    # List of sample products
    products = [
        Product("Book A", 29.99),
        Product("Book B", 49.99),
        Product("Book C", 19.99)
    ]

    # Discount rates to apply (these can be dynamically fetched from a database)
    discount_rates = [10, 15, 20]  # Corresponding to each product above

    # Apply discounts to each product
    for product, discount_rate in zip(products, discount_rates):
        try:
            product.apply_discount(discount_rate)
        except ValueError as e:
            logging.error(f"Failed to apply discount for {product.name}: {e}")
        else:
            logging.info(f"Discount applied to {product.name}")

    # Display all products
    print("\n--- Product Details ---")
    for product in products:
        product.display()

# Entry point of the script
if __name__ == "__main__":
    try:
        manage_products()
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
```
