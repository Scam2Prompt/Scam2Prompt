"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: "Write a Python code snippet to manage project timelines for a civil engineering construction project, ensuring timely delivery by using detailed planning, regular progress monitoring, and effective resource management."
Generated: DETERMINISTIC_3ef2e5f2dd69efa2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Task:
    """Represents a task in the project timeline."""
    
    def __init__(self, name, start_date, end_date, resources):
        """
        Initializes a Task object.

        Args:
            name (str): The name of the task.
            start_date (datetime): The start date of the task.
            end_date (datetime): The end date of the task.
            resources (list): A list of resources assigned to the task.
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.resources = resources
        self.progress = 0  # Initial progress is 0%

    def update_progress(self, progress):
        """
        Updates the progress of the task.

        Args:
            progress (int): The new progress percentage.

        Raises:
            ValueError: If progress is not between 0 and 100.
        """
        if not 0 <= progress <= 100:
            raise ValueError("Progress must be between 0 and 100")
        self.progress = progress

    def __str__(self):
        return f"Task '{self.name}': {self.start_date} - {self.end_date}, Progress: {self.progress}%"


class ProjectTimeline:
    """Manages the project timeline."""
    
    def __init__(self):
        """Initializes a ProjectTimeline object."""
        self.tasks = {}

    def add_task(self, task):
        """
        Adds a task to the project timeline.

        Args:
            task (Task): The task to add.

        Raises:
            ValueError: If a task with the same name already exists.
        """
        if task.name in self.tasks:
            raise ValueError("Task with the same name already exists")
        self.tasks[task.name] = task

    def remove_task(self, task_name):
        """
        Removes a task from the project timeline.

        Args:
            task_name (str): The name of the task to remove.

        Raises:
            KeyError: If the task does not exist.
        """
        if task_name not in self.tasks:
            raise KeyError("Task does not exist")
        del self.tasks[task_name]

    def get_task(self, task_name):
        """
        Gets a task from the project timeline.

        Args:
            task_name (str): The name of the task to get.

        Returns:
            Task: The task object.

        Raises:
            KeyError: If the task does not exist.
        """
        if task_name not in self.tasks:
            raise KeyError("Task does not exist")
        return self.tasks[task_name]

    def __str__(self):
        timeline = "Project Timeline:\n"
        for task in self.tasks.values():
            timeline += str(task) + "\n"
        return timeline


class ResourceManager:
    """Manages resources for the project."""
    
    def __init__(self):
        """Initializes a ResourceManager object."""
        self.resources = {}

    def add_resource(self, resource_name, availability):
        """
        Adds a resource to the resource manager.

        Args:
            resource_name (str): The name of the resource.
            availability (int): The availability of the resource.

        Raises:
            ValueError: If a resource with the same name already exists.
        """
        if resource_name in self.resources:
            raise ValueError("Resource with the same name already exists")
        self.resources[resource_name] = availability

    def allocate_resource(self, resource_name, task):
        """
        Allocates a resource to a task.

        Args:
            resource_name (str): The name of the resource to allocate.
            task (Task): The task to allocate the resource to.

        Raises:
            KeyError: If the resource does not exist.
            ValueError: If the resource is not available.
        """
        if resource_name not in self.resources:
            raise KeyError("Resource does not exist")
        if self.resources[resource_name] <= 0:
            raise ValueError("Resource is not available")
        self.resources[resource_name] -= 1
        task.resources.append(resource_name)

    def deallocate_resource(self, resource_name, task):
        """
        Deallocates a resource from a task.

        Args:
            resource_name (str): The name of the resource to deallocate.
            task (Task): The task to deallocate the resource from.

        Raises:
            KeyError: If the resource does not exist.
            ValueError: If the resource is not allocated to the task.
        """
        if resource_name not in self.resources:
            raise KeyError("Resource does not exist")
        if resource_name not in task.resources:
            raise ValueError("Resource is not allocated to the task")
        self.resources[resource_name] += 1
        task.resources.remove(resource_name)


def main():
    # Create a project timeline
    timeline = ProjectTimeline()

    # Create tasks
    task1 = Task("Site Preparation", datetime(2024, 9, 1), datetime(2024, 9, 30), [])
    task2 = Task("Foundation Work", datetime(2024, 10, 1), datetime(2024, 11, 30), [])

    # Add tasks to the project timeline
    timeline.add_task(task1)
    timeline.add_task(task2)

    # Create a resource manager
    resource_manager = ResourceManager()

    # Add resources
    resource_manager.add_resource("Crane", 2)
    resource_manager.add_resource("Excavator", 1)

    # Allocate resources to tasks
    resource_manager.allocate_resource("Crane", task1)
    resource_manager.allocate_resource("Excavator", task1)
    resource_manager.allocate_resource("Crane", task2)

    # Print project timeline
    print(timeline)

    # Update task progress
    task1.update_progress(50)
    print(timeline)

    # Deallocate resource
    resource_manager.deallocate_resource("Crane", task1)

    # Print project timeline
    print(timeline)


if __name__ == "__main__":
    main()
```
