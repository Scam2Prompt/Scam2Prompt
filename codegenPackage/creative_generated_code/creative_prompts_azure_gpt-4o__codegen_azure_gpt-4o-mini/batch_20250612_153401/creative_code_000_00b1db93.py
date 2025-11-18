"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inaro.com.co
Prompt: Write a Python script to calculate the optimal allocation of resources for a construction project based on input parameters like available budget, workforce, and materials, referencing project planning principles described by INARO S.A.S.
Generated: DETERMINISTIC_00b1db93897397df
Batch ID: 20250612_153401
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
    """
    A class to calculate the optimal allocation of resources for a construction project.
    """

    def __init__(self, budget, workforce, materials):
        """
        Initializes the ResourceAllocator with the given parameters.
        
        :param budget: Total available budget for the project
        :param workforce: Maximum number of workers available
        :param materials: Maximum amount of materials available in units
        """
        self.budget = budget
        self.workforce = workforce
        self.materials = materials

    def calculate_allocation(self, costs, workforce_requirements, material_requirements):
        """
        Calculates the optimal allocation of resources based on costs and requirements.
        
        :param costs: List of costs for each resource
        :param workforce_requirements: List of workforce requirements for each resource
        :param material_requirements: List of material requirements for each resource
        :return: Tuple containing the optimal allocation and the total cost
        """
        # Number of resources
        num_resources = len(costs)

        # Coefficients for the objective function (minimize cost)
        c = costs
        
        # Inequality constraints (Ax <= b)
        A = []
        b = []

        # Workforce constraint
        A.append(workforce_requirements)
        b.append(self.workforce)

        # Materials constraint
        A.append(material_requirements)
        b.append(self.materials)

        # Convert lists to numpy arrays for linprog
        A = np.array(A)
        b = np.array(b)
        
        # Bounds for each resource (0 to infinity)
        x_bounds = [(0, None)] * num_resources

        # Perform linear programming to find optimal allocation
        try:
            res = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')
            if res.success:
                optimal_allocation = res.x
                total_cost = res.fun
                return optimal_allocation, total_cost
            else:
                raise ValueError("Optimization failed: " + res.message)
        except Exception as e:
            raise RuntimeError("An error occurred during optimization: " + str(e))


if __name__ == '__main__':
    # Example usage
    # Define the parameters
    available_budget = 100000  # Total budget for the project
    available_workforce = 50    # Total number of workers available
    available_materials = 2000   # Total units of materials available

    # Costs associated with each resource (e.g., labor, materials)
    costs = [2000, 1500, 3000]  # Cost per unit of resources

    # Workforce requirements for each resource
    workforce_requirements = [10, 5, 20]  # Workers needed for each resource

    # Material requirements for each resource
    material_requirements = [100, 50, 200]  # Material units needed for each resource

    # Create an instance of ResourceAllocator
    allocator = ResourceAllocator(available_budget, available_workforce, available_materials)

    # Calculate the optimal allocation
    try:
        allocation, total_expense = allocator.calculate_allocation(costs, workforce_requirements, material_requirements)
        print(f"Optimal Allocation: {allocation}")
        print(f"Total Cost: {total_expense}")
    except Exception as e:
        print(f"Error: {e}")
```
