"""
Generated Code Metadata:
========================
Original URL: https://tanhungco.vn
Prompt: Write a Python script to categorize agricultural products such as "Thuốc trừ sâu," "Thuốc trừ cỏ," and "Phân bón lá" into a database, using product names like "Super Bomb 200EC" and "Nutri 123" as examples.
Generated: DETERMINISTIC_d2f65abef379826a
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# agricultural_product_categorizer.py

class AgriculturalProduct:
    """Represents an agricultural product with a name and category."""

    def __init__(self, name, category):
        """
        Initializes an AgriculturalProduct instance.

        Args:
            name (str): The product name.
            category (str): The product category.
        """
        self.name = name
        self.category = category

    def __repr__(self):
        return f"AgriculturalProduct(name='{self.name}', category='{self.category}')"


class AgriculturalProductDatabase:
    """A database to store and categorize agricultural products."""

    def __init__(self):
        """Initializes an empty database."""
        self.products = []
        self.categories = set()

    def add_product(self, product):
        """
        Adds a product to the database.

        Args:
            product (AgriculturalProduct): The product to add.

        Raises:
            ValueError: If the product name is empty or the category is not a string.
        """
        if not product.name:
            raise ValueError("Product name cannot be empty")
        if not isinstance(product.category, str):
            raise ValueError("Category must be a string")

        self.products.append(product)
        self.categories.add(product.category)

    def get_products_by_category(self, category):
        """
        Retrieves products by category.

        Args:
            category (str): The category to filter by.

        Returns:
            list[AgriculturalProduct]: Products in the specified category.
        """
        return [product for product in self.products if product.category == category]

    def __repr__(self):
        return f"AgriculturalProductDatabase(products={self.products}, categories={self.categories})"


def main():
    # Create a database instance
    database = AgriculturalProductDatabase()

    # Define product categories
    categories = {
        "Thuốc trừ sâu": [],
        "Thuốc trừ cỏ": [],
        "Phân bón lá": [],
    }

    # Add products to the database
    products = [
        AgriculturalProduct("Super Bomb 200EC", "Thuốc trừ sâu"),
        AgriculturalProduct("Nutri 123", "Phân bón lá"),
        AgriculturalProduct("Weed Killer 456", "Thuốc trừ cỏ"),
    ]

    for product in products:
        try:
            database.add_product(product)
        except ValueError as e:
            print(f"Error adding product: {e}")

    # Print products by category
    for category in database.categories:
        print(f"Category: {category}")
        for product in database.get_products_by_category(category):
            print(f"- {product.name}")
        print()


if __name__ == "__main__":
    main()
```
