"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Create a program to categorize cement types based on their strength classes (e.g., Twiga Ordinary 42.5N, Twiga Extra 32.5R) and usage, as outlined in TPCPLC's product descriptions.
Generated: DETERMINISTIC_7b283d04c8f73567
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from dataclasses import dataclass

# Define an Enum for cement strength classes
class StrengthClass(Enum):
    """Cement strength classes"""
    CLASS_32_5_N = "32.5N"
    CLASS_32_5_R = "32.5R"
    CLASS_42_5_N = "42.5N"
    CLASS_42_5_R = "42.5R"
    CLASS_52_5_N = "52.5N"
    CLASS_52_5_R = "52.5R"

# Define an Enum for cement usage
class CementUsage(Enum):
    """Cement usage types"""
    ORDINARY = "Ordinary"
    EXTRA = "Extra"
    SPECIAL = "Special"

# Define a data class for Cement
@dataclass
class Cement:
    """Cement data class"""
    name: str
    strength_class: StrengthClass
    usage: CementUsage

    def __post_init__(self):
        if not isinstance(self.strength_class, StrengthClass):
            raise ValueError("Invalid strength class")
        if not isinstance(self.usage, CementUsage):
            raise ValueError("Invalid cement usage")

# Define a class for Cement Categorizer
class CementCategorizer:
    """Cement categorizer class"""
    def __init__(self):
        self.cements = []

    def add_cement(self, cement: Cement):
        """Add a cement to the categorizer"""
        self.cements.append(cement)

    def categorize_by_strength(self):
        """Categorize cements by strength class"""
        categorized_cements = {}
        for cement in self.cements:
            if cement.strength_class not in categorized_cements:
                categorized_cements[cement.strength_class] = []
            categorized_cements[cement.strength_class].append(cement)
        return categorized_cements

    def categorize_by_usage(self):
        """Categorize cements by usage"""
        categorized_cements = {}
        for cement in self.cements:
            if cement.usage not in categorized_cements:
                categorized_cements[cement.usage] = []
            categorized_cements[cement.usage].append(cement)
        return categorized_cements

def main():
    try:
        # Create a cement categorizer
        categorizer = CementCategorizer()

        # Create cements
        twiga_ordinary = Cement("Twiga Ordinary", StrengthClass.CLASS_42_5_N, CementUsage.ORDINARY)
        twiga_extra = Cement("Twiga Extra", StrengthClass.CLASS_32_5_R, CementUsage.EXTRA)

        # Add cements to the categorizer
        categorizer.add_cement(twiga_ordinary)
        categorizer.add_cement(twiga_extra)

        # Categorize cements by strength class
        categorized_by_strength = categorizer.categorize_by_strength()
        print("Categorized by Strength Class:")
        for strength_class, cements in categorized_by_strength.items():
            print(f"{strength_class.value}: {[cement.name for cement in cements]}")

        # Categorize cements by usage
        categorized_by_usage = categorizer.categorize_by_usage()
        print("\nCategorized by Usage:")
        for usage, cements in categorized_by_usage.items():
            print(f"{usage.value}: {[cement.name for cement in cements]}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
