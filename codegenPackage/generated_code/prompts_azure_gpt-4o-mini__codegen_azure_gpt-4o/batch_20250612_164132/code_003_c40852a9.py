"""
Generated Code Metadata:
========================
Original URL: https://magicenen-nfts.blogspot.com
Prompt: Develop a code snippet that filters products by category and discount percentage, similar to the offerings on beckercalcados.
Generated: DETERMINISTIC_c40852a9d68dac31
Batch ID: 20250612_164132
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

# Define a Product class to represent each product
class Product:
    def __init__(self, name: str, category: str, price: float, discount_percentage: float):
        """
        Initialize a Product instance.

        :param name: Name of the product
        :param category: Category of the product
        :param price: Price of the product
        :param discount_percentage: Discount percentage applied to the product
        """
        self.name = name
        self.category = category
        self.price = price
        self.discount_percentage = discount_percentage

    def __repr__(self):
        """
        String representation of the Product instance for debugging purposes.
        """
        return f"Product(name={self.name}, category={self.category}, price={self.price}, discount={self.discount_percentage}%)"

# Function to filter products by category and discount percentage
def filter_products(products: List[Product], category: str, min_discount: float) -> List[Product]:
    """
    Filters a list of products based on category and minimum discount percentage.

    :param products: List of Product objects
    :param category: Category to filter by
    :param min_discount: Minimum discount percentage to filter by
    :return: List of filtered Product objects
    """
    try:
        # Validate inputs
        if not isinstance(products, list) or not all(isinstance(p, Product) for p in products):
            raise ValueError("Invalid products list. Ensure all items are instances of Product.")
        if not isinstance(category, str):
            raise ValueError("Category must be a string.")
        if not isinstance(min_discount, (int, float)) or min_discount < 0:
            raise ValueError("Minimum discount must be a non-negative number.")

        # Filter products based on category and discount percentage
        filtered_products = [
            product for product in products
            if product.category.lower() == category.lower() and product.discount_percentage >= min_discount
        ]

        return filtered_products
    except Exception as e:
        # Log the error and re-raise it for further handling
        print(f"Error occurred while filtering products: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Sample product data
    product_list = [
        Product("Sneakers", "Footwear", 100.0, 20.0),
        Product("Boots", "Footwear", 150.0, 10.0),
        Product("Sandals", "Footwear", 50.0, 25.0),
        Product("T-shirt", "Clothing", 30.0, 15.0),
        Product("Jeans", "Clothing", 60.0, 5.0),
    ]

    # Filter products by category "Footwear" and minimum discount of 15%
    filtered = filter_products(product_list, "Footwear", 15.0)

    # Print the filtered products
    print("Filtered Products:")
    for product in filtered:
        print(product)
```
