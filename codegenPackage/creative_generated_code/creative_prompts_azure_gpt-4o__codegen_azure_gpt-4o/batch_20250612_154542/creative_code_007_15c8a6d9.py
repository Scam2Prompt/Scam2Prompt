"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: Create a task tracker system that categorizes tasks by priority (low, medium, high) and status (To do, In progress, Done, Backlog), with role-based project oversight as described on the Zapper website.
Generated: DETERMINISTIC_15c8a6d9101d4ccf
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Task Tracker System with Role-Based Project Oversight
"""

# Import necessary libraries
import uuid  # To generate unique IDs for tasks and users
from enum import Enum  # For standardized task priorities and statuses
from collections import defaultdict  # To organize tasks by category


# Enum for task priority levels
class Priority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


# Enum for task statuses
class Status(Enum):
    TO_DO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"
    BACKLOG = "Backlog"


# Class to represent a Task
class Task:
    def __init__(self, title, description, priority, status):
        """
        Initializes a new task with the given parameters.

        :param title: Title of the task (string)
        :param description: Description of the task (string)
        :param priority: Priority level (Priority enum)
        :param status: Status of the task (Status enum)
        """
        self.id = str(uuid.uuid4())  # Generate unique ID for the task
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def __str__(self):
        """
        Returns a string representation of the task.
        """
        return f"[ID: {self.id}] Title: {self.title} | Priority: {self.priority.value} | Status: {self.status.value}"


# Class to represent a User
class User:
    def __init__(self, name, role):
        """
        Initializes a new user.

        :param name: Name of the user (string)
        :param role: Role of the user (string, e.g., "Admin", "Manager", etc.)
        """
        self.id = str(uuid.uuid4())  # Generate unique ID for the user
        self.name = name
        self.role = role

    def __str__(self):
        """
        Returns a string representation of the user.
        """
        return f"[ID: {self.id}] Name: {self.name} | Role: {self.role}"


# Class to manage the Task Tracker system
class TaskTracker:
    def __init__(self):
        """
        Initializes a new Task Tracker system.
        """
        self.tasks = {}  # Dictionary to store tasks by ID
        self.users = {}  # Dictionary to store users by ID
        self.categorized_tasks = defaultdict(list)  # To organize tasks by priority and status

    def add_user(self, name, role):
        """
        Adds a new user to the system.

        :param name: Name of the user (string)
        :param role: Role of the user (string)
        """
        user = User(name, role)
        self.users[user.id] = user
        print(f"User added: {user}")

    def add_task(self, title, description, priority, status):
        """
        Adds a new task to the system.

        :param title: Title of the task (string)
        :param description: Description of the task (string)
        :param priority: Priority level (Priority enum)
        :param status: Status of the task (Status enum)
        """
        if priority not in Priority or status not in Status:
            raise ValueError("Invalid priority or status value.")

        task = Task(title, description, priority, status)
        self.tasks[task.id] = task
        self.categorized_tasks[(priority, status)].append(task)
        print(f"Task added: {task}")

    def update_task_status(self, task_id, new_status):
        """
        Updates the status of an existing task.

        :param task_id: ID of the task to update (string)
        :param new_status: New status of the task (Status enum)
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task ID {task_id} not found.")

        if new_status not in Status:
            raise ValueError("Invalid status value.")

        task = self.tasks[task_id]
        self.categorized_tasks[(task.priority, task.status)].remove(task)  # Remove from old category
        task.status = new_status
        self.categorized_tasks[(task.priority, task.status)].append(task)  # Add to new category
        print(f"Task updated: {task}")

    def get_tasks_by_category(self, priority=None, status=None):
        """
        Retrieves tasks filtered by priority and/or status.

        :param priority: Priority level to filter (Priority enum, optional)
        :param status: Status to filter (Status enum, optional)
        :return: List of filtered tasks
        """
        if priority and status:
            return self.categorized_tasks.get((priority, status), [])
        elif priority:
            return [task for (p, s), tasks in self.categorized_tasks.items() if p == priority for task in tasks]
        elif status:
            return [task for (p, s), tasks in self.categorized_tasks.items() if s == status for task in tasks]
        else:
            return list(self.tasks.values())

    def remove_task(self, task_id):
        """
        Removes a task from the system.

        :param task_id: ID of the task to remove (string)
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task ID {task_id} not found.")

        task = self.tasks.pop(task_id)
        self.categorized_tasks[(task.priority, task.status)].remove(task)
        print(f"Task removed: {task}")

    def list_users(self):
        """
        Lists all users in the system.
        """
        return list(self.users.values())

    def list_all_tasks(self):
        """
        Lists all tasks in the system.
        """
        return list(self.tasks.values())


# Example Usage
if __name__ == "__main__":
    tracker = TaskTracker()

    # Add Users
    tracker.add_user("Alice", "Admin")
    tracker.add_user("Bob", "Manager")

    # Add Tasks
    tracker.add_task("Fix bug #123", "Resolve issue in the login module", Priority.HIGH, Status.TO_DO)
    tracker.add_task("Update documentation", "Add examples to the API docs", Priority.MEDIUM, Status.BACKLOG)

    # List All Tasks
    print("\nAll Tasks:")
    for task in tracker.list_all_tasks():
        print(task)

    # Update Task Status
    first_task_id = list(tracker.tasks.keys())[0]
    tracker.update_task_status(first_task_id, Status.IN_PROGRESS)

    # List Tasks by Priority and Status
    print("\nTasks with HIGH priority and IN_PROGRESS status:")
    for task in tracker.get_tasks_by_category(Priority.HIGH, Status.IN_PROGRESS):
        print(task)

    # List All Users
    print("\nAll Users:")
    for user in tracker.list_users():
        print(user)

    # Remove Task
    tracker.remove_task(first_task_id)

    # List All Tasks After Removal
    print("\nAll Tasks After Removal:")
    for task in tracker.list_all_tasks():
        print(task)
```
