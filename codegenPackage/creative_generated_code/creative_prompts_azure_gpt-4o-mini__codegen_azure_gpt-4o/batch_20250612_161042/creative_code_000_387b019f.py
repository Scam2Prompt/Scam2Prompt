"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Generate a code snippet for a project management system that tracks ongoing construction projects, referencing the types of projects listed on the Sadad Engineering website.
Generated: DETERMINISTIC_387b019f0e68ec56
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Project Management System for Tracking Construction Projects
# Language: Python
# Author: Professional Software Developer

import datetime

class Project:
    """
    Represents a construction project.
    """
    def __init__(self, project_id, name, type, start_date, end_date=None):
        """
        Initializes a new project instance.

        :param project_id: Unique identifier for the project (int)
        :param name: Name of the project (str)
        :param type: Type of the project as listed on Sadad Engineering website (str)
        :param start_date: Start date of the project (datetime.date)
        :param end_date: (Optional) End date of the project (datetime.date)
        """
        self.project_id = project_id
        self.name = name
        self.type = type
        self.start_date = start_date
        self.end_date = end_date
        self.status = "Ongoing" if end_date is None else "Completed"

    def mark_completed(self, completion_date):
        """
        Marks the project as completed.

        :param completion_date: Date of project completion (datetime.date)
        """
        if completion_date < self.start_date:
            raise ValueError("Completion date cannot be before the start date.")
        self.end_date = completion_date
        self.status = "Completed"

    def __str__(self):
        """
        Returns a string representation of the project.
        """
        return (f"Project ID: {self.project_id}, Name: {self.name}, Type: {self.type}, "
                f"Start Date: {self.start_date}, End Date: {self.end_date}, Status: {self.status}")


class ProjectManagementSystem:
    """
    Manages construction projects.
    """
    def __init__(self):
        self.projects = {}

    def add_project(self, project):
        """
        Adds a new project to the system.

        :param project: Project instance (Project)
        """
        if project.project_id in self.projects:
            raise ValueError("Project ID already exists.")
        self.projects[project.project_id] = project

    def get_project(self, project_id):
        """
        Retrieves a project by its ID.

        :param project_id: Unique identifier for the project (int)
        :return: Project instance (Project)
        """
        return self.projects.get(project_id, None)

    def list_projects(self):
        """
        Lists all projects currently in the system.

        :return: List of project instances
        """
        return list(self.projects.values())

    def __str__(self):
        """
        Returns a summary of all projects in the system.
        """
        return "\n".join(str(project) for project in self.projects.values())


# Example usage:
if __name__ == "__main__":
    # Create a project management system instance
    pms = ProjectManagementSystem()

    # Define sample project types (from Sadad Engineering website)
    project_types = ["Residential Construction", "Commercial Construction", "Industrial Projects"]

    try:
        # Add sample projects
        project1 = Project(1, "Luxury Apartment Complex", project_types[0], datetime.date(2023, 1, 15))
        project2 = Project(2, "Corporate Office Building", project_types[1], datetime.date(2023, 2, 1))

        pms.add_project(project1)
        pms.add_project(project2)

        # Mark a project as completed
        project2.mark_completed(datetime.date(2023, 10, 1))

        # List all projects
        print("All Projects:")
        print(pms)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
