"""
Generated Code Metadata:
========================
Original URL: https://safarait.com
Prompt: Create a sample project plan for a corporate marketing site using Safara IT's web design services.
Generated: DETERMINISTIC_b30b3023bff374ee
Batch ID: 20250612_155200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Sample Project Plan for Corporate Marketing Site
# Using Safara IT's Web Design Services

class ProjectPlan:
    def __init__(self, project_name, client_name, start_date, end_date):
        """
        Initializes the project plan with basic details.

        :param project_name: Name of the project
        :param client_name: Name of the client
        :param start_date: Project start date
        :param end_date: Project end date
        """
        self.project_name = project_name
        self.client_name = client_name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []

    def add_task(self, task_name, assigned_to, due_date, status='Pending'):
        """
        Adds a task to the project plan.

        :param task_name: Name of the task
        :param assigned_to: Person assigned to the task
        :param due_date: Due date for the task
        :param status: Current status of the task (default is 'Pending')
        """
        task = {
            'task_name': task_name,
            'assigned_to': assigned_to,
            'due_date': due_date,
            'status': status
        }
        self.tasks.append(task)

    def update_task_status(self, task_name, new_status):
        """
        Updates the status of a specific task.

        :param task_name: Name of the task to update
        :param new_status: New status to set for the task
        :raises ValueError: If the task is not found
        """
        for task in self.tasks:
            if task['task_name'] == task_name:
                task['status'] = new_status
                return
        raise ValueError(f"Task '{task_name}' not found.")

    def display_plan(self):
        """
        Displays the project plan details including tasks.
        """
        print(f"Project Name: {self.project_name}")
        print(f"Client Name: {self.client_name}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print("\nTasks:")
        for task in self.tasks:
            print(f" - {task['task_name']} (Assigned to: {task['assigned_to']}, Due: {task['due_date']}, Status: {task['status']})")

# Example usage
if __name__ == "__main__":
    try:
        # Create a new project plan
        project = ProjectPlan("Corporate Marketing Site", "Safara IT", "2023-10-01", "2024-01-01")

        # Add tasks to the project plan
        project.add_task("Initial Design Mockup", "Alice", "2023-10-15")
        project.add_task("Client Review", "Bob", "2023-10-20")
        project.add_task("Development Phase", "Charlie", "2023-11-01")
        project.add_task("Testing Phase", "Diana", "2023-12-01")
        project.add_task("Launch", "Eve", "2024-01-01")

        # Update a task status
        project.update_task_status("Client Review", "Completed")

        # Display the project plan
        project.display_plan()

    except Exception as e:
        print(f"An error occurred: {e}")
```
