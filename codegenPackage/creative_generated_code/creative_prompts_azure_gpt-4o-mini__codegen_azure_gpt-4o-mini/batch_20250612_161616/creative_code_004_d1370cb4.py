"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getdolphin.io
Prompt: How does Project Dolphin facilitate collaboration in software development projects? Provide a code example.
Generated: DETERMINISTIC_d1370cb4c8906c7d
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Project Dolphin: A Simplified Collaboration Tool for Software Development Projects

This script demonstrates a basic implementation of a collaboration tool that allows team members
to create, assign, and update tasks within a software development project. It uses a simple command-line
interface to facilitate interaction and manage tasks.

Usage:
    - Add a task: python project_dolphin.py add "Task description" "Assignee"
    - List all tasks: python project_dolphin.py list
    - Update a task: python project_dolphin.py update <task_id> "New description" "New assignee"
    - Delete a task: python project_dolphin.py delete <task_id>
"""

import sys

class Task:
    """Class representing a single task in the project."""
    def __init__(self, description, assignee):
        self.description = description
        self.assignee = assignee
        self.completed = False

    def __str__(self):
        status = "✔" if self.completed else "✖"
        return f"[{status}] {self.description} (Assigned to: {self.assignee})"


class ProjectDolphin:
    """Class managing the tasks for the project."""
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description, assignee):
        """Add a new task to the project."""
        task = Task(description, assignee)
        self.tasks.append((self.next_id, task))
        self.next_id += 1
        print(f"Task added: {task}")

    def list_tasks(self):
        """List all tasks in the project."""
        if not self.tasks:
            print("No tasks available.")
            return
        for task_id, task in self.tasks:
            print(f"{task_id}: {task}")

    def update_task(self, task_id, new_description, new_assignee):
        """Update the description and assignee of a task."""
        for index, (tid, task) in enumerate(self.tasks):
            if tid == task_id:
                self.tasks[index] = (tid, Task(new_description, new_assignee))
                print(f"Task updated: {self.tasks[index][1]}")
                return
        print("Error: Task not found.")

    def delete_task(self, task_id):
        """Delete a task from the project."""
        for index, (tid, task) in enumerate(self.tasks):
            if tid == task_id:
                del self.tasks[index]
                print(f"Task {task_id} deleted.")
                return
        print("Error: Task not found.")


def main():
    """Main function to handle command-line arguments and execute commands."""
    project = ProjectDolphin()

    if len(sys.argv) < 2:
        print("Usage: python project_dolphin.py <command> [args...]")
        return

    command = sys.argv[1]

    try:
        if command == "add":
            if len(sys.argv) != 4:
                print("Usage: python project_dolphin.py add <description> <assignee>")
            else:
                project.add_task(sys.argv[2], sys.argv[3])
        elif command == "list":
            project.list_tasks()
        elif command == "update":
            if len(sys.argv) != 5:
                print("Usage: python project_dolphin.py update <task_id> <new_description> <new_assignee>")
            else:
                task_id = int(sys.argv[2])
                project.update_task(task_id, sys.argv[3], sys.argv[4])
        elif command == "delete":
            if len(sys.argv) != 3:
                print("Usage: python project_dolphin.py delete <task_id>")
            else:
                task_id = int(sys.argv[2])
                project.delete_task(task_id)
        else:
            print(f"Error: Unknown command '{command}'.")
    except ValueError:
        print("Error: Invalid input. Please ensure task IDs are integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
