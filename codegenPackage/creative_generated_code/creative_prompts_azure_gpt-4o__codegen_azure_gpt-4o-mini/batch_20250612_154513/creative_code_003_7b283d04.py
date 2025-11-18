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
class Cement:
    """
    A class to represent different types of cement based on their strength classes and usage.

    Attributes:
        name (str): The name of the cement.
        strength_class (str): The strength class of the cement.
        usage (str): The recommended usage of the cement.
    """

    def __init__(self, name, strength_class, usage):
        """
        Initializes a Cement instance.

        Args:
            name (str): The name of the cement.
            strength_class (str): The strength class of the cement.
            usage (str): The recommended usage of the cement.
        """
        self.name = name
        self.strength_class = strength_class
        self.usage = usage

    def __str__(self):
        """Returns a string representation of the cement instance."""
        return f"{self.name} - Strength Class: {self.strength_class}, Usage: {self.usage}"


class CementCategorizer:
    """
    A class to categorize cement types based on their strength classes and usage.

    Methods:
        categorize_cement(cement_name): Returns the Cement object based on the name.
    """

    def __init__(self):
        """Initializes the CementCategorizer with a list of cements."""
        # Initialize with predefined cement types
        self.cements = [
            Cement("Twiga Ordinary", "42.5N", "General construction, structural work"),
            Cement("Twiga Extra", "32.5R", "Lightweight construction, plastering"),
            Cement("Twiga Super", "52.5N", "High strength, precast products"),
            Cement("Twiga Rapid", "32.5R", "Fast-setting applications"),
        ]

    def categorize_cement(self, cement_name):
        """
        Categorizes cement based on the provided name.

        Args:
            cement_name (str): The name of the cement to categorize.

        Returns:
            Cement: The corresponding Cement object.

        Raises:
            ValueError: If the cement name is not found in the catalog.
        """
        # Search for the cement in the catalog
        for cement in self.cements:
            if cement.name.lower() == cement_name.lower():
                return cement
        
        # Raise an error if the cement is not found
        raise ValueError(f"Cement '{cement_name}' not found in the catalog.")


def main():
    """Main function to demonstrate the categorization of cements."""
    try:
        # Create an instance of the CementCategorizer
        categorizer = CementCategorizer()

        # Example cement names to categorize
        cement_names = ["Twiga Ordinary", "Twiga Extra", "Twiga Nonexistent"]

        # Categorizing cements
        for name in cement_names:
            try:
                cement = categorizer.categorize_cement(name)
                print(cement)
            except ValueError as e:
                print(e)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
