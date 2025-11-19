"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: Write a function to filter and display food packaging products like microwavable containers and dessert containers from a product catalog, inspired by Isoplas Corporation's portfolio.
Generated: DETERMINISTIC_b52b86b4a21c4136
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# food_packaging_filter.py

from enum import Enum
from typing import List, Dict

class ProductCategory(Enum):
    """Enum for product categories."""
    MICROWAVABLE_CONTAINERS = 1
    DESSERT_CONTAINERS = 2
    OTHER = 3

class Product:
    """Class representing a product in the catalog."""
    def __init__(self, id: int, name: str, category: ProductCategory, description: str):
        """
        Initialize a Product.

        Args:
        id (int): Unique product ID.
        name (str): Product name.
        category (ProductCategory): Product category.
        description (str): Product description.
        """
        self.id = id
        self.name = name
        self.category = category
        self.description = description

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', category={self.category}, description='{self.description}')"

def filter_products(products: List[Product], categories: List[ProductCategory]) -> List[Product]:
    """
    Filter products by category.

    Args:
    products (List[Product]): List of products to filter.
    categories (List[ProductCategory]): List of categories to filter by.

    Returns:
    List[Product]: Filtered list of products.
    """
    return [product for product in products if product.category in categories]

def display_products(products: List[Product]) -> None:
    """
    Display product information.

    Args:
    products (List[Product]): List of products to display.
    """
    for product in products:
        print(f"ID: {product.id}")
        print(f"Name: {product.name}")
        print(f"Category: {product.category.name}")
        print(f"Description: {product.description}")
        print("------------------------")

def main() -> None:
    # Example product catalog
    products: List[Product] = [
        Product(1, "Microwavable Container", ProductCategory.MICROWAVABLE_CONTAINERS, "For microwave use"),
        Product(2, "Dessert Container", ProductCategory.DESSERT_CONTAINERS, "For serving desserts"),
        Product(3, "Water Bottle", ProductCategory.OTHER, "For storing water"),
        Product(4, "Microwavable Bowl", ProductCategory.MICROWAVABLE_CONTAINERS, "For microwave use"),
        Product(5, "Cake Box", ProductCategory.DESSERT_CONTAINERS, "For storing cakes"),
    ]

    # Filter categories
    filter_categories: List[ProductCategory] = [ProductCategory.MICROWAVABLE_CONTAINERS, ProductCategory.DESSERT_CONTAINERS]

    try:
        # Filter products
        filtered_products: List[Product] = filter_products(products, filter_categories)

        # Display filtered products
        if filtered_products:
            display_products(filtered_products)
        else:
            print("No products found in the specified categories.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
