"""
Generated Code Metadata:
========================
Original URL: https://www.curativesurgicalindustry.com
Prompt: Create a JSON structure to represent the featured product categories ("Dental Instruments," "Manicure Products," "Surgical Products") and their respective product codes from the Curative Surgical Industry webpage.
Generated: DETERMINISTIC_1b2f9fdbb8888a62
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ProductCategory:
    """Represents a product category with its name and product codes."""

    def __init__(self, name, product_codes):
        """
        Initializes a ProductCategory instance.

        Args:
            name (str): The name of the product category.
            product_codes (list): A list of product codes in the category.
        """
        self.name = name
        self.product_codes = product_codes

    def to_dict(self):
        """Converts the ProductCategory instance to a dictionary."""
        return {
            "category_name": self.name,
            "product_codes": self.product_codes
        }

class FeaturedProductCategories:
    """Represents the featured product categories."""

    def __init__(self):
        """Initializes a FeaturedProductCategories instance."""
        self.categories = []

    def add_category(self, category):
        """
        Adds a product category.

        Args:
            category (ProductCategory): The product category to add.
        """
        self.categories.append(category)

    def to_json(self):
        """Converts the FeaturedProductCategories instance to a JSON string."""
        categories_dict = [category.to_dict() for category in self.categories]
        return json.dumps(categories_dict, indent=4)

def main():
    try:
        # Create product categories
        dental_instruments = ProductCategory(
            "Dental Instruments",
            ["DI001", "DI002", "DI003"]
        )

        manicure_products = ProductCategory(
            "Manicure Products",
            ["MP001", "MP002", "MP003"]
        )

        surgical_products = ProductCategory(
            "Surgical Products",
            ["SP001", "SP002", "SP003"]
        )

        # Create featured product categories
        featured_categories = FeaturedProductCategories()
        featured_categories.add_category(dental_instruments)
        featured_categories.add_category(manicure_products)
        featured_categories.add_category(surgical_products)

        # Convert to JSON
        json_structure = featured_categories.to_json()
        print(json_structure)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
