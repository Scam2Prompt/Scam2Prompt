"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curvii.fi
Prompt: Develop a code snippet that categorizes clothing items based on their size and style, specifically for the plus-size range offered by Curvii.fi.
Generated: DETERMINISTIC_a29ad8ddaacf8b46
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ClothingItem:
    """
    A class to represent a clothing item.

    Attributes:
        name (str): The name of the clothing item.
        size (str): The size of the clothing item.
        style (str): The style of the clothing item.
    """

    def __init__(self, name, size, style):
        """
        Initializes a new ClothingItem instance.

        Parameters:
            name (str): The name of the clothing item.
            size (str): The size of the clothing item.
            style (str): The style of the clothing item.
        """
        self.name = name
        self.size = self.validate_size(size)
        self.style = style

    def validate_size(self, size):
        """
        Validates the size of the clothing item.
        
        Parameters:
            size (str): The size to validate.

        Returns:
            str: Validated size if it's in the plus-size category.
        
        Raises:
            ValueError: If the size is not a recognized plus-size.
        """
        plus_sizes = {"XL", "2XL", "3XL", "4XL", "5XL"}
        if size not in plus_sizes:
            raise ValueError(f"Size '{size}' is not a recognized plus-size.")
        return size


class ClothingCategorizer:
    """
    A class to categorize clothing items based on size and style.
    """

    def __init__(self):
        """Initializes the ClothingCategorizer with an empty inventory."""
        self.inventory = {}

    def add_item(self, item):
        """
        Adds a clothing item to the inventory.

        Parameters:
            item (ClothingItem): The clothing item to add.
        """
        if not isinstance(item, ClothingItem):
            raise TypeError("Expected an instance of ClothingItem.")
        
        category_key = (item.size, item.style)
        if category_key not in self.inventory:
            self.inventory[category_key] = []
        self.inventory[category_key].append(item)

    def get_inventory(self):
        """
        Returns the current inventory categorized by size and style.

        Returns:
            dict: A dictionary with size and style as keys and lists of items as values.
        """
        return self.inventory


# Example usage
if __name__ == "__main__":
    try:
        # Create some clothing items
        shirt = ClothingItem("Curvii Plus T-Shirt", "2XL", "Casual")
        dress = ClothingItem("Curvii Plus Dress", "3XL", "Formal")
        
        # Initialize the categorizer
        categorizer = ClothingCategorizer()

        # Add items to the inventory
        categorizer.add_item(shirt)
        categorizer.add_item(dress)

        # Retrieve and display the inventory
        inventory = categorizer.get_inventory()
        for category, items in inventory.items():
            print(f"Size: {category[0]}, Style: {category[1]}")
            for item in items:
                print(f" - {item.name}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
