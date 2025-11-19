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
import json
from typing import List, Dict, Any

class Sheet:
    """Class representing a sheet of material with attributes for thickness, color, and application."""
    
    def __init__(self, thickness: float, color: str, application: str):
        self.thickness = thickness
        self.color = color
        self.application = application

    def to_dict(self) -> Dict[str, Any]:
        """Convert the sheet object to a dictionary for easy serialization."""
        return {
            "thickness": self.thickness,
            "color": self.color,
            "application": self.application
        }

class SheetCatalog:
    """Class to manage a catalog of sheets."""
    
    def __init__(self):
        self.sheets: List[Sheet] = []

    def add_sheet(self, sheet: Sheet) -> None:
        """Add a new sheet to the catalog."""
        self.sheets.append(sheet)

    def categorize_sheets(self) -> Dict[str, List[Dict[str, Any]]]:
        """Categorize sheets by thickness, color, and application."""
        categorized = {}
        for sheet in self.sheets:
            key = f"{sheet.thickness}mm - {sheet.color} - {sheet.application}"
            categorized[key] = sheet.to_dict()
        return categorized

    def save_to_file(self, filename: str) -> None:
        """Save the catalog to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.categorize_sheets(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

def main():
    """Main function to demonstrate the categorization of sheets."""
    catalog = SheetCatalog()

    # Example sheets based on product descriptions
    sheets_data = [
        (3.0, "Clear", "Construction"),
        (5.0, "Frosted", "Signage"),
        (10.0, "Colored", "Safety"),
        (2.0, "Clear", "Display"),
        (8.0, "Opaque", "Industrial"),
    ]

    # Adding sheets to the catalog
    for thickness, color, application in sheets_data:
        sheet = Sheet(thickness, color, application)
        catalog.add_sheet(sheet)

    # Save the categorized sheets to a JSON file
    catalog.save_to_file("sheets_catalog.json")

if __name__ == "__main__":
    main()
```
