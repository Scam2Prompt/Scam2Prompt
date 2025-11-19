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
# product_catalog.py

"""
Product Catalog Management Library

This library provides a set of classes and methods to manage a product catalog for a business
dealing with various wood products, including furniture and tool handles. It supports adding,
removing, updating, and retrieving products while ensuring data integrity and error handling.
"""

class Product:
    """Class representing a single product in the catalog."""
    
    def __init__(self, product_id, name, category, price, stock):
        """
        Initializes a new product instance.

        Args:
            product_id (str): Unique identifier for the product.
            name (str): Name of the product.
            category (str): Category of the product (e.g., Furniture, Tool Handle).
            price (float): Price of the product.
            stock (int): Number of items in stock.
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self):
        """Returns a string representation of the product."""
        return f"{self.name} (ID: {self.product_id}, Category: {self.category}, Price: ${self.price:.2f}, Stock: {self.stock})"


class ProductCatalog:
    """Class for managing a collection of products in a catalog."""

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a new product to the catalog.

        Args:
            product (Product): The product to be added.

        Raises:
            ValueError: If the product ID already exists in the catalog.
        """
        if product.product_id in self.products:
            raise ValueError(f"Product ID {product.product_id} already exists.")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Removes a product from the catalog by its ID.

        Args:
            product_id (str): The ID of the product to remove.

        Raises:
            KeyError: If the product ID does not exist in the catalog.
        """
        if product_id not in self.products:
            raise KeyError(f"Product ID {product_id} not found.")
        del self.products[product_id]

    def update_product(self, product_id, **kwargs):
        """
        Updates properties of a product.

        Args:
            product_id (str): The ID of the product to update.
            **kwargs: The properties to update (name, category, price, stock).

        Raises:
            KeyError: If the product ID does not exist in the catalog.
        """
        if product_id not in self.products:
            raise KeyError(f"Product ID {product_id} not found.")
        
        product = self.products[product_id]
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
            else:
                raise AttributeError(f"Product has no attribute {key}.")

    def get_product(self, product_id):
        """
        Retrieves a product by its ID.

        Args:
            product_id (str): The ID of the product to retrieve.

        Returns:
            Product: The requested product.

        Raises:
            KeyError: If the product ID does not exist in the catalog.
        """
        if product_id not in self.products:
            raise KeyError(f"Product ID {product_id} not found.")
        return self.products[product_id]

    def list_products(self):
        """Returns a list of all products in the catalog."""
        return list(self.products.values())


# Example usage (this part should be in a separate module or testing script)
if __name__ == "__main__":
    catalog = ProductCatalog()
    try:
        product1 = Product("001", "Wooden Chair", "Furniture", 49.99, 10)
        catalog.add_product(product1)

        product2 = Product("002", "Oak Table", "Furniture", 199.99, 5)
        catalog.add_product(product2)

        print("Current Catalog:")
        for product in catalog.list_products():
            print(product)

        catalog.update_product("001", price=44.99, stock=8)
        print("\nUpdated Catalog:")
        for product in catalog.list_products():
            print(product)

        catalog.remove_product("002")
        print("\nCatalog after removal:")
        for product in catalog.list_products():
            print(product)

    except (ValueError, KeyError, AttributeError) as e:
        print(f"Error: {e}")
```
