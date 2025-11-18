"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activesport.cz
Prompt: Write a Python script to categorize sports equipment into "cycling," "camping," "skiing," and "hiking" based on product descriptions and tags, as seen on the ActiveSport.cz website.
Generated: DETERMINISTIC_e10998587011cfa4
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import List, Dict

class EquipmentCategorizer:
    """Class to categorize sports equipment based on product descriptions and tags."""
    
    def __init__(self):
        # Define keywords for each category
        self.categories: Dict[str, List[str]] = {
            "cycling": ["bike", "cycling", "bicycle", "helmet", "pedal", "gear"],
            "camping": ["tent", "sleeping bag", "camp", "outdoor", "backpack"],
            "skiing": ["ski", "snowboard", "goggles", "pole", "slalom"],
            "hiking": ["hike", "trek", "trail", "boots", "water bottle"],
        }

    def categorize_equipment(self, description: str) -> str:
        """
        Categorizes the equipment based on the given description.
        
        Args:
            description (str): The product description or tags.
        
        Returns:
            str: The category of the product or 'unknown' if not categorized.
        """
        # Normalize the description by converting it to lowercase
        description = description.lower()
        
        for category, keywords in self.categories.items():
            # Check if any keyword for the category is in the description
            if any(re.search(r'\b' + re.escape(keyword) + r'\b', description) for keyword in keywords):
                return category
        
        return "unknown"

    def categorize_multiple(self, descriptions: List[str]) -> Dict[str, str]:
        """
        Categorizes multiple equipment descriptions.
        
        Args:
            descriptions (List[str]): A list of product descriptions.
        
        Returns:
            Dict[str, str]: A dictionary mapping descriptions to their categories.
        """
        categorized_results = {}
        
        for desc in descriptions:
            # Handle potential errors in description processing
            try:
                category = self.categorize_equipment(desc)
                categorized_results[desc] = category
            except Exception as e:
                categorized_results[desc] = f"error: {str(e)}"
        
        return categorized_results

if __name__ == "__main__":
    # Sample product descriptions
    product_descriptions = [
        "Mountain bike with advanced gear and helmet",
        "High-quality tent for camping trips",
        "Ski poles for winter sports",
        "Durable hiking boots for trail walking",
        "Portable water bottle for outdoor activities"
    ]
    
    # Create an instance of the EquipmentCategorizer
    categorizer = EquipmentCategorizer()
    
    # Categorize the sample products
    categorized_products = categorizer.categorize_multiple(product_descriptions)
    
    # Print the categorized results
    for description, category in categorized_products.items():
        print(f"'{description}' is categorized as: {category}")
```
