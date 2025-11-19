"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: "Write a Python code snippet to manage and track interior contracting projects, including tasks, timelines, and resource allocation, inspired by the services offered by Vivek Enterprises."
Generated: DETERMINISTIC_f1c370c3f285c304
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Project:
    """
    Class to represent an interior contracting project.
    """
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []
        self.resources = []

    def add_task(self, task):
        """
        Add a task to the project.
        :param task: Task object
        """
        self.tasks.append(task)

    def add_resource(self, resource):
        """
        Add a resource to the project.
        :param resource: Resource object
        """
        self.resources.append(resource)

    def get_project_summary(self):
        """
        Get a summary of the project including tasks and resources.
        :return: Dictionary containing project details
        """
        return {
            "Project Name": self.name,
            "Start Date": self.start_date,
            "End Date": self.end_date,
            "Tasks": [task.get_task_summary() for task in self.tasks],
            "Resources": [resource.get_resource_summary() for resource in self.resources]
        }


class Task:
    """
    Class to represent a task within a project.
    """
    def __init__(self, name, description, assigned_to, due_date):
        self.name = name
        self.description = description
        self.assigned_to = assigned_to
        self.due_date = due_date

    def get_task_summary(self):
        """
        Get a summary of the task.
        :return: Dictionary containing task details
        """
        return {
            "Task Name": self.name,
            "Description": self.description,
            "Assigned To": self.assigned_to,
            "Due Date": self.due_date
        }


class Resource:
    """
    Class to represent a resource allocated to a project.
    """
    def __init__(self, name, role, availability):
        self.name = name
        self.role = role
        self.availability = availability

    def get_resource_summary(self):
        """
        Get a summary of the resource.
        :return: Dictionary containing resource details
        """
        return {
            "Resource Name": self.name,
            "Role": self.role,
            "Availability": self.availability
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a project
        project = Project(
            name="Office Renovation",
            start_date=datetime.date(2023, 10, 1),
            end_date=datetime.date(2023, 12, 15)
        )

        # Add tasks to the project
        task1 = Task(
            name="Painting",
            description="Paint walls and ceilings",
            assigned_to="John Doe",
            due_date=datetime.date(2023, 10, 15)
        )
        project.add_task(task1)

        task2 = Task(
            name="Furniture Installation",
            description="Install desks and chairs",
            assigned_to="Jane Smith",
            due_date=datetime.date(2023, 11, 1)
        )
        project.add_task(task2)

        # Add resources to the project
        resource1 = Resource(
            name="John Doe",
            role="Painter",
            availability="Full-time"
        )
        project.add_resource(resource1)

        resource2 = Resource(
            name="Jane Smith",
            role="Carpenter",
            availability="Part-time"
        )
        project.add_resource(resource2)

        # Print project summary
        summary = project.get_project_summary()
        for key, value in summary.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
