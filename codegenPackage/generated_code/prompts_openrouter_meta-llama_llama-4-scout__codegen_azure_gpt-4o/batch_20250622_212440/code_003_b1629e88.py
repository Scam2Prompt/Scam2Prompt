"""
Generated Code Metadata:
========================
Original URL: https://dev-x-studios.com
Prompt: "Create a Python script to manage game development projects, including tasks such as design, development, and advertisement, using Agile methodologies."
Generated: DETERMINISTIC_b1629e8827e329fd
Batch ID: 20250622_212440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Task:
    """
    Represents a single task in the project.
    """
    def __init__(self, name, description, assignee, due_date, status="To Do"):
        self.name = name
        self.description = description
        self.assignee = assignee
        self.due_date = due_date
        self.status = status

    def update_status(self, new_status):
        """
        Updates the status of the task.
        """
        valid_statuses = ["To Do", "In Progress", "Completed"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are {valid_statuses}.")

    def __str__(self):
        """
        Returns a string representation of the task.
        """
        return (f"Task: {self.name}\n"
                f"Description: {self.description}\n"
                f"Assignee: {self.assignee}\n"
                f"Due Date: {self.due_date}\n"
                f"Status: {self.status}\n")


class AgileBoard:
    """
    Represents an Agile board for managing tasks in a project.
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """
        Adds a new task to the board.
        """
        if not isinstance(task, Task):
            raise TypeError("Only Task objects can be added to the board.")
        self.tasks.append(task)

    def remove_task(self, task_name):
        """
        Removes a task from the board by its name.
        """
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                return
        raise ValueError(f"Task with name '{task_name}' not found.")

    def list_tasks(self, status=None):
        """
        Lists all tasks, optionally filtered by status.
        """
        if status:
            return [task for task in self.tasks if task.status == status]
        return self.tasks

    def __str__(self):
        """
        Returns a string representation of the Agile board.
        """
        return "\n".join(str(task) for task in self.tasks)


def main():
    """
    Main function to demonstrate the Agile project management script.
    """
    try:
        # Create an Agile board
        board = AgileBoard()

        # Add tasks to the board
        task1 = Task(
            name="Design Game Characters",
            description="Create concept art for main characters.",
            assignee="Alice",
            due_date=datetime.date(2023, 11, 15)
        )
        board.add_task(task1)

        task2 = Task(
            name="Develop Game Mechanics",
            description="Implement core gameplay mechanics.",
            assignee="Bob",
            due_date=datetime.date(2023, 12, 1)
        )
        board.add_task(task2)

        task3 = Task(
            name="Advertise Game",
            description="Launch marketing campaign for the game.",
            assignee="Charlie",
            due_date=datetime.date(2023, 12, 10)
        )
        board.add_task(task3)

        # Update task status
        task1.update_status("In Progress")

        # List all tasks
        print("All Tasks:")
        print(board)

        # List tasks filtered by status
        print("\nTasks In Progress:")
        for task in board.list_tasks(status="In Progress"):
            print(task)

        # Remove a task
        board.remove_task("Advertise Game")
        print("\nAfter Removing 'Advertise Game':")
        print(board)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
