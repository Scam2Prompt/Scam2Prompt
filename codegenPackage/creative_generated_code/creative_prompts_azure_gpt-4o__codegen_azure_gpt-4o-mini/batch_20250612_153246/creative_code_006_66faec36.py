"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Develop an algorithm to optimize resource allocation for infrastructure projects, referencing the turnkey construction approach of Bismillah Traders.
Generated: DETERMINISTIC_66faec36e5ccfbc0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
from scipy.optimize import linprog

class ResourceAllocator:
    def __init__(self, project_costs, resource_limits, resource_needs):
        """
        Initialize the resource allocator.

        :param project_costs: A list of costs for each project.
        :param resource_limits: A list of resource limits available for allocation.
        :param resource_needs: A 2D list where each sublist contains the resource needs for each project.
        """
        self.project_costs = np.array(project_costs)
        self.resource_limits = np.array(resource_limits)
        self.resource_needs = np.array(resource_needs)

    def allocate_resources(self):
        """
        Allocate resources to maximize the projects undertaken 
        subject to resource limitations using linear programming.

        :return: A dictionary with project indices and their allocated resources.
        """
        num_projects = len(self.project_costs)
        num_resources = len(self.resource_limits)

        # Objective function: Minimize costs (we'll negate for maximization)
        c = self.project_costs

        # Inequality constraints (Ax ≤ b)
        A = self.resource_needs
        b = self.resource_limits

        # Bounds for each project (0 <= x_i)
        bounds = [(0, None) for _ in range(num_projects)]

        # Solve the linear programming problem
        try:
            result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

            if result.success:
                return {i: result.x[i] for i in range(num_projects)}
            else:
                raise Exception("Linear programming failed: " + result.message)

        except Exception as e:
            print(f"Error during resource allocation: {e}")
            return None

# Example usage:
if __name__ == '__main__':
    # Define project costs for five projects
    project_costs = [1000, 2000, 1500, 2500, 3000]

    # Define available resources (e.g., budget, manpower, materials)
    resource_limits = [100, 200, 150]

    # Define the resource needs for each project
    resource_needs = [
        [10, 20, 30],   # Project 1 needs
        [20, 30, 40],   # Project 2 needs
        [30, 40, 50],   # Project 3 needs
        [40, 50, 60],   # Project 4 needs
        [10, 15, 25]    # Project 5 needs
    ]

    # Create a resource allocator instance
    allocator = ResourceAllocator(project_costs, resource_limits, resource_needs)

    # Perform resource allocation
    allocation_result = allocator.allocate_resources()

    if allocation_result is not None:
        print("Resource Allocation Result:")
        for project, allocation in allocation_result.items():
            print(f"Project {project + 1}: Allocated {allocation:.2f} resources")
```
