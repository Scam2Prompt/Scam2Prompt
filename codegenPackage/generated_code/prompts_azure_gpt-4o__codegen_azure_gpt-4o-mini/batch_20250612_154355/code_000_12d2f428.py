"""
Generated Code Metadata:
========================
Original URL: https://wwereplicabelts.com
Prompt: Write code to create a product catalog for replica championship belts, including categories like WWE, NBA, NFL, NHL, and MLB, with features for filtering by price and design.
Generated: DETERMINISTIC_12d2f428a2e6829e
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_catalog.py

class Product:
    """Class representing a product in the catalog."""
    
    def __init__(self, name, category, price, design):
        """
        Initialize a new product.

        :param name: str - The name of the product
        :param category: str - The category of the product (e.g., WWE, NBA)
        :param price: float - The price of the product
        :param design: str - The design of the product
        """
        self.name = name
        self.category = category
        self.price = price
        self.design = design

    def __repr__(self):
        """Return a string representation of the product."""
        return f"{self.name} ({self.category}) - ${self.price:.2f} [{self.design}]"


class ProductCatalog:
    """Class representing a catalog of products."""
    
    def __init__(self):
        """Initialize an empty product catalog."""
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        :param product: Product - The product to add
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the catalog.")
        self.products.append(product)

    def filter_by_price(self, min_price=0, max_price=float('inf')):
        """
        Filter products by price range.

        :param min_price: float - Minimum price (inclusive)
        :param max_price: float - Maximum price (inclusive)
        :return: list - List of products within the specified price range
        """
        return [product for product in self.products if min_price <= product.price <= max_price]

    def filter_by_design(self, design):
        """
        Filter products by design.

        :param design: str - The design to filter by
        :return: list - List of products that match the specified design
        """
        return [product for product in self.products if product.design.lower() == design.lower()]

    def filter_by_category(self, category):
        """
        Filter products by category.

        :param category: str - The category to filter by
        :return: list - List of products that match the specified category
        """
        return [product for product in self.products if product.category.lower() == category.lower()]


# Example usage
if __name__ == "__main__":
    # Create a product catalog
    catalog = ProductCatalog()

    # Add products to the catalog
    catalog.add_product(Product("WWE Championship Belt", "WWE", 299.99, "Gold"))
    catalog.add_product(Product("NBA Championship Belt", "NBA", 249.99, "Silver"))
    catalog.add_product(Product("NFL Championship Belt", "NFL", 199.99, "Black"))
    catalog.add_product(Product("NHL Championship Belt", "NHL", 179.99, "Blue"))
    catalog.add_product(Product("MLB Championship Belt", "MLB", 159.99, "Red"))

    # Filter products by price
    print("Products priced between $150 and $250:")
    for product in catalog.filter_by_price(150, 250):
        print(product)

    # Filter products by design
    print("\nProducts with 'Gold' design:")
    for product in catalog.filter_by_design("Gold"):
        print(product)

    # Filter products by category
    print("\nProducts in the 'WWE' category:")
    for product in catalog.filter_by_category("WWE"):
        print(product)
```
