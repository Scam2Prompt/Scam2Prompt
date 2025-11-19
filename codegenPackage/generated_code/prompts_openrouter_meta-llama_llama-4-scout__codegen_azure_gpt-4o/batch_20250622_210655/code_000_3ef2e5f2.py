"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: "Write a Python code snippet to manage project timelines for a civil engineering construction project, ensuring timely delivery by using detailed planning, regular progress monitoring, and effective resource management."
Generated: DETERMINISTIC_3ef2e5f2dd69efa2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class Task:
    """
    Represents a single task in the project timeline.
    """
    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date, resources: List[str]):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.resources = resources
        self.progress = 0  # Progress in percentage (0-100)

    def update_progress(self, progress: int):
        """
        Updates the progress of the task.
        :param progress: Progress percentage (0-100)
        """
        if 0 <= progress <= 100:
            self.progress = progress
        else:
            raise ValueError("Progress must be between 0 and 100.")

    def is_delayed(self) -> bool:
        """
        Checks if the task is delayed based on the current date.
        :return: True if delayed, False otherwise.
        """
        today = datetime.date.today()
        return today > self.end_date and self.progress < 100


class ProjectTimeline:
    """
    Manages the overall project timeline.
    """
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """
        Adds a new task to the project timeline.
        :param task: Task object to be added.
        """
        self.tasks.append(task)

    def monitor_progress(self) -> Dict[str, str]:
        """
        Monitors the progress of all tasks and checks for delays.
        :return: Dictionary with task names and their status.
        """
        status = {}
        for task in self.tasks:
            if task.is_delayed():
                status[task.name] = "Delayed"
            elif task.progress == 100:
                status[task.name] = "Completed"
            else:
                status[task.name] = "In Progress"
        return status

    def allocate_resources(self, task_name: str, resources: List[str]):
        """
        Allocates resources to a specific task.
        :param task_name: Name of the task to allocate resources to.
        :param resources: List of resources to allocate.
        """
        for task in self.tasks:
            if task.name == task_name:
                task.resources.extend(resources)
                return
        raise ValueError(f"Task '{task_name}' not found.")

    def generate_report(self) -> str:
        """
        Generates a report of the project timeline.
        :return: String report of all tasks and their statuses.
        """
        report = f"Project: {self.project_name}\n"
        report += "Task Report:\n"
        for task in self.tasks:
            report += f"- {task.name}: Progress {task.progress}%, Status: "
            if task.is_delayed():
                report += "Delayed\n"
            elif task.progress == 100:
                report += "Completed\n"
            else:
                report += "In Progress\n"
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Create a project timeline
        project = ProjectTimeline("Civil Engineering Construction Project")

        # Add tasks
        task1 = Task("Foundation Work", datetime.date(2023, 10, 1), datetime.date(2023, 10, 15), ["Excavator", "Concrete Mixer"])
        task2 = Task("Framing", datetime.date(2023, 10, 16), datetime.date(2023, 10, 30), ["Carpenters", "Wood"])
        project.add_task(task1)
        project.add_task(task2)

        # Update progress
        task1.update_progress(50)
        task2.update_progress(20)

        # Monitor progress
        progress_status = project.monitor_progress()
        print("Progress Status:", progress_status)

        # Allocate resources
        project.allocate_resources("Framing", ["Nails", "Hammer"])

        # Generate report
        report = project.generate_report()
        print(report)

    except Exception as e:
        print(f"Error: {e}")
```
