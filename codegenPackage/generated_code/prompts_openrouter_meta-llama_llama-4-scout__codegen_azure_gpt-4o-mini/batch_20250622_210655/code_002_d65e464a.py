"""
Generated Code Metadata:
========================
Original URL: https://sitechgt.com
Prompt: "Write a code snippet to implement a project management tool inspired by Études Architectural Solutions' approach."
Generated: DETERMINISTIC_d65e464ac55676c1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_tool.py

class Task:
    """
    Represents a task in the project management tool.
    """
    def __init__(self, title, description, status='Pending'):
        self.title = title
        self.description = description
        self.status = status

    def update_status(self, new_status):
        """
        Update the status of the task.
        
        Args:
            new_status (str): The new status of the task.
        """
        valid_statuses = ['Pending', 'In Progress', 'Completed']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status

    def __str__(self):
        return f"Task(title='{self.title}', description='{self.description}', status='{self.status}')"


class Project:
    """
    Represents a project containing multiple tasks.
    """
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the project.
        
        Args:
            task (Task): The task to be added.
        """
        if not isinstance(task, Task):
            raise TypeError("Expected a Task instance.")
        self.tasks.append(task)

    def get_tasks(self):
        """
        Retrieve all tasks in the project.
        
        Returns:
            list: A list of tasks in the project.
        """
        return self.tasks

    def __str__(self):
        return f"Project(name='{self.name}', tasks={self.tasks})"


def main():
    """
    Main function to demonstrate the project management tool.
    """
    try:
        # Create a new project
        project = Project("Website Redesign")

        # Create tasks
        task1 = Task("Design Mockups", "Create design mockups for the new website.")
        task2 = Task("Develop Frontend", "Implement the frontend using React.")

        # Add tasks to the project
        project.add_task(task1)
        project.add_task(task2)

        # Update task status
        task1.update_status("In Progress")

        # Print project details
        print(project)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
