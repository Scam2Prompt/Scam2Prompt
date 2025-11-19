"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Recommend a library or tool for managing product categories such as "Equipamentos," "Suprimentos," and "Home Decor" in an e-commerce platform, referencing the ebrasilbrazz website structure.
Generated: DETERMINISTIC_4d281db0240b5535
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict, Optional

class Category:
    """
    A class to represent a product category in an e-commerce platform.
    """

    def __init__(self, name: str, description: Optional[str] = None):
        """
        Initializes a new category with a name and an optional description.

        :param name: The name of the category.
        :param description: A brief description of the category.
        """
        if not name:
            raise ValueError("Category name cannot be empty.")
        self.name = name
        self.description = description
        self.subcategories: List['Category'] = []

    def add_subcategory(self, subcategory: 'Category'):
        """
        Adds a subcategory to the current category.

        :param subcategory: The subcategory to be added.
        """
        if not isinstance(subcategory, Category):
            raise TypeError("Subcategory must be an instance of Category.")
        self.subcategories.append(subcategory)

    def to_dict(self) -> Dict:
        """
        Converts the category and its subcategories to a dictionary format.

        :return: A dictionary representation of the category.
        """
        return {
            'name': self.name,
            'description': self.description,
            'subcategories': [subcategory.to_dict() for subcategory in self.subcategories]
        }

class CategoryManager:
    """
    A class to manage product categories in an e-commerce platform.
    """

    def __init__(self):
        """
        Initializes the CategoryManager with an empty list of categories.
        """
        self.categories: List[Category] = []

    def add_category(self, category: Category):
        """
        Adds a new category to the manager.

        :param category: The category to be added.
        """
        if not isinstance(category, Category):
            raise TypeError("Category must be an instance of Category.")
        self.categories.append(category)

    def find_category(self, name: str) -> Optional[Category]:
        """
        Finds a category by its name.

        :param name: The name of the category to find.
        :return: The found category or None if not found.
        """
        for category in self.categories:
            if category.name == name:
                return category
        return None

    def get_categories(self) -> List[Dict]:
        """
        Retrieves all categories in dictionary format.

        :return: A list of dictionaries representing all categories.
        """
        return [category.to_dict() for category in self.categories]

# Example usage
if __name__ == "__main__":
    try:
        # Create a category manager
        category_manager = CategoryManager()

        # Create main categories
        equipamentos = Category("Equipamentos", "All types of equipment.")
        suprimentos = Category("Suprimentos", "Various supplies.")
        home_decor = Category("Home Decor", "Decorative items for home.")

        # Add categories to the manager
        category_manager.add_category(equipamentos)
        category_manager.add_category(suprimentos)
        category_manager.add_category(home_decor)

        # Create and add subcategories
        equipamentos.add_subcategory(Category("Tools", "Hand and power tools."))
        suprimentos.add_subcategory(Category("Office Supplies", "Stationery and office items."))

        # Retrieve and print all categories
        all_categories = category_manager.get_categories()
        print(all_categories)

    except Exception as e:
        print(f"An error occurred: {e}")
```
