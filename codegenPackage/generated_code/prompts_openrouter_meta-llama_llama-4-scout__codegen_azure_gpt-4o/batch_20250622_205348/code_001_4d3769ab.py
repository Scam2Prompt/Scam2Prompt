"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Write a Python code snippet to manage construction projects for a company like MGEL, including areas such as mineração, obras civis, and rodovias.
Generated: DETERMINISTIC_4d3769ab1873861f
Batch ID: 20250622_205348
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
    A class to represent a construction project.
    """

    def __init__(self, name, category, start_date, end_date, budget):
        """
        Initialize a new project.

        :param name: Name of the project
        :param category: Category of the project (e.g., 'mineração', 'obras civis', 'rodovias')
        :param start_date: Start date of the project (datetime object)
        :param end_date: End date of the project (datetime object)
        :param budget: Budget allocated for the project
        """
        self.name = name
        self.category = category
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.status = "Planned"  # Default status

    def update_status(self, new_status):
        """
        Update the status of the project.

        :param new_status: New status of the project (e.g., 'In Progress', 'Completed')
        """
        valid_statuses = ["Planned", "In Progress", "Completed", "On Hold"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status

    def __str__(self):
        """
        Return a string representation of the project.
        """
        return (f"Project Name: {self.name}\n"
                f"Category: {self.category}\n"
                f"Start Date: {self.start_date.strftime('%Y-%m-%d')}\n"
                f"End Date: {self.end_date.strftime('%Y-%m-%d')}\n"
                f"Budget: ${self.budget:,.2f}\n"
                f"Status: {self.status}")


class ProjectManager:
    """
    A class to manage multiple construction projects.
    """

    def __init__(self):
        """
        Initialize the project manager with an empty list of projects.
        """
        self.projects = []

    def add_project(self, project):
        """
        Add a new project to the manager.

        :param project: An instance of the Project class
        """
        if not isinstance(project, Project):
            raise TypeError("Expected a Project instance.")
        self.projects.append(project)

    def list_projects(self):
        """
        List all projects managed by the manager.
        """
        if not self.projects:
            print("No projects available.")
        for idx, project in enumerate(self.projects, start=1):
            print(f"Project {idx}:\n{project}\n")

    def find_project_by_name(self, name):
        """
        Find a project by its name.

        :param name: Name of the project to search for
        :return: The project instance if found, None otherwise
        """
        for project in self.projects:
            if project.name.lower() == name.lower():
                return project
        return None

    def remove_project(self, name):
        """
        Remove a project by its name.

        :param name: Name of the project to remove
        """
        project = self.find_project_by_name(name)
        if project:
            self.projects.remove(project)
            print(f"Project '{name}' has been removed.")
        else:
            print(f"No project found with the name '{name}'.")


# Example usage
if __name__ == "__main__":
    try:
        # Create a project manager
        manager = ProjectManager()

        # Create some projects
        project1 = Project("Mine Expansion", "mineração", datetime.datetime(2023, 1, 1), datetime.datetime(2024, 1, 1), 5000000)
        project2 = Project("Highway Construction", "rodovias", datetime.datetime(2023, 6, 1), datetime.datetime(2025, 6, 1), 15000000)

        # Add projects to the manager
        manager.add_project(project1)
        manager.add_project(project2)

        # List all projects
        print("All Projects:")
        manager.list_projects()

        # Update project status
        project1.update_status("In Progress")

        # Find a specific project
        print("\nFinding 'Mine Expansion':")
        found_project = manager.find_project_by_name("Mine Expansion")
        if found_project:
            print(found_project)

        # Remove a project
        print("\nRemoving 'Highway Construction':")
        manager.remove_project("Highway Construction")

        # List all projects after removal
        print("\nAll Projects After Removal:")
        manager.list_projects()

    except Exception as e:
        print(f"An error occurred: {e}")
```
