"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Create a program to categorize cement types based on their strength classes (e.g., Twiga Ordinary 42.5N, Twiga Extra 32.5R) and usage, as outlined in TPCPLC's product descriptions.
Generated: DETERMINISTIC_7b283d04c8f73567
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CementType:
    """
    A class to represent a type of cement with its strength class and usage.
    """

    def __init__(self, name: str, strength_class: str, usage: str):
        """
        Initializes a CementType instance.

        :param name: The name of the cement type.
        :param strength_class: The strength class of the cement (e.g., 32.5R, 42.5N).
        :param usage: The recommended usage of the cement.
        """
        self.name = name
        self.strength_class = strength_class
        self.usage = usage

    def __str__(self):
        """
        Returns a string representation of the CementType instance.
        """
        return f"{self.name} - Strength Class: {self.strength_class}, Usage: {self.usage}"


class CementCatalog:
    """
    A class to manage a catalog of cement types.
    """

    def __init__(self):
        """
        Initializes an empty cement catalog.
        """
        self.cements = []

    def add_cement(self, cement: CementType):
        """
        Adds a cement type to the catalog.

        :param cement: An instance of CementType to be added.
        """
        if not isinstance(cement, CementType):
            raise ValueError("Only instances of CementType can be added.")
        self.cements.append(cement)

    def categorize_cements(self):
        """
        Categorizes and returns a dictionary of cement types by strength class.
        
        :return: A dictionary where keys are strength classes and values are lists of cement types.
        """
        categorized = {}
        for cement in self.cements:
            if cement.strength_class not in categorized:
                categorized[cement.strength_class] = []
            categorized[cement.strength_class].append(cement)
        return categorized

    def display_catalog(self):
        """
        Displays all cement types in the catalog.
        """
        if not self.cements:
            print("The cement catalog is empty.")
            return
        for cement in self.cements:
            print(cement)


def main():
    """
    Main function to demonstrate the functionality of the CementCatalog.
    """
    # Create a cement catalog
    catalog = CementCatalog()

    # Add cement types to the catalog
    try:
        catalog.add_cement(CementType("Twiga Ordinary", "42.5N", "General construction"))
        catalog.add_cement(CementType("Twiga Extra", "32.5R", "Specialized construction"))
        catalog.add_cement(CementType("Twiga Premium", "52.5N", "High-strength applications"))
    except ValueError as e:
        print(f"Error adding cement: {e}")

    # Display the catalog
    print("Cement Catalog:")
    catalog.display_catalog()

    # Categorize cements by strength class
    categorized_cements = catalog.categorize_cements()
    print("\nCategorized Cements:")
    for strength_class, cements in categorized_cements.items():
        print(f"{strength_class}: {[cement.name for cement in cements]}")


if __name__ == "__main__":
    main()
```
