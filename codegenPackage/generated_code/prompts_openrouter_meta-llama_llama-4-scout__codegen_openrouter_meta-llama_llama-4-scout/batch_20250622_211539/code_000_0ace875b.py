"""
Generated Code Metadata:
========================
Original URL: https://accessthepooc00in.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce website for selling sandals and shoes, including product categories for masculine and feminine footwear.
Generated: DETERMINISTIC_0ace875b080a00a7
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_website.py

# Import required libraries
from enum import Enum
from typing import List, Dict

# Define an Enum for product categories
class ProductCategory(Enum):
    MASCULINE_FOOTWEAR = "Masculine Footwear"
    FEMININE_FOOTWEAR = "Feminine Footwear"

# Define a class for Product
class Product:
    def __init__(self, id: int, name: str, category: ProductCategory, price: float, description: str):
        """
        Initialize a Product object.

        Args:
        id (int): Unique product ID
        name (str): Product name
        category (ProductCategory): Product category
        price (float): Product price
        description (str): Product description
        """
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.description = description

# Define a class for ECommerceWebsite
class ECommerceWebsite:
    def __init__(self):
        """
        Initialize an ECommerceWebsite object.
        """
        self.products: Dict[int, Product] = {}
        self.categories: Dict[ProductCategory, List[Product]] = {
            ProductCategory.MASCULINE_FOOTWEAR: [],
            ProductCategory.FEMININE_FOOTWEAR: []
        }

    def add_product(self, product: Product):
        """
        Add a product to the website.

        Args:
        product (Product): Product to add
        """
        try:
            if product.id in self.products:
                raise ValueError("Product ID already exists")
            self.products[product.id] = product
            self.categories[product.category].append(product)
        except Exception as e:
            print(f"Error adding product: {str(e)}")

    def remove_product(self, product_id: int):
        """
        Remove a product from the website.

        Args:
        product_id (int): ID of the product to remove
        """
        try:
            if product_id not in self.products:
                raise ValueError("Product ID does not exist")
            product = self.products.pop(product_id)
            self.categories[product.category].remove(product)
        except Exception as e:
            print(f"Error removing product: {str(e)}")

    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """
        Get products by category.

        Args:
        category (ProductCategory): Category to retrieve products for

        Returns:
        List[Product]: List of products in the specified category
        """
        return self.categories[category]

    def display_products(self):
        """
        Display all products on the website.
        """
        for product in self.products.values():
            print(f"ID: {product.id}, Name: {product.name}, Category: {product.category.value}, Price: ${product.price:.2f}")
            print(f"Description: {product.description}")
            print("------------------------")

# Create an instance of ECommerceWebsite
website = ECommerceWebsite()

# Create products
product1 = Product(1, "Sandal", ProductCategory.MASCULINE_FOOTWEAR, 49.99, "Comfortable sandals for men")
product2 = Product(2, "Shoe", ProductCategory.MASCULINE_FOOTWEAR, 79.99, "Stylish shoes for men")
product3 = Product(3, "Heel", ProductCategory.FEMININE_FOOTWEAR, 69.99, "Elegant heels for women")
product4 = Product(4, "Sandal", ProductCategory.FEMININE_FOOTWEAR, 59.99, "Fashionable sandals for women")

# Add products to the website
website.add_product(product1)
website.add_product(product2)
website.add_product(product3)
website.add_product(product4)

# Display products
print("All Products:")
website.display_products()

# Get products by category
print("\nMasculine Footwear:")
for product in website.get_products_by_category(ProductCategory.MASCULINE_FOOTWEAR):
    print(f"ID: {product.id}, Name: {product.name}, Price: ${product.price:.2f}")

print("\nFeminine Footwear:")
for product in website.get_products_by_category(ProductCategory.FEMININE_FOOTWEAR):
    print(f"ID: {product.id}, Name: {product.name}, Price: ${product.price:.2f}")

# Remove a product
website.remove_product(2)

# Display products after removal
print("\nAll Products after removal:")
website.display_products()
```
