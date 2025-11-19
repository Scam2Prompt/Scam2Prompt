"""
Generated Code Metadata:
========================
Original URL: https://new.joss-home.com
Prompt: Develop a search functionality for an e-commerce site that allows users to find furniture items based on keywords like "дивани" or "ліжка," similar to the search feature on the Joss Home website.
Generated: DETERMINISTIC_69b7a74ba7c5971e
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Any
import re

class FurnitureItem:
    """Class representing a furniture item."""
    
    def __init__(self, name: str, description: str, category: str):
        self.name = name
        self.description = description
        self.category = category

    def __repr__(self) -> str:
        return f"FurnitureItem(name={self.name}, category={self.category})"


class FurnitureSearch:
    """Class to handle searching for furniture items."""
    
    def __init__(self, items: List[FurnitureItem]):
        """
        Initialize the search with a list of furniture items.

        :param items: List of FurnitureItem objects to search through.
        """
        self.items = items

    def search(self, keyword: str) -> List[FurnitureItem]:
        """
        Search for furniture items that match the given keyword.

        :param keyword: The keyword to search for in item names and descriptions.
        :return: A list of matching FurnitureItem objects.
        """
        if not keyword:
            raise ValueError("Keyword must not be empty.")

        # Normalize the keyword for case-insensitive matching
        keyword_pattern = re.compile(re.escape(keyword), re.IGNORECASE)

        # Filter items based on the keyword
        matching_items = [
            item for item in self.items
            if keyword_pattern.search(item.name) or keyword_pattern.search(item.description)
        ]

        return matching_items


# Example usage
if __name__ == "__main__":
    # Sample furniture items
    furniture_items = [
        FurnitureItem("Диван", "Комфортний диван для вітальні", "меблі"),
        FurnitureItem("Ліжко", "Зручне ліжко з матрацом", "меблі"),
        FurnitureItem("Стіл", "Стіл для обіду", "меблі"),
        FurnitureItem("Крісло", "Зручне крісло для читання", "меблі"),
    ]

    # Initialize the search functionality
    search_functionality = FurnitureSearch(furniture_items)

    # Perform a search
    try:
        keyword = "ліжка"
        results = search_functionality.search(keyword)
        print(f"Search results for '{keyword}': {results}")
    except ValueError as e:
        print(f"Error: {e}")
```
