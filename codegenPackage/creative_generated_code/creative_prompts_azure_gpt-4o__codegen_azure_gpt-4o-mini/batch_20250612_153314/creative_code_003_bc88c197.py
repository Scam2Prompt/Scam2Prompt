"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haseebbaig.me
Prompt: Provide code examples for implementing Agile project management principles in software development, referencing the consultant's experience in Agile environments.
Generated: DETERMINISTIC_bc88c19760c7e305
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Agile Project Management Example in Python

This module demonstrates a basic implementation of Agile project management principles
using classes to represent a simple task board. It includes functionalities for managing tasks,
updating their status, and tracking progress in a sprint.

Author: [Your Name]
Date: [Current Date]
"""

class Task:
    """
    Represents a task in the Agile project management system.
    
    Attributes:
        title (str): The title of the task.
        status (str): The current status of the task ("To Do", "In Progress", "Done").
    """
    def __init__(self, title):
        self.title = title
        self.status = "To Do"

    def update_status(self, new_status):
        """
        Updates the status of the task.
        
        Args:
            new_status (str): The new status to set for the task.
        
        Raises:
            ValueError: If the new_status is not one of the allowed statuses.
        """
        allowed_statuses = ["To Do", "In Progress", "Done"]
        if new_status not in allowed_statuses:
            raise ValueError(f"Invalid status: {new_status}. Allowed statuses are: {allowed_statuses}.")
        self.status = new_status


class Sprint:
    """
    Represents a sprint in the Agile project management system.
    
    Attributes:
        tasks (list): A list of tasks included in the sprint.
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """
        Adds a task to the sprint.
        
        Args:
            task (Task): The task to add to the sprint.
        """
        self.tasks.append(task)

    def update_task_status(self, task_title, new_status):
        """
        Updates the status of a task by its title.
        
        Args:
            task_title (str): The title of the task.
            new_status (str): The new status to set for the task.
        
        Raises:
            ValueError: If the task is not found or if the new_status is invalid.
        """
        for task in self.tasks:
            if task.title == task_title:
                task.update_status(new_status)
                return
        raise ValueError(f"Task with title '{task_title}' not found.")

    def get_progress(self):
        """
        Returns the progress of the sprint as a dictionary.
        
        Returns:
            dict: A summary of the number of tasks in each status.
        """
        progress = {"To Do": 0, "In Progress": 0, "Done": 0}
        for task in self.tasks:
            progress[task.status] += 1
        return progress


# Example Usage
if __name__ == "__main__":
    # Create a new sprint
    sprint = Sprint()

    # Create tasks
    task1 = Task("Implement user authentication")
    task2 = Task("Set up database schema")
    task3 = Task("Develop API for user management")

    # Add tasks to sprint
    sprint.add_task(task1)
    sprint.add_task(task2)
    sprint.add_task(task3)

    # Update task status
    try:
        sprint.update_task_status("Implement user authentication", "In Progress")
        sprint.update_task_status("Set up database schema", "Done")
    except ValueError as e:
        print(f"Error: {e}")

    # Get and print sprint progress
    progress = sprint.get_progress()
    print("Sprint Progress:", progress)
```
