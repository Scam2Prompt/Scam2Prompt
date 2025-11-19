"""
Generated Code Metadata:
========================
Original URL: https://modern-boutique.com.ua
Prompt: Generate a list of women's clothing items, including dresses, tops, pants, and outerwear, with descriptions and prices, similar to the product catalog on Modern Boutique.
Generated: DETERMINISTIC_561adafd357a0eaa
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class ClothingItem:
    """Class to represent a clothing item."""
    
    def __init__(self, name: str, category: str, description: str, price: float):
        """
        Initialize a new clothing item.

        :param name: Name of the clothing item
        :param category: Category of the clothing item (e.g., dress, top, pants, outerwear)
        :param description: Description of the clothing item
        :param price: Price of the clothing item
        """
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def to_dict(self) -> Dict:
        """Convert the clothing item to a dictionary."""
        return {
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "price": self.price
        }

class ClothingCatalog:
    """Class to manage a catalog of clothing items."""
    
    def __init__(self):
        """Initialize an empty clothing catalog."""
        self.items: List[ClothingItem] = []

    def add_item(self, item: ClothingItem):
        """Add a clothing item to the catalog.

        :param item: ClothingItem instance to add
        """
        self.items.append(item)

    def to_json(self) -> str:
        """Convert the catalog to a JSON string."""
        return json.dumps([item.to_dict() for item in self.items], indent=4)

def main():
    """Main function to create a clothing catalog and print it as JSON."""
    try:
        # Create a clothing catalog
        catalog = ClothingCatalog()

        # Add clothing items to the catalog
        catalog.add_item(ClothingItem("Floral Maxi Dress", "Dress", "A beautiful floral maxi dress perfect for summer.", 49.99))
        catalog.add_item(ClothingItem("Casual T-Shirt", "Top", "A comfortable casual t-shirt for everyday wear.", 19.99))
        catalog.add_item(ClothingItem("High-Waisted Jeans", "Pants", "Stylish high-waisted jeans that fit perfectly.", 39.99))
        catalog.add_item(ClothingItem("Lightweight Jacket", "Outerwear", "A lightweight jacket for those chilly evenings.", 59.99))

        # Print the catalog in JSON format
        print(catalog.to_json())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
