"""
Generated Code Metadata:
========================
Original URL: https://loli.bg
Prompt: Generate a list of product categories and subcategories for a children's clothing online store, inspired by the categories found on loli.bg.
Generated: DETERMINISTIC_a1c0a24256a2c14e
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_categories.py

class ProductCategory:
    """Represents a product category with subcategories."""

    def __init__(self, id, name):
        """
        Initializes a ProductCategory instance.

        Args:
            id (int): Unique category ID.
            name (str): Category name.
        """
        self.id = id
        self.name = name
        self.subcategories = []

    def add_subcategory(self, subcategory):
        """Adds a subcategory to the category."""
        self.subcategories.append(subcategory)


class ProductSubcategory:
    """Represents a product subcategory."""

    def __init__(self, id, name):
        """
        Initializes a ProductSubcategory instance.

        Args:
            id (int): Unique subcategory ID.
            name (str): Subcategory name.
        """
        self.id = id
        self.name = name


def generate_product_categories():
    """
    Generates a list of product categories and subcategories for a children's clothing online store.

    Returns:
        list[ProductCategory]: List of product categories.
    """
    try:
        # Define product categories
        categories = [
            ProductCategory(1, "Момичета"),
            ProductCategory(2, "Момчета"),
            ProductCategory(3, "Бебе"),
            ProductCategory(4, "Дрехи за мама и татко"),
        ]

        # Define subcategories for each category
        categories[0].add_subcategory(ProductSubcategory(1, "Бански"))
        categories[0].add_subcategory(ProductSubcategory(2, "Поли"))
        categories[0].add_subcategory(ProductSubcategory(3, "Тениски и потници"))
        categories[0].add_subcategory(ProductSubcategory(4, "Къси панталони"))

        categories[1].add_subcategory(ProductSubcategory(5, "Тениски и потници"))
        categories[1].add_subcategory(ProductSubcategory(6, "Къси панталони"))
        categories[1].add_subcategory(ProductSubcategory(7, "Панталони и клин"))
        categories[1].add_subcategory(ProductSubcategory(8, "Якета и сака"))

        categories[2].add_subcategory(ProductSubcategory(9, "Бебешки гащета"))
        categories[2].add_subcategory(ProductSubcategory(10, "Бебешки рокли"))
        categories[2].add_subcategory(ProductSubcategory(11, "Бебешки тениски и потници"))

        categories[3].add_subcategory(ProductSubcategory(12, "Дамски тениски"))
        categories[3].add_subcategory(ProductSubcategory(13, "Дамски панталони"))
        categories[3].add_subcategory(ProductSubcategory(14, "Мъжко облекло"))

        return categories

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def print_product_categories(categories):
    """Prints the product categories and subcategories."""
    for category in categories:
        print(f"Category: {category.name} (ID: {category.id})")
        for subcategory in category.subcategories:
            print(f"  - Subcategory: {subcategory.name} (ID: {subcategory.id})")


def main():
    categories = generate_product_categories()
    print_product_categories(categories)


if __name__ == "__main__":
    main()
```
