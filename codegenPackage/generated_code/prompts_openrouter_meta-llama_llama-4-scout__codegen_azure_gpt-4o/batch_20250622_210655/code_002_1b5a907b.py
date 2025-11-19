"""
Generated Code Metadata:
========================
Original URL: https://www.matinshop.dk
Prompt: "Generate a Python code snippet for an e-commerce product filter that categorizes hair care products by type (e.g., shampoo, styling cream, hair powder) and price range, inspired by the product offerings on Matin Shop."
Generated: DETERMINISTIC_1b5a907bf89f116f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict

# Define a Product class to represent individual products
class Product:
    def __init__(self, name: str, category: str, price: float):
        """
        Initialize a Product instance.

        :param name: Name of the product
        :param category: Category of the product (e.g., shampoo, styling cream, hair powder)
        :param price: Price of the product
        """
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        """
        String representation of the Product instance for debugging purposes.
        """
        return f"Product(name='{self.name}', category='{self.category}', price={self.price})"

# Define a function to filter products by category and price range
def filter_products(products: List[Product], category: str, min_price: float, max_price: float) -> List[Product]:
    """
    Filter products based on category and price range.

    :param products: List of Product objects
    :param category: Desired category to filter by (e.g., shampoo, styling cream, hair powder)
    :param min_price: Minimum price of the product
    :param max_price: Maximum price of the product
    :return: List of filtered Product objects
    """
    try:
        # Validate inputs
        if min_price < 0 or max_price < 0:
            raise ValueError("Price range values must be non-negative.")
        if min_price > max_price:
            raise ValueError("Minimum price cannot be greater than maximum price.")

        # Filter products based on category and price range
        filtered = [
            product for product in products
            if product.category.lower() == category.lower() and min_price <= product.price <= max_price
        ]
        return filtered
    except Exception as e:
        # Log the error and return an empty list
        print(f"Error while filtering products: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Sample product list inspired by Matin Shop
    product_list = [
        Product("Herbal Shampoo", "shampoo", 15.99),
        Product("Volumizing Hair Powder", "hair powder", 12.49),
        Product("Styling Cream", "styling cream", 18.75),
        Product("Moisturizing Shampoo", "shampoo", 22.50),
        Product("Texturizing Hair Powder", "hair powder", 14.99),
    ]

    # Filter products by category and price range
    category_to_filter = "shampoo"
    min_price = 10.00
    max_price = 20.00

    filtered_products = filter_products(product_list, category_to_filter, min_price, max_price)

    # Display the filtered products
    print("Filtered Products:")
    for product in filtered_products:
        print(product)
```
