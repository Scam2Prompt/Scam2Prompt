"""
Generated Code Metadata:
========================
Original URL: https://curvii.fi
Prompt: Develop a code snippet that categorizes clothing items based on their size and style, specifically for the plus-size range offered by Curvii.fi.
Generated: DETERMINISTIC_a29ad8ddaacf8b46
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class ClothingItem:
    def __init__(self, name: str, size: str, style: str):
        """
        Initialize a ClothingItem object.

        Args:
        - name (str): The name of the clothing item.
        - size (str): The size of the clothing item (e.g., 1XL, 2XL, etc.).
        - style (str): The style of the clothing item (e.g., casual, formal, etc.).
        """
        self.name = name
        self.size = size
        self.style = style

class ClothingCategorizer:
    def __init__(self):
        """
        Initialize a ClothingCategorizer object.
        """
        self.size_ranges = {
            "plus_size": ["1XL", "2XL", "3XL", "4XL", "5XL"],
        }
        self.styles = ["casual", "formal", "activewear"]

    def categorize(self, clothing_item: ClothingItem) -> Dict[str, str]:
        """
        Categorize a clothing item based on its size and style.

        Args:
        - clothing_item (ClothingItem): The clothing item to categorize.

        Returns:
        - Dict[str, str]: A dictionary containing the category and details of the clothing item.

        Raises:
        - ValueError: If the clothing item's size or style is invalid.
        """
        if clothing_item.size not in self.size_ranges["plus_size"]:
            raise ValueError(f"Invalid size: {clothing_item.size}. Must be one of: {self.size_ranges['plus_size']}")

        if clothing_item.style not in self.styles:
            raise ValueError(f"Invalid style: {clothing_item.style}. Must be one of: {self.styles}")

        category = "plus_size" if clothing_item.size in self.size_ranges["plus_size"] else "invalid_size"
        style_category = clothing_item.style

        return {
            "category": category,
            "style": style_category,
            "name": clothing_item.name,
            "size": clothing_item.size,
        }

def main():
    # Example usage:
    categorizer = ClothingCategorizer()

    clothing_items: List[ClothingItem] = [
        ClothingItem("T-Shirt", "1XL", "casual"),
        ClothingItem("Dress", "2XL", "formal"),
        ClothingItem("Sweatpants", "3XL", "activewear"),
        ClothingItem("Invalid Item", "XS", "casual"),  # Invalid size
        ClothingItem("Invalid Item", "1XL", "invalid_style"),  # Invalid style
    ]

    for item in clothing_items:
        try:
            category = categorizer.categorize(item)
            print(category)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
