"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: "Generate a catalog of outdoor furniture collections that feature sustainable materials, including a description of the eco-friendly features of the Olyna filament used in the products."
Generated: DETERMINISTIC_40cf1199be05e1f8
Batch ID: 20250622_210703
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

class OutdoorFurnitureCollection:
    """
    A class to represent a collection of outdoor furniture made from sustainable materials.
    """

    def __init__(self, name: str, description: str, eco_friendly_features: List[str]):
        """
        Initializes the OutdoorFurnitureCollection with a name, description, and eco-friendly features.

        :param name: The name of the furniture collection.
        :param description: A description of the collection.
        :param eco_friendly_features: A list of eco-friendly features of the collection.
        """
        self.name = name
        self.description = description
        self.eco_friendly_features = eco_friendly_features

    def to_dict(self) -> Dict:
        """
        Converts the collection to a dictionary format for easy serialization.

        :return: A dictionary representation of the collection.
        """
        return {
            "name": self.name,
            "description": self.description,
            "eco_friendly_features": self.eco_friendly_features
        }

def create_furniture_catalog() -> List[OutdoorFurnitureCollection]:
    """
    Creates a catalog of outdoor furniture collections featuring sustainable materials.

    :return: A list of OutdoorFurnitureCollection objects.
    """
    return [
        OutdoorFurnitureCollection(
            name="Olyna Collection",
            description="The Olyna Collection features elegant outdoor furniture crafted from sustainable materials, including Olyna filament.",
            eco_friendly_features=[
                "Made from 100% recycled materials",
                "UV-resistant and durable for long-lasting use",
                "Non-toxic and safe for the environment",
                "Lightweight yet sturdy design"
            ]
        ),
        OutdoorFurnitureCollection(
            name="EcoWave Collection",
            description="The EcoWave Collection combines modern design with eco-friendly materials, perfect for any outdoor space.",
            eco_friendly_features=[
                "Constructed from reclaimed wood",
                "Water-resistant finishes using natural oils",
                "Biodegradable packaging",
                "Supports local artisans"
            ]
        )
    ]

def save_catalog_to_json(catalog: List[OutdoorFurnitureCollection], filename: str) -> None:
    """
    Saves the furniture catalog to a JSON file.

    :param catalog: A list of OutdoorFurnitureCollection objects.
    :param filename: The name of the file to save the catalog to.
    """
    try:
        with open(filename, 'w') as json_file:
            json.dump([collection.to_dict() for collection in catalog], json_file, indent=4)
        print(f"Catalog successfully saved to {filename}.")
    except IOError as e:
        print(f"Error saving catalog to {filename}: {e}")

if __name__ == "__main__":
    # Create the furniture catalog
    catalog = create_furniture_catalog()
    
    # Save the catalog to a JSON file
    save_catalog_to_json(catalog, 'outdoor_furniture_catalog.json')
```
