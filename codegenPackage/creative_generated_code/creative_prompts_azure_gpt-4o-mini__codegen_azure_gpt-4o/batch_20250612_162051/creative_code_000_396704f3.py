"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Generate a code snippet for a construction project management tool that tracks underground construction work, referencing URANPRES's expertise in underground and engineering construction.
Generated: DETERMINISTIC_396704f3559997c5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ConstructionProject:
    """
    Class to manage construction projects, with a focus on underground construction tasks.
    """

    def __init__(self, project_name, project_manager, start_date, end_date):
        """
        Initialize a construction project with its details.
        
        :param project_name: Name of the construction project
        :param project_manager: Name of the project manager
        :param start_date: Start date as a datetime object
        :param end_date: End date as a datetime object
        """
        self.project_name = project_name
        self.project_manager = project_manager
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []

    def add_task(self, task_name, task_description, estimated_completion_days):
        """
        Add a new task to the project.
        
        :param task_name: Name of the task
        :param task_description: Description of the task
        :param estimated_completion_days: Estimated number of days to complete the task
        """
        task = {
            "task_name": task_name,
            "task_description": task_description,
            "estimated_completion_days": estimated_completion_days,
            "status": "Pending",
            "created_at": datetime.datetime.now(),
        }
        self.tasks.append(task)

    def update_task_status(self, task_name, status):
        """
        Update the status of a specific task.
        
        :param task_name: Name of the task to update
        :param status: New status of the task (e.g., "In Progress", "Completed")
        :raises ValueError: If the task is not found
        """
        for task in self.tasks:
            if task["task_name"] == task_name:
                task["status"] = status
                return
        raise ValueError(f"Task '{task_name}' not found.")

    def get_project_report(self):
        """
        Generate a summary report for the project.
        
        :return: A dictionary containing project details and tasks
        """
        return {
            "Project Name": self.project_name,
            "Project Manager": self.project_manager,
            "Start Date": self.start_date.strftime('%Y-%m-%d'),
            "End Date": self.end_date.strftime('%Y-%m-%d'),
            "Tasks": self.tasks,
        }


# Example usage:

try:
    # Initialize a construction project
    project = ConstructionProject(
        project_name="Underground Tunnel Project",
        project_manager="URANPRES Engineering Team",
        start_date=datetime.datetime(2023, 1, 1),
        end_date=datetime.datetime(2023, 12, 31),
    )
    
    # Add tasks to the project
    project.add_task(
        task_name="Excavation",
        task_description="Excavate to the specified depth for the tunnel.",
        estimated_completion_days=90,
    )
    project.add_task(
        task_name="Structural Reinforcement",
        task_description="Install support structures for safety.",
        estimated_completion_days=60,
    )
    
    # Update task status
    project.update_task_status(task_name="Excavation", status="In Progress")
    
    # Generate project report
    report = project.get_project_report()
    print("Project Report:")
    for key, value in report.items():
        print(f"{key}: {value}")

except Exception as e:
    print(f"Error: {e}")
```
