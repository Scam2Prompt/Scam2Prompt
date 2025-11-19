"""
Generated Code Metadata:
========================
Original URL: https://semillasplantae.com
Prompt: "Generate a list of product categories and subcategories for an online store selling organic seeds, using Semillas Plantae as a reference."
Generated: DETERMINISTIC_17bad5053acb0cf5
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ProductCategory:
    """
    A class to represent a product category and its subcategories.
    """

    def __init__(self, name):
        """
        Initializes a new product category.

        :param name: The name of the category.
        """
        self.name = name
        self.subcategories = []

    def add_subcategory(self, subcategory):
        """
        Adds a subcategory to the product category.

        :param subcategory: The name of the subcategory to add.
        """
        self.subcategories.append(subcategory)

    def __repr__(self):
        """
        Returns a string representation of the product category.
        """
        return f"ProductCategory(name={self.name}, subcategories={self.subcategories})"


def create_product_categories():
    """
    Creates a list of product categories and their subcategories for an online store selling organic seeds.

    :return: A list of ProductCategory objects.
    """
    try:
        # Initialize the main categories
        categories = []

        # Create category for Vegetables
        vegetable_category = ProductCategory("Vegetables")
        vegetable_category.add_subcategory("Tomatoes")
        vegetable_category.add_subcategory("Carrots")
        vegetable_category.add_subcategory("Lettuce")
        categories.append(vegetable_category)

        # Create category for Herbs
        herb_category = ProductCategory("Herbs")
        herb_category.add_subcategory("Basil")
        herb_category.add_subcategory("Cilantro")
        herb_category.add_subcategory("Mint")
        categories.append(herb_category)

        # Create category for Flowers
        flower_category = ProductCategory("Flowers")
        flower_category.add_subcategory("Sunflowers")
        flower_category.add_subcategory("Marigolds")
        flower_category.add_subcategory("Lavender")
        categories.append(flower_category)

        # Create category for Fruits
        fruit_category = ProductCategory("Fruits")
        fruit_category.add_subcategory("Strawberries")
        fruit_category.add_subcategory("Blueberries")
        fruit_category.add_subcategory("Raspberries")
        categories.append(fruit_category)

        return categories

    except Exception as e:
        print(f"An error occurred while creating product categories: {e}")
        return []


if __name__ == "__main__":
    # Generate the product categories and print them
    product_categories = create_product_categories()
    for category in product_categories:
        print(category)
```
