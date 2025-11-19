"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itls-iso.com
Prompt: Can you provide a code example that integrates iTLS concepts into a project management tool for better resource optimization?
Generated: DETERMINISTIC_bb40b56dfed3f209
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Resource:
    """
    Represents a resource in the project management tool.
    Attributes:
        name (str): The name of the resource.
        availability (float): The availability of the resource in hours.
    """

    def __init__(self, name: str, availability: float):
        self.name = name
        self.availability = availability

    def __repr__(self):
        return f"Resource(name={self.name}, availability={self.availability})"


class Task:
    """
    Represents a task in the project.
    Attributes:
        name (str): The name of the task.
        duration (float): The duration of the task in hours.
        assigned_resource (Resource): The resource assigned to the task.
    """

    def __init__(self, name: str, duration: float):
        self.name = name
        self.duration = duration
        self.assigned_resource = None

    def assign_resource(self, resource: Resource):
        """
        Assign a resource to the task if it's available.
        Args:
            resource (Resource): The resource to assign.
        Raises:
            ValueError: If the resource is not available for the required duration.
        """
        if resource.availability < self.duration:
            raise ValueError(f"Resource {resource.name} does not have enough availability.")
        self.assigned_resource = resource
        resource.availability -= self.duration

    def __repr__(self):
        return f"Task(name={self.name}, duration={self.duration}, assigned_resource={self.assigned_resource})"


class Project:
    """
    Represents a project that consists of multiple tasks and resources.
    Attributes:
        name (str): The name of the project.
        tasks (list): A list of tasks in the project.
        resources (list): A list of available resources.
    """

    def __init__(self, name: str):
        self.name = name
        self.tasks = []
        self.resources = []

    def add_task(self, task: Task):
        """
        Add a new task to the project.
        Args:
            task (Task): The task to add.
        """
        self.tasks.append(task)

    def add_resource(self, resource: Resource):
        """
        Add a new resource to the project.
        Args:
            resource (Resource): The resource to add.
        """
        self.resources.append(resource)

    def optimize_resources(self):
        """
        Optimizes the allocation of resources to tasks for better efficiency.
        This method iterates over all tasks and attempts to assign resources
        based on availability.
        """
        for task in self.tasks:
            for resource in self.resources:
                if task.assigned_resource is None:
                    try:
                        task.assign_resource(resource)
                        print(f"Assigned {resource.name} to task {task.name}.")
                    except ValueError:
                        pass  # Resource not available, continue to next resource

    def __repr__(self):
        return f"Project(name={self.name}, tasks={self.tasks}, resources={self.resources})"


# Example usage
if __name__ == "__main__":
    # Create a project
    project = Project("Website Development")

    # Create resources
    resource1 = Resource("Alice", 40)
    resource2 = Resource("Bob", 30)

    # Add resources to the project
    project.add_resource(resource1)
    project.add_resource(resource2)

    # Create tasks
    task1 = Task("Design", 20)
    task2 = Task("Development", 50)
    task3 = Task("Testing", 15)

    # Add tasks to the project
    project.add_task(task1)
    project.add_task(task2)
    project.add_task(task3)

    # Optimize resource allocation
    project.optimize_resources()

    # Display project status
    print(project)
```
