"""
Generated Code Metadata:
========================
Original URL: https://samaalnaser.co
Prompt: How can I implement a project management tool for real estate investments similar to what Sama Al-Naser Group does in Dubai? Provide a code example.
Generated: DETERMINISTIC_1999edf7478cf222
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Tool for Real Estate Investments
This script implements a basic project management tool for tracking real estate investments.
It includes functionality for adding projects, updating project status, and viewing project details.
"""

import datetime

class Project:
    """
    Represents a real estate investment project.
    """
    def __init__(self, name, location, budget, start_date, end_date):
        """
        Initialize a new project.

        :param name: Name of the project
        :param location: Location of the project
        :param budget: Budget allocated for the project
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        """
        self.name = name
        self.location = location
        self.budget = budget
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.status = "Planned"  # Default status
        self.tasks = []  # List of tasks associated with the project

    def update_status(self, new_status):
        """
        Update the status of the project.

        :param new_status: New status of the project (e.g., "In Progress", "Completed")
        """
        valid_statuses = ["Planned", "In Progress", "Completed", "On Hold"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")

    def add_task(self, task_name, task_deadline):
        """
        Add a task to the project.

        :param task_name: Name of the task
        :param task_deadline: Deadline for the task (YYYY-MM-DD)
        """
        task = {
            "name": task_name,
            "deadline": datetime.datetime.strptime(task_deadline, "%Y-%m-%d"),
            "status": "Pending"  # Default task status
        }
        self.tasks.append(task)

    def update_task_status(self, task_name, new_status):
        """
        Update the status of a specific task.

        :param task_name: Name of the task to update
        :param new_status: New status of the task (e.g., "Pending", "Completed")
        """
        valid_statuses = ["Pending", "In Progress", "Completed"]
        for task in self.tasks:
            if task["name"] == task_name:
                if new_status in valid_statuses:
                    task["status"] = new_status
                else:
                    raise ValueError(f"Invalid task status: {new_status}. Valid statuses are: {valid_statuses}")
                return
        raise ValueError(f"Task '{task_name}' not found in project '{self.name}'.")

    def view_details(self):
        """
        View the details of the project.

        :return: A dictionary containing project details
        """
        return {
            "name": self.name,
            "location": self.location,
            "budget": self.budget,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "status": self.status,
            "tasks": self.tasks
        }


class ProjectManagementTool:
    """
    A tool for managing multiple real estate investment projects.
    """
    def __init__(self):
        """
        Initialize the project management tool.
        """
        self.projects = []  # List of projects

    def add_project(self, project):
        """
        Add a new project to the tool.

        :param project: An instance of the Project class
        """
        self.projects.append(project)

    def find_project(self, project_name):
        """
        Find a project by name.

        :param project_name: Name of the project to find
        :return: The project instance if found, None otherwise
        """
        for project in self.projects:
            if project.name == project_name:
                return project
        return None

    def view_all_projects(self):
        """
        View details of all projects.

        :return: A list of dictionaries containing project details
        """
        return [project.view_details() for project in self.projects]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the project management tool
        tool = ProjectManagementTool()

        # Create a new project
        project1 = Project(
            name="Luxury Apartments",
            location="Dubai Marina",
            budget=5000000,
            start_date="2023-01-01",
            end_date="2024-12-31"
        )

        # Add the project to the tool
        tool.add_project(project1)

        # Add tasks to the project
        project1.add_task("Foundation Work", "2023-06-30")
        project1.add_task("Interior Design", "2024-06-30")

        # Update project status
        project1.update_status("In Progress")

        # Update task status
        project1.update_task_status("Foundation Work", "Completed")

        # View project details
        print("Project Details:")
        print(project1.view_details())

        # View all projects
        print("\nAll Projects:")
        print(tool.view_all_projects())

    except Exception as e:
        print(f"Error: {e}")
```
