"""
Generated Code Metadata:
========================
Original URL: https://thegladiatorshoes.com
Prompt: "List the different types of safety shoes (e.g., steel toe, composite toe, metal-free) and their applications."
Generated: DETERMINISTIC_5b37f5c1b86103ee
Batch ID: 20250622_210703
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

class SafetyShoeType(str, Enum):
    """Enum for different types of safety shoes."""
    STEEL_TOE = "Steel Toe"
    COMPOSITE_TOE = "Composite Toe"
    METAL_FREE = "Metal-Free"
    ELECTRICAL_HAZARD = "Electrical Hazard"
    ANKLE_PROTECTION = "Ankle Protection"

class SafetyShoe:
    """Class representing a safety shoe."""
    def __init__(self, shoe_type: SafetyShoeType, description: str, application: str):
        """
        Initialize a SafetyShoe object.

        Args:
        shoe_type (SafetyShoeType): The type of safety shoe.
        description (str): A brief description of the shoe.
        application (str): The application or industry where the shoe is used.
        """
        self.shoe_type = shoe_type
        self.description = description
        self.application = application

    def __str__(self):
        return f"{self.shoe_type.value}: {self.description} - {self.application}"

class SafetyShoeCatalog:
    """Class representing a catalog of safety shoes."""
    def __init__(self):
        self.shoes: Dict[SafetyShoeType, SafetyShoe] = {}

    def add_shoe(self, shoe: SafetyShoe):
        """
        Add a safety shoe to the catalog.

        Args:
        shoe (SafetyShoe): The safety shoe to add.
        """
        self.shoes[shoe.shoe_type] = shoe

    def list_shoes(self) -> List[SafetyShoe]:
        """
        List all safety shoes in the catalog.

        Returns:
        List[SafetyShoe]: A list of safety shoes.
        """
        return list(self.shoes.values())

def main():
    try:
        catalog = SafetyShoeCatalog()

        # Add safety shoes to the catalog
        catalog.add_shoe(SafetyShoe(
            SafetyShoeType.STEEL_TOE,
            "Steel toe shoes provide protection from heavy objects.",
            "Construction, manufacturing, warehousing"
        ))

        catalog.add_shoe(SafetyShoe(
            SafetyShoeType.COMPOSITE_TOE,
            "Composite toe shoes offer lightweight protection.",
            "Aviation, aerospace, food processing"
        ))

        catalog.add_shoe(SafetyShoe(
            SafetyShoeType.METAL_FREE,
            "Metal-free shoes are ideal for industries with metal detectors.",
            "Food processing, pharmaceuticals, hospitals"
        ))

        catalog.add_shoe(SafetyShoe(
            SafetyShoeType.ELECTRICAL_HAZARD,
            "Electrical hazard shoes protect against electrical shocks.",
            "Construction, manufacturing, electrical work"
        ))

        catalog.add_shoe(SafetyShoe(
            SafetyShoeType.ANKLE_PROTECTION,
            "Ankle protection shoes provide support and protection.",
            "Construction, manufacturing, hiking"
        ))

        # List safety shoes
        print("Safety Shoes:")
        for shoe in catalog.list_shoes():
            print(shoe)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
