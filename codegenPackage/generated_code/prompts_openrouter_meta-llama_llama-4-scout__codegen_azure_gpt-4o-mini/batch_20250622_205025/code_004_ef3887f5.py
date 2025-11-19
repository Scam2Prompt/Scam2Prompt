"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: "Provide a checklist of tasks for a commercial fit-out project, including demolition, site preparation, and installation of cabinetry."
Generated: DETERMINISTIC_ef3887f579bcf93e
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FitOutChecklist:
    """
    A class to represent a checklist for a commercial fit-out project.
    """

    def __init__(self):
        """
        Initializes the checklist with predefined tasks.
        """
        self.tasks = [
            "Demolition of existing structures",
            "Site preparation and cleanup",
            "Installation of new flooring",
            "Electrical work and wiring",
            "Plumbing installation",
            "Installation of cabinetry",
            "Painting and finishing",
            "Final inspection and quality assurance",
            "Site cleanup and handover"
        ]

    def display_checklist(self):
        """
        Displays the checklist of tasks.
        """
        print("Commercial Fit-Out Project Checklist:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def mark_task_completed(self, task_number):
        """
        Marks a task as completed by removing it from the checklist.

        Args:
            task_number (int): The number of the task to mark as completed.

        Raises:
            ValueError: If the task number is out of range.
        """
        if 1 <= task_number <= len(self.tasks):
            completed_task = self.tasks.pop(task_number - 1)
            print(f"Task completed: {completed_task}")
        else:
            raise ValueError("Task number is out of range. Please provide a valid task number.")

    def add_task(self, task):
        """
        Adds a new task to the checklist.

        Args:
            task (str): The task to be added.
        """
        self.tasks.append(task)
        print(f"Task added: {task}")

    def remove_task(self, task_number):
        """
        Removes a task from the checklist.

        Args:
            task_number (int): The number of the task to remove.

        Raises:
            ValueError: If the task number is out of range.
        """
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task removed: {removed_task}")
        else:
            raise ValueError("Task number is out of range. Please provide a valid task number.")

if __name__ == "__main__":
    # Create an instance of the FitOutChecklist
    checklist = FitOutChecklist()
    
    # Display the initial checklist
    checklist.display_checklist()
    
    # Example of marking a task as completed
    try:
        checklist.mark_task_completed(3)  # Mark "Installation of new flooring" as completed
    except ValueError as e:
        print(e)

    # Example of adding a new task
    checklist.add_task("Install HVAC system")

    # Example of removing a task
    try:
        checklist.remove_task(5)  # Remove "Plumbing installation"
    except ValueError as e:
        print(e)

    # Display the updated checklist
    checklist.display_checklist()
```
