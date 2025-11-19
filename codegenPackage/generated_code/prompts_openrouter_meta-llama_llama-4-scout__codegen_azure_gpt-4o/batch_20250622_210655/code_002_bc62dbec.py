"""
Generated Code Metadata:
========================
Original URL: https://bolle.com.co
Prompt: Generate a Python code snippet to manage an e-commerce product catalog for sports protective gear, including items like FURO MIPS helmets and CHRONOSHIELD TITANIUM MATTE sunglasses.
Generated: DETERMINISTIC_bc62dbec77ee2ee5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ProductCatalog:
    """
    A class to manage an e-commerce product catalog for sports protective gear.
    """

    def __init__(self):
        """
        Initializes an empty product catalog.
        """
        self.catalog = {}

    def add_product(self, product_id, name, category, price, stock):
        """
        Adds a new product to the catalog.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param category: Category of the product (e.g., helmets, sunglasses)
        :param price: Price of the product
        :param stock: Number of items available in stock
        """
        if product_id in self.catalog:
            raise ValueError(f"Product ID '{product_id}' already exists in the catalog.")
        
        self.catalog[product_id] = {
            "name": name,
            "category": category,
            "price": price,
            "stock": stock
        }

    def update_stock(self, product_id, new_stock):
        """
        Updates the stock for a specific product.

        :param product_id: Unique identifier for the product
        :param new_stock: New stock quantity
        """
        if product_id not in self.catalog:
            raise KeyError(f"Product ID '{product_id}' not found in the catalog.")
        
        self.catalog[product_id]["stock"] = new_stock

    def get_product(self, product_id):
        """
        Retrieves details of a specific product.

        :param product_id: Unique identifier for the product
        :return: Dictionary containing product details
        """
        if product_id not in self.catalog:
            raise KeyError(f"Product ID '{product_id}' not found in the catalog.")
        
        return self.catalog[product_id]

    def remove_product(self, product_id):
        """
        Removes a product from the catalog.

        :param product_id: Unique identifier for the product
        """
        if product_id not in self.catalog:
            raise KeyError(f"Product ID '{product_id}' not found in the catalog.")
        
        del self.catalog[product_id]

    def list_products(self):
        """
        Lists all products in the catalog.

        :return: List of dictionaries containing product details
        """
        return list(self.catalog.values())

    def save_catalog_to_file(self, file_path):
        """
        Saves the catalog to a JSON file.

        :param file_path: Path to the file where the catalog will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.catalog, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save catalog to file: {e}")

    def load_catalog_from_file(self, file_path):
        """
        Loads the catalog from a JSON file.

        :param file_path: Path to the file from which the catalog will be loaded
        """
        try:
            with open(file_path, 'r') as file:
                self.catalog = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load catalog from file: {e}")


# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog()

    # Adding products
    catalog.add_product("001", "FURO MIPS Helmet", "Helmets", 199.99, 10)
    catalog.add_product("002", "CHRONOSHIELD TITANIUM MATTE Sunglasses", "Sunglasses", 149.99, 5)

    # Listing products
    print("Product Catalog:")
    print(catalog.list_products())

    # Updating stock
    catalog.update_stock("001", 8)

    # Retrieving a product
    print("\nProduct Details (ID: 001):")
    print(catalog.get_product("001"))

    # Saving catalog to file
    catalog.save_catalog_to_file("product_catalog.json")

    # Loading catalog from file
    new_catalog = ProductCatalog()
    new_catalog.load_catalog_from_file("product_catalog.json")
    print("\nLoaded Product Catalog:")
    print(new_catalog.list_products())
```
