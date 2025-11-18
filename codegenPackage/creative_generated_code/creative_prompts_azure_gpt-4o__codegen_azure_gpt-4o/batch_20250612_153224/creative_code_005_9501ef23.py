"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillah-traders.com
Prompt: Develop a Python program to optimize resource allocation for a design-build construction project, based on the single-point-of-contact delivery model mentioned on the Bismillah Traders website.
Generated: DETERMINISTIC_9501ef23367da113
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class ResourceAllocator:
    """
    A class to optimize resource allocation for a design-build construction project.
    Follows the single-point-of-contact delivery model.
    """

    def __init__(self, resources, tasks, resource_constraints):
        """
        Initialize the allocator with available resources, tasks, and constraints.

        :param resources: A dictionary of available resources with their capacities.
                          Example: {"Labor": 50, "Machinery": 10, "Material": 100}
        :param tasks: A list of tasks with required resources for each task.
                      Example: [{"Task": "Foundation", "Labor": 20, "Machinery": 5, "Material": 30}]
        :param resource_constraints: A dictionary of constraints on resources.
                                      Example: {"Labor": 60, "Machinery": 15, "Material": 120}
        """
        self.resources = resources
        self.tasks = tasks
        self.resource_constraints = resource_constraints

    def validate_inputs(self):
        """
        Validate input data and constraints.
        Raises ValueError if inputs are invalid.
        """
        for resource, capacity in self.resources.items():
            if resource not in self.resource_constraints:
                raise ValueError(f"Resource '{resource}' is missing constraints.")
            if capacity > self.resource_constraints[resource]:
                raise ValueError(f"Resource '{resource}' exceeds its constraint capacity.")

        for task in self.tasks:
            for resource in self.resources.keys():
                if resource not in task:
                    raise ValueError(f"Task '{task['Task']}' is missing required resource '{resource}'.")

    def allocate_resources(self):
        """
        Optimize resource allocation across tasks.
        
        :return: Pandas DataFrame containing optimal allocation.
        """
        allocation = []
        remaining_resources = self.resources.copy()

        for task in self.tasks:
            task_allocation = {"Task": task["Task"]}
            for resource, required_amount in task.items():
                if resource == "Task":
                    continue

                # Check resource availability and allocate
                if resource in remaining_resources and required_amount <= remaining_resources[resource]:
                    task_allocation[resource] = required_amount
                    remaining_resources[resource] -= required_amount
                else:
                    task_allocation[resource] = 0  # Unable to allocate due to constraints

            allocation.append(task_allocation)
        
        return pd.DataFrame(allocation)

    def run_optimizer(self):
        """
        Execute the optimization workflow.

        :return: Pandas DataFrame containing the optimal allocation plan.
        """
        try:
            self.validate_inputs()
            print("Input validation successful.")
            optimal_allocation = self.allocate_resources()
            print("Resource allocation completed.")
            return optimal_allocation
        except ValueError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Define available resources and constraints
    resources = {"Labor": 50, "Machinery": 10, "Material": 100}
    resource_constraints = {"Labor": 60, "Machinery": 15, "Material": 120}

    # Define tasks with resource requirements
    tasks = [
        {"Task": "Foundation", "Labor": 20, "Machinery": 5, "Material": 30},
        {"Task": "Framing", "Labor": 30, "Machinery": 5, "Material": 50},
        {"Task": "Roofing", "Labor": 10, "Machinery": 4, "Material": 20}
    ]

    # Instantiate the ResourceAllocator
    allocator = ResourceAllocator(resources, tasks, resource_constraints)

    # Run the optimizer and print the allocation result
    allocation_result = allocator.run_optimizer()
    if allocation_result is not None:
        print("\nOptimal Resource Allocation:")
        print(allocation_result)
```
