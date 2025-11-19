"""
Generated Code Metadata:
========================
Original URL: https://fotopoint.com.ar
Prompt: "Design a product catalog system using a programming language of your choice, inspired by Fotopoint's product categories and subcategories."
Generated: DETERMINISTIC_8dfdb27bfcd73d9e
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_catalog.py

from enum import Enum
from typing import List, Dict

class ProductStatus(str, Enum):
    """Product status enumeration"""
    IN_STOCK = "in_stock"
    OUT_OF_STOCK = "out_of_stock"
    DISCONTINUED = "discontinued"

class ProductCategory:
    """Product category class"""
    def __init__(self, id: int, name: str):
        """
        Initialize product category

        Args:
        id (int): Unique category ID
        name (str): Category name
        """
        self.id = id
        self.name = name
        self.subcategories: Dict[int, ProductSubcategory] = {}

    def add_subcategory(self, subcategory: 'ProductSubcategory'):
        """
        Add subcategory to category

        Args:
        subcategory (ProductSubcategory): Subcategory to add
        """
        self.subcategories[subcategory.id] = subcategory

class ProductSubcategory:
    """Product subcategory class"""
    def __init__(self, id: int, name: str, category_id: int):
        """
        Initialize product subcategory

        Args:
        id (int): Unique subcategory ID
        name (str): Subcategory name
        category_id (int): Parent category ID
        """
        self.id = id
        self.name = name
        self.category_id = category_id
        self.products: Dict[int, Product] = {}

    def add_product(self, product: 'Product'):
        """
        Add product to subcategory

        Args:
        product (Product): Product to add
        """
        self.products[product.id] = product

class Product:
    """Product class"""
    def __init__(self, id: int, name: str, description: str, price: float, status: ProductStatus, subcategory_id: int):
        """
        Initialize product

        Args:
        id (int): Unique product ID
        name (str): Product name
        description (str): Product description
        price (float): Product price
        status (ProductStatus): Product status
        subcategory_id (int): Parent subcategory ID
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.status = status
        self.subcategory_id = subcategory_id

class ProductCatalog:
    """Product catalog class"""
    def __init__(self):
        self.categories: Dict[int, ProductCategory] = {}

    def add_category(self, category: ProductCategory):
        """
        Add category to catalog

        Args:
        category (ProductCategory): Category to add
        """
        self.categories[category.id] = category

    def get_category(self, category_id: int) -> ProductCategory:
        """
        Get category by ID

        Args:
        category_id (int): Category ID

        Returns:
        ProductCategory: Category object or None if not found
        """
        return self.categories.get(category_id)

    def get_subcategory(self, category_id: int, subcategory_id: int) -> ProductSubcategory:
        """
        Get subcategory by ID

        Args:
        category_id (int): Category ID
        subcategory_id (int): Subcategory ID

        Returns:
        ProductSubcategory: Subcategory object or None if not found
        """
        category = self.get_category(category_id)
        if category:
            return category.subcategories.get(subcategory_id)
        return None

    def get_product(self, category_id: int, subcategory_id: int, product_id: int) -> Product:
        """
        Get product by ID

        Args:
        category_id (int): Category ID
        subcategory_id (int): Subcategory ID
        product_id (int): Product ID

        Returns:
        Product: Product object or None if not found
        """
        subcategory = self.get_subcategory(category_id, subcategory_id)
        if subcategory:
            return subcategory.products.get(product_id)
        return None

def main():
    catalog = ProductCatalog()

    # Create categories
    electronics = ProductCategory(1, "Electronics")
    fashion = ProductCategory(2, "Fashion")

    # Add categories to catalog
    catalog.add_category(electronics)
    catalog.add_category(fashion)

    # Create subcategories
    smartphones = ProductSubcategory(1, "Smartphones", 1)
    laptops = ProductSubcategory(2, "Laptops", 1)
    shirts = ProductSubcategory(1, "Shirts", 2)

    # Add subcategories to categories
    electronics.add_subcategory(smartphones)
    electronics.add_subcategory(laptops)
    fashion.add_subcategory(shirts)

    # Create products
    iphone = Product(1, "iPhone", "Apple iPhone", 999.99, ProductStatus.IN_STOCK, 1)
    macbook = Product(2, "MacBook", "Apple MacBook", 1299.99, ProductStatus.IN_STOCK, 2)
    nike_shirt = Product(1, "Nike Shirt", "Nike T-Shirt", 29.99, ProductStatus.IN_STOCK, 1)

    # Add products to subcategories
    smartphones.add_product(iphone)
    laptops.add_product(macbook)
    shirts.add_product(nike_shirt)

    # Retrieve product
    product = catalog.get_product(1, 1, 1)
    if product:
        print(f"Product: {product.name}, Price: {product.price}, Status: {product.status.value}")
    else:
        print("Product not found")

if __name__ == "__main__":
    main()
```
