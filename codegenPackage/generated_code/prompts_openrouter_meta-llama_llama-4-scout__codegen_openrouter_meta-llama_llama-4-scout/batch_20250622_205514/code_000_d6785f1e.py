"""
Generated Code Metadata:
========================
Original URL: https://sassmgmt.com
Prompt: What are the categories of talent represented by SASS MGMT?
Generated: DETERMINISTIC_d6785f1e8b7ce4ed
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# talent_categories.py

class TalentCategory:
    """Represents a talent category."""

    def __init__(self, name):
        """
        Initializes a TalentCategory.

        Args:
            name (str): The name of the talent category.
        """
        self.name = name

class SASSMGMT:
    """Represents SASS MGMT talent categories."""

    def __init__(self):
        """
        Initializes SASSMGMT.

        Attributes:
            categories (list[TalentCategory]): A list of talent categories.
        """
        self.categories = []

    def add_category(self, category):
        """
        Adds a talent category.

        Args:
            category (TalentCategory): The category to add.

        Raises:
            TypeError: If category is not a TalentCategory.
        """
        if not isinstance(category, TalentCategory):
            raise TypeError("Category must be a TalentCategory")
        self.categories.append(category)

    def get_categories(self):
        """
        Retrieves the list of talent categories.

        Returns:
            list[TalentCategory]: A list of talent categories.
        """
        return self.categories

def main():
    try:
        # Create SASS MGMT
        sass_mgmt = SASSMGMT()

        # Define talent categories
        software_engineering = TalentCategory("Software Engineering")
        data_science = TalentCategory("Data Science")
        product_management = TalentCategory("Product Management")
        ux_design = TalentCategory("UX Design")

        # Add categories to SASS MGMT
        sass_mgmt.add_category(software_engineering)
        sass_mgmt.add_category(data_science)
        sass_mgmt.add_category(product_management)
        sass_mgmt.add_category(ux_design)

        # Retrieve and print categories
        categories = sass_mgmt.get_categories()
        print("Talent Categories of SASS MGMT:")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category.name}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
