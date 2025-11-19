"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://musicequipment.site
Prompt: How does musicequipment.site categorize its resources for music equipment?
Generated: DETERMINISTIC_4369d44af0051c5a
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class MusicEquipmentCatalog:
    """
    A class to represent a catalog of music equipment.
    """

    def __init__(self):
        """Initialize the catalog with an empty list of equipment."""
        self.equipment_list: List[Dict[str, Any]] = []

    def add_equipment(self, name: str, category: str, price: float) -> None:
        """
        Add a new piece of music equipment to the catalog.

        :param name: The name of the equipment.
        :param category: The category of the equipment (e.g., 'Guitar', 'Drum').
        :param price: The price of the equipment.
        :raises ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")

        equipment = {
            "name": name,
            "category": category,
            "price": price
        }
        self.equipment_list.append(equipment)

    def categorize_resources(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Categorize equipment resources by their category.

        :return: A dictionary with categories as keys and lists of equipment as values.
        """
        categorized_resources = {}
        for equipment in self.equipment_list:
            category = equipment["category"]
            if category not in categorized_resources:
                categorized_resources[category] = []
            categorized_resources[category].append(equipment)

        return categorized_resources

    def save_to_file(self, filename: str) -> None:
        """
        Save the catalog to a JSON file.

        :param filename: The name of the file to save the catalog.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.equipment_list, json_file, indent=4)
        except Exception as e:
            raise IOError(f"An error occurred while writing to the file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load equipment data from a JSON file into the catalog.

        :param filename: The name of the file to load the catalog from.
        :raises IOError: If there is an error reading the file.
        :raises json.JSONDecodeError: If the file contents are not valid JSON.
        """
        try:
            with open(filename, 'r') as json_file:
                self.equipment_list = json.load(json_file)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"An error occurred while reading the file: {e}")

# Example usage:
if __name__ == "__main__":
    catalog = MusicEquipmentCatalog()
    
    # Add some equipment to the catalog
    catalog.add_equipment("Fender Stratocaster", "Guitar", 1200.00)
    catalog.add_equipment("Yamaha DTX402", "Drum", 500.00)
    catalog.add_equipment("Shure SM58", "Microphone", 100.00)

    # Categorize the resources
    categorized = catalog.categorize_resources()
    print(json.dumps(categorized, indent=4))

    # Save the catalog to a file
    catalog.save_to_file("music_equipment_catalog.json")

    # Load the catalog from a file
    catalog.load_from_file("music_equipment_catalog.json")
```
