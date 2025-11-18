"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://makerfinance.net
Prompt: Write code to implement a product listing and categorization system for industries like machinery, electronics, and textiles, modeled after 搜了网's detailed product categories.
Generated: DETERMINISTIC_8306b26a2a6de003
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# product_listing.py

from typing import List, Dict, Optional

class Product:
    """
    A class to represent a product in the system.

    Attributes:
        id (int): Unique identifier for the product.
        name (str): The name of the product.
        category (str): The category under which the product falls.
        description (str): A brief description of the product.
        price (float): The price of the product.
    """

    def __init__(self, id: int, name: str, category: str, description: str, price: float):
        self.id = id
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', category='{self.category}', price={self.price})"


class ProductCatalog:
    """
    A class to manage a catalog of products.

    Attributes:
        products (List[Product]): A list of products in the catalog.
    """

    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """
        Adds a new product to the catalog.

        Args:
            product (Product): The product to be added.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if any(p.id == product.id for p in self.products):
            raise ValueError(f"Product with ID {product.id} already exists.")
        self.products.append(product)

    def get_product(self, product_id: int) -> Optional[Product]:
        """
        Retrieves a product by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Optional[Product]: The product if found, otherwise None.
        """
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def list_products_by_category(self, category: str) -> List[Product]:
        """
        Lists all products in a given category.

        Args:
            category (str): The category to filter products.

        Returns:
            List[Product]: A list of products in the specified category.
        """
        return [product for product in self.products if product.category == category]


# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog()

    try:
        # Adding products to the catalog
        catalog.add_product(Product(1, "Excavator", "Machinery", "Heavy-duty excavator for construction.", 120000.0))
        catalog.add_product(Product(2, "LED Monitor", "Electronics", "27 inch LED monitor with 4K resolution.", 300.0))
        catalog.add_product(Product(3, "Cotton Fabric", "Textiles", "High-quality cotton fabric for garments.", 5.0))

        # Attempting to add a duplicate product
        catalog.add_product(Product(1, "Excavator", "Machinery", "Duplicate excavator product.", 115000.0))  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")

    # Listing products by category
    machinery_products = catalog.list_products_by_category("Machinery")
    print("Machinery Products:", machinery_products)

    # Retrieving a specific product
    product = catalog.get_product(1)
    print("Retrieved Product:", product)
```
