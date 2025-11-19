"""
Generated Code Metadata:
========================
Original URL: https://arpgroupcorp.com
Prompt: Create a project plan template for IT project management that ensures timelines and budgets are met, inspired by ARP Group Corporation's methodology.
Generated: DETERMINISTIC_a56183e65b95474c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_plan_template.py

from datetime import datetime, timedelta
from enum import Enum

class ProjectStatus(Enum):
    """Project status enumeration"""
    INITIATED = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    DELAYED = 4
    CANCELED = 5

class Task:
    """Task class representing a single task in the project plan"""
    def __init__(self, name, start_date, end_date, budget):
        """
        Initialize a Task object.

        Args:
            name (str): Task name
            start_date (datetime): Task start date
            end_date (datetime): Task end date
            budget (float): Task budget
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.status = ProjectStatus.INITIATED

    def update_status(self, status):
        """Update task status"""
        self.status = status

    def __str__(self):
        return f"Task '{self.name}': {self.start_date} - {self.end_date}, Budget: {self.budget}, Status: {self.status.name}"

class ProjectPlan:
    """ProjectPlan class representing the project plan"""
    def __init__(self, project_name, start_date, end_date, budget):
        """
        Initialize a ProjectPlan object.

        Args:
            project_name (str): Project name
            start_date (datetime): Project start date
            end_date (datetime): Project end date
            budget (float): Project budget
        """
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.tasks = []

    def add_task(self, task):
        """Add a task to the project plan"""
        self.tasks.append(task)

    def remove_task(self, task_name):
        """Remove a task from the project plan"""
        self.tasks = [task for task in self.tasks if task.name != task_name]

    def update_project_budget(self, new_budget):
        """Update project budget"""
        self.budget = new_budget

    def get_project_status(self):
        """Get project status"""
        total_budget = sum(task.budget for task in self.tasks)
        if total_budget > self.budget:
            raise ValueError("Total task budget exceeds project budget")

        completed_tasks = [task for task in self.tasks if task.status == ProjectStatus.COMPLETED]
        if len(completed_tasks) == len(self.tasks):
            return ProjectStatus.COMPLETED
        elif any(task.status == ProjectStatus.DELAYED for task in self.tasks):
            return ProjectStatus.DELAYED
        else:
            return ProjectStatus.IN_PROGRESS

    def __str__(self):
        project_info = f"Project: {self.project_name}, Start Date: {self.start_date}, End Date: {self.end_date}, Budget: {self.budget}\n"
        tasks_info = "\n".join(str(task) for task in self.tasks)
        return project_info + tasks_info

def main():
    try:
        # Create project plan
        project_start_date = datetime(2024, 9, 16)
        project_end_date = project_start_date + timedelta(days=30)
        project_plan = ProjectPlan("IT Project", project_start_date, project_end_date, 100000.0)

        # Create tasks
        task1_start_date = project_start_date
        task1_end_date = task1_start_date + timedelta(days=10)
        task1 = Task("Task 1", task1_start_date, task1_end_date, 30000.0)

        task2_start_date = task1_end_date
        task2_end_date = task2_start_date + timedelta(days=10)
        task2 = Task("Task 2", task2_start_date, task2_end_date, 40000.0)

        task3_start_date = task2_end_date
        task3_end_date = task3_start_date + timedelta(days=10)
        task3 = Task("Task 3", task3_start_date, task3_end_date, 30000.0)

        # Add tasks to project plan
        project_plan.add_task(task1)
        project_plan.add_task(task2)
        project_plan.add_task(task3)

        # Print project plan
        print(project_plan)

        # Update task status
        task1.update_status(ProjectStatus.COMPLETED)
        task2.update_status(ProjectStatus.IN_PROGRESS)

        # Get project status
        project_status = project_plan.get_project_status()
        print(f"Project Status: {project_status.name}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
