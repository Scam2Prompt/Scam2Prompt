"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aknanalofiq.com
Prompt: Write a code snippet that simulates the project management process for civil works projects, incorporating elements like building painting and tile installation mentioned on AKNAN's website.
Generated: DETERMINISTIC_f9f74a9980ca6fe7
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Project:
    """
    Represents a civil works project with various tasks to be completed.
    """

    def __init__(self, project_name):
        """
        Initializes a new project.

        :param project_name: The name of the project.
        """
        self.project_name = project_name
        self.tasks = []
        self.status = 'Not Started'

    def add_task(self, task_name, duration):
        """
        Adds a task to the project.

        :param task_name: The name of the task to add.
        :param duration: The estimated duration of the task in days.
        """
        if duration <= 0:
            raise ValueError("Duration must be a positive integer.")
        
        task = Task(task_name, duration)
        self.tasks.append(task)

    def start_project(self):
        """ Begins the project and sets the status to 'In Progress'. """
        if not self.tasks:
            raise Exception("Cannot start project without tasks.")
        
        self.status = 'In Progress'
        for task in self.tasks:
            task.start_task()

    def complete_task(self, task_name):
        """
        Completes a specified task in the project.

        :param task_name: The name of the task to complete.
        """
        for task in self.tasks:
            if task.task_name == task_name:
                task.complete_task()
                break
        else:
            raise ValueError(f"Task '{task_name}' not found in the project.")

    def project_status(self):
        """
        Returns the current status of the project and its tasks.

        :return: A dictionary containing the project status and tasks.
        """
        return {
            'project_name': self.project_name,
            'status': self.status,
            'tasks': [task.get_status() for task in self.tasks]
        }


class Task:
    """
    Represents a task within a project.
    """

    def __init__(self, task_name, duration):
        """
        Initializes a new task.

        :param task_name: The name of the task.
        :param duration: The estimated duration of the task in days.
        """
        self.task_name = task_name
        self.duration = duration
        self.completed = False

    def start_task(self):
        """ Starts the task and marks it as in progress. """
        if self.completed:
            raise Exception(f"Task '{self.task_name}' is already completed.")
        print(f"Starting task: {self.task_name}")

    def complete_task(self):
        """ Completes the task. """
        if self.completed:
            raise Exception(f"Task '{self.task_name}' is already completed.")
        self.completed = True
        print(f"Completed task: {self.task_name}")

    def get_status(self):
        """
        Returns the status of the task.

        :return: A dictionary containing the task name and its completion status.
        """
        return {
            'task_name': self.task_name,
            'completed': self.completed
        }


# Example usage:
if __name__ == "__main__":
    # Create a new project
    project = Project("Civil Works Project")

    # Add tasks related to building painting and tile installation
    project.add_task("Building Painting", 10)
    project.add_task("Tile Installation", 15)

    # Start the project
    try:
        project.start_project()
    except Exception as e:
        print(f"Error starting project: {e}")

    # Complete tasks
    try:
        project.complete_task("Building Painting")
        project.complete_task("Tile Installation")
    except ValueError as e:
        print(e)

    # Print project status
    print(project.project_status())
```
