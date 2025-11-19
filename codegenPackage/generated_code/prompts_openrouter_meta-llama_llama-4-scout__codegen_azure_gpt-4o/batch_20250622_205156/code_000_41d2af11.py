"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Write a Python script to manage construction projects for a company like 株式会社タイコーテクノ, including tracking pole construction work, electrical and civil engineering projects, and anti-ball net fence construction.
Generated: DETERMINISTIC_41d2af115455480a
Batch ID: 20250622_205156
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
    Base class for construction projects.
    """
    def __init__(self, project_id, name, start_date, end_date, status="Pending"):
        self.project_id = project_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def update_status(self, new_status):
        """
        Update the status of the project.
        """
        valid_statuses = ["Pending", "In Progress", "Completed", "On Hold"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status

    def __str__(self):
        """
        String representation of the project.
        """
        return f"Project ID: {self.project_id}, Name: {self.name}, Start Date: {self.start_date}, End Date: {self.end_date}, Status: {self.status}"


class PoleConstruction(Project):
    """
    Class for managing pole construction projects.
    """
    def __init__(self, project_id, name, start_date, end_date, pole_count, status="Pending"):
        super().__init__(project_id, name, start_date, end_date, status)
        self.pole_count = pole_count

    def __str__(self):
        return super().__str__() + f", Pole Count: {self.pole_count}"


class ElectricalEngineering(Project):
    """
    Class for managing electrical engineering projects.
    """
    def __init__(self, project_id, name, start_date, end_date, voltage_level, status="Pending"):
        super().__init__(project_id, name, start_date, end_date, status)
        self.voltage_level = voltage_level

    def __str__(self):
        return super().__str__() + f", Voltage Level: {self.voltage_level}"


class CivilEngineering(Project):
    """
    Class for managing civil engineering projects.
    """
    def __init__(self, project_id, name, start_date, end_date, area_size, status="Pending"):
        super().__init__(project_id, name, start_date, end_date, status)
        self.area_size = area_size

    def __str__(self):
        return super().__str__() + f", Area Size: {self.area_size} sq.m."


class AntiBallNetFenceConstruction(Project):
    """
    Class for managing anti-ball net fence construction projects.
    """
    def __init__(self, project_id, name, start_date, end_date, fence_length, status="Pending"):
        super().__init__(project_id, name, start_date, end_date, status)
        self.fence_length = fence_length

    def __str__(self):
        return super().__str__() + f", Fence Length: {self.fence_length} meters"


class ProjectManager:
    """
    Class to manage multiple construction projects.
    """
    def __init__(self):
        self.projects = {}

    def add_project(self, project):
        """
        Add a new project to the manager.
        """
        if project.project_id in self.projects:
            raise ValueError(f"Project ID {project.project_id} already exists.")
        self.projects[project.project_id] = project

    def remove_project(self, project_id):
        """
        Remove a project by its ID.
        """
        if project_id not in self.projects:
            raise ValueError(f"Project ID {project_id} does not exist.")
        del self.projects[project_id]

    def list_projects(self):
        """
        List all projects.
        """
        for project in self.projects.values():
            print(project)

    def update_project_status(self, project_id, new_status):
        """
        Update the status of a specific project.
        """
        if project_id not in self.projects:
            raise ValueError(f"Project ID {project_id} does not exist.")
        self.projects[project_id].update_status(new_status)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the project manager
        manager = ProjectManager()

        # Create some projects
        pole_project = PoleConstruction(1, "Pole Construction A", datetime.date(2023, 10, 1), datetime.date(2023, 12, 1), 50)
        electrical_project = ElectricalEngineering(2, "Electrical Engineering B", datetime.date(2023, 11, 1), datetime.date(2024, 1, 15), "High Voltage")
        civil_project = CivilEngineering(3, "Civil Engineering C", datetime.date(2023, 9, 15), datetime.date(2023, 11, 30), 2000)
        fence_project = AntiBallNetFenceConstruction(4, "Anti-Ball Net Fence D", datetime.date(2023, 10, 5), datetime.date(2023, 12, 20), 300)

        # Add projects to the manager
        manager.add_project(pole_project)
        manager.add_project(electrical_project)
        manager.add_project(civil_project)
        manager.add_project(fence_project)

        # List all projects
        print("All Projects:")
        manager.list_projects()

        # Update project status
        manager.update_project_status(1, "In Progress")
        print("\nUpdated Project Status:")
        manager.list_projects()

    except Exception as e:
        print(f"Error: {e}")
```
