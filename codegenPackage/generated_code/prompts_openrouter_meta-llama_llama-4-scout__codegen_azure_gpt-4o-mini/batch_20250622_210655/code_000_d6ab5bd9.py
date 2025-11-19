"""
Generated Code Metadata:
========================
Original URL: https://settlement.owlspriority.ca
Prompt: Write a checklist for a newcomer arriving in Canada, including essential tasks to complete when settling into their new life.
Generated: DETERMINISTIC_d6ab5bd9775c6c1a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NewcomerChecklist:
    """
    A class to represent a checklist for newcomers arriving in Canada.
    """

    def __init__(self):
        """
        Initializes the checklist with essential tasks.
        """
        self.tasks = [
            "Apply for a Social Insurance Number (SIN)",
            "Open a Canadian bank account",
            "Register for healthcare services",
            "Find suitable housing",
            "Get a local phone number",
            "Learn about Canadian laws and rights",
            "Enroll children in school (if applicable)",
            "Explore local community resources",
            "Set up utilities (electricity, water, internet)",
            "Familiarize yourself with public transportation",
            "Connect with local immigrant services",
            "Learn about Canadian culture and customs"
        ]
        self.completed_tasks = []

    def display_checklist(self):
        """
        Displays the current checklist of tasks.
        """
        print("Newcomer Checklist:")
        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task in self.completed_tasks else "✗"
            print(f"{index}. [{status}] {task}")

    def complete_task(self, task_number):
        """
        Marks a task as completed.

        Args:
            task_number (int): The number of the task to complete.

        Raises:
            ValueError: If the task number is out of range.
        """
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            if task not in self.completed_tasks:
                self.completed_tasks.append(task)
                print(f"Task '{task}' marked as completed.")
            else:
                print(f"Task '{task}' is already completed.")
        else:
            raise ValueError("Task number is out of range. Please provide a valid number.")

    def reset_checklist(self):
        """
        Resets the checklist, marking all tasks as incomplete.
        """
        self.completed_tasks.clear()
        print("Checklist has been reset.")

if __name__ == "__main__":
    checklist = NewcomerChecklist()
    
    # Display the initial checklist
    checklist.display_checklist()

    # Example of completing a task
    try:
        checklist.complete_task(1)  # Completing the first task
        checklist.display_checklist()  # Display updated checklist
    except ValueError as e:
        print(e)

    # Resetting the checklist
    checklist.reset_checklist()
    checklist.display_checklist()  # Display checklist after reset
```
