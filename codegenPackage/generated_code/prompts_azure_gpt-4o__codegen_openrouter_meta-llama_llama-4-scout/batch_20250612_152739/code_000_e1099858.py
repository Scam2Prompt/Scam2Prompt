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
# equipment_categorizer.py

import re
from typing import List, Dict

class EquipmentCategorizer:
    """
    Categorize sports equipment into cycling, camping, skiing, and hiking based on product descriptions and tags.
    """

    def __init__(self):
        # Define keywords for each category
        self.keywords: Dict[str, List[str]] = {
            "cycling": ["bike", "cycle", "cycling", "road bike", "mountain bike", "wheel", "pedal", "chain"],
            "camping": ["tent", "sleeping bag", "backpack", "camp", "camping", "gear", "outdoor"],
            "skiing": ["ski", "snowboard", "skiing", "snow", "boot", "binding", "pole"],
            "hiking": ["hike", "hiking", "trail", "shoe", "boot", "backpack", "trekking"]
        }

    def categorize(self, description: str, tags: List[str]) -> str:
        """
        Categorize equipment based on description and tags.

        Args:
        - description (str): Product description.
        - tags (List[str]): Product tags.

        Returns:
        - str: Category name.
        """
        # Combine description and tags into a single string
        text: str = description.lower() + " " + " ".join(tag.lower() for tag in tags)

        # Check for category keywords
        for category, keywords in self.keywords.items():
            for keyword in keywords:
                if re.search(r"\b" + re.escape(keyword) + r"\b", text):
                    return category

        # If no match found, return unknown
        return "unknown"


def main():
    # Example usage
    categorizer: EquipmentCategorizer = EquipmentCategorizer()

    equipment_list: List[Dict[str, str]] = [
        {"description": "Road bike for sale", "tags": ["bike", "road"]},
        {"description": "Lightweight tent for camping", "tags": ["tent", "gear"]},
        {"description": "Downhill skiing equipment", "tags": ["ski", "snowboard"]},
        {"description": "Hiking boots for trekking", "tags": ["shoe", "boot"]},
        {"description": "Unknown product", "tags": []}
    ]

    for equipment in equipment_list:
        category: str = categorizer.categorize(equipment["description"], equipment["tags"])
        print(f"Description: {equipment['description']}, Tags: {equipment['tags']}, Category: {category}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```
