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
    def __init__(self, id, name, category, price, design):
        """
        Initialize a Product object.

        Args:
            id (int): Unique product ID.
            name (str): Product name.
            category (str): Product category (e.g., WWE, NBA, NFL, NHL, MLB).
            price (float): Product price.
            design (str): Product design.
        """
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.design = design

class ProductCatalog:
    def __init__(self):
        """
        Initialize a ProductCatalog object.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        Args:
            product (Product): Product to add.
        """
        self.products.append(product)

    def filter_by_category(self, category):
        """
        Filter products by category.

        Args:
            category (str): Category to filter by.

        Returns:
            list[Product]: Filtered products.
        """
        return [product for product in self.products if product.category == category]

    def filter_by_price(self, min_price, max_price):
        """
        Filter products by price range.

        Args:
            min_price (float): Minimum price.
            max_price (float): Maximum price.

        Returns:
            list[Product]: Filtered products.
        """
        return [product for product in self.products if min_price <= product.price <= max_price]

    def filter_by_design(self, design):
        """
        Filter products by design.

        Args:
            design (str): Design to filter by.

        Returns:
            list[Product]: Filtered products.
        """
        return [product for product in self.products if product.design == design]

def main():
    # Create product catalog
    catalog = ProductCatalog()

    # Add products
    catalog.add_product(Product(1, "WWE Championship Belt", "WWE", 50.99, "Gold"))
    catalog.add_product(Product(2, "NBA Championship Belt", "NBA", 40.99, "Silver"))
    catalog.add_product(Product(3, "NFL Championship Belt", "NFL", 60.99, "Gold"))
    catalog.add_product(Product(4, "NHL Championship Belt", "NHL", 45.99, "Silver"))
    catalog.add_product(Product(5, "MLB Championship Belt", "MLB", 55.99, "Gold"))

    # Filter by category
    wwe_products = catalog.filter_by_category("WWE")
    print("WWE Products:")
    for product in wwe_products:
        print(f"ID: {product.id}, Name: {product.name}, Price: ${product.price:.2f}")

    # Filter by price
    affordable_products = catalog.filter_by_price(40.0, 50.0)
    print("\nAffordable Products ($40-$50):")
    for product in affordable_products:
        print(f"ID: {product.id}, Name: {product.name}, Price: ${product.price:.2f}")

    # Filter by design
    gold_products = catalog.filter_by_design("Gold")
    print("\nGold Products:")
    for product in gold_products:
        print(f"ID: {product.id}, Name: {product.name}, Price: ${product.price:.2f}")

if __name__ == "__main__":
    main()
```
