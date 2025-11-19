"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: What are the main product categories offered by Milly Mally, and how do they cater to different age groups of children?
Generated: DETERMINISTIC_4a2d3cb5ec4c7e43
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# milly_mally_product_categories.py

class ProductCategory:
    """Represents a product category offered by Milly Mally."""

    def __init__(self, name, age_groups):
        """
        Initializes a ProductCategory object.

        Args:
            name (str): The name of the product category.
            age_groups (list): A list of age groups catered to by the category.
        """
        self.name = name
        self.age_groups = age_groups

class MillyMally:
    """Represents the Milly Mally product catalog."""

    def __init__(self):
        """
        Initializes a MillyMally object with a list of product categories.
        """
        self.product_categories = [
            ProductCategory("Toys", ["0-3", "4-6", "7-12"]),
            ProductCategory("Games", ["4-6", "7-12", "13-18"]),
            ProductCategory("Puzzles", ["4-6", "7-12"]),
            ProductCategory("Books", ["0-3", "4-6", "7-12", "13-18"]),
            ProductCategory("Outdoor Play", ["4-6", "7-12", "13-18"]),
        ]

    def get_product_categories(self):
        """
        Retrieves a list of product categories offered by Milly Mally.

        Returns:
            list: A list of ProductCategory objects.
        """
        return self.product_categories

    def get_categories_by_age_group(self):
        """
        Retrieves a dictionary mapping age groups to product categories.

        Returns:
            dict: A dictionary where each key is an age group and each value is a list of product categories.
        """
        age_groups = {}
        for category in self.product_categories:
            for age_group in category.age_groups:
                if age_group not in age_groups:
                    age_groups[age_group] = []
                age_groups[age_group].append(category.name)
        return age_groups

def main():
    try:
        milly_mally = MillyMally()
        print("Product Categories:")
        for category in milly_mally.get_product_categories():
            print(f"- {category.name} ({', '.join(category.age_groups)})")

        print("\nCategories by Age Group:")
        age_groups = milly_mally.get_categories_by_age_group()
        for age_group, categories in age_groups.items():
            print(f"{age_group}: {', '.join(categories)}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
