"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crestagile.com
Prompt: Generate a code snippet for an Agile project management tool that incorporates interactive learning features as described on the CrestAgile website.
Generated: DETERMINISTIC_6bca754ef7c11569
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Agile Project Management Tool with Interactive Learning Features
# This script implements a simplified Agile tool with interactive learning functionality.

import sys
from datetime import datetime

class Task:
    """
    Represents a single task in the Agile project.
    """
    def __init__(self, title, description, status="To-Do"):
        self.title = title
        self.description = description
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_status(self, new_status):
        """
        Update the status of the task.
        """
        if new_status not in ["To-Do", "In Progress", "Completed"]:
            raise ValueError("Invalid status. Must be 'To-Do', 'In Progress', or 'Completed'.")
        self.status = new_status
        self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation of the task.
        """
        return f"[{self.status}] {self.title} - {self.description} (Last updated: {self.updated_at})"

class AgileBoard:
    """
    Represents an Agile board with tasks.
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        """
        Add a new task to the board.
        """
        task = Task(title, description)
        self.tasks.append(task)

    def list_tasks(self):
        """
        List all tasks on the board.
        """
        if not self.tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def update_task_status(self, task_index, new_status):
        """
        Update the status of a specific task.
        """
        try:
            task = self.tasks[task_index - 1]
            task.update_status(new_status)
            print(f"Task '{task.title}' status updated to '{new_status}'.")
        except IndexError:
            print("Invalid task index. Please choose a valid task number.")
        except ValueError as e:
            print(e)

    def interactive_learning(self):
        """
        Interactive learning feature to guide users on Agile practices.
        """
        print("\n--- Interactive Learning ---")
        print("1. What is Agile?")
        print("2. Key Agile Principles")
        print("3. How to conduct a Scrum meeting?")
        print("4. Exit Learning Module")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            print("\nAgile is a project management methodology focused on iterative development, collaboration, and customer feedback.")
        elif choice == "2":
            print("\nKey Agile Principles:\n1. Customer satisfaction through early and continuous delivery.\n2. Embrace change.\n3. Deliver working software frequently.\n4. Collaboration over processes.\n")
        elif choice == "3":
            print("\nScrum meetings typically include:\n1. Reviewing completed tasks.\n2. Discussing ongoing work and blockers.\n3. Setting goals for the next sprint.")
        elif choice == "4":
            print("\nExiting Learning Module.")
        else:
            print("\nInvalid choice. Please select a valid option.")

# Main application loop
def main():
    """
    Main application to run the Agile project management tool.
    """
    board = AgileBoard()

    while True:
        # Display menu options
        print("\n--- Agile Project Management Tool ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task Status")
        print("4. Interactive Learning")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                title = input("\nEnter Task Title: ")
                description = input("Enter Task Description: ")
                board.add_task(title, description)
                print(f"\nTask '{title}' added successfully.")
            elif choice == 2:
                print("\n--- Tasks ---")
                board.list_tasks()
            elif choice == 3:
                board.list_tasks()
                task_index = int(input("\nEnter the Task Number to Update: "))
                new_status = input("Enter the New Status (To-Do/In Progress/Completed): ")
                board.update_task_status(task_index, new_status)
            elif choice == 4:
                board.interactive_learning()
            elif choice == 5:
                print("\nExiting Agile Project Management Tool. Goodbye!")
                sys.exit(0)
            else:
                print("\nInvalid choice. Please select a valid option.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
