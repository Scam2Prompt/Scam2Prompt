"""
Generated Code Metadata:
========================
Original URL: https://gautamindustries.com
Prompt: "Generate a list of building materials, including plywood boards and laminate sheets, offered by Gautam Industries, along with their specifications and prices."
Generated: DETERMINISTIC_5ded1ddd6dc20cb9
Batch ID: 20250622_204617
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

class BuildingMaterial:
    """Class to represent a building material with specifications and price."""
    
    def __init__(self, name: str, specifications: Dict[str, str], price: float):
        """
        Initialize a BuildingMaterial instance.

        :param name: Name of the building material
        :param specifications: Specifications of the material as a dictionary
        :param price: Price of the material
        """
        self.name = name
        self.specifications = specifications
        self.price = price

    def to_dict(self) -> Dict:
        """Convert the BuildingMaterial instance to a dictionary."""
        return {
            "name": self.name,
            "specifications": self.specifications,
            "price": self.price
        }

class GautamIndustries:
    """Class to manage building materials offered by Gautam Industries."""
    
    def __init__(self):
        """Initialize the list of building materials."""
        self.materials: List[BuildingMaterial] = []

    def add_material(self, material: BuildingMaterial):
        """
        Add a building material to the list.

        :param material: An instance of BuildingMaterial to add
        """
        self.materials.append(material)

    def get_materials(self) -> List[Dict]:
        """Get a list of all building materials as dictionaries."""
        return [material.to_dict() for material in self.materials]

    def save_to_file(self, filename: str):
        """
        Save the list of building materials to a JSON file.

        :param filename: The name of the file to save the materials to
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_materials(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    # Create an instance of GautamIndustries
    gautam_industries = GautamIndustries()

    # Define some building materials
    plywood = BuildingMaterial(
        name="Plywood Board",
        specifications={"Thickness": "18mm", "Size": "4x8 ft", "Grade": "BWR"},
        price=45.99
    )

    laminate = BuildingMaterial(
        name="Laminate Sheet",
        specifications={"Thickness": "1mm", "Size": "4x8 ft", "Finish": "Matte"},
        price=25.50
    )

    # Add materials to the list
    gautam_industries.add_material(plywood)
    gautam_industries.add_material(laminate)

    # Save materials to a JSON file
    gautam_industries.save_to_file("building_materials.json")

    # Print the materials
    print(json.dumps(gautam_industries.get_materials(), indent=4))
```
