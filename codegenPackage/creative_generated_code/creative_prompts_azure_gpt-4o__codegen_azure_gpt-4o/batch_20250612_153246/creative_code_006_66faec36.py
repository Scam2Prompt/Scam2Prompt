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

Here's the Python code for optimizing resource allocation for infrastructure projects.

```python
import numpy as np

class ResourceAllocationOptimizer:
    """
    Class to optimize resource allocation for infrastructure projects using 
    a cost-effective and turnkey approach.
    """

    def __init__(self, resource_matrix, project_requirements, budget):
        """
        Initialize the optimizer with resource data, project requirements, and budget.

        :param resource_matrix: 2D list where each row represents a resource 
                                and columns represent cost and availability.
        :param project_requirements: List of required quantities for each resource.
        :param budget: Total budget allocated for the project.
        """
        self.resource_matrix = np.array(resource_matrix)
        self.project_requirements = np.array(project_requirements)
        self.budget = budget

    def validate_inputs(self):
        """
        Validates the dimensions of resource_matrix and project_requirements.
        """
        if self.resource_matrix.shape[0] != len(self.project_requirements):
            raise ValueError("Resource matrix and project requirements dimensions do not match.")

    def optimize_allocation(self):
        """
        Optimize resource allocation based on project requirements and budget.

        :return: Dictionary with optimized allocation details.
        """
        # Sort resources by cost per unit (ascending order)
        cost_per_unit = self.resource_matrix[:, 0] / self.resource_matrix[:, 1]
        sorted_indices = np.argsort(cost_per_unit)
        sorted_resources = self.resource_matrix[sorted_indices]
        sorted_requirements = self.project_requirements[sorted_indices]

        allocation = []
        total_cost = 0

        # Allocate resources within the budget
        for i in range(len(sorted_resources)):
            if sorted_requirements[i] <= sorted_resources[i][1]:  # Check availability
                required_units = sorted_requirements[i]
            else:
                required_units = sorted_resources[i][1]  # Use available units only

            cost_for_current_resource = required_units * sorted_resources[i][0]
            if total_cost + cost_for_current_resource <= self.budget:
                allocation.append(required_units)
                total_cost += cost_for_current_resource
            else:
                # Allocate as much as possible within the remaining budget
                remaining_budget = self.budget - total_cost
                max_possible_units = remaining_budget // sorted_resources[i][0]
                allocation.append(max_possible_units)
                total_cost += max_possible_units * sorted_resources[i][0]
                break

        # Fill remaining allocation with 0s for unutilized resources
        while len(allocation) < len(sorted_resources):
            allocation.append(0)

        # Map allocation back to original order
        original_order_allocation = [0] * len(sorted_resources)
        for i, index in enumerate(sorted_indices):
            original_order_allocation[index] = allocation[i]

        return {
            "allocation": original_order_allocation,
            "total_cost": total_cost
        }


# Example usage
if __name__ == "__main__":
    # Define resource matrix: [cost per unit, availability]
    resources = [
        [10, 100],  # Resource 1: $10 per unit, 100 units available
        [5, 50],    # Resource 2: $5 per unit, 50 units available
        [20, 200]   # Resource 3: $20 per unit, 200 units available
    ]

    # Define project requirements for each resource
    requirements = [80, 40, 150]

    # Define total budget for the project
    budget = 1500

    try:
        optimizer = ResourceAllocationOptimizer(resources, requirements, budget)
        optimizer.validate_inputs()
        result = optimizer.optimize_allocation()
        print("Optimized Allocation:", result["allocation"])
        print("Total Cost:", result["total_cost"])
    except ValueError as e:
        print("Input Error:", str(e))
    except Exception as e:
        print("An unexpected error occurred:", str(e))
```

This code is a production-ready implementation for optimizing resource allocation. It handles input validation, sorts resources by cost-efficiency, and allocates them within the given budget.
