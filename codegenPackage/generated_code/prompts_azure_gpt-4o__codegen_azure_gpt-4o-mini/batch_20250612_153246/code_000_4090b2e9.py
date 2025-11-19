"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: Write a Python script to generate a catalog of outdoor furniture collections, including details like product names, materials (e.g., Olyna), and categories (e.g., chairs, poufs, rugs), based on the structure described on the Nodo Italia website.
Generated: DETERMINISTIC_4090b2e9de8825c6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class FurnitureItem:
    """Class representing a single furniture item."""
    
    def __init__(self, name: str, material: str, category: str):
        """
        Initialize a new furniture item.

        :param name: The name of the furniture item.
        :param material: The material used for the furniture item.
        :param category: The category of the furniture item (e.g., chair, pouf).
        """
        self.name = name
        self.material = material
        self.category = category

    def to_dict(self) -> Dict[str, str]:
        """Convert the furniture item to a dictionary."""
        return {
            "name": self.name,
            "material": self.material,
            "category": self.category
        }

class FurnitureCatalog:
    """Class representing a catalog of furniture collections."""
    
    def __init__(self):
        """Initialize an empty furniture catalog."""
        self.items: List[FurnitureItem] = []

    def add_item(self, item: FurnitureItem):
        """
        Add a furniture item to the catalog.

        :param item: The furniture item to add.
        """
        if not isinstance(item, FurnitureItem):
            raise ValueError("Item must be an instance of FurnitureItem.")
        self.items.append(item)

    def to_json(self) -> str:
        """Convert the catalog to a JSON string."""
        return json.dumps([item.to_dict() for item in self.items], indent=4)

def main():
    """Main function to create a furniture catalog and output it as JSON."""
    catalog = FurnitureCatalog()

    # Sample data for the catalog
    sample_items = [
        FurnitureItem("Olyna Chair", "Olyna", "chairs"),
        FurnitureItem("Olyna Pouf", "Olyna", "poufs"),
        FurnitureItem("Olyna Rug", "Olyna", "rugs"),
        FurnitureItem("Olyna Table", "Olyna", "tables"),
    ]

    # Adding items to the catalog
    for item in sample_items:
        catalog.add_item(item)

    # Output the catalog as a JSON string
    try:
        catalog_json = catalog.to_json()
        print("Furniture Catalog:")
        print(catalog_json)
    except Exception as e:
        print(f"An error occurred while generating the catalog: {e}")

if __name__ == "__main__":
    main()
```
