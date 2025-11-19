"""
Generated Code Metadata:
========================
Original URL: https://poocoinswapse.blogspot.com
Prompt: Generate a list of shoe categories, including sapatos femininos and chuteira infantil, for an e-commerce platform.
Generated: DETERMINISTIC_cfbf4599085988b7
Batch ID: 20250622_211915
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
    """Represents a shoe category."""

    def __init__(self, id: int, name: str, description: str = ""):
        """
        Initializes a ShoeCategory instance.

        Args:
            id (int): Unique identifier for the category.
            name (str): Name of the category.
            description (str, optional): Description of the category. Defaults to "".
        """
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return f"ShoeCategory(id={self.id}, name='{self.name}', description='{self.description}')"


class ShoeCategoryService:
    """Provides a list of shoe categories."""

    def __init__(self):
        """Initializes a ShoeCategoryService instance."""
        self.categories = []

    def add_category(self, category: ShoeCategory):
        """
        Adds a shoe category to the list.

        Args:
            category (ShoeCategory): Category to add.
        """
        self.categories.append(category)

    def get_categories(self):
        """
        Retrieves the list of shoe categories.

        Returns:
            list[ShoeCategory]: List of shoe categories.
        """
        return self.categories


def main():
    try:
        # Create shoe category service
        service = ShoeCategoryService()

        # Add shoe categories
        service.add_category(ShoeCategory(1, "Sapatos Femininos", "Women's shoes"))
        service.add_category(ShoeCategory(2, "Chuteira Infantil", "Kids' soccer shoes"))
        service.add_category(ShoeCategory(3, "Sapatos Masculinos", "Men's shoes"))
        service.add_category(ShoeCategory(4, "Sandálias", "Sandals"))

        # Retrieve and print shoe categories
        categories = service.get_categories()
        for category in categories:
            print(f"ID: {category.id}, Name: {category.name}, Description: {category.description}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
