"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: Develop a program to calculate the environmental impact of architectural materials used in projects like those described by Linea 7, emphasizing sustainability and livability.
Generated: DETERMINISTIC_948a05c00322f84c
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Material:
    """
    A class to represent a building material and its environmental impact.
    """

    def __init__(self, name, carbon_footprint, recyclability, durability):
        """
        Initializes a Material instance.

        :param name: str - The name of the material.
        :param carbon_footprint: float - The carbon footprint of the material (kg CO2e per unit).
        :param recyclability: float - The recyclability percentage of the material (0 to 100).
        :param durability: float - The durability of the material (years).
        """
        self.name = name
        self.carbon_footprint = carbon_footprint
        self.recyclability = recyclability
        self.durability = durability

    def environmental_impact(self, quantity):
        """
        Calculates the total environmental impact of the material based on quantity.

        :param quantity: float - The quantity of the material used.
        :return: dict - A dictionary containing the total carbon footprint and recyclability impact.
        """
        total_footprint = self.carbon_footprint * quantity
        recyclability_impact = (self.recyclability / 100) * total_footprint
        return {
            "total_carbon_footprint": total_footprint,
            "recyclability_impact": recyclability_impact
        }


class Project:
    """
    A class to represent a construction project and its materials.
    """

    def __init__(self, name):
        """
        Initializes a Project instance.

        :param name: str - The name of the project.
        """
        self.name = name
        self.materials = []

    def add_material(self, material, quantity):
        """
        Adds a material to the project.

        :param material: Material - The material to be added.
        :param quantity: float - The quantity of the material.
        """
        self.materials.append((material, quantity))

    def calculate_total_impact(self):
        """
        Calculates the total environmental impact of all materials in the project.

        :return: dict - A dictionary containing the total carbon footprint and recyclability impact.
        """
        total_impact = {
            "total_carbon_footprint": 0,
            "total_recyclability_impact": 0
        }

        for material, quantity in self.materials:
            impact = material.environmental_impact(quantity)
            total_impact["total_carbon_footprint"] += impact["total_carbon_footprint"]
            total_impact["total_recyclability_impact"] += impact["recyclability_impact"]

        return total_impact


def load_materials_from_json(file_path):
    """
    Loads materials from a JSON file.

    :param file_path: str - The path to the JSON file.
    :return: list - A list of Material instances.
    """
    try:
        with open(file_path, 'r') as file:
            materials_data = json.load(file)
            materials = []
            for item in materials_data:
                materials.append(Material(
                    name=item['name'],
                    carbon_footprint=item['carbon_footprint'],
                    recyclability=item['recyclability'],
                    durability=item['durability']
                ))
            return materials
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def main():
    """
    Main function to execute the program.
    """
    # Load materials from a JSON file
    materials = load_materials_from_json('materials.json')

    # Create a project
    project = Project("Sustainable Building Project")

    # Add materials to the project
    for material in materials:
        project.add_material(material, quantity=100)  # Example quantity

    # Calculate and display the total environmental impact
    total_impact = project.calculate_total_impact()
    print(f"Total Carbon Footprint: {total_impact['total_carbon_footprint']} kg CO2e")
    print(f"Total Recyclability Impact: {total_impact['total_recyclability_impact']} kg CO2e")

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have a `materials.json` file in the same directory with the appropriate structure to run this code successfully. The JSON file should contain an array of materials with their respective properties.
