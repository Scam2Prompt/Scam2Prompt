"""
Generated Code Metadata:
========================
Original URL: https://haseebbaig.me
Prompt: Provide code examples for implementing Agile project management principles in software development, referencing the consultant's experience in Agile environments.
Generated: DETERMINISTIC_bc88c19760c7e305
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# agile_project_management.py

class AgileProject:
    def __init__(self, name, team_members):
        """
        Initialize an Agile project.

        Args:
            name (str): The name of the project.
            team_members (list): A list of team member names.
        """
        self.name = name
        self.team_members = team_members
        self.sprint_backlog = []
        self.product_backlog = []

    def add_to_product_backlog(self, item):
        """
        Add an item to the product backlog.

        Args:
            item (str): The item to add.
        """
        self.product_backlog.append(item)

    def prioritize_product_backlog(self, item, priority):
        """
        Prioritize an item in the product backlog.

        Args:
            item (str): The item to prioritize.
            priority (int): The priority of the item.

        Raises:
            ValueError: If the item is not in the product backlog.
        """
        if item not in self.product_backlog:
            raise ValueError("Item not in product backlog")
        self.product_backlog.remove(item)
        self.product_backlog.insert(priority - 1, item)

    def create_sprint(self, sprint_name, duration):
        """
        Create a sprint.

        Args:
            sprint_name (str): The name of the sprint.
            duration (int): The duration of the sprint in days.

        Returns:
            Sprint: The created sprint.
        """
        sprint = Sprint(sprint_name, duration)
        self.sprint_backlog.append(sprint)
        return sprint

class Sprint:
    def __init__(self, name, duration):
        """
        Initialize a sprint.

        Args:
            name (str): The name of the sprint.
            duration (int): The duration of the sprint in days.
        """
        self.name = name
        self.duration = duration
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the sprint.

        Args:
            task (Task): The task to add.
        """
        self.tasks.append(task)

class Task:
    def __init__(self, name, estimate):
        """
        Initialize a task.

        Args:
            name (str): The name of the task.
            estimate (int): The estimated effort for the task.
        """
        self.name = name
        self.estimate = estimate
        self.status = "To-Do"

    def update_status(self, status):
        """
        Update the status of the task.

        Args:
            status (str): The new status of the task.

        Raises:
            ValueError: If the status is not valid.
        """
        valid_statuses = ["To-Do", "In Progress", "Done"]
        if status not in valid_statuses:
            raise ValueError("Invalid status")
        self.status = status

def main():
    # Create an Agile project
    project = AgileProject("Example Project", ["John", "Jane", "Bob"])

    # Add items to the product backlog
    project.add_to_product_backlog("Implement feature A")
    project.add_to_product_backlog("Implement feature B")
    project.add_to_product_backlog("Fix bug C")

    # Prioritize the product backlog
    project.prioritize_product_backlog("Implement feature A", 1)

    # Create a sprint
    sprint = project.create_sprint("Sprint 1", 14)

    # Add tasks to the sprint
    task1 = Task("Implement feature A", 8)
    task2 = Task("Implement feature B", 5)
    sprint.add_task(task1)
    sprint.add_task(task2)

    # Update the status of a task
    task1.update_status("In Progress")

    # Print the project and sprint information
    print(f"Project: {project.name}")
    print(f"Team Members: {project.team_members}")
    print(f"Product Backlog: {project.product_backlog}")
    print(f"Sprint: {sprint.name}")
    print(f"Duration: {sprint.duration} days")
    for task in sprint.tasks:
        print(f"Task: {task.name}, Estimate: {task.estimate}, Status: {task.status}")

if __name__ == "__main__":
    main()
```
