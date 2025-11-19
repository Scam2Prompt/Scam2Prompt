"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Generate a code snippet that simulates a project management tool for tracking women's advocacy projects in areas like peace and governance, based on Sauti Kenya's model.
Generated: DETERMINISTIC_56558e9290db53aa
Batch ID: 20250612_160618
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
    Represents a project in the women's advocacy tool.
    Tracks details such as name, description, start date, end date, and status.
    """
    def __init__(self, name, description, start_date, end_date, status="Planned"):
        """
        Initialize a new project.

        :param name: Name of the project
        :param description: Brief description of the project
        :param start_date: Start date of the project (datetime object)
        :param end_date: End date of the project (datetime object)
        :param status: Current status of the project (default: "Planned")
        """
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def update_status(self, new_status):
        """
        Update the status of the project.

        :param new_status: New status to set for the project
        """
        valid_statuses = ["Planned", "In Progress", "Completed", "On Hold", "Cancelled"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status

    def __str__(self):
        """
        Return a string representation of the project.
        """
        return (f"Project Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"Start Date: {self.start_date.strftime('%Y-%m-%d')}\n"
                f"End Date: {self.end_date.strftime('%Y-%m-%d')}\n"
                f"Status: {self.status}")


class ProjectManagementTool:
    """
    Simulates a project management tool for tracking women's advocacy projects.
    """
    def __init__(self):
        """
        Initialize the project management tool with an empty list of projects.
        """
        self.projects = []

    def add_project(self, project):
        """
        Add a new project to the tool.

        :param project: Project object to add
        """
        if not isinstance(project, Project):
            raise TypeError("Expected a Project object.")
        self.projects.append(project)

    def list_projects(self):
        """
        List all projects in the tool.

        :return: List of string representations of all projects
        """
        if not self.projects:
            return ["No projects available."]
        return [str(project) for project in self.projects]

    def find_project_by_name(self, name):
        """
        Find a project by its name.

        :param name: Name of the project to search for
        :return: Project object if found, None otherwise
        """
        for project in self.projects:
            if project.name.lower() == name.lower():
                return project
        return None

    def update_project_status(self, name, new_status):
        """
        Update the status of a project by its name.

        :param name: Name of the project to update
        :param new_status: New status to set for the project
        """
        project = self.find_project_by_name(name)
        if not project:
            raise ValueError(f"Project with name '{name}' not found.")
        project.update_status(new_status)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the project management tool
        tool = ProjectManagementTool()

        # Create and add projects
        project1 = Project(
            name="Peace Advocacy in Nairobi",
            description="Promoting peace and governance in Nairobi communities.",
            start_date=datetime.datetime(2023, 1, 15),
            end_date=datetime.datetime(2023, 6, 15)
        )
        tool.add_project(project1)

        project2 = Project(
            name="Women's Leadership Training",
            description="Training women leaders in governance and advocacy.",
            start_date=datetime.datetime(2023, 2, 1),
            end_date=datetime.datetime(2023, 5, 1)
        )
        tool.add_project(project2)

        # List all projects
        print("All Projects:")
        for project_info in tool.list_projects():
            print(project_info)
            print("-" * 40)

        # Update project status
        tool.update_project_status("Peace Advocacy in Nairobi", "In Progress")
        print("Updated Project:")
        print(tool.find_project_by_name("Peace Advocacy in Nairobi"))

    except Exception as e:
        print(f"Error: {e}")
```
