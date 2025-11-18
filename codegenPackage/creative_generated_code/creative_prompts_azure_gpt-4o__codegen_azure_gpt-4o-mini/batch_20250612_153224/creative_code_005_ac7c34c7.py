"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bursapleksi.com.tr
Prompt: Develop a script to categorize plexiglass and polycarbonate sheets by thickness, color, and application, as outlined in Bursa Pleksi Merkezi's product descriptions.
Generated: DETERMINISTIC_ac7c34c745893ec0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Sheet:
    """Class representing a sheet of material with attributes for thickness, color, and application."""
    
    def __init__(self, thickness, color, application):
        """
        Initializes a new Sheet instance.
        
        :param thickness: The thickness of the sheet in mm.
        :param color: The color of the sheet.
        :param application: The intended application for the sheet.
        """
        self.thickness = thickness
        self.color = color
        self.application = application

    def to_dict(self):
        """Convert the Sheet instance to a dictionary."""
        return {
            "thickness": self.thickness,
            "color": self.color,
            "application": self.application
        }


class SheetCatalog:
    """Class to manage a catalog of sheets."""
    
    def __init__(self):
        """Initializes an empty sheet catalog."""
        self.sheets = []

    def add_sheet(self, sheet):
        """
        Adds a new sheet to the catalog.

        :param sheet: An instance of Sheet to be added.
        """
        if not isinstance(sheet, Sheet):
            raise ValueError("Only instances of Sheet can be added to the catalog.")
        self.sheets.append(sheet)

    def categorize_sheets(self):
        """Categorize sheets based on their attributes."""
        categorized = {}
        
        for sheet in self.sheets:
            key = (sheet.thickness, sheet.color, sheet.application)
            if key not in categorized:
                categorized[key] = []
            categorized[key].append(sheet)

        return categorized

    def export_to_json(self, filename):
        """
        Exports the sheet catalog to a JSON file.

        :param filename: The name of the file to which the data will be saved.
        """
        data = [sheet.to_dict() for sheet in self.sheets]
        try:
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except IOError as e:
            print(f"Error writing to file {filename}: {e}")


def main():
    """Main function to demonstrate the SheetCatalog functionality."""
    catalog = SheetCatalog()

    # Sample data - in a real application, this could come from a database or user input
    example_sheets = [
        Sheet(3, 'clear', 'signage'),
        Sheet(5, 'blue', 'prototyping'),
        Sheet(10, 'green', 'display cases'),
        Sheet(3, 'clear', 'signage'),  # Duplicate for demonstration
        Sheet(8, 'smoked', 'safety glazing'),
    ]

    # Adding sheets to the catalog
    for sheet in example_sheets:
        catalog.add_sheet(sheet)

    # Categorizing sheets
    categorized_sheets = catalog.categorize_sheets()
    print("Categorized Sheets:")
    for key, sheets in categorized_sheets.items():
        print(f"Thickness: {key[0]}mm, Color: {key[1]}, Application: {key[2]}, Count: {len(sheets)}")

    # Exporting the catalog to JSON
    catalog.export_to_json("sheet_catalog.json")


if __name__ == "__main__":
    main()
```
