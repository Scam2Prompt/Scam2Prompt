"""
Generated Code Metadata:
========================
Original URL: https://help-phatom.teachable.com
Prompt: Can you provide an example of how to use Teachable's features to organize and display products, such as sorting by import_export, and handling source visibility?
Generated: DETERMINISTIC_b51c11b700494fd4
Batch ID: 20250622_210935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import teachable as t

class Product:
    """
    A class to represent a product in the Teachable platform.
    """

    def __init__(self, name, import_export, source_visibility):
        """
        Initialize a new product.

        :param name: str - The name of the product
        :param import_export: str - The import/export status of the product
        :param source_visibility: bool - Visibility status of the product source
        """
        self.name = name
        self.import_export = import_export
        self.source_visibility = source_visibility

    def __repr__(self):
        return f"Product(name={self.name}, import_export={self.import_export}, source_visibility={self.source_visibility})"


class ProductManager:
    """
    A class to manage a collection of products.
    """

    def __init__(self):
        """
        Initialize the ProductManager with an empty product list.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the collection.

        :param product: Product - The product to add
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added.")
        self.products.append(product)

    def sort_products(self, by='import_export'):
        """
        Sort products based on a specified attribute.

        :param by: str - The attribute to sort by ('import_export' or 'name')
        :return: list - Sorted list of products
        """
        if by not in ['import_export', 'name']:
            raise ValueError("Sort attribute must be 'import_export' or 'name'.")
        return sorted(self.products, key=lambda x: getattr(x, by))

    def filter_visible_sources(self):
        """
        Filter products to only include those with visible sources.

        :return: list - List of products with visible sources
        """
        return [product for product in self.products if product.source_visibility]


# Example usage
if __name__ == "__main__":
    # Create a ProductManager instance
    manager = ProductManager()

    # Add products to the manager
    try:
        manager.add_product(Product("Product A", "import", True))
        manager.add_product(Product("Product B", "export", False))
        manager.add_product(Product("Product C", "import", True))
    except ValueError as e:
        print(f"Error adding product: {e}")

    # Sort products by import_export
    sorted_products = manager.sort_products(by='import_export')
    print("Sorted Products by Import/Export:")
    for product in sorted_products:
        print(product)

    # Filter products with visible sources
    visible_products = manager.filter_visible_sources()
    print("\nProducts with Visible Sources:")
    for product in visible_products:
        print(product)
```
