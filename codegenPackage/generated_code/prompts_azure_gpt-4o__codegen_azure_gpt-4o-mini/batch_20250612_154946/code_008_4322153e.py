"""
Generated Code Metadata:
========================
Original URL: https://adp-magiceden.lojaintegrada.com.br
Prompt: Implement a feature in an e-commerce platform to display products with the highest discounts, such as "-50% Perfume Al Wataniah Special Oud Eau de Parfum Unissex 100ml."
Generated: DETERMINISTIC_4322153ed23d7d47
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class Product:
    """Class representing a product in the e-commerce platform."""
    
    def __init__(self, name: str, original_price: float, discount_percentage: float):
        """
        Initialize a new product.

        :param name: The name of the product.
        :param original_price: The original price of the product.
        :param discount_percentage: The discount percentage applied to the product.
        """
        self.name = name
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def discounted_price(self) -> float:
        """
        Calculate the discounted price of the product.

        :return: The price after applying the discount.
        """
        return self.original_price * (1 - self.discount_percentage / 100)

    def __str__(self) -> str:
        """
        String representation of the product.

        :return: A formatted string showing the discount and product name.
        """
        return f"-{self.discount_percentage}% {self.name} ({self.discounted_price():.2f} USD)"


class ProductCatalog:
    """Class to manage a catalog of products."""
    
    def __init__(self):
        """Initialize an empty product catalog."""
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Add a product to the catalog.

        :param product: An instance of Product to be added.
        """
        self.products.append(product)
        logging.info(f"Added product: {product}")

    def get_top_discounted_products(self, top_n: int) -> List[Product]:
        """
        Retrieve the top N products with the highest discounts.

        :param top_n: The number of top discounted products to retrieve.
        :return: A list of the top N discounted products.
        """
        if top_n <= 0:
            logging.error("Invalid number of products requested.")
            raise ValueError("top_n must be greater than 0")

        # Sort products by discount percentage in descending order
        sorted_products = sorted(self.products, key=lambda p: p.discount_percentage, reverse=True)
        return sorted_products[:top_n]


def main():
    """Main function to demonstrate the product catalog functionality."""
    catalog = ProductCatalog()

    # Sample products
    catalog.add_product(Product("Perfume Al Wataniah Special Oud Eau de Parfum Unissex 100ml", 100.00, 50))
    catalog.add_product(Product("Luxury Watch Model X", 500.00, 30))
    catalog.add_product(Product("Designer Handbag", 300.00, 20))
    catalog.add_product(Product("Wireless Headphones", 150.00, 40))

    try:
        # Get top 3 discounted products
        top_discounted_products = catalog.get_top_discounted_products(3)
        logging.info("Top discounted products:")
        for product in top_discounted_products:
            print(product)
    except ValueError as e:
        logging.error(f"Error retrieving products: {e}")


if __name__ == "__main__":
    main()
```
