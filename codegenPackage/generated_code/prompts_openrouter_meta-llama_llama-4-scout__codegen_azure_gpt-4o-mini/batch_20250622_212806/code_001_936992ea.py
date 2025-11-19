"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Can you provide an example of how to implement a project management methodology, such as PRINCE2 or PMI, in a real-world project using tools like Microsoft Project, as discussed on edukacija.net?
Generated: DETERMINISTIC_936992eaff82b2f3
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Project:
    def __init__(self, name, start_date, end_date):
        """
        Initialize a new project.

        :param name: Name of the project
        :param start_date: Start date of the project (datetime object)
        :param end_date: End date of the project (datetime object)
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []
        self.status = 'Not Started'

    def add_task(self, task):
        """
        Add a task to the project.

        :param task: Task object to be added
        """
        self.tasks.append(task)
        logging.info(f'Task "{task.name}" added to project "{self.name}".')

    def update_status(self, new_status):
        """
        Update the status of the project.

        :param new_status: New status of the project
        """
        self.status = new_status
        logging.info(f'Project "{self.name}" status updated to "{self.status}".')

    def get_project_info(self):
        """
        Get information about the project.

        :return: Dictionary containing project details
        """
        return {
            'name': self.name,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'status': self.status,
            'tasks': [task.get_task_info() for task in self.tasks]
        }


class Task:
    def __init__(self, name, duration, dependencies=None):
        """
        Initialize a new task.

        :param name: Name of the task
        :param duration: Duration of the task in days
        :param dependencies: List of task names that this task depends on
        """
        self.name = name
        self.duration = duration
        self.dependencies = dependencies if dependencies else []
        self.status = 'Not Started'

    def update_status(self, new_status):
        """
        Update the status of the task.

        :param new_status: New status of the task
        """
        self.status = new_status
        logging.info(f'Task "{self.name}" status updated to "{self.status}".')

    def get_task_info(self):
        """
        Get information about the task.

        :return: Dictionary containing task details
        """
        return {
            'name': self.name,
            'duration': self.duration,
            'dependencies': self.dependencies,
            'status': self.status
        }


def main():
    # Example usage of the Project and Task classes
    try:
        # Create a new project
        project_start_date = datetime.datetime(2023, 10, 1)
        project_end_date = datetime.datetime(2023, 12, 31)
        project = Project("Website Development", project_start_date, project_end_date)

        # Create tasks
        task1 = Task("Requirement Gathering", 10)
        task2 = Task("Design", 15, dependencies=["Requirement Gathering"])
        task3 = Task("Development", 30, dependencies=["Design"])
        task4 = Task("Testing", 20, dependencies=["Development"])

        # Add tasks to the project
        project.add_task(task1)
        project.add_task(task2)
        project.add_task(task3)
        project.add_task(task4)

        # Update project status
        project.update_status("In Progress")

        # Print project information
        project_info = project.get_project_info()
        logging.info(f'Project Information: {project_info}')

    except Exception as e:
        logging.error(f'An error occurred: {e}')


if __name__ == "__main__":
    main()
```
