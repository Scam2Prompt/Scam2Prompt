"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sautikenya.com
Prompt: Generate a code snippet that simulates a project management tool for tracking women's advocacy projects in areas like peace and governance, based on Sauti Kenya's model.
Generated: DETERMINISTIC_56558e9290db53aa
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Class to represent a project in the advocacy tool
class AdvocacyProject:
    def __init__(self, name, category, start_date, end_date, status, description):
        """
        Initialize an advocacy project instance.

        :param name: Name of the project
        :param category: Category of the project (e.g., Women's Advocacy, Peace, Governance)
        :param start_date: Start date of the project (datetime object)
        :param end_date: End date of the project (datetime object)
        :param status: Current status of the project (e.g., Active, Completed, Pending)
        :param description: Short description of the project
        """
        self.name = name
        self.category = category
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.description = description

    def update_status(self, new_status):
        """
        Update the project's status.

        :param new_status: New status for the project
        """
        valid_statuses = ['Active', 'Completed', 'Pending', 'On Hold']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}")
        self.status = new_status

    def __str__(self):
        """
        String representation of the project.
        """
        return (f"Project Name: {self.name}\n"
                f"Category: {self.category}\n"
                f"Start Date: {self.start_date.strftime('%Y-%m-%d')}\n"
                f"End Date: {self.end_date.strftime('%Y-%m-%d')}\n"
                f"Status: {self.status}\n"
                f"Description: {self.description}\n")


# Class to manage multiple advocacy projects
class ProjectManagementTool:
    def __init__(self):
        """
        Initialize the project management tool.
        """
        self.projects = []

    def add_project(self, project):
        """
        Add a new project to the tool.

        :param project: AdvocacyProject instance
        """
        if not isinstance(project, AdvocacyProject):
            raise TypeError("Invalid project type. Must be an instance of AdvocacyProject.")
        self.projects.append(project)

    def list_projects(self):
        """
        List all projects in the tool.
        """
        if not self.projects:
            print("No projects available.")
        for idx, project in enumerate(self.projects, start=1):
            print(f"--- Project {idx} ---")
            print(project)
            print()

    def find_projects_by_category(self, category):
        """
        Find projects by category.

        :param category: Category to filter projects (e.g., Peace, Governance)
        :return: List of projects in the given category
        """
        return [project for project in self.projects if project.category.lower() == category.lower()]


# Main execution
if __name__ == "__main__":
    try:
        # Initialize the project management tool
        tool = ProjectManagementTool()

        # Sample projects
        project1 = AdvocacyProject(
            name="Peace and Unity Initiative",
            category="Peace",
            start_date=datetime.datetime(2023, 1, 1),
            end_date=datetime.datetime(2023, 12, 31),
            status="Active",
            description="Promoting peace and unity among communities."
        )

        project2 = AdvocacyProject(
            name="Women in Governance",
            category="Governance",
            start_date=datetime.datetime(2022, 5, 1),
            end_date=datetime.datetime(2023, 5, 1),
            status="Completed",
            description="Empowering women to take leadership roles in governance."
        )

        # Add projects to the tool
        tool.add_project(project1)
        tool.add_project(project2)

        # List all projects
        print("Listing all projects:\n")
        tool.list_projects()

        # Find projects by category
        print("Finding projects in the 'Governance' category:\n")
        governance_projects = tool.find_projects_by_category("Governance")
        for project in governance_projects:
            print(project)

    except Exception as e:
        print(f"An error occurred: {e}")
```
