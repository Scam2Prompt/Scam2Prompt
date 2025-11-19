"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maderaselaboradas.com.ar
Prompt: Outline a library recommendation for managing product catalogs for a business like Maderas Elaboradas that deals with various wood products, including furniture and tool handles.
Generated: DETERMINISTIC_5af837d4ee979eec
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Library: ProductCatalogManager
Description: A Python library to manage product catalogs for a business like Maderas Elaboradas, 
which deals with various wood products including furniture and tool handles.

Features:
- Add products to the catalog
- Update product information
- Remove products from the catalog
- Search for products in the catalog
- List all products in the catalog
"""

import json
from typing import List, Optional


class Product:
    """
    Class to represent a product in the catalog.
    """
    def __init__(self, product_id: int, name: str, category: str, price: float, stock: int):
        """
        Initialize a Product instance.

        :param product_id: Unique ID for the product
        :param name: Name of the product
        :param category: Category of the product (e.g., furniture, tool handles, etc.)
        :param price: Price of the product
        :param stock: Number of items available in stock
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def to_dict(self) -> dict:
        """
        Convert Product instance to dictionary format.

        :return: Dictionary representation of the Product instance
        """
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "stock": self.stock
        }


class ProductCatalogManager:
    """
    Class to manage a product catalog.
    """
    def __init__(self, catalog_file: str = "product_catalog.json"):
        """
        Initialize the ProductCatalogManager instance.

        :param catalog_file: Path to the JSON file for storing the catalog data
        """
        self.catalog_file = catalog_file
        self.products = self._load_catalog()

    def _load_catalog(self) -> List[dict]:
        """
        Load catalog data from the JSON file.

        :return: List of products from the catalog file
        """
        try:
            with open(self.catalog_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # Return an empty list if the catalog file does not exist
            return []
        except json.JSONDecodeError:
            raise ValueError("Error decoding the catalog file. Ensure it is a valid JSON file.")

    def _save_catalog(self) -> None:
        """
        Save the current catalog data to the JSON file.

        :raises: IOError if there's an error writing to the file.
        """
        try:
            with open(self.catalog_file, 'w') as file:
                json.dump(self.products, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving catalog data to file: {e}")

    def add_product(self, product: Product) -> None:
        """
        Add a new product to the catalog.

        :param product: Product instance to be added
        :raises: ValueError if a product with the same product_id already exists
        """
        if any(p['product_id'] == product.product_id for p in self.products):
            raise ValueError(f"Product with ID {product.product_id} already exists.")
        self.products.append(product.to_dict())
        self._save_catalog()

    def update_product(self, product_id: int, **updates) -> None:
        """
        Update an existing product in the catalog.

        :param product_id: ID of the product to update
        :param updates: Dictionary of fields to update (e.g., name="New Name", price=99.99)
        :raises: ValueError if the product is not found
        """
        for product in self.products:
            if product['product_id'] == product_id:
                product.update(updates)
                self._save_catalog()
                return
        raise ValueError(f"Product with ID {product_id} not found.")

    def remove_product(self, product_id: int) -> None:
        """
        Remove a product from the catalog.

        :param product_id: ID of the product to be removed
        :raises: ValueError if the product is not found
        """
        for product in self.products:
            if product['product_id'] == product_id:
                self.products.remove(product)
                self._save_catalog()
                return
        raise ValueError(f"Product with ID {product_id} not found.")

    def search_product(self, product_id: int) -> Optional[dict]:
        """
        Search for a product in the catalog by its ID.

        :param product_id: ID of the product to search for
        :return: Dictionary representation of the product if found, None otherwise
        """
        for product in self.products:
            if product['product_id'] == product_id:
                return product
        return None

    def list_products(self) -> List[dict]:
        """
        List all products in the catalog.

        :return: List of dictionaries representing all products in the catalog
        """
        return self.products


# Example usage (commented out for production-ready code)
"""
# Initialize product catalog manager
manager = ProductCatalogManager()

# Add a product
product = Product(product_id=1, name="Wooden Chair", category="Furniture", price=49.99, stock=100)
manager.add_product(product)

# Update a product
manager.update_product(product_id=1, price=59.99)

# Search for a product
print(manager.search_product(product_id=1))

# List all products
print(manager.list_products())

# Remove a product
manager.remove_product(product_id=1)
"""
```
