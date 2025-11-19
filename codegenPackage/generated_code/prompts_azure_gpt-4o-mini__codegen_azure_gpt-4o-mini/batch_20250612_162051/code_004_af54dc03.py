"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: Create a checklist for a home renovation project that includes water leak detection and insulation, inspired by the services of شمس المملكة.
Generated: DETERMINISTIC_af54dc03146b4cda
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HomeRenovationChecklist:
    """
    A class to represent a home renovation checklist.
    This checklist includes tasks related to water leak detection and insulation.
    """

    def __init__(self):
        """
        Initializes the checklist with default tasks.
        """
        self.tasks = [
            "Inspect plumbing for leaks",
            "Install water leak detection system",
            "Check insulation in walls and attic",
            "Seal any gaps in insulation",
            "Test water leak detection system functionality",
            "Evaluate insulation R-value",
            "Consider upgrading insulation materials",
            "Schedule regular maintenance checks"
        ]
        self.completed_tasks = []

    def display_checklist(self):
        """
        Displays the current checklist of tasks.
        """
        print("Home Renovation Checklist:")
        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task in self.completed_tasks else "✗"
            print(f"{index}. [{status}] {task}")

    def mark_task_completed(self, task_number):
        """
        Marks a task as completed based on its number.

        Args:
            task_number (int): The number of the task to mark as completed.

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
        print("Checklist has been reset. All tasks are now incomplete.")

def main():
    """
    Main function to run the home renovation checklist program.
    """
    checklist = HomeRenovationChecklist()
    
    while True:
        checklist.display_checklist()
        try:
            user_input = input("Enter the task number to mark as completed (or 'reset' to reset, 'exit' to quit): ").strip()
            if user_input.lower() == 'exit':
                print("Exiting the checklist program.")
                break
            elif user_input.lower() == 'reset':
                checklist.reset_checklist()
            else:
                task_number = int(user_input)
                checklist.mark_task_completed(task_number)
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    main()
```
