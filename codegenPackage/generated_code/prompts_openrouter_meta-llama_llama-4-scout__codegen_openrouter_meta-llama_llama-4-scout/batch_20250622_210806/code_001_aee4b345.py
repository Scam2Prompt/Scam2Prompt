"""
Generated Code Metadata:
========================
Original URL: https://icestyle.pl
Prompt: "Write a Python code to manage an e-commerce store for figure skating accessories, including product categories for skates, clothing, and costumes."
Generated: DETERMINISTIC_aee4b34589fb20fb
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_store.py

from enum import Enum
from typing import List, Dict

class ProductCategory(str, Enum):
    """Product categories for the e-commerce store."""
    SKATES = "skates"
    CLOTHING = "clothing"
    COSTUMES = "costumes"

class Product:
    """Represents a product in the e-commerce store."""
    
    def __init__(self, 
                 product_id: int, 
                 name: str, 
                 category: ProductCategory, 
                 price: float, 
                 description: str = ""):
        """
        Initializes a Product instance.

        Args:
        - product_id (int): Unique identifier for the product.
        - name (str): Product name.
        - category (ProductCategory): Product category.
        - price (float): Product price.
        - description (str): Optional product description.
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.description = description

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.category}, {self.price}, {self.description})"

class ECommerceStore:
    """Manages products in the e-commerce store."""
    
    def __init__(self):
        """Initializes an empty e-commerce store."""
        self.products: Dict[int, Product] = {}
        self.category_map: Dict[ProductCategory, List[int]] = {
            ProductCategory.SKATES: [],
            ProductCategory.CLOTHING: [],
            ProductCategory.COSTUMES: []
        }

    def add_product(self, product: Product):
        """
        Adds a product to the e-commerce store.

        Args:
        - product (Product): Product to add.

        Raises:
        - ValueError: If a product with the same ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product with the same ID already exists")
        
        self.products[product.product_id] = product
        self.category_map[product.category].append(product.product_id)

    def remove_product(self, product_id: int):
        """
        Removes a product from the e-commerce store.

        Args:
        - product_id (int): ID of the product to remove.

        Raises:
        - ValueError: If the product does not exist.
        """
        if product_id not in self.products:
            raise ValueError("Product does not exist")
        
        product = self.products.pop(product_id)
        self.category_map[product.category].remove(product_id)

    def get_product(self, product_id: int) -> Product:
        """
        Retrieves a product by ID.

        Args:
        - product_id (int): ID of the product to retrieve.

        Returns:
        - Product: The product instance.

        Raises:
        - ValueError: If the product does not exist.
        """
        try:
            return self.products[product_id]
        except KeyError:
            raise ValueError("Product does not exist")

    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """
        Retrieves products by category.

        Args:
        - category (ProductCategory): Category to filter by.

        Returns:
        - List[Product]: List of products in the specified category.
        """
        return [self.products[product_id] for product_id in self.category_map[category]]

def main():
    store = ECommerceStore()

    # Create products
    skate_product = Product(1, "Skate X", ProductCategory.SKATES, 199.99)
    clothing_product = Product(2, "Skating Jacket", ProductCategory.CLOTHING, 49.99)
    costume_product = Product(3, "Competition Costume", ProductCategory.COSTUMES, 99.99)

    # Add products to the store
    store.add_product(skate_product)
    store.add_product(clothing_product)
    store.add_product(costume_product)

    # Retrieve products
    print("All Skates:")
    for product in store.get_products_by_category(ProductCategory.SKATES):
        print(product)

    print("\nAll Clothing:")
    for product in store.get_products_by_category(ProductCategory.CLOTHING):
        print(product)

    print("\nProduct by ID:")
    print(store.get_product(1))

    # Remove a product
    store.remove_product(2)

    try:
        store.get_product(2)
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
```
