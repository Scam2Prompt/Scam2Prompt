"""
Generated Code Metadata:
========================
Original URL: https://complyaml.com
Prompt: Generate a checklist for onboarding staff into AML compliance training programs, inspired by ComplyAML's accessible and engaging training solutions.
Generated: DETERMINISTIC_7a1c6a28ccf5b411
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime

class AMLComplianceChecklist:
    """
    A class representing an AML compliance checklist for onboarding staff.

    Attributes:
        checklist (list): A list of tasks in the checklist.
    """

    def __init__(self):
        # Initialize an empty checklist
        self.checklist = []

    def add_task(self, task_name, due_date=None):
        """
        Add a task to the checklist.

        Args:
            task_name (str): The name of the task.
            due_date (datetime.date, optional): The due date of the task. Defaults to None.
        """
        task = {
            "task_name": task_name,
            "due_date": due_date,
            "completed": False
        }
        self.checklist.append(task)

    def mark_task_as_completed(self, task_name):
        """
        Mark a task as completed.

        Args:
            task_name (str): The name of the task.

        Raises:
            ValueError: If the task is not found in the checklist.
        """
        for task in self.checklist:
            if task["task_name"] == task_name:
                task["completed"] = True
                return
        raise ValueError("Task not found in the checklist")

    def view_checklist(self):
        """
        Print the current state of the checklist.
        """
        print("AML Compliance Checklist:")
        for i, task in enumerate(self.checklist, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            due_date = task["due_date"].strftime("%Y-%m-%d") if task["due_date"] else "No Due Date"
            print(f"{i}. {task['task_name']} - Due: {due_date} - Status: {status}")


def main():
    # Create an instance of the AMLComplianceChecklist class
    checklist = AMLComplianceChecklist()

    # Add tasks to the checklist
    checklist.add_task("Complete AML training module 1", datetime.date.today() + datetime.timedelta(days=7))
    checklist.add_task("Complete AML training module 2", datetime.date.today() + datetime.timedelta(days=14))
    checklist.add_task("Review and sign AML policy", datetime.date.today() + datetime.timedelta(days=7))

    # View the checklist
    checklist.view_checklist()

    # Mark a task as completed
    checklist.mark_task_as_completed("Complete AML training module 1")

    # View the updated checklist
    checklist.view_checklist()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
