"""
Generated Code Metadata:
========================
Original URL: https://barbudogrowler.cl
Prompt: Generate a list of beer categories and subcategories based on the product offerings of the Barbudo Growler online store.
Generated: DETERMINISTIC_cfd0fe4fbffca467
Batch ID: 20250622_205919
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

class BeerCategory:
    """Class representing a beer category with subcategories."""
    
    def __init__(self, name: str, subcategories: List[str]):
        """
        Initialize a BeerCategory instance.

        :param name: The name of the beer category.
        :param subcategories: A list of subcategories under this category.
        """
        self.name = name
        self.subcategories = subcategories

    def to_dict(self) -> Dict:
        """Convert the BeerCategory instance to a dictionary."""
        return {
            "name": self.name,
            "subcategories": self.subcategories
        }

def generate_beer_categories() -> List[BeerCategory]:
    """Generate a list of beer categories and their subcategories.

    :return: A list of BeerCategory instances.
    """
    try:
        categories = [
            BeerCategory("Lager", ["Pale Lager", "Dark Lager", "Bock"]),
            BeerCategory("Ale", ["Pale Ale", "Brown Ale", "IPA", "Stout"]),
            BeerCategory("Wheat Beer", ["Hefeweizen", "Witbier"]),
            BeerCategory("Sour Beer", ["Berliner Weisse", "Gose", "Lambic"]),
            BeerCategory("Specialty Beer", ["Fruit Beer", "Spiced Beer"]),
        ]
        return categories
    except Exception as e:
        print(f"Error generating beer categories: {e}")
        return []

def save_categories_to_json(categories: List[BeerCategory], filename: str) -> None:
    """Save the beer categories to a JSON file.

    :param categories: A list of BeerCategory instances.
    :param filename: The name of the file to save the categories to.
    """
    try:
        with open(filename, 'w') as json_file:
            json.dump([category.to_dict() for category in categories], json_file, indent=4)
    except IOError as e:
        print(f"Error saving categories to {filename}: {e}")

def main():
    """Main function to generate and save beer categories."""
    categories = generate_beer_categories()
    if categories:
        save_categories_to_json(categories, 'beer_categories.json')
        print("Beer categories saved successfully.")

if __name__ == "__main__":
    main()
```
