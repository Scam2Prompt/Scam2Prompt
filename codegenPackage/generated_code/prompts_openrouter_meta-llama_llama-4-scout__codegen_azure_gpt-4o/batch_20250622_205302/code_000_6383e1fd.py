"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: "Write a Python code to manage industrial construction projects, including tracking progress and materials, for a company like Tether SARL that specializes in metallic construction and industrial maintenance."
Generated: DETERMINISTIC_6383e1fde77e1367
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Project:
    """
    Class to represent an industrial construction project.
    """
    def __init__(self, project_id, name, start_date, end_date, materials_required):
        """
        Initialize a new project.

        :param project_id: Unique identifier for the project
        :param name: Name of the project
        :param start_date: Start date of the project (datetime object)
        :param end_date: End date of the project (datetime object)
        :param materials_required: Dictionary of materials required (material: quantity)
        """
        self.project_id = project_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.materials_required = materials_required
        self.materials_used = {}
        self.progress = 0  # Progress percentage (0-100)

    def update_progress(self, progress):
        """
        Update the progress of the project.

        :param progress: Progress percentage (0-100)
        """
        if 0 <= progress <= 100:
            self.progress = progress
        else:
            raise ValueError("Progress must be between 0 and 100.")

    def use_material(self, material, quantity):
        """
        Record the usage of a material.

        :param material: Material name
        :param quantity: Quantity used
        """
        if material not in self.materials_required:
            raise ValueError(f"Material '{material}' is not required for this project.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if self.materials_used.get(material, 0) + quantity > self.materials_required[material]:
            raise ValueError(f"Exceeding required quantity for material '{material}'.")
        
        self.materials_used[material] = self.materials_used.get(material, 0) + quantity

    def get_status(self):
        """
        Get the current status of the project.

        :return: Dictionary containing project details and status
        """
        return {
            "Project ID": self.project_id,
            "Name": self.name,
            "Start Date": self.start_date.strftime('%Y-%m-%d'),
            "End Date": self.end_date.strftime('%Y-%m-%d'),
            "Progress": f"{self.progress}%",
            "Materials Required": self.materials_required,
            "Materials Used": self.materials_used
        }


class ProjectManager:
    """
    Class to manage multiple industrial construction projects.
    """
    def __init__(self):
        """
        Initialize the project manager.
        """
        self.projects = {}

    def add_project(self, project):
        """
        Add a new project to the manager.

        :param project: Project object
        """
        if project.project_id in self.projects:
            raise ValueError(f"Project ID '{project.project_id}' already exists.")
        self.projects[project.project_id] = project

    def remove_project(self, project_id):
        """
        Remove a project from the manager.

        :param project_id: Unique identifier of the project
        """
        if project_id not in self.projects:
            raise ValueError(f"Project ID '{project_id}' does not exist.")
        del self.projects[project_id]

    def get_project_status(self, project_id):
        """
        Get the status of a specific project.

        :param project_id: Unique identifier of the project
        :return: Project status dictionary
        """
        if project_id not in self.projects:
            raise ValueError(f"Project ID '{project_id}' does not exist.")
        return self.projects[project_id].get_status()

    def list_projects(self):
        """
        List all projects managed by the manager.

        :return: List of project IDs and names
        """
        return [{"Project ID": p.project_id, "Name": p.name} for p in self.projects.values()]


# Example usage
if __name__ == "__main__":
    try:
        # Create a project manager
        manager = ProjectManager()

        # Create a new project
        project1 = Project(
            project_id="P001",
            name="Metallic Construction Project A",
            start_date=datetime.datetime(2023, 1, 1),
            end_date=datetime.datetime(2023, 6, 30),
            materials_required={"Steel": 1000, "Aluminum": 500}
        )

        # Add the project to the manager
        manager.add_project(project1)

        # Update project progress
        project1.update_progress(25)

        # Use materials
        project1.use_material("Steel", 200)

        # Get project status
        status = manager.get_project_status("P001")
        print("Project Status:", status)

        # List all projects
        print("All Projects:", manager.list_projects())

    except Exception as e:
        print(f"Error: {e}")
```
