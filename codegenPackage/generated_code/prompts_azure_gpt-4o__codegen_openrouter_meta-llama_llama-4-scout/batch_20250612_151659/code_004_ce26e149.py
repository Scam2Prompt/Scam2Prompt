"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Suggest a Python library for optimizing resource allocation in heavy construction projects, considering MGEL's emphasis on quality and punctuality.
Generated: DETERMINISTIC_ce26e149051ec7f0
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np
from scipy.optimize import linear_sum_assignment
from typing import List, Dict

class ResourceAllocator:
    """
    A class to optimize resource allocation in heavy construction projects.

    Attributes:
    -----------
    resources : List[str]
        A list of available resources.
    tasks : List[str]
        A list of tasks to be allocated.
    cost_matrix : np.ndarray
        A 2D array representing the cost of allocating each resource to each task.

    Methods:
    --------
    allocate_resources() -> Dict[str, str]
        Allocates resources to tasks using the Hungarian Algorithm.
    """

    def __init__(self, resources: List[str], tasks: List[str], cost_matrix: List[List[float]]):
        """
        Initializes the ResourceAllocator class.

        Args:
        -----
        resources (List[str]): A list of available resources.
        tasks (List[str]): A list of tasks to be allocated.
        cost_matrix (List[List[float]]): A 2D array representing the cost of allocating each resource to each task.
        """
        self.resources = resources
        self.tasks = tasks
        self.cost_matrix = np.array(cost_matrix)

    def allocate_resources(self) -> Dict[str, str]:
        """
        Allocates resources to tasks using the Hungarian Algorithm.

        Returns:
        -------
        Dict[str, str]: A dictionary mapping resources to tasks.
        """
        try:
            # Use the Hungarian Algorithm to find the optimal allocation
            row_ind, col_ind = linear_sum_assignment(self.cost_matrix)

            # Create a dictionary mapping resources to tasks
            allocation = {self.resources[i]: self.tasks[j] for i, j in zip(row_ind, col_ind)}

            return allocation

        except Exception as e:
            # Handle any exceptions that occur during allocation
            print(f"An error occurred: {e}")
            return {}

def main():
    # Example usage
    resources = ["Crane", "Excavator", "Bulldozer"]
    tasks = ["Demolition", "Excavation", "Grading"]
    cost_matrix = [
        [10, 15, 20],
        [12, 10, 18],
        [15, 18, 12]
    ]

    allocator = ResourceAllocator(resources, tasks, cost_matrix)
    allocation = allocator.allocate_resources()

    print("Optimal Resource Allocation:")
    for resource, task in allocation.items():
        print(f"{resource}: {task}")

if __name__ == "__main__":
    main()
```
