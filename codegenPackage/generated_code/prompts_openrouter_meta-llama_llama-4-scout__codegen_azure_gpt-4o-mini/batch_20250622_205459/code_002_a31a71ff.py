"""
Generated Code Metadata:
========================
Original URL: https://poocoiin-app-swaps.blogspot.com
Prompt: Generate a list of shoe categories for an e-commerce platform, including sapatos femininos, sapatos masculinos, and sandalias masculinas.
Generated: DETERMINISTIC_a31a71ffdf537cd2
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shoe_categories.py

class ShoeCategory:
    """Class to represent a shoe category."""

    def __init__(self, name: str):
        """
        Initialize a new ShoeCategory instance.

        Args:
            name (str): The name of the shoe category.
        """
        if not name:
            raise ValueError("Category name cannot be empty.")
        self.name = name

    def __str__(self):
        """Return the string representation of the shoe category."""
        return self.name


class ShoeCategoryManager:
    """Class to manage shoe categories."""

    def __init__(self):
        """Initialize the ShoeCategoryManager with an empty category list."""
        self.categories = []

    def add_category(self, category: ShoeCategory):
        """
        Add a new shoe category to the list.

        Args:
            category (ShoeCategory): The shoe category to add.
        """
        if not isinstance(category, ShoeCategory):
            raise TypeError("Expected a ShoeCategory instance.")
        self.categories.append(category)

    def get_categories(self):
        """Return the list of shoe categories."""
        return [str(category) for category in self.categories]


def main():
    """Main function to demonstrate shoe category management."""
    try:
        # Create an instance of ShoeCategoryManager
        manager = ShoeCategoryManager()

        # Define shoe categories
        categories = [
            "sapatos femininos",
            "sapatos masculinos",
            "sandalias masculinas"
        ]

        # Add categories to the manager
        for category_name in categories:
            category = ShoeCategory(category_name)
            manager.add_category(category)

        # Retrieve and print the list of categories
        print("Shoe Categories:")
        for category in manager.get_categories():
            print(f"- {category}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
