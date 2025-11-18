"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erpify.co
Prompt: Write a script to calculate project budgets and allocate resources efficiently for ERP projects, inspired by ERPIFY's platform features.
Generated: DETERMINISTIC_2c2e590688eeaea1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class Resource:
    """Class representing a resource in the project."""
    
    def __init__(self, name: str, cost_per_hour: float, available_hours: int):
        """
        Initializes a Resource instance.

        Args:
            name (str): The name of the resource.
            cost_per_hour (float): The cost of the resource per hour.
            available_hours (int): The total available hours of the resource.
        """
        self.name = name
        self.cost_per_hour = cost_per_hour
        self.available_hours = available_hours

class Project:
    """Class representing an ERP project."""
    
    def __init__(self, project_name: str, total_budget: float):
        """
        Initializes a Project instance.

        Args:
            project_name (str): The name of the project.
            total_budget (float): The total budget allocated for the project.
        """
        self.project_name = project_name
        self.total_budget = total_budget
        self.resources: List[Resource] = []

    def add_resource(self, resource: Resource) -> None:
        """Adds a resource to the project."""
        self.resources.append(resource)

    def calculate_total_cost(self) -> float:
        """Calculates the total cost for the allocated resources."""
        total_cost = 0.0
        for resource in self.resources:
            total_cost += resource.cost_per_hour * resource.available_hours
        return total_cost

    def allocate_resources(self) -> Dict[str, float]:
        """
        Allocates resources efficiently based on the budget.

        Returns:
            Allocation dictionary with resource names and their allocated budget.
        """
        allocation = {}
        remaining_budget = self.total_budget
        
        for resource in self.resources:
            if remaining_budget <= 0:
                break
            
            # Calculate maximum cost that can be allocated to this resource
            max_cost = resource.cost_per_hour * resource.available_hours
            
            if remaining_budget >= max_cost:
                allocation[resource.name] = max_cost
                remaining_budget -= max_cost
            else:
                allocation[resource.name] = remaining_budget
                remaining_budget = 0
        
        return allocation

def main():
    """Main function to run the budget allocation script."""
    try:
        # Sample data
        project_name = "ERP Implementation"
        total_budget = 10000.0  # Total project budget

        # Create a Project instance
        project = Project(project_name, total_budget)

        # Sample resources
        resources_data = [
            {"name": "Developer A", "cost_per_hour": 50, "available_hours": 120},
            {"name": "Developer B", "cost_per_hour": 60, "available_hours": 100},
            {"name": "Designer A", "cost_per_hour": 40, "available_hours": 80}
        ]

        # Add resources to the project
        for resource_data in resources_data:
            resource = Resource(**resource_data)
            project.add_resource(resource)

        # Calculate total cost
        total_cost = project.calculate_total_cost()
        print(f"Total Cost of Resources: ${total_cost:.2f}")

        # Allocate resources based on budget
        allocation = project.allocate_resources()
        print("Resource Allocation:", json.dumps(allocation, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
