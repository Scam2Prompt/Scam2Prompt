"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanurisupplies.com
Prompt: Develop a program to categorize office supplies into different sections (computers, printers, files, folders, etc.) for large-scale and small-scale businesses, as mentioned on Sanuri Supplies' website.
Generated: DETERMINISTIC_f8cee16ec6549a65
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import Dict, List, Any

class OfficeSuppliesCategorizer:
    """A class to categorize office supplies into different sections for businesses."""
    
    def __init__(self, supply_data: Dict[str, List[str]]):
        """
        Initializes the categorizer with supply data.
        
        Parameters:
        supply_data (dict): A dictionary where keys are categories and values are lists of items.
        """
        self.supply_data = supply_data

    def categorize_supplies(self) -> Dict[str, List[str]]:
        """Categorizes the office supplies based on predefined categories."""
        categorized_supplies = {}
        for category, items in self.supply_data.items():
            if not isinstance(items, list):
                raise ValueError(f"Items for {category} must be a list.")
            categorized_supplies[category] = [item for item in items if item]
        return categorized_supplies

    def save_to_file(self, file_path: str) -> None:
        """
        Saves the categorized supplies to a JSON file.
        
        Parameters:
        file_path (str): The path where the JSON file will be saved.
        
        Raises:
        IOError: If the file cannot be created or written to.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.categorize_supplies(), json_file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing to file: {e}")

def main() -> None:
    """Main function to run the office supplies categorizer."""
    # Sample supply data as mentioned in the user's request
    supply_data = {
        "Computers": ["Laptops", "Desktops", "Monitors"],
        "Printers": ["Inkjet Printers", "Laser Printers", "3D Printers"],
        "Files": ["Document Files", "Project Files"],
        "Folders": ["Manila Folders", "Plastic Folders"],
        "Stationery": ["Pens", "Pencils", "Notebooks"]
    }

    # Initialize the categorizer
    categorizer = OfficeSuppliesCategorizer(supply_data)
    
    # Define the output file path
    output_file_path = os.path.join(os.getcwd(), "categorized_supplies.json")
    
    # Save categorized supplies to a file
    try:
        categorizer.save_to_file(output_file_path)
        print(f"Categorized supplies successfully saved to {output_file_path}")
    except Exception as e:
        print(f"Failed to categorize supplies: {e}")

if __name__ == "__main__":
    main()
```
