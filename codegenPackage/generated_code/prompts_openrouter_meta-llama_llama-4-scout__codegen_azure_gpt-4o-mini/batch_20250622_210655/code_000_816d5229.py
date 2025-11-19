"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: "Generate a Python script to manage interior design projects using the services offered by The Design Umbrella, including space curation and material selection."
Generated: DETERMINISTIC_816d52295d3146b9
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class InteriorDesignProject:
    """
    A class to represent an interior design project.
    """

    def __init__(self, project_name: str, client_name: str):
        """
        Initializes a new interior design project.

        :param project_name: Name of the project
        :param client_name: Name of the client
        """
        self.project_name = project_name
        self.client_name = client_name
        self.space_curation = []
        self.material_selection = []

    def add_space(self, space: str) -> None:
        """
        Adds a space to the project.

        :param space: Name of the space to be curated
        """
        self.space_curation.append(space)

    def add_material(self, material: str) -> None:
        """
        Adds a material to the project.

        :param material: Name of the material to be selected
        """
        self.material_selection.append(material)

    def get_project_details(self) -> Dict[str, Any]:
        """
        Returns the details of the project.

        :return: A dictionary containing project details
        """
        return {
            "project_name": self.project_name,
            "client_name": self.client_name,
            "space_curation": self.space_curation,
            "material_selection": self.material_selection
        }

    def save_project(self, filename: str) -> None:
        """
        Saves the project details to a JSON file.

        :param filename: The name of the file to save the project details
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_project_details(), file, indent=4)
            print(f"Project '{self.project_name}' saved successfully to '{filename}'.")
        except IOError as e:
            print(f"Error saving project to file: {e}")

    @staticmethod
    def load_project(filename: str) -> 'InteriorDesignProject':
        """
        Loads a project from a JSON file.

        :param filename: The name of the file to load the project details from
        :return: An instance of InteriorDesignProject
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                project = InteriorDesignProject(data['project_name'], data['client_name'])
                project.space_curation = data['space_curation']
                project.material_selection = data['material_selection']
                return project
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading project from file: {e}")
            return None

def main():
    """
    Main function to demonstrate the usage of the InteriorDesignProject class.
    """
    # Create a new project
    project = InteriorDesignProject("Modern Living Room", "Alice Smith")

    # Add spaces and materials
    project.add_space("Living Room")
    project.add_space("Dining Area")
    project.add_material("Leather Sofa")
    project.add_material("Wooden Dining Table")

    # Save the project to a file
    project.save_project("modern_living_room_project.json")

    # Load the project from the file
    loaded_project = InteriorDesignProject.load_project("modern_living_room_project.json")
    if loaded_project:
        print("Loaded Project Details:")
        print(json.dumps(loaded_project.get_project_details(), indent=4))

if __name__ == "__main__":
    main()
```
