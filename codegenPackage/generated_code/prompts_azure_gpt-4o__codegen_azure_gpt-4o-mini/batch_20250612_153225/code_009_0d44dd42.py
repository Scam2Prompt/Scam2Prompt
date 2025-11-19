"""
Generated Code Metadata:
========================
Original URL: https://globalchainsas.com
Prompt: Write a program to assist in the planning and execution of industrial projects, ensuring alignment with the strategies and timelines described by GlobalChain SAS.
Generated: DETERMINISTIC_0d44dd42b9243140
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Project:
    """
    A class to represent an industrial project.

    Attributes:
        name (str): The name of the project.
        start_date (datetime.date): The start date of the project.
        end_date (datetime.date): The end date of the project.
        status (str): The current status of the project.
        tasks (List[Dict]): A list of tasks associated with the project.
    """

    def __init__(self, name: str, start_date: str, end_date: str):
        """
        Initializes a new project with the given name, start date, and end date.

        Args:
            name (str): The name of the project.
            start_date (str): The start date of the project in 'YYYY-MM-DD' format.
            end_date (str): The end date of the project in 'YYYY-MM-DD' format.
        """
        self.name = name
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)
        self.status = "Planned"
        self.tasks = []

    def _parse_date(self, date_str: str) -> datetime.date:
        """
        Parses a date string into a datetime.date object.

        Args:
            date_str (str): The date string to parse.

        Returns:
            datetime.date: The parsed date.

        Raises:
            ValueError: If the date string is not in the correct format.
        """
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def add_task(self, task_name: str, due_date: str) -> None:
        """
        Adds a task to the project.

        Args:
            task_name (str): The name of the task.
            due_date (str): The due date of the task in 'YYYY-MM-DD' format.

        Raises:
            ValueError: If the due date is not within the project timeline.
        """
        due_date_obj = self._parse_date(due_date)
        if not (self.start_date <= due_date_obj <= self.end_date):
            raise ValueError(f"Task due date {due_date} is outside the project timeline.")
        
        self.tasks.append({"name": task_name, "due_date": due_date_obj, "status": "Pending"})

    def update_status(self, new_status: str) -> None:
        """
        Updates the status of the project.

        Args:
            new_status (str): The new status of the project.
        """
        self.status = new_status

    def __str__(self) -> str:
        """
        Returns a string representation of the project.
        """
        return f"Project: {self.name}, Status: {self.status}, Start: {self.start_date}, End: {self.end_date}, Tasks: {len(self.tasks)}"


class ProjectManager:
    """
    A class to manage multiple projects.

    Attributes:
        projects (List[Project]): A list of projects being managed.
    """

    def __init__(self):
        """Initializes the ProjectManager with an empty project list."""
        self.projects: List[Project] = []

    def create_project(self, name: str, start_date: str, end_date: str) -> Project:
        """
        Creates a new project and adds it to the project list.

        Args:
            name (str): The name of the project.
            start_date (str): The start date of the project in 'YYYY-MM-DD' format.
            end_date (str): The end date of the project in 'YYYY-MM-DD' format.

        Returns:
            Project: The created project.
        """
        project = Project(name, start_date, end_date)
        self.projects.append(project)
        return project

    def get_project(self, name: str) -> Optional[Project]:
        """
        Retrieves a project by name.

        Args:
            name (str): The name of the project to retrieve.

        Returns:
            Optional[Project]: The project if found, otherwise None.
        """
        for project in self.projects:
            if project.name == name:
                return project
        return None

    def list_projects(self) -> List[str]:
        """
        Lists all projects with their statuses.

        Returns:
            List[str]: A list of project summaries.
        """
        return [str(project) for project in self.projects]


# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Create a new project
    try:
        project = manager.create_project("Industrial Expansion", "2023-01-01", "2023-12-31")
        project.add_task("Site Preparation", "2023-02-15")
        project.add_task("Foundation Work", "2023-05-01")
        project.update_status("In Progress")
        
        # List all projects
        for summary in manager.list_projects():
            print(summary)
    except Exception as e:
        print(f"Error: {e}")
```
