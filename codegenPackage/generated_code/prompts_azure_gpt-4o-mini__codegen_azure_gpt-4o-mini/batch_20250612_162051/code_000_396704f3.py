"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Generate a code snippet for a construction project management tool that tracks underground construction work, referencing URANPRES's expertise in underground and engineering construction.
Generated: DETERMINISTIC_396704f3559997c5
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
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UndergroundConstructionProject:
    """
    A class to represent an underground construction project.
    """

    def __init__(self, project_name, start_date, end_date):
        """
        Initializes the project with a name, start date, and end date.

        :param project_name: Name of the construction project
        :param start_date: Start date of the project (datetime object)
        :param end_date: End date of the project (datetime object)
        """
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []
        self.status = 'Not Started'

    def add_task(self, task_name, assigned_to, due_date):
        """
        Adds a task to the project.

        :param task_name: Name of the task
        :param assigned_to: Person assigned to the task
        :param due_date: Due date for the task (datetime object)
        """
        if due_date < self.start_date or due_date > self.end_date:
            logging.error("Due date must be within the project timeline.")
            raise ValueError("Due date must be within the project timeline.")
        
        task = {
            'task_name': task_name,
            'assigned_to': assigned_to,
            'due_date': due_date,
            'completed': False
        }
        self.tasks.append(task)
        logging.info(f"Task '{task_name}' added to project '{self.project_name}'.")

    def complete_task(self, task_name):
        """
        Marks a task as completed.

        :param task_name: Name of the task to be completed
        """
        for task in self.tasks:
            if task['task_name'] == task_name:
                task['completed'] = True
                logging.info(f"Task '{task_name}' marked as completed.")
                return
        logging.warning(f"Task '{task_name}' not found in project '{self.project_name}'.")

    def project_status(self):
        """
        Returns the current status of the project.
        """
        completed_tasks = sum(task['completed'] for task in self.tasks)
        total_tasks = len(self.tasks)
        if total_tasks == 0:
            return "No tasks available."
        completion_percentage = (completed_tasks / total_tasks) * 100
        return f"Project '{self.project_name}' is {completion_percentage:.2f}% complete."

# Example usage
if __name__ == "__main__":
    try:
        # Create a new underground construction project
        project = UndergroundConstructionProject(
            project_name="URANPRES Underground Tunnel",
            start_date=datetime.datetime(2023, 10, 1),
            end_date=datetime.datetime(2024, 10, 1)
        )

        # Add tasks to the project
        project.add_task("Excavation", "Alice", datetime.datetime(2023, 10, 15))
        project.add_task("Reinforcement", "Bob", datetime.datetime(2023, 11, 15))

        # Complete a task
        project.complete_task("Excavation")

        # Print project status
        print(project.project_status())

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
