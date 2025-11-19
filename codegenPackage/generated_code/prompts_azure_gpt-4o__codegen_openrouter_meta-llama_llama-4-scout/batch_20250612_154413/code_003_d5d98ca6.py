"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Write a program in Python to parse and organize fabric data from Shaoxing Eagles Textile Co., Ltd., grouping items like "French Terry," "Hacci," and "Two Face Waffle Cloth" into categories.
Generated: DETERMINISTIC_d5d98ca629857ee7
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fabric_parser.py

from enum import Enum
from typing import Dict, List

class FabricCategory(Enum):
    """Fabric categories"""
    FRENCH_TERRY = "French Terry"
    HACCI = "Hacci"
    TWO_FACE_WAFFLE_CLOTH = "Two Face Waffle Cloth"
    OTHER = "Other"

class Fabric:
    """Fabric data model"""
    def __init__(self, name: str, category: FabricCategory, weight: str, width: str):
        self.name = name
        self.category = category
        self.weight = weight
        self.width = width

    def __repr__(self):
        return f"Fabric(name='{self.name}', category={self.category}, weight='{self.weight}', width='{self.width}')"

class FabricParser:
    """Fabric data parser and organizer"""
    def __init__(self):
        self.fabrics: Dict[FabricCategory, List[Fabric]] = {
            FabricCategory.FRENCH_TERRY: [],
            FabricCategory.HACCI: [],
            FabricCategory.TWO_FACE_WAFFLE_CLOTH: [],
            FabricCategory.OTHER: []
        }

    def parse_fabric(self, data: Dict[str, str]):
        """Parse fabric data and categorize it"""
        try:
            name = data["name"]
            category = self._get_category(name)
            weight = data.get("weight", "")
            width = data.get("width", "")
            fabric = Fabric(name, category, weight, width)
            self.fabrics[category].append(fabric)
        except KeyError as e:
            print(f"Error parsing fabric data: {e}")

    def _get_category(self, name: str) -> FabricCategory:
        """Determine fabric category based on name"""
        name = name.lower()
        if "french terry" in name:
            return FabricCategory.FRENCH_TERRY
        elif "hacci" in name:
            return FabricCategory.HACCI
        elif "two face waffle cloth" in name:
            return FabricCategory.TWO_FACE_WAFFLE_CLOTH
        else:
            return FabricCategory.OTHER

    def organize_fabrics(self):
        """Organize fabrics by category"""
        return self.fabrics

def main():
    parser = FabricParser()

    # Example fabric data
    fabrics_data = [
        {"name": "French Terry Fabric", "weight": "300gsm", "width": "180cm"},
        {"name": "Hacci Fabric", "weight": "250gsm", "width": "160cm"},
        {"name": "Two Face Waffle Cloth", "weight": "200gsm", "width": "140cm"},
        {"name": "Unknown Fabric", "weight": "100gsm", "width": "120cm"},
        {"name": "French Terry Cloth", "weight": "350gsm", "width": "200cm"},
    ]

    for fabric_data in fabrics_data:
        parser.parse_fabric(fabric_data)

    organized_fabrics = parser.organize_fabrics()

    for category, fabrics in organized_fabrics.items():
        print(f"Category: {category.value}")
        for fabric in fabrics:
            print(fabric)
        print()

if __name__ == "__main__":
    main()
```
