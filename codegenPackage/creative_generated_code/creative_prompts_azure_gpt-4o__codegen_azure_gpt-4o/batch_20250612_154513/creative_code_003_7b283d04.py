"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.twigacementgroup.com
Prompt: Create a program to categorize cement types based on their strength classes (e.g., Twiga Ordinary 42.5N, Twiga Extra 32.5R) and usage, as outlined in TPCPLC's product descriptions.
Generated: DETERMINISTIC_7b283d04c8f73567
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Cement Categorization Program
# This program categorizes cement types based on their strength classes and usage

class Cement:
    """
    A class representing a cement product.
    Attributes:
        name (str): Name of the cement product.
        strength_class (str): Strength class of the cement (e.g., 42.5N, 32.5R).
        usage (str): Typical usage of the cement (e.g., general construction, heavy-duty applications).
    """
    def __init__(self, name, strength_class, usage):
        self.name = name
        self.strength_class = strength_class
        self.usage = usage

    def __str__(self):
        return f"{self.name} - Strength Class: {self.strength_class}, Usage: {self.usage}"


class CementCategorizer:
    """
    A class to categorize cement products.
    Attributes:
        categories (dict): A dictionary where keys are strength classes and values are lists of cement products.
    Methods:
        add_cement(cement): Adds a cement product to the appropriate category.
        display_categories(): Displays categorized cement products.
    """
    def __init__(self):
        self.categories = {}

    def add_cement(self, cement):
        """
        Adds a cement product to the appropriate category based on its strength class.
        Args:
            cement (Cement): The cement product to categorize.
        """
        try:
            if cement.strength_class not in self.categories:
                self.categories[cement.strength_class] = []
            self.categories[cement.strength_class].append(cement)
        except AttributeError as e:
            print(f"Error while adding cement: {e}")
    
    def display_categories(self):
        """
        Displays categorized cement products.
        """
        try:
            if not self.categories:
                print("No cement products have been categorized.")
                return
            
            print("Cement Categories:")
            for strength_class, products in self.categories.items():
                print(f"\nStrength Class: {strength_class}")
                for product in products:
                    print(f"  - {product}")
        except Exception as e:
            print(f"Error while displaying categories: {e}")


def main():
    """
    Main function to drive the program.
    """
    try:
        # Create CementCategorizer instance
        categorizer = CementCategorizer()

        # Sample cement products based on TPCPLC's product descriptions
        cement1 = Cement("Twiga Ordinary", "42.5N", "General construction")
        cement2 = Cement("Twiga Extra", "32.5R", "Residential and light industrial use")
        cement3 = Cement("Twiga Plus", "42.5R", "Heavy-duty applications")

        # Add cement products to categorizer
        categorizer.add_cement(cement1)
        categorizer.add_cement(cement2)
        categorizer.add_cement(cement3)

        # Display categorized cement products
        categorizer.display_categories()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the program
    main()
```
