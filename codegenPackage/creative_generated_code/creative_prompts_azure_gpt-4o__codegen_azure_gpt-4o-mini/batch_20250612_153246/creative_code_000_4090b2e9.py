"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodoitalia.com
Prompt: Write a Python script to generate a catalog of outdoor furniture collections, including details like product names, materials (e.g., Olyna), and categories (e.g., chairs, poufs, rugs), based on the structure described on the Nodo Italia website.
Generated: DETERMINISTIC_4090b2e9de8825c6
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
from typing import List, Dict, Any

class FurnitureItem:
    """
    A class to represent an outdoor furniture item.
    """
    def __init__(self, name: str, material: str, category: str):
        self.name = name
        self.material = material
        self.category = category

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the FurnitureItem instance to a dictionary.
        """
        return {
            'name': self.name,
            'material': self.material,
            'category': self.category
        }

class FurnitureCatalog:
    """
    A class to represent a catalog of outdoor furniture collections.
    """
    def __init__(self):
        self.items: List[FurnitureItem] = []

    def add_item(self, item: FurnitureItem) -> None:
        """
        Add a FurnitureItem to the catalog.
        """
        self.items.append(item)

    def to_json(self) -> str:
        """
        Convert the catalog to a JSON string.
        """
        return json.dumps([item.to_dict() for item in self.items], indent=4)

def main() -> None:
    """
    Main function to create a furniture catalog and generate a JSON representation.
    """
    # Create a catalog instance
    catalog = FurnitureCatalog()

    # Sample data to populate the catalog
    sample_data = [
        {'name': 'Olyna Chair', 'material': 'Olyna', 'category': 'chairs'},
        {'name': 'Olyna Pouf', 'material': 'Olyna', 'category': 'poufs'},
        {'name': 'Olyna Rug', 'material': 'Olyna', 'category': 'rugs'},
        {'name': 'Olyna Sofa', 'material': 'Olyna', 'category': 'sofas'},
    ]

    # Populate the catalog with furniture items
    for data in sample_data:
        try:
            item = FurnitureItem(name=data['name'], material=data['material'], category=data['category'])
            catalog.add_item(item)
        except KeyError as e:
            print(f"Missing key in data: {e}")
        except Exception as e:
            print(f"An error occurred while adding item: {e}")

    # Generate and print the JSON representation of the catalog
    try:
        catalog_json = catalog.to_json()
        print(catalog_json)
    except Exception as e:
        print(f"An error occurred while converting catalog to JSON: {e}")

if __name__ == '__main__':
    main()
```
