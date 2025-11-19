"""
Generated Code Metadata:
========================
Original URL: https://ac-world-galagames.blogspot.com
Prompt: Write a Python script to categorize vintage toys into different types, such as "Ambulância", "Animal", "Arvore", etc.
Generated: DETERMINISTIC_c0532e9b0f3803fa
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# toy_categorizer.py

class Toy:
    """Represents a vintage toy with a name and category."""

    def __init__(self, name, category):
        """
        Initializes a Toy object.

        Args:
            name (str): The name of the toy.
            category (str): The category of the toy.
        """
        self.name = name
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category})"


class ToyCategorizer:
    """Categorizes vintage toys into different types."""

    def __init__(self):
        """
        Initializes a ToyCategorizer object with an empty dictionary of categories.
        """
        self.categories = {}
        self.known_categories = ["Ambulância", "Animal", "Arvore"]

    def add_toy(self, toy):
        """
        Adds a toy to the categorizer.

        Args:
            toy (Toy): The toy to add.

        Raises:
            ValueError: If the toy's category is not a string.
        """
        if not isinstance(toy.category, str):
            raise ValueError("Toy category must be a string")

        if toy.category not in self.categories:
            self.categories[toy.category] = []

        self.categories[toy.category].append(toy)

    def get_toys_by_category(self, category):
        """
        Gets all toys in a specific category.

        Args:
            category (str): The category to retrieve toys from.

        Returns:
            list[Toy]: A list of toys in the specified category.

        Raises:
            ValueError: If the category is not a string.
        """
        if not isinstance(category, str):
            raise ValueError("Category must be a string")

        return self.categories.get(category, [])

    def validate_category(self, category):
        """
        Validates if a category is known.

        Args:
            category (str): The category to validate.

        Returns:
            bool: True if the category is known, False otherwise.
        """
        return category in self.known_categories


def main():
    categorizer = ToyCategorizer()

    toys = [
        Toy("Fire Truck", "Ambulância"),
        Toy("Teddy Bear", "Animal"),
        Toy("Christmas Tree", "Arvore"),
        Toy("Car", "Vehicle"),
    ]

    for toy in toys:
        if categorizer.validate_category(toy.category):
            categorizer.add_toy(toy)
        else:
            print(f"Unknown category: {toy.category}. Skipping...")

    print("Toys by category:")
    for category, toys_in_category in categorizer.categories.items():
        print(f"Category: {category}")
        for toy in toys_in_category:
            print(toy)
        print()


if __name__ == "__main__":
    main()
```
