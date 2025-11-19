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
# Import necessary libraries
import datetime

class ConstructionProject:
    """
    A class to represent a construction project and manage its timelines and quality assurance.
    """

    def __init__(self, project_name, start_date, end_date):
        """
        Initialize the ConstructionProject object.

        :param project_name: Name of the construction project
        :param start_date: Project start date (YYYY-MM-DD)
        :param end_date: Project end date (YYYY-MM-DD)
        """
        self.project_name = project_name
        try:
            self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
        
        if self.start_date >= self.end_date:
            raise ValueError("End date must be after the start date.")
        
        self.tasks = []  # List to track tasks in the project
        self.quality_checks = []  # List to track quality check results
    
    def add_task(self, task_name, deadline):
        """
        Add a task to the project timeline.

        :param task_name: Name of the task
        :param deadline: Deadline for the task (YYYY-MM-DD)
        """
        try:
            deadline_date = datetime.datetime.strptime(deadline, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format for deadline. Use 'YYYY-MM-DD'.")
        
        if not (self.start_date <= deadline_date <= self.end_date):
            raise ValueError("Task deadline must fall within the project timeline.")
        
        self.tasks.append({
            "task_name": task_name,
            "deadline": deadline_date,
            "completed": False
        })

    def mark_task_completed(self, task_name):
        """
        Mark a task as completed.

        :param task_name: Name of the task to mark as completed
        """
        for task in self.tasks:
            if task["task_name"] == task_name:
                task["completed"] = True
                return
        raise ValueError(f"Task '{task_name}' not found in the project.")

    def add_quality_check(self, check_name, passed):
        """
        Add a quality check result for the project.

        :param check_name: Name of the quality check
        :param passed: Boolean indicating whether the quality check passed
        """
        self.quality_checks.append({
            "check_name": check_name,
            "passed": passed,
            "timestamp": datetime.datetime.now()
        })

    def get_project_status(self):
        """
        Get a summary of the project status.

        :return: Project status summary
        """
        completed_tasks = sum(1 for task in self.tasks if task["completed"])
        total_tasks = len(self.tasks)
        passed_checks = sum(1 for check in self.quality_checks if check["passed"])
        total_checks = len(self.quality_checks)

        return {
            "project_name": self.project_name,
            "start_date": self.start_date.strftime('%Y-%m-%d'),
            "end_date": self.end_date.strftime('%Y-%m-%d'),
            "tasks_completed": f"{completed_tasks}/{total_tasks}",
            "quality_checks_passed": f"{passed_checks}/{total_checks}"
        }


# Example usage:
if __name__ == "__main__":
    try:
        # Create a project
        project = ConstructionProject("Building A", "2023-01-01", "2023-12-31")
        
        # Add tasks
        project.add_task("Foundation Work", "2023-03-01")
        project.add_task("Roof Installation", "2023-06-01")
        
        # Mark a task as completed
        project.mark_task_completed("Foundation Work")
        
        # Record quality checks
        project.add_quality_check("Foundation Quality", True)
        project.add_quality_check("Roof Quality", False)
        
        # Get and print project status
        status = project.get_project_status()
        print("Project Status:")
        print(status)
    except Exception as e:
        print(f"Error: {e}")
```
