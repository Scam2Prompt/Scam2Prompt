"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for auto parts, including product codes, names, and prices, similar to the one found on autopecasbrazz.
Generated: DETERMINISTIC_72c805eb833ca877
Batch ID: 20250622_205612
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
    A class to represent an e-commerce product catalog for auto parts.
    """

    def __init__(self):
        """
        Initializes an empty product catalog.
        """
        self.products = {}

    def add_product(self, product_code, name, price):
        """
        Adds a product to the catalog.

        Args:
            product_code (str): Unique identifier for the product.
            name (str): Name of the product.
            price (float): Price of the product.

        Raises:
            ValueError: If the product code already exists or if price is negative.
        """
        if product_code in self.products:
            raise ValueError(f"Product code '{product_code}' already exists.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.products[product_code] = {
            "name": name,
            "price": price
        }

    def remove_product(self, product_code):
        """
        Removes a product from the catalog.

        Args:
            product_code (str): Unique identifier for the product.

        Raises:
            KeyError: If the product code does not exist.
        """
        if product_code not in self.products:
            raise KeyError(f"Product code '{product_code}' does not exist.")
        
        del self.products[product_code]

    def update_product(self, product_code, name=None, price=None):
        """
        Updates the details of a product in the catalog.

        Args:
            product_code (str): Unique identifier for the product.
            name (str, optional): New name for the product.
            price (float, optional): New price for the product.

        Raises:
            KeyError: If the product code does not exist.
            ValueError: If the price is negative.
        """
        if product_code not in self.products:
            raise KeyError(f"Product code '{product_code}' does not exist.")
        if price is not None and price < 0:
            raise ValueError("Price cannot be negative.")
        
        if name:
            self.products[product_code]["name"] = name
        if price is not None:
            self.products[product_code]["price"] = price

    def get_product(self, product_code):
        """
        Retrieves the details of a product.

        Args:
            product_code (str): Unique identifier for the product.

        Returns:
            dict: Details of the product.

        Raises:
            KeyError: If the product code does not exist.
        """
        if product_code not in self.products:
            raise KeyError(f"Product code '{product_code}' does not exist.")
        
        return self.products[product_code]

    def list_products(self):
        """
        Lists all products in the catalog.

        Returns:
            dict: All products in the catalog.
        """
        return self.products

    def save_to_file(self, file_path):
        """
        Saves the product catalog to a JSON file.

        Args:
            file_path (str): Path to the file where the catalog will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.products, file, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_from_file(self, file_path):
        """
        Loads the product catalog from a JSON file.

        Args:
            file_path (str): Path to the file from which the catalog will be loaded.

        Raises:
            IOError: If there is an error reading the file.
        """
        try:
            with open(file_path, 'r') as file:
                self.products = json.load(file)
        except IOError as e:
            print(f"Error loading catalog from file: {e}")


# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog()

    # Adding products
    catalog.add_product("A123", "Brake Pad", 29.99)
    catalog.add_product("B456", "Oil Filter", 15.49)
    catalog.add_product("C789", "Spark Plug", 8.99)

    # Listing products
    print("Product Catalog:")
    print(catalog.list_products())

    # Updating a product
    catalog.update_product("A123", price=31.99)

    # Retrieving a product
    print("\nUpdated Product:")
    print(catalog.get_product("A123"))

    # Saving to file
    catalog.save_to_file("product_catalog.json")

    # Loading from file
    new_catalog = ProductCatalog()
    new_catalog.load_from_file("product_catalog.json")
    print("\nLoaded Product Catalog:")
    print(new_catalog.list_products())
```
