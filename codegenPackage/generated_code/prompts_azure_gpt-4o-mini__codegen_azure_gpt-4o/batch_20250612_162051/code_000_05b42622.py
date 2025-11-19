"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Write a Python script that uses project management principles to track the progress of a building project, incorporating features that TWM Associates emphasizes in their services.
Generated: DETERMINISTIC_05b42622786cc8d0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json


class Task:
    """
    Represents a single task in the building project.
    """

    def __init__(self, name, start_date, end_date, assigned_to):
        """
        Initialize a task with its details.
        :param name: Name of the task
        :param start_date: Start date of the task (YYYY-MM-DD)
        :param end_date: End date of the task (YYYY-MM-DD)
        :param assigned_to: Person or team responsible for the task
        """
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.assigned_to = assigned_to
        self.status = "Not Started"  # Default status

    def update_status(self, status):
        """
        Update the status of the task.
        :param status: New status (e.g., "In Progress", "Completed")
        """
        if status not in ["Not Started", "In Progress", "Completed"]:
            raise ValueError("Invalid status. Choose from 'Not Started', 'In Progress', or 'Completed'.")
        self.status = status

    def is_overdue(self):
        """
        Check if the task is overdue.
        :return: True if overdue, False otherwise
        """
        return self.status != "Completed" and datetime.datetime.now() > self.end_date

    def to_dict(self):
        """
        Convert the task to a dictionary for serialization.
        :return: Dictionary representation of the task
        """
        return {
            "name": self.name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "assigned_to": self.assigned_to,
            "status": self.status,
            "is_overdue": self.is_overdue(),
        }


class Project:
    """
    Represents a building project with multiple tasks.
    """

    def __init__(self, name, client_name):
        """
        Initialize a project with its details.
        :param name: Name of the project
        :param client_name: Name of the client
        """
        self.name = name
        self.client_name = client_name
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the project.
        :param task: Task object to add
        """
        if not isinstance(task, Task):
            raise TypeError("Only Task objects can be added.")
        self.tasks.append(task)

    def get_progress(self):
        """
        Calculate the progress of the project.
        :return: Percentage of tasks completed
        """
        if not self.tasks:
            return 0
        completed_tasks = sum(1 for task in self.tasks if task.status == "Completed")
        return (completed_tasks / len(self.tasks)) * 100

    def to_dict(self):
        """
        Convert the project to a dictionary for serialization.
        :return: Dictionary representation of the project
        """
        return {
            "name": self.name,
            "client_name": self.client_name,
            "progress": self.get_progress(),
            "tasks": [task.to_dict() for task in self.tasks],
        }

    def save_to_file(self, filename):
        """
        Save the project details to a JSON file.
        :param filename: Name of the file to save to
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.to_dict(), file, indent=4)
        except IOError as e:
            print(f"Error saving project to file: {e}")

    def load_from_file(self, filename):
        """
        Load project details from a JSON file.
        :param filename: Name of the file to load from
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.name = data["name"]
                self.client_name = data["client_name"]
                self.tasks = [
                    Task(
                        task["name"],
                        task["start_date"],
                        task["end_date"],
                        task["assigned_to"],
                    )
                    for task in data["tasks"]
                ]
                for task, task_data in zip(self.tasks, data["tasks"]):
                    task.update_status(task_data["status"])
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading project from file: {e}")


# Example usage
if __name__ == "__main__":
    # Create a project
    project = Project("Building Construction", "TWM Associates")

    # Add tasks to the project
    project.add_task(Task("Foundation Work", "2023-01-01", "2023-01-15", "Team A"))
    project.add_task(Task("Framing", "2023-01-16", "2023-01-30", "Team B"))
    project.add_task(Task("Roofing", "2023-02-01", "2023-02-15", "Team C"))

    # Update task status
    project.tasks[0].update_status("Completed")
    project.tasks[1].update_status("In Progress")

    # Display project progress
    print(f"Project Progress: {project.get_progress():.2f}%")

    # Save project to file
    project.save_to_file("project_data.json")

    # Load project from file
    new_project = Project("", "")
    new_project.load_from_file("project_data.json")
    print(f"Loaded Project: {new_project.to_dict()}")
```
