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
from typing import List, Dict, Any

class Product:
    """Class representing a hair care product."""
    
    def __init__(self, name: str, product_type: str, price: float):
        """
        Initialize a new product.

        :param name: Name of the product
        :param product_type: Type of the product (e.g., shampoo, styling cream)
        :param price: Price of the product
        """
        self.name = name
        self.product_type = product_type
        self.price = price

    def __repr__(self) -> str:
        """Return a string representation of the product."""
        return f"{self.name} ({self.product_type}): ${self.price:.2f}"


class ProductFilter:
    """Class to filter hair care products by type and price range."""
    
    def __init__(self, products: List[Product]):
        """
        Initialize the product filter with a list of products.

        :param products: List of Product objects
        """
        self.products = products

    def filter_by_type(self, product_type: str) -> List[Product]:
        """
        Filter products by type.

        :param product_type: The type of product to filter by
        :return: List of products matching the specified type
        """
        filtered_products = [product for product in self.products if product.product_type.lower() == product_type.lower()]
        return filtered_products

    def filter_by_price_range(self, min_price: float, max_price: float) -> List[Product]:
        """
        Filter products by price range.

        :param min_price: Minimum price of the product
        :param max_price: Maximum price of the product
        :return: List of products within the specified price range
        """
        if min_price < 0 or max_price < 0:
            raise ValueError("Price values must be non-negative.")
        if min_price > max_price:
            raise ValueError("Minimum price cannot be greater than maximum price.")

        filtered_products = [product for product in self.products if min_price <= product.price <= max_price]
        return filtered_products

    def filter_by_type_and_price(self, product_type: str, min_price: float, max_price: float) -> List[Product]:
        """
        Filter products by both type and price range.

        :param product_type: The type of product to filter by
        :param min_price: Minimum price of the product
        :param max_price: Maximum price of the product
        :return: List of products matching the specified type and within the price range
        """
        return self.filter_by_price_range(min_price, max_price) and self.filter_by_type(product_type)


# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        Product("Moisturizing Shampoo", "Shampoo", 12.99),
        Product("Volumizing Styling Cream", "Styling Cream", 15.49),
        Product("Dry Shampoo Powder", "Hair Powder", 9.99),
        Product("Nourishing Conditioner", "Conditioner", 14.99),
        Product("Smoothing Serum", "Styling Cream", 19.99),
    ]

    # Create a product filter
    product_filter = ProductFilter(products)

    # Filter by type
    try:
        shampoo_products = product_filter.filter_by_type("Shampoo")
        print("Shampoo Products:", shampoo_products)

        # Filter by price range
        affordable_products = product_filter.filter_by_price_range(10, 15)
        print("Affordable Products:", affordable_products)

        # Filter by type and price range
        specific_products = product_filter.filter_by_type_and_price("Styling Cream", 10, 20)
        print("Styling Cream Products in Price Range:", specific_products)

    except ValueError as e:
        print(f"Error: {e}")
```
