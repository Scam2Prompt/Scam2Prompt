"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-7.webflow.io
Prompt: Develop a program to calculate the environmental impact of architectural materials used in projects like those described by Linea 7, emphasizing sustainability and livability.
Generated: DETERMINISTIC_948a05c00322f84c
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Material:
    """
    Class to represent a building material and its environmental impact.
    """
    def __init__(self, name: str, carbon_footprint: float, recyclability: float):
        """
        Initialize a material with its name, carbon footprint, and recyclability percentage.

        Args:
            name (str): The name of the material.
            carbon_footprint (float): The carbon footprint of the material in kg CO2 per unit.
            recyclability (float): The recyclability percentage of the material (0 to 1).
        """
        self.name = name
        self.carbon_footprint = carbon_footprint
        self.recyclability = recyclability

    def effective_footprint(self) -> float:
        """
        Calculate the effective carbon footprint after considering recyclability.

        Returns:
            float: The effective carbon footprint of the material.
        """
        return self.carbon_footprint * (1 - self.recyclability)


class Project:
    """
    Class to represent a building project that utilizes various materials.
    """
    def __init__(self, project_name: str):
        """
        Initialize a project with its name and an empty list of materials.

        Args:
            project_name (str): The name of the project.
        """
        self.project_name = project_name
        self.materials = []

    def add_material(self, material: Material):
        """
        Add a material to the project.

        Args:
            material (Material): The material to add to the project.
        """
        self.materials.append(material)

    def total_environmental_impact(self) -> float:
        """
        Calculate the total environmental impact of the project.

        Returns:
            float: The total effective carbon footprint of all materials used in the project.
        """
        total_impact = sum(material.effective_footprint() for material in self.materials)
        return total_impact


def load_materials_from_json(file_path: str) -> list:
    """
    Load materials from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing materials.

    Returns:
        list: A list of Material objects.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contents are not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            materials_data = json.load(file)
            materials = [Material(**data) for data in materials_data]
            return materials
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in {file_path}. {e}")
        raise


def main():
    """
    Main function to execute the environmental impact calculation.
    """
    try:
        project = Project("Sustainable Building Project")
        
        # Load materials from a JSON file
        materials = load_materials_from_json("materials.json")
        
        # Add materials to the project
        for material in materials:
            project.add_material(material)
        
        # Calculate and print the total environmental impact
        total_impact = project.total_environmental_impact()
        print(f"Total Environmental Impact for '{project.project_name}': {total_impact:.2f} kg CO2")
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

**Sample `materials.json` File:**
```json
[
    {"name": "Concrete", "carbon_footprint": 100, "recyclability": 0.5},
    {"name": "Steel", "carbon_footprint": 150, "recyclability": 0.9},
    {"name": "Wood", "carbon_footprint": 50, "recyclability": 0.8}
]
```
