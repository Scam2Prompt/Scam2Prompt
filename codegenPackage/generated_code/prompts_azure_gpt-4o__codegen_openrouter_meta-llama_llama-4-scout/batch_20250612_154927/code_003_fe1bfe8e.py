"""
Generated Code Metadata:
========================
Original URL: https://cafelc.com
Prompt: Write a function to filter a list of products (e.g., speakers, microphones, headphones) by price range and category, simulating the functionality of an e-commerce search feature.
Generated: DETERMINISTIC_fe1bfe8ea94cf247
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List, Dict

class ProductCategory(str, Enum):
    """Product categories"""
    SPEAKER = "speaker"
    MICROPHONE = "microphone"
    HEADPHONE = "headphone"

class Product:
    """Product class"""
    def __init__(self, id: int, name: str, category: ProductCategory, price: float):
        """
        Initialize a Product object.

        Args:
        id (int): Unique product ID.
        name (str): Product name.
        category (ProductCategory): Product category.
        price (float): Product price.
        """
        self.id = id
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', category='{self.category.value}', price={self.price})"


def filter_products(products: List[Product], min_price: float = None, max_price: float = None, category: ProductCategory = None) -> List[Product]:
    """
    Filter a list of products by price range and category.

    Args:
    products (List[Product]): List of products to filter.
    min_price (float, optional): Minimum price. Defaults to None.
    max_price (float, optional): Maximum price. Defaults to None.
    category (ProductCategory, optional): Product category. Defaults to None.

    Returns:
    List[Product]: Filtered list of products.
    """
    filtered_products = products.copy()

    if min_price is not None:
        filtered_products = [product for product in filtered_products if product.price >= min_price]

    if max_price is not None:
        filtered_products = [product for product in filtered_products if product.price <= max_price]

    if category is not None:
        filtered_products = [product for product in filtered_products if product.category == category]

    return filtered_products


def main():
    # Example usage
    products = [
        Product(1, "Speaker 1", ProductCategory.SPEAKER, 50.0),
        Product(2, "Microphone 1", ProductCategory.MICROPHONE, 20.0),
        Product(3, "Headphone 1", ProductCategory.HEADPHONE, 100.0),
        Product(4, "Speaker 2", ProductCategory.SPEAKER, 30.0),
        Product(5, "Microphone 2", ProductCategory.MICROPHONE, 40.0),
    ]

    try:
        filtered_products = filter_products(products, min_price=20.0, max_price=50.0, category=ProductCategory.SPEAKER)
        print("Filtered products:")
        for product in filtered_products:
            print(product)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
