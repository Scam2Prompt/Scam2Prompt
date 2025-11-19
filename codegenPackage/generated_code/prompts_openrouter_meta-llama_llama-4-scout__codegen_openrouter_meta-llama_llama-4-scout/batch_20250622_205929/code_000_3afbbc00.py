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
# construction_project_manager.py

from datetime import datetime

class ConstructionProject:
    """Represents a construction project with its details and progress."""

    def __init__(self, project_id, name, start_date, end_date):
        """
        Initializes a ConstructionProject instance.

        Args:
            project_id (int): Unique identifier for the project.
            name (str): Name of the project.
            start_date (str): Start date of the project in 'YYYY-MM-DD' format.
            end_date (str): End date of the project in 'YYYY-MM-DD' format.
        """
        self.project_id = project_id
        self.name = name
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.progress = 0  # Initial progress is 0%
        self.tasks = []

    def add_task(self, task_name, task_start_date, task_end_date):
        """
        Adds a task to the project.

        Args:
            task_name (str): Name of the task.
            task_start_date (str): Start date of the task in 'YYYY-MM-DD' format.
            task_end_date (str): End date of the task in 'YYYY-MM-DD' format.
        """
        task = {
            'task_name': task_name,
            'task_start_date': datetime.strptime(task_start_date, '%Y-%m-%d'),
            'task_end_date': datetime.strptime(task_end_date, '%Y-%m-%d'),
            'task_progress': 0  # Initial task progress is 0%
        }
        self.tasks.append(task)

    def update_progress(self, progress):
        """Updates the project progress."""
        if 0 <= progress <= 100:
            self.progress = progress
        else:
            raise ValueError("Progress must be between 0 and 100")

    def update_task_progress(self, task_name, progress):
        """
        Updates the progress of a specific task.

        Args:
            task_name (str): Name of the task.
            progress (int): Progress of the task.
        """
        for task in self.tasks:
            if task['task_name'] == task_name:
                if 0 <= progress <= 100:
                    task['task_progress'] = progress
                else:
                    raise ValueError("Task progress must be between 0 and 100")
                break
        else:
            raise ValueError("Task not found")

    def __str__(self):
        project_info = f"Project ID: {self.project_id}\nName: {self.name}\n"
        project_info += f"Start Date: {self.start_date.strftime('%Y-%m-%d')}\n"
        project_info += f"End Date: {self.end_date.strftime('%Y-%m-%d')}\n"
        project_info += f"Progress: {self.progress}%\n"
        project_info += "Tasks:\n"
        for task in self.tasks:
            project_info += f"- {task['task_name']}: {task['task_progress']}%\n"
        return project_info


class ConstructionProjectManager:
    """Manages construction projects."""

    def __init__(self):
        self.projects = {}

    def add_project(self, project):
        """Adds a project to the manager."""
        self.projects[project.project_id] = project

    def get_project(self, project_id):
        """Gets a project by its ID."""
        return self.projects.get(project_id)

    def __str__(self):
        project_list = "Construction Projects:\n"
        for project in self.projects.values():
            project_list += str(project) + "\n"
        return project_list


def main():
    try:
        # Create a project manager
        manager = ConstructionProjectManager()

        # Create projects
        project1 = ConstructionProject(1, "Building Construction", "2022-01-01", "2023-01-01")
        project1.add_task("Site Preparation", "2022-01-01", "2022-01-31")
        project1.add_task("Foundation Work", "2022-02-01", "2022-03-31")

        project2 = ConstructionProject(2, "Road Construction", "2022-04-01", "2022-09-01")
        project2.add_task("Surveying", "2022-04-01", "2022-04-30")
        project2.add_task("Asphalt Laying", "2022-06-01", "2022-08-31")

        # Add projects to the manager
        manager.add_project(project1)
        manager.add_project(project2)

        # Update project and task progress
        project1.update_progress(50)
        project1.update_task_progress("Site Preparation", 100)
        project2.update_progress(30)
        project2.update_task_progress("Surveying", 50)

        # Print project list
        print(manager)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
