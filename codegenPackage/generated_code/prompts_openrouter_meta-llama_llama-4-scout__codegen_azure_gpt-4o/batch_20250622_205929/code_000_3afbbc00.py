"""
Generated Code Metadata:
========================
Original URL: https://www.sadadeng.com
Prompt: Write a Python script to manage construction projects, including tracking progress and deadlines, similar to the projects listed on the Sadad Engineering and Construction Company website.
Generated: DETERMINISTIC_3afbbc0079505591
Batch ID: 20250622_205929
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

    def __init__(self, name, description, start_date, end_date):
        """
        Initialize a new project.

        :param name: Name of the project
        :param description: Description of the project
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        """
        self.name = name
        self.description = description
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.progress = 0  # Progress in percentage (0-100)

    def update_progress(self, progress):
        """
        Update the progress of the project.

        :param progress: Progress percentage (0-100)
        :raises ValueError: If progress is not between 0 and 100
        """
        if not (0 <= progress <= 100):
            raise ValueError("Progress must be between 0 and 100.")
        self.progress = progress

    def is_overdue(self):
        """
        Check if the project is overdue.

        :return: True if the current date is past the end date, False otherwise
        """
        return datetime.datetime.now() > self.end_date

    def __str__(self):
        """
        Return a string representation of the project.

        :return: String containing project details
        """
        return (
            f"Project Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Start Date: {self.start_date.strftime('%Y-%m-%d')}\n"
            f"End Date: {self.end_date.strftime('%Y-%m-%d')}\n"
            f"Progress: {self.progress}%\n"
            f"Overdue: {'Yes' if self.is_overdue() else 'No'}"
        )


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

        :param project: Instance of the Project class
        """
        self.projects.append(project)

    def list_projects(self):
        """
        List all projects managed by the project manager.

        :return: List of project details
        """
        return [str(project) for project in self.projects]

    def find_project_by_name(self, name):
        """
        Find a project by its name.

        :param name: Name of the project to search for
        :return: Project instance if found, None otherwise
        """
        for project in self.projects:
            if project.name == name:
                return project
        return None

    def update_project_progress(self, name, progress):
        """
        Update the progress of a specific project.

        :param name: Name of the project
        :param progress: Progress percentage (0-100)
        :raises ValueError: If the project is not found
        """
        project = self.find_project_by_name(name)
        if not project:
            raise ValueError(f"Project with name '{name}' not found.")
        project.update_progress(progress)


# Example usage
if __name__ == "__main__":
    try:
        # Create a project manager
        manager = ProjectManager()

        # Add projects
        project1 = Project(
            name="Residential Building",
            description="Construction of a 10-story residential building.",
            start_date="2023-01-01",
            end_date="2023-12-31",
        )
        project2 = Project(
            name="Bridge Construction",
            description="Building a suspension bridge over the river.",
            start_date="2023-03-01",
            end_date="2024-06-30",
        )

        manager.add_project(project1)
        manager.add_project(project2)

        # Update progress
        manager.update_project_progress("Residential Building", 50)

        # List all projects
        for project_details in manager.list_projects():
            print(project_details)
            print("-" * 40)

    except Exception as e:
        print(f"Error: {e}")
```
