"""
Generated Code Metadata:
========================
Original URL: https://sanurisupplies.com
Prompt: Develop a program to categorize office supplies into different sections (computers, printers, files, folders, etc.) for large-scale and small-scale businesses, as mentioned on Sanuri Supplies' website.
Generated: DETERMINISTIC_f8cee16ec6549a65
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# office_supplies_categorizer.py

class OfficeSupply:
    """Represents an office supply item."""

    def __init__(self, name, category, quantity):
        """
        Initializes an OfficeSupply object.

        Args:
            name (str): The name of the office supply.
            category (str): The category of the office supply.
            quantity (int): The quantity of the office supply.
        """
        self.name = name
        self.category = category
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.category}): {self.quantity}"


class OfficeSupplyCategorizer:
    """Categorizes office supplies into different sections."""

    def __init__(self):
        """
        Initializes an OfficeSupplyCategorizer object.

        Attributes:
            categories (dict): A dictionary of categories and their corresponding office supplies.
        """
        self.categories = {}

    def add_category(self, category):
        """
        Adds a new category.

        Args:
            category (str): The name of the category.

        Raises:
            ValueError: If the category already exists.
        """
        if category in self.categories:
            raise ValueError(f"Category '{category}' already exists.")
        self.categories[category] = []

    def remove_category(self, category):
        """
        Removes a category.

        Args:
            category (str): The name of the category.

        Raises:
            ValueError: If the category does not exist.
        """
        if category not in self.categories:
            raise ValueError(f"Category '{category}' does not exist.")
        del self.categories[category]

    def add_supply(self, supply):
        """
        Adds an office supply to a category.

        Args:
            supply (OfficeSupply): The office supply to add.

        Raises:
            ValueError: If the category does not exist.
        """
        if supply.category not in self.categories:
            raise ValueError(f"Category '{supply.category}' does not exist.")
        self.categories[supply.category].append(supply)

    def remove_supply(self, category, supply_name):
        """
        Removes an office supply from a category.

        Args:
            category (str): The name of the category.
            supply_name (str): The name of the office supply.

        Raises:
            ValueError: If the category or office supply does not exist.
        """
        if category not in self.categories:
            raise ValueError(f"Category '{category}' does not exist.")
        self.categories[category] = [s for s in self.categories[category] if s.name != supply_name]

    def print_categories(self):
        """Prints all categories and their office supplies."""
        for category, supplies in self.categories.items():
            print(f"**{category.capitalize()}**")
            for supply in supplies:
                print(f"- {supply}")
            print()


def main():
    # Create an office supply categorizer
    categorizer = OfficeSupplyCategorizer()

    # Add categories
    categorizer.add_category("computers")
    categorizer.add_category("printers")
    categorizer.add_category("files")
    categorizer.add_category("folders")

    # Create office supplies
    supplies = [
        OfficeSupply("Laptop", "computers", 10),
        OfficeSupply("Desktop", "computers", 20),
        OfficeSupply("Inkjet Printer", "printers", 5),
        OfficeSupply("Laser Printer", "printers", 3),
        OfficeSupply("File Folder", "files", 50),
        OfficeSupply("Binder", "folders", 20),
    ]

    # Add office supplies to categories
    for supply in supplies:
        categorizer.add_supply(supply)

    # Print categories
    categorizer.print_categories()

    # Remove an office supply
    categorizer.remove_supply("computers", "Laptop")

    # Print categories again
    print("After removing Laptop:")
    categorizer.print_categories()


if __name__ == "__main__":
    main()
```
