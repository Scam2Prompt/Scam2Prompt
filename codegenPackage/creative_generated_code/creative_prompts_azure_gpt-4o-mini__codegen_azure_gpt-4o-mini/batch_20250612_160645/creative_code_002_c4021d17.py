"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ra-don.com
Prompt: Write a function to manage product categories and items for a site catalog, similar to the offerings on ra-don.com.
Generated: DETERMINISTIC_c4021d172a1f0ff8
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """A class to represent a product."""

    def __init__(self, name: str, price: float, category: str):
        """
        Initialize a new product.

        :param name: The name of the product.
        :param price: The price of the product.
        :param category: The category to which the product belongs.
        """
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        """Return a string representation of the product."""
        return f"Product(name={self.name}, price={self.price}, category={self.category})"


class Category:
    """A class to represent a product category."""

    def __init__(self, name: str):
        """
        Initialize a new category.

        :param name: The name of the category.
        """
        self.name = name
        self.products = []

    def add_product(self, product: Product):
        """
        Add a product to the category.

        :param product: The product to add.
        """
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added.")
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Remove a product from the category.

        :param product: The product to remove.
        """
        try:
            self.products.remove(product)
        except ValueError:
            raise ValueError("Product not found in this category.")

    def list_products(self):
        """List all products in the category."""
        return self.products

    def __repr__(self):
        """Return a string representation of the category."""
        return f"Category(name={self.name}, products={self.products})"


class Catalog:
    """A class to manage the product catalog."""

    def __init__(self):
        """Initialize a new catalog."""
        self.categories = {}

    def add_category(self, category: Category):
        """
        Add a category to the catalog.

        :param category: The category to add.
        """
        if not isinstance(category, Category):
            raise TypeError("Only Category instances can be added.")
        self.categories[category.name] = category

    def remove_category(self, category_name: str):
        """
        Remove a category from the catalog.

        :param category_name: The name of the category to remove.
        """
        if category_name in self.categories:
            del self.categories[category_name]
        else:
            raise KeyError("Category not found in the catalog.")

    def get_category(self, category_name: str) -> Category:
        """
        Retrieve a category by its name.

        :param category_name: The name of the category to retrieve.
        :return: The category object.
        :raises KeyError: If the category is not found.
        """
        try:
            return self.categories[category_name]
        except KeyError:
            raise KeyError("Category not found in the catalog.")

    def list_categories(self):
        """List all categories in the catalog."""
        return list(self.categories.values())


# Example usage
if __name__ == "__main__":
    # Create a catalog
    catalog = Catalog()

    # Create categories
    electronics = Category("Electronics")
    clothing = Category("Clothing")

    # Add categories to the catalog
    catalog.add_category(electronics)
    catalog.add_category(clothing)

    # Create products
    laptop = Product("Laptop", 999.99, "Electronics")
    shirt = Product("Shirt", 29.99, "Clothing")

    # Add products to categories
    electronics.add_product(laptop)
    clothing.add_product(shirt)

    # List categories and their products
    for category in catalog.list_categories():
        print(category)
```
