"""
Generated Code Metadata:
========================
Original URL: https://creditu.com.ar
Prompt: "Write a Python code snippet to create an e-commerce product catalog like Creditu, including categories for electronics, home appliances, and furniture."
Generated: DETERMINISTIC_af597cad691d915b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_product_catalog.py

from enum import Enum
from typing import List, Dict

class Category(str, Enum):
    """Product categories"""
    ELECTRONICS = "Electronics"
    HOME_APPLIANCES = "Home Appliances"
    FURNITURE = "Furniture"

class Product:
    """Represents a product in the catalog"""
    def __init__(self, id: int, name: str, description: str, price: float, category: Category):
        """
        Initializes a Product instance

        Args:
        id (int): Unique product ID
        name (str): Product name
        description (str): Product description
        price (float): Product price
        category (Category): Product category
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category

class ProductCatalog:
    """E-commerce product catalog"""
    def __init__(self):
        """Initializes an empty product catalog"""
        self.products: Dict[int, Product] = {}
        self.categories: Dict[Category, List[int]] = {
            Category.ELECTRONICS: [],
            Category.HOME_APPLIANCES: [],
            Category.FURNITURE: []
        }

    def add_product(self, product: Product):
        """
        Adds a product to the catalog

        Args:
        product (Product): Product to add

        Raises:
        ValueError: If product ID already exists
        """
        if product.id in self.products:
            raise ValueError("Product ID already exists")
        self.products[product.id] = product
        self.categories[product.category].append(product.id)

    def get_product(self, id: int) -> Product:
        """
        Retrieves a product by ID

        Args:
        id (int): Product ID

        Returns:
        Product: Product instance

        Raises:
        ValueError: If product ID does not exist
        """
        try:
            return self.products[id]
        except KeyError:
            raise ValueError("Product ID does not exist")

    def get_products_by_category(self, category: Category) -> List[Product]:
        """
        Retrieves products by category

        Args:
        category (Category): Product category

        Returns:
        List[Product]: List of products in the category
        """
        product_ids = self.categories[category]
        return [self.products[id] for id in product_ids]

def main():
    catalog = ProductCatalog()

    # Create products
    product1 = Product(1, "Smartphone", "High-end smartphone", 999.99, Category.ELECTRONICS)
    product2 = Product(2, "Refrigerator", "Large capacity refrigerator", 1299.99, Category.HOME_APPLIANCES)
    product3 = Product(3, "Sofa", "Comfortable sofa", 499.99, Category.FURNITURE)

    # Add products to catalog
    catalog.add_product(product1)
    catalog.add_product(product2)
    catalog.add_product(product3)

    # Retrieve products
    print("Electronics:")
    for product in catalog.get_products_by_category(Category.ELECTRONICS):
        print(f"{product.name}: ${product.price:.2f}")

    print("\nHome Appliances:")
    for product in catalog.get_products_by_category(Category.HOME_APPLIANCES):
        print(f"{product.name}: ${product.price:.2f}")

    print("\nFurniture:")
    for product in catalog.get_products_by_category(Category.FURNITURE):
        print(f"{product.name}: ${product.price:.2f}")

if __name__ == "__main__":
    main()
```
