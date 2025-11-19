"""
Generated Code Metadata:
========================
Original URL: https://maderaselaboradas.com.ar
Prompt: Outline a library recommendation for managing product catalogs for a business like Maderas Elaboradas that deals with various wood products, including furniture and tool handles.
Generated: DETERMINISTIC_5af837d4ee979eec
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Library: ProductCatalogManager
Description: A Python library for managing product catalogs for businesses dealing with wood products.
Features:
- Add, update, delete, and retrieve products.
- Search products by name, category, or price range.
- Export product catalog to JSON for external use.
- Error handling for invalid operations.
"""

import json

class ProductCatalogManager:
    """
    A class to manage product catalogs for businesses.
    """

    def __init__(self):
        """
        Initializes an empty product catalog.
        """
        self.catalog = {}

    def add_product(self, product_id, name, category, price, stock):
        """
        Adds a new product to the catalog.

        Args:
            product_id (str): Unique identifier for the product.
            name (str): Name of the product.
            category (str): Category of the product (e.g., furniture, tool handles).
            price (float): Price of the product.
            stock (int): Quantity of the product in stock.

        Raises:
            ValueError: If product_id already exists in the catalog.
        """
        if product_id in self.catalog:
            raise ValueError(f"Product ID '{product_id}' already exists.")
        self.catalog[product_id] = {
            "name": name,
            "category": category,
            "price": price,
            "stock": stock
        }

    def update_product(self, product_id, **kwargs):
        """
        Updates an existing product in the catalog.

        Args:
            product_id (str): Unique identifier for the product.
            **kwargs: Fields to update (e.g., name, category, price, stock).

        Raises:
            KeyError: If product_id does not exist in the catalog.
        """
        if product_id not in self.catalog:
            raise KeyError(f"Product ID '{product_id}' not found.")
        self.catalog[product_id].update(kwargs)

    def delete_product(self, product_id):
        """
        Deletes a product from the catalog.

        Args:
            product_id (str): Unique identifier for the product.

        Raises:
            KeyError: If product_id does not exist in the catalog.
        """
        if product_id not in self.catalog:
            raise KeyError(f"Product ID '{product_id}' not found.")
        del self.catalog[product_id]

    def get_product(self, product_id):
        """
        Retrieves a product from the catalog.

        Args:
            product_id (str): Unique identifier for the product.

        Returns:
            dict: Product details.

        Raises:
            KeyError: If product_id does not exist in the catalog.
        """
        if product_id not in self.catalog:
            raise KeyError(f"Product ID '{product_id}' not found.")
        return self.catalog[product_id]

    def search_products(self, name=None, category=None, price_range=None):
        """
        Searches for products in the catalog based on criteria.

        Args:
            name (str, optional): Name of the product to search for.
            category (str, optional): Category of the product to search for.
            price_range (tuple, optional): Price range (min_price, max_price).

        Returns:
            list: List of matching products.
        """
        results = []
        for product in self.catalog.values():
            if name and name.lower() not in product["name"].lower():
                continue
            if category and category.lower() != product["category"].lower():
                continue
            if price_range:
                min_price, max_price = price_range
                if not (min_price <= product["price"] <= max_price):
                    continue
            results.append(product)
        return results

    def export_catalog(self, file_path):
        """
        Exports the product catalog to a JSON file.

        Args:
            file_path (str): Path to the output JSON file.

        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.catalog, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write to file: {e}")

    def import_catalog(self, file_path):
        """
        Imports a product catalog from a JSON file.

        Args:
            file_path (str): Path to the input JSON file.

        Raises:
            IOError: If there is an issue reading the file.
            ValueError: If the file content is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.catalog = json.load(file)
        except IOError as e:
            raise IOError(f"Failed to read file: {e}")
        except ValueError as e:
            raise ValueError(f"Invalid JSON content: {e}")


# Example usage (uncomment to test):
# manager = ProductCatalogManager()
# manager.add_product("001", "Wooden Chair", "Furniture", 49.99, 10)
# manager.add_product("002", "Tool Handle", "Tool Handles", 15.99, 50)
# print(manager.search_products(category="Furniture"))
# manager.export_catalog("catalog.json")
# manager.import_catalog("catalog.json")
```
