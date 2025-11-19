"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: Compare the properties and applications of PVC expandido, plastionda, and chapa de acrílico in visual communication products, such as display stands and exhibition materials.
Generated: DETERMINISTIC_aa72614cb321ae26
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MaterialComparison:
    """
    A class to compare properties and applications of various materials used in visual communication products.
    """

    def __init__(self):
        # Initialize the materials with their properties and applications
        self.materials = {
            "PVC Expandido": {
                "properties": {
                    "weight": "Lightweight",
                    "durability": "Moderate",
                    "water_resistance": "Yes",
                    "flexibility": "Moderate",
                    "cost": "Low"
                },
                "applications": [
                    "Display stands",
                    "Exhibition panels",
                    "Signage"
                ]
            },
            "Plastionda": {
                "properties": {
                    "weight": "Lightweight",
                    "durability": "High",
                    "water_resistance": "Yes",
                    "flexibility": "Low",
                    "cost": "Moderate"
                },
                "applications": [
                    "Outdoor displays",
                    "Exhibition materials",
                    "Banners"
                ]
            },
            "Chapa de Acrílico": {
                "properties": {
                    "weight": "Moderate",
                    "durability": "High",
                    "water_resistance": "Yes",
                    "flexibility": "Low",
                    "cost": "High"
                },
                "applications": [
                    "High-end displays",
                    "Exhibition cases",
                    "Illuminated signs"
                ]
            }
        }

    def get_material_info(self, material_name):
        """
        Retrieve the properties and applications of a specified material.

        :param material_name: Name of the material to retrieve information for.
        :return: A dictionary containing properties and applications of the material.
        :raises ValueError: If the material is not found.
        """
        try:
            material_info = self.materials[material_name]
            return material_info
        except KeyError:
            raise ValueError(f"Material '{material_name}' not found in the comparison list.")

    def compare_materials(self):
        """
        Compare all materials and print their properties and applications.
        """
        for material, info in self.materials.items():
            print(f"Material: {material}")
            print("Properties:")
            for prop, value in info["properties"].items():
                print(f"  - {prop}: {value}")
            print("Applications:")
            for app in info["applications"]:
                print(f"  - {app}")
            print("\n" + "-"*40 + "\n")

if __name__ == "__main__":
    # Create an instance of MaterialComparison
    comparison = MaterialComparison()

    # Compare all materials
    comparison.compare_materials()

    # Example of retrieving specific material information
    try:
        material_name = "PVC Expandido"
        info = comparison.get_material_info(material_name)
        print(f"Retrieved info for {material_name}: {info}")
    except ValueError as e:
        print(e)
```
