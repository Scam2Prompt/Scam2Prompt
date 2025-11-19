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
import numpy as np
from scipy.optimize import linprog
from typing import List, Dict, Tuple

class ResourceAllocator:
    """
    Optimizes resource allocation for infrastructure projects using linear programming.
    Implements a turnkey construction approach similar to Bismillah Traders.
    """
    
    def __init__(self, resources: Dict[str, int], projects: List[Dict]):
        """
        Initialize the allocator with available resources and project requirements.
        
        Args:
            resources: Dictionary of available resources (e.g., {'labor': 100, 'cement': 500})
            projects: List of project dictionaries with requirements and profits
                     (e.g., [{'name': 'Project1', 'requirements': {'labor': 2, 'cement': 5}, 'profit': 10}])
        """
        self.resources = resources
        self.projects = projects
        self.resource_names = sorted(resources.keys())
        self.project_names = [p['name'] for p in projects]
        
    def _build_coefficients(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Build matrices for linear programming problem.
        
        Returns:
            Tuple of (A_ub, b_ub, c) where:
            - A_ub: Resource coefficient matrix (inequality constraints)
            - b_ub: Available resource limits
            - c: Profit coefficients for objective function
        """
        num_projects = len(self.projects)
        num_resources = len(self.resource_names)
        
        # Initialize matrices
        A_ub = np.zeros((num_resources, num_projects))
        b_ub = np.zeros(num_resources)
        c = np.zeros(num_projects)
        
        # Fill resource constraints (A_ub and b_ub)
        for res_idx, res_name in enumerate(self.resource_names):
            b_ub[res_idx] = self.resources[res_name]
            for proj_idx, project in enumerate(self.projects):
                A_ub[res_idx, proj_idx] = project['requirements'].get(res_name, 0)
        
        # Fill profit coefficients (c)
        for proj_idx, project in enumerate(self.projects):
            c[proj_idx] = -project['profit']  # Negative for maximization
            
        return A_ub, b_ub, c
    
    def optimize(self) -> Dict:
        """
        Optimize resource allocation using linear programming.
        
        Returns:
            Dictionary containing:
            - 'allocation': Optimal project allocations
            - 'total_profit': Maximum achievable profit
            - 'status': Optimization status
            - 'resource_usage': Resource utilization
        """
        try:
            A_ub, b_ub, c = self._build_coefficients()
            
            # Solve linear programming problem
            result = linprog(
                c=c,
                A_ub=A_ub,
                b_ub=b_ub,
                bounds=(0, None),  # Projects can't be negative
                method='highs'
            )
            
            if not result.success:
                raise ValueError(f"Optimization failed: {result.message}")
            
            # Prepare results
            allocation = {
                self.project_names[i]: round(x, 2)
                for i, x in enumerate(result.x)
            }
            
            resource_usage = {
                res_name: sum(
                    allocation[proj['name']] * proj['requirements'].get(res_name, 0)
                    for proj in self.projects
                )
                for res_name in self.resource_names
            }
            
            return {
                'allocation': allocation,
                'total_profit': round(-result.fun, 2),  # Convert back to positive
                'status': result.message,
                'resource_usage': resource_usage
            }
            
        except Exception as e:
            return {
                'error': str(e),
                'status': 'failed'
            }
    
    @staticmethod
    def validate_inputs(resources: Dict, projects: List[Dict]) -> bool:
        """
        Validate input data for the optimizer.
        
        Args:
            resources: Dictionary of available resources
            projects: List of project dictionaries
            
        Returns:
            bool: True if inputs are valid, False otherwise
        """
        if not isinstance(resources, dict) or not resources:
            return False
            
        if not isinstance(projects, list) or not projects:
            return False
            
        for project in projects:
            if not isinstance(project, dict):
                return False
            if 'name' not in project or 'requirements' not in project or 'profit' not in project:
                return False
            if not isinstance(project['requirements'], dict):
                return False
                
        return True


# Example usage
if __name__ == "__main__":
    # Define available resources
    resources = {
        'labor': 1000,  # man-hours
        'cement': 500,  # tons
        'steel': 200    # tons
    }
    
    # Define projects with requirements and profits
    projects = [
        {
            'name': 'Residential Complex',
            'requirements': {'labor': 5, 'cement': 2, 'steel': 1},
            'profit': 10  # in million dollars
        },
        {
            'name': 'Commercial Tower',
            'requirements': {'labor': 8, 'cement': 3, 'steel': 2},
            'profit': 15
        },
        {
            'name': 'Bridge',
            'requirements': {'labor': 10, 'cement': 1, 'steel': 5},
            'profit': 20
        }
    ]
    
    # Validate inputs
    if not ResourceAllocator.validate_inputs(resources, projects):
        print("Invalid input data")
    else:
        # Optimize allocation
        allocator = ResourceAllocator(resources, projects)
        result = allocator.optimize()
        
        if 'error' in result:
            print(f"Error: {result['error']}")
        else:
            print("Optimal Project Allocation:")
            for project, amount in result['allocation'].items():
                print(f"- {project}: {amount} units")
            
            print(f"\nTotal Profit: ${result['total_profit']} million")
            print(f"\nResource Usage:")
            for resource, usage in result['resource_usage'].items():
                print(f"- {resource}: {usage} / {resources[resource]}")
            
            print(f"\nStatus: {result['status']}")
```
