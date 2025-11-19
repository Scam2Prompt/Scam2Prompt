"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: What are the steps to create a scientific and technical support system for construction projects, as mentioned by the Geotechnical Center?
Generated: DETERMINISTIC_5a9f7c9346732916
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# scientific_and_technical_support_system.py

class ConstructionProject:
    """Represents a construction project."""

    def __init__(self, project_name, location):
        """
        Initializes a ConstructionProject.

        Args:
            project_name (str): The name of the project.
            location (str): The location of the project.
        """
        self.project_name = project_name
        self.location = location
        self.geotechnical_data = []

    def add_geotechnical_data(self, data):
        """
        Adds geotechnical data to the project.

        Args:
            data (dict): The geotechnical data to add.
        """
        self.geotechnical_data.append(data)


class GeotechnicalCenter:
    """Represents the Geotechnical Center."""

    def __init__(self):
        """Initializes a GeotechnicalCenter."""
        self.projects = {}

    def create_project(self, project_name, location):
        """
        Creates a new construction project.

        Args:
            project_name (str): The name of the project.
            location (str): The location of the project.

        Returns:
            ConstructionProject: The created project.
        """
        if project_name in self.projects:
            raise ValueError("Project already exists")

        project = ConstructionProject(project_name, location)
        self.projects[project_name] = project
        return project

    def get_project(self, project_name):
        """
        Gets a construction project.

        Args:
            project_name (str): The name of the project.

        Returns:
            ConstructionProject: The project with the given name.

        Raises:
            ValueError: If the project does not exist.
        """
        if project_name not in self.projects:
            raise ValueError("Project does not exist")

        return self.projects[project_name]

    def provide_scientific_and_technical_support(self, project_name):
        """
        Provides scientific and technical support for a construction project.

        Args:
            project_name (str): The name of the project.

        Returns:
            list: The steps to provide scientific and technical support.
        """
        try:
            project = self.get_project(project_name)
        except ValueError as e:
            print(f"Error: {e}")
            return []

        steps = [
            "Conduct site investigation",
            "Collect and analyze geotechnical data",
            "Develop a geotechnical model",
            "Provide design recommendations",
            "Monitor and analyze data during construction"
        ]

        # Simulate providing support
        for step in steps:
            print(f"Providing {step} for {project_name}...")

        return steps


def main():
    geotechnical_center = GeotechnicalCenter()

    project_name = "Example Project"
    location = "123 Main St"

    try:
        project = geotechnical_center.create_project(project_name, location)
        geotechnical_data = {
            "soil_type": "clay",
            "density": 1.8
        }
        project.add_geotechnical_data(geotechnical_data)

        steps = geotechnical_center.provide_scientific_and_technical_support(project_name)
        print("Steps to provide scientific and technical support:")
        for i, step in enumerate(steps, start=1):
            print(f"{i}. {step}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
