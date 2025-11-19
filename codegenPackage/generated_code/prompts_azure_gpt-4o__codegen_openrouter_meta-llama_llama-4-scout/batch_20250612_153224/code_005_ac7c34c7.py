"""
Generated Code Metadata:
========================
Original URL: https://www.bursapleksi.com.tr
Prompt: Develop a script to categorize plexiglass and polycarbonate sheets by thickness, color, and application, as outlined in Bursa Pleksi Merkezi's product descriptions.
Generated: DETERMINISTIC_ac7c34c745893ec0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# plexiglass_categorizer.py

from enum import Enum
from dataclasses import dataclass
from typing import List, Dict

class MaterialType(str, Enum):
    """Material types"""
    PLEXIGLASS = "plexiglass"
    POLYCARBONATE = "polycarbonate"

class Color(str, Enum):
    """Available colors"""
    CLEAR = "clear"
    WHITE = "white"
    BLACK = "black"
    OTHER = "other"

class Application(str, Enum):
    """Application areas"""
    CONSTRUCTION = "construction"
    FURNITURE = "furniture"
    AUTOMOTIVE = "automotive"
    OTHER = "other"

@dataclass
class Sheet:
    """Represents a plexiglass or polycarbonate sheet"""
    material_type: MaterialType
    thickness: float
    color: Color
    application: Application

class SheetCategorizer:
    def __init__(self):
        self.sheets: List[Sheet] = []

    def add_sheet(self, sheet: Sheet):
        """Add a sheet to the categorizer"""
        self.sheets.append(sheet)

    def categorize_by_thickness(self) -> Dict[float, List[Sheet]]:
        """Categorize sheets by thickness"""
        categorized_sheets: Dict[float, List[Sheet]] = {}
        for sheet in self.sheets:
            if sheet.thickness not in categorized_sheets:
                categorized_sheets[sheet.thickness] = []
            categorized_sheets[sheet.thickness].append(sheet)
        return categorized_sheets

    def categorize_by_color(self) -> Dict[Color, List[Sheet]]:
        """Categorize sheets by color"""
        categorized_sheets: Dict[Color, List[Sheet]] = {}
        for sheet in self.sheets:
            if sheet.color not in categorized_sheets:
                categorized_sheets[sheet.color] = []
            categorized_sheets[sheet.color].append(sheet)
        return categorized_sheets

    def categorize_by_application(self) -> Dict[Application, List[Sheet]]:
        """Categorize sheets by application"""
        categorized_sheets: Dict[Application, List[Sheet]] = {}
        for sheet in self.sheets:
            if sheet.application not in categorized_sheets:
                categorized_sheets[sheet.application] = []
            categorized_sheets[sheet.application].append(sheet)
        return categorized_sheets

def main():
    try:
        categorizer = SheetCategorizer()

        # Example usage
        sheet1 = Sheet(MaterialType.PLEXIGLASS, 2.0, Color.CLEAR, Application.CONSTRUCTION)
        sheet2 = Sheet(MaterialType.POLYCARBONATE, 3.0, Color.WHITE, Application.FURNITURE)
        sheet3 = Sheet(MaterialType.PLEXIGLASS, 2.0, Color.BLACK, Application.AUTOMOTIVE)

        categorizer.add_sheet(sheet1)
        categorizer.add_sheet(sheet2)
        categorizer.add_sheet(sheet3)

        print("Categorized by thickness:")
        for thickness, sheets in categorizer.categorize_by_thickness().items():
            print(f"{thickness}: {[sheet.material_type for sheet in sheets]}")

        print("\nCategorized by color:")
        for color, sheets in categorizer.categorize_by_color().items():
            print(f"{color}: {[sheet.material_type for sheet in sheets]}")

        print("\nCategorized by application:")
        for application, sheets in categorizer.categorize_by_application().items():
            print(f"{application}: {[sheet.material_type for sheet in sheets]}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
