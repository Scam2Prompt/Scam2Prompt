"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atwg.xyz
Prompt: Provide an example of an IT consultancy project plan that aligns with ATWG LTD's approach to digital transformation and operational streamlining.
Generated: DETERMINISTIC_9691d4b047fe1243
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class ProjectPlan:
    """
    A class to represent an IT consultancy project plan that aligns with 
    ATWG LTD's approach to digital transformation and operational streamlining.
    """

    def __init__(self, project_name):
        """
        Initialize a new project plan.

        :param project_name: Name of the project.
        """
        self.project_name = project_name
        self.start_date = None
        self.end_date = None
        self.tasks = []

    def set_project_timeline(self, duration_days):
        """
        Set the start and end date of the project.

        :param duration_days: Duration of the project in days.
        :raise ValueError: If duration_days is not positive.
        """
        if duration_days <= 0:
            raise ValueError("Duration of the project must be a positive number.")
        
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=duration_days)

    def add_task(self, task_name, assigned_to, due_date):
        """
        Add a task to the project.

        :param task_name: Name of the task.
        :param assigned_to: Team member assigned to the task.
        :param due_date: Due date for the task.
        :raise ValueError: If due_date is in the past.
        """
        if due_date < datetime.now():
            raise ValueError("Due date cannot be in the past.")
        
        task = {
            'task_name': task_name,
            'assigned_to': assigned_to,
            'due_date': due_date
        }
        self.tasks.append(task)

    def generate_project_plan(self):
        """
        Generate a project plan as a dictionary.

        :return: Dictionary representation of the project plan.
        """
        return {
            'project_name': self.project_name,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'tasks': self.tasks
        }

    def save_project_plan(self, filename):
        """
        Save the project plan to a JSON file.

        :param filename: Name of the file to save the project plan.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.generate_project_plan(), f, indent=4)
            print(f"Project plan saved successfully to {filename}.")
        except IOError as e:
            print(f"Error saving project plan: {e}")

# Example usage of the ProjectPlan class
if __name__ == "__main__":
    # Create a new project plan
    project = ProjectPlan("Digital Transformation Initiative")
    
    # Set the project timeline to 30 days
    project.set_project_timeline(30)
    
    # Add tasks to the project
    try:
        project.add_task("Initial Assessment", "Alice", datetime.now() + timedelta(days=5))
        project.add_task("Technology Selection", "Bob", datetime.now() + timedelta(days=10))
        project.add_task("Implementation Phase", "Charlie", datetime.now() + timedelta(days=25))
    except ValueError as e:
        print(f"Error adding task: {e}")

    # Save the project plan to a JSON file
    project.save_project_plan("project_plan.json")
```
