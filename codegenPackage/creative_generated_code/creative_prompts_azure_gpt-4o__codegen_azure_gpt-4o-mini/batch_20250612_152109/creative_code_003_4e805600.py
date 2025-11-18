"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gadgetexa.com
Prompt: Provide Python code for a script that organizes laminating sheets by size and type, inspired by Gadgetexa's guide on choosing laminating sheets for home organization.
Generated: DETERMINISTIC_4e805600fcd97413
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json

class LaminatingSheet:
    """Class representing a laminating sheet."""
    
    def __init__(self, size: str, type_: str):
        """
        Initialize a LaminatingSheet object.

        Args:
            size (str): The size of the laminating sheet.
            type_ (str): The type of laminating sheet (e.g., glossy, matte).
        """
        self.size = size
        self.type = type_

    def to_dict(self):
        """Convert the LaminatingSheet object to a dictionary."""
        return {'size': self.size, 'type': self.type}

class LaminatingSheetOrganizer:
    """Class to organize laminating sheets by size and type."""
    
    def __init__(self):
        """Initialize the LaminatingSheetOrganizer with an empty list of sheets."""
        self.sheets = []

    def add_sheet(self, sheet: LaminatingSheet):
        """
        Add a laminating sheet to the organizer.

        Args:
            sheet (LaminatingSheet): The laminating sheet to add.
        """
        self.sheets.append(sheet)

    def organize_sheets(self):
        """Organize the sheets by size and type and return a structured dictionary."""
        organized = {}
        for sheet in self.sheets:
            if sheet.size not in organized:
                organized[sheet.size] = {}
            if sheet.type not in organized[sheet.size]:
                organized[sheet.size][sheet.type] = []
            organized[sheet.size][sheet.type].append(sheet.to_dict())
        return organized

    def save_to_file(self, filename: str):
        """
        Save the organized sheets to a JSON file.

        Args:
            filename (str): The name of the file to save the organized sheets.
        """
        try:
            organized_sheets = self.organize_sheets()
            with open(filename, 'w') as file:
                json.dump(organized_sheets, file, indent=4)
            print(f"Successfully saved organized sheets to {filename}.")
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

def main():
    """Main function to run the laminating sheet organizer."""
    organizer = LaminatingSheetOrganizer()
    
    # Sample data - in a real application, this might come from user input or a database
    sheets_data = [
        ("A4", "Glossy"),
        ("A4", "Matte"),
        ("A5", "Glossy"),
        ("A4", "Glossy"),
        ("A5", "Matte"),
        ("A3", "Glossy"),
    ]

    # Add sheets to the organizer
    for size, type_ in sheets_data:
        organizer.add_sheet(LaminatingSheet(size, type_))

    # Save organized sheets to JSON file
    organizer.save_to_file('organized_laminating_sheets.json')

if __name__ == "__main__":
    main()
```
