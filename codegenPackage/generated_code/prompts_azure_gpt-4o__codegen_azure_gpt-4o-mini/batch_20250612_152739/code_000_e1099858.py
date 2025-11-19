"""
Generated Code Metadata:
========================
Original URL: https://activesport.cz
Prompt: Write a Python script to categorize sports equipment into "cycling," "camping," "skiing," and "hiking" based on product descriptions and tags, as seen on the ActiveSport.cz website.
Generated: DETERMINISTIC_e10998587011cfa4
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List, Dict

class EquipmentCategorizer:
    """
    A class to categorize sports equipment based on product descriptions and tags.
    """

    def __init__(self):
        # Define keywords for each category
        self.categories = {
            "cycling": ["bike", "bicycle", "cycling", "helmet", "pedal", "gear"],
            "camping": ["tent", "sleeping bag", "camp", "outdoor", "stove", "backpack"],
            "skiing": ["ski", "snowboard", "goggles", "poles", "snow", "winter"],
            "hiking": ["hike", "trail", "boots", "backpack", "outdoor", "climb"]
        }

    def categorize_equipment(self, product_descriptions: List[str]) -> Dict[str, List[str]]:
        """
        Categorizes a list of product descriptions into predefined categories.

        Args:
            product_descriptions (List[str]): A list of product descriptions.

        Returns:
            Dict[str, List[str]]: A dictionary with categories as keys and lists of product descriptions as values.
        """
        categorized_products = {category: [] for category in self.categories}

        for description in product_descriptions:
            # Normalize the description to lower case for matching
            normalized_description = description.lower()
            found_category = False
            
            for category, keywords in self.categories.items():
                # Check if any keyword is present in the description
                if any(re.search(r'\b' + re.escape(keyword) + r'\b', normalized_description) for keyword in keywords):
                    categorized_products[category].append(description)
                    found_category = True
                    break
            
            # If no category is found, you can choose to log or handle it
            if not found_category:
                print(f"Warning: No category found for description: '{description}'")

        return categorized_products

def main():
    # Sample product descriptions
    product_descriptions = [
        "Mountain bike with advanced features",
        "Camping tent for 4 people",
        "Ski goggles for winter sports",
        "Hiking boots for rugged trails",
        "Portable camping stove",
        "Bicycle helmet for safety",
        "Snowboard for the slopes",
        "Lightweight backpack for hiking"
    ]

    # Create an instance of EquipmentCategorizer
    categorizer = EquipmentCategorizer()

    # Categorize the equipment
    categorized_equipment = categorizer.categorize_equipment(product_descriptions)

    # Print the categorized equipment
    for category, items in categorized_equipment.items():
        print(f"{category.capitalize()} ({len(items)} items):")
        for item in items:
            print(f" - {item}")
        print()  # New line for better readability

if __name__ == "__main__":
    main()
```
