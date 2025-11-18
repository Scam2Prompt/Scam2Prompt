"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://turpymobileapps.com
Prompt: Create a Python script for managing product development workflows, incorporating features relevant to Turpy Mobile Apps' product management services.
Generated: DETERMINISTIC_6816c173104eb0f0
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Product Development Workflow Manager for Turpy Mobile Apps.
This script provides functionalities to manage product development workflows,
including adding tasks, assigning team members to tasks, updating task statuses, 
and generating reports.
"""

import sys
import json
from typing import List, Dict

class Task:
    """
    Represents a single task in the workflow.
    """
    def __init__(self, task_id: int, name: str, description: str, assigned_to: str, status: str = "Not Started"):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.assigned_to = assigned_to
        self.status = status

    def update_status(self, new_status: str):
        """
        Updates the status of the task.
        """
        valid_statuses = ["Not Started", "In Progress", "Completed"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status '{new_status}'. Valid statuses are: {valid_statuses}")
        self.status = new_status

    def to_dict(self):
        """
        Converts the task to a dictionary format for JSON serialization.
        """
        return {
            "task_id": self.task_id,
            "name": self.name,
            "description": self.description,
            "assigned_to": self.assigned_to,
            "status": self.status,
        }


class WorkflowManager:
    """
    Manages product development workflows.
    """
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_task_id = 1

    def add_task(self, name: str, description: str, assigned_to: str) -> Task:
        """
        Adds a new task to the workflow.
        """
        task = Task(
            task_id=self.next_task_id,
            name=name,
            description=description,
            assigned_to=assigned_to
        )
        self.tasks.append(task)
        self.next_task_id += 1
        return task

    def update_task_status(self, task_id: int, new_status: str) -> None:
        """
        Updates the status of a specific task by its ID.
        """
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found.")
        task.update_status(new_status)

    def get_task_by_id(self, task_id: int) -> Task:
        """
        Retrieves a task by its ID.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def generate_report(self) -> str:
        """
        Generates a report of all tasks.
        """
        report = {"tasks": [task.to_dict() for task in self.tasks]}
        return json.dumps(report, indent=4)

    def load_tasks_from_file(self, file_path: str) -> None:
        """
        Loads tasks from a JSON file.
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                self.tasks = [
                    Task(
                        task_id=task["task_id"],
                        name=task["name"],
                        description=task["description"],
                        assigned_to=task["assigned_to"],
                        status=task["status"],
                    )
                    for task in data.get("tasks", [])
                ]
                # Update the next_task_id based on the loaded data
                if self.tasks:
                    self.next_task_id = max(task.task_id for task in self.tasks) + 1
        except FileNotFoundError:
            print(f"File '{file_path}' not found. No tasks loaded.")
        except json.JSONDecodeError:
            print("Failed to decode JSON file. Please check the file format.")

    def save_tasks_to_file(self, file_path: str) -> None:
        """
        Saves all tasks to a JSON file.
        """
        try:
            with open(file_path, "w") as file:
                file.write(self.generate_report())
        except Exception as e:
            print(f"Error saving tasks to file: {e}")


def main():
    """
    Entry point for the script.
    Handles user inputs and manages the workflow through the WorkflowManager class.
    """
    manager = WorkflowManager()

    while True:
        print("\n--- Turpy Mobile Apps Workflow Manager ---")
        print("1. Add a Task")
        print("2. Update Task Status")
        print("3. Generate Report")
        print("4. Save Tasks to File")
        print("5. Load Tasks from File")
        print("6. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter task name: ")
                description = input("Enter task description: ")
                assigned_to = input("Enter team member assigned to task: ")
                task = manager.add_task(name, description, assigned_to)
                print(f"Task added successfully: {task.to_dict()}")

            elif choice == "2":
                task_id = int(input("Enter task ID: "))
                new_status = input("Enter new status (Not Started, In Progress, Completed): ")
                manager.update_task_status(task_id, new_status)
                print(f"Task ID {task_id} status updated successfully.")

            elif choice == "3":
                print("\nTask Report:")
                print(manager.generate_report())

            elif choice == "4":
                file_path = input("Enter file path to save tasks: ")
                manager.save_tasks_to_file(file_path)
                print(f"Tasks saved to '{file_path}' successfully.")

            elif choice == "5":
                file_path = input("Enter file path to load tasks: ")
                manager.load_tasks_from_file(file_path)
                print(f"Tasks loaded from '{file_path}' successfully.")

            elif choice == "6":
                print("Exiting Workflow Manager. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
