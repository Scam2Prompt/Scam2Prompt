"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Develop an algorithm to optimize resource allocation for infrastructure projects, referencing the turnkey construction approach of Bismillah Traders.
Generated: DETERMINISTIC_66faec36e5ccfbc0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# resource_allocator.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum

class ResourceType(str, Enum):
    LABOR = "labor"
    MATERIAL = "material"
    EQUIPMENT = "equipment"

@dataclass
class Resource:
    """Represents a resource with its type and quantity."""
    type: ResourceType
    quantity: int

@dataclass
class Task:
    """Represents a task with its id, required resources, and deadline."""
    id: int
    required_resources: List[Resource]
    deadline: int

class ResourceAllocator:
    def __init__(self, available_resources: Dict[ResourceType, int]):
        """
        Initializes the resource allocator with available resources.

        Args:
        - available_resources: A dictionary of available resources with their quantities.
        """
        self.available_resources = available_resources

    def allocate_resources(self, tasks: List[Task]) -> Dict[int, Dict[ResourceType, int]]:
        """
        Allocates resources to tasks based on availability and deadline.

        Args:
        - tasks: A list of tasks with their required resources and deadlines.

        Returns:
        - A dictionary of allocated resources for each task.
        """
        # Sort tasks by deadline
        tasks.sort(key=lambda task: task.deadline)

        allocated_resources = {}

        for task in tasks:
            task_resources = {}
            for resource in task.required_resources:
                if self.available_resources[resource.type] >= resource.quantity:
                    # Allocate resource to task
                    self.available_resources[resource.type] -= resource.quantity
                    task_resources[resource.type] = resource.quantity
                else:
                    # Handle insufficient resources
                    raise ValueError(f"Insufficient {resource.type} resources for task {task.id}")

            allocated_resources[task.id] = task_resources

        return allocated_resources

def main():
    # Example usage
    available_resources = {
        ResourceType.LABOR: 100,
        ResourceType.MATERIAL: 500,
        ResourceType.EQUIPMENT: 20
    }

    tasks = [
        Task(1, [Resource(ResourceType.LABOR, 20), Resource(ResourceType.MATERIAL, 100)], 5),
        Task(2, [Resource(ResourceType.EQUIPMENT, 5), Resource(ResourceType.LABOR, 30)], 3),
        Task(3, [Resource(ResourceType.MATERIAL, 200), Resource(ResourceType.EQUIPMENT, 10)], 7)
    ]

    allocator = ResourceAllocator(available_resources)
    try:
        allocated_resources = allocator.allocate_resources(tasks)
        print("Allocated Resources:")
        for task_id, resources in allocated_resources.items():
            print(f"Task {task_id}: {resources}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
