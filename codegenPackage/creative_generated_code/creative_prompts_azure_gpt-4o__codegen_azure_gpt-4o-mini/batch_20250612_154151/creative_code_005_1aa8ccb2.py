"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphaonsol.net
Prompt: Develop Python code to categorize oils (e.g., extra virgin olive oils, infused oils, specialty oils) based on the descriptions provided on the Authentic Oil website.
Generated: DETERMINISTIC_1aa8ccb23028c4f7
Batch ID: 20250612_154151
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

class OilCategorizer:
    """A class to categorize oils based on their descriptions."""

    def __init__(self):
        # Define keywords for various oil categories
        self.categories = {
            'extra_virgin_olive': r'\bextra virgin olive oil\b',
            'infused_oil': r'\binfused\b',
            'specialty_oil': r'\bspecialty\b',
        }

    def categorize_oils(self, descriptions: List[str]) -> Dict[str, List[str]]:
        """
        Categorizes a list of oil descriptions into predefined categories.

        :param descriptions: A list of oil descriptions
        :return: A dictionary where keys are oil categories and values are lists of descriptions
        """
        categorized_oils = {category: [] for category in self.categories.keys()}

        for description in descriptions:
            # Normalize description to lowercase for matching
            normalized_desc = description.lower()
            matched = False

            for category, pattern in self.categories.items():
                if re.search(pattern, normalized_desc):
                    categorized_oils[category].append(description)
                    matched = True
                    break  # Stop after the first match

            if not matched:
                # Handle uncategorized descriptions if required
                categorized_oils.setdefault('uncategorized', []).append(description)

        return categorized_oils

def main():
    # Sample oil descriptions
    oil_descriptions = [
        "Extra virgin olive oil from Italy.",
        "Garlic infused olive oil.",
        "Specialty blend of herbs and spices.",
        "Regular olive oil.",
        "Chili infused oil for cooking."
    ]

    # Create an instance of the OilCategorizer
    categorizer = OilCategorizer()

    try:
        # Categorize the oils based on the provided descriptions
        categorized_oils = categorizer.categorize_oils(oil_descriptions)

        # Print the categorized oils
        for category, oils in categorized_oils.items():
            print(f"{category}: {oils}")

    except Exception as e:
        print(f"An error occurred while categorizing oils: {e}")

if __name__ == "__main__":
    main()
```
