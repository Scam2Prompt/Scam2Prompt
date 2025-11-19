"""
Generated Code Metadata:
========================
Original URL: https://allorashopping.com
Prompt: Create a Python script to generate clothing filters for an online shopping platform, including style categories such as athleisure, vintage, bohemian, and gothic, along with fit types like regular fit, slim fit, and oversized fit.
Generated: DETERMINISTIC_4af0ce7672e00f92
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# clothing_filter_generator.py

from enum import Enum
from typing import List, Dict

class StyleCategory(str, Enum):
    """Style categories for clothing filters"""
    ATHLEISURE = "athleisure"
    VINTAGE = "vintage"
    BOHEMIAN = "bohemian"
    GOTHIC = "gothic"

class FitType(str, Enum):
    """Fit types for clothing filters"""
    REGULAR_FIT = "regular fit"
    SLIM_FIT = "slim fit"
    OVERSIZED_FIT = "oversized fit"

class ClothingFilter:
    """Represents a clothing filter with style category and fit type"""
    def __init__(self, style_category: StyleCategory, fit_type: FitType):
        self.style_category = style_category
        self.fit_type = fit_type

    def __str__(self):
        return f"{self.style_category.value} - {self.fit_type.value}"

class ClothingFilterGenerator:
    """Generates clothing filters for an online shopping platform"""
    def __init__(self):
        self.style_categories = list(StyleCategory)
        self.fit_types = list(FitType)

    def generate_filters(self) -> List[ClothingFilter]:
        """Generates all possible clothing filters"""
        filters = []
        for style_category in self.style_categories:
            for fit_type in self.fit_types:
                filters.append(ClothingFilter(style_category, fit_type))
        return filters

    def generate_filter_combinations(self) -> Dict[str, List[FitType]]:
        """Generates filter combinations by style category"""
        filter_combinations = {}
        for style_category in self.style_categories:
            filter_combinations[style_category.value] = self.fit_types
        return filter_combinations

def main():
    try:
        generator = ClothingFilterGenerator()
        filters = generator.generate_filters()
        filter_combinations = generator.generate_filter_combinations()

        print("All Clothing Filters:")
        for filter in filters:
            print(filter)

        print("\nFilter Combinations by Style Category:")
        for style_category, fit_types in filter_combinations.items():
            print(f"{style_category}:")
            for fit_type in fit_types:
                print(f"- {fit_type.value}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
