"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sstco.ma
Prompt: Generate a code snippet for a construction project management tool that tracks project timelines and ensures quality delivery, similar to SSTCO's commitment to timely and quality services.
Generated: DETERMINISTIC_328a30c3623dfc0d
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Task:
    """
    Represents a task in the construction project.
    Each task has a name, start date, end date, and status.
    """
    def __init__(self, name: str, start_date: datetime, end_date: datetime):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.status = 'Pending'  # Status can be 'Pending', 'In Progress', or 'Completed'

    def mark_as_completed(self):
        """Mark the task as completed."""
        self.status = 'Completed'
        logging.info(f'Task "{self.name}" marked as completed.')

    def is_overdue(self) -> bool:
        """Check if the task is overdue."""
        return self.end_date < datetime.now() and self.status != 'Completed'


class Project:
    """
    Represents a construction project that contains multiple tasks.
    It tracks the project timeline and quality delivery.
    """
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.tasks = []

    def add_task(self, task: Task):
        """Add a new task to the project."""
        self.tasks.append(task)
        logging.info(f'Task "{task.name}" added to project "{self.project_name}".')

    def check_project_status(self):
        """Check the overall status of the project."""
        overdue_tasks = [task for task in self.tasks if task.is_overdue()]
        if overdue_tasks:
            logging.warning(f'Project "{self.project_name}" has overdue tasks: {[task.name for task in overdue_tasks]}')
        else:
            logging.info(f'All tasks in project "{self.project_name}" are on schedule.')

    def complete_task(self, task_name: str):
        """Complete a task by its name."""
        for task in self.tasks:
            if task.name == task_name:
                task.mark_as_completed()
                return
        logging.error(f'Task "{task_name}" not found in project "{self.project_name}".')

    def project_summary(self):
        """Print a summary of the project."""
        summary = {
            'project_name': self.project_name,
            'total_tasks': len(self.tasks),
            'completed_tasks': sum(1 for task in self.tasks if task.status == 'Completed'),
            'pending_tasks': sum(1 for task in self.tasks if task.status == 'Pending'),
            'overdue_tasks': sum(1 for task in self.tasks if task.is_overdue()),
        }
        return summary


# Example usage
if __name__ == '__main__':
    # Create a project instance
    project = Project("Highway Construction")

    # Create tasks and add them to the project
    task1 = Task("Site Preparation", datetime.now(), datetime.now() + timedelta(days=7))
    task2 = Task("Foundation Work", datetime.now() + timedelta(days=5), datetime.now() + timedelta(days=15))
    
    project.add_task(task1)
    project.add_task(task2)

    # Check project status and summary
    project.check_project_status()
    logging.info(f'Project Summary: {project.project_summary()}')

    # Complete a task
    project.complete_task("Site Preparation")
    
    # Check project status again
    project.check_project_status()
    logging.info(f'Updated Project Summary: {project.project_summary()}')
```
