"""
Generated Code Metadata:
========================
Original URL: https://tari.ee
Prompt: Create a tool for comparing architectural project designs, inspired by the diverse projects listed on Tari.ee, such as Hornslandet and Päästeamet.
Generated: DETERMINISTIC_7fda1a65ba48ca8a
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# architectural_project_comparator.py

import json
import os

class ArchitecturalProject:
    """Represents an architectural project with its attributes."""

    def __init__(self, name, location, year, architect, description):
        """
        Initializes an ArchitecturalProject instance.

        Args:
            name (str): The name of the project.
            location (str): The location of the project.
            year (int): The year the project was completed.
            architect (str): The architect or architectural firm.
            description (str): A brief description of the project.
        """
        self.name = name
        self.location = location
        self.year = year
        self.architect = architect
        self.description = description

    def to_dict(self):
        """Returns a dictionary representation of the project."""
        return {
            "name": self.name,
            "location": self.location,
            "year": self.year,
            "architect": self.architect,
            "description": self.description,
        }

class ProjectComparator:
    """Compares architectural projects based on their attributes."""

    def __init__(self, projects):
        """
        Initializes a ProjectComparator instance.

        Args:
            projects (list[ArchitecturalProject]): A list of projects to compare.
        """
        self.projects = projects

    def compare_by_year(self):
        """Returns a list of projects sorted by year."""
        return sorted(self.projects, key=lambda x: x.year)

    def compare_by_architect(self):
        """Returns a dictionary of projects grouped by architect."""
        architect_projects = {}
        for project in self.projects:
            if project.architect not in architect_projects:
                architect_projects[project.architect] = []
            architect_projects[project.architect].append(project)
        return architect_projects

def load_projects_from_json(file_path):
    """
    Loads a list of projects from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list[ArchitecturalProject]: A list of projects loaded from the JSON file.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return [ArchitecturalProject(**project) for project in data]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return []

def save_projects_to_json(projects, file_path):
    """
    Saves a list of projects to a JSON file.

    Args:
        projects (list[ArchitecturalProject]): A list of projects to save.
        file_path (str): The path to the JSON file.

    Raises:
        Exception: If an error occurs while writing to the file.
    """
    try:
        data = [project.to_dict() for project in projects]
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving projects: {e}")

def main():
    # Example usage
    projects = [
        ArchitecturalProject("Hornslandet", "Sweden", 2020, "Inredningsgruppen", "A unique residential building"),
        ArchitecturalProject("Päästeamet", "Estonia", 2019, "Killa Design", "A modern fire station"),
    ]

    comparator = ProjectComparator(projects)

    print("Projects sorted by year:")
    for project in comparator.compare_by_year():
        print(project.name, project.year)

    print("\nProjects grouped by architect:")
    for architect, architect_projects in comparator.compare_by_architect().items():
        print(architect)
        for project in architect_projects:
            print(f"  - {project.name}")

    # Load and save projects to JSON
    json_file_path = "projects.json"
    loaded_projects = load_projects_from_json(json_file_path)
    if loaded_projects:
        print("\nLoaded projects:")
        for project in loaded_projects:
            print(project.name)

    save_projects_to_json(projects, json_file_path)

if __name__ == "__main__":
    main()
```
