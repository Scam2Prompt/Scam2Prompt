"""
Generated Code Metadata:
========================
Original URL: https://erpify.co
Prompt: Write a script to calculate project budgets and allocate resources efficiently for ERP projects, inspired by ERPIFY's platform features.
Generated: DETERMINISTIC_2c2e590688eeaea1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class Resource:
    """Class representing a resource in the project."""
    
    def __init__(self, name: str, cost_per_hour: float, availability: int):
        """
        Initialize a resource with a name, cost per hour, and availability in hours.
        
        :param name: Name of the resource
        :param cost_per_hour: Cost of the resource per hour
        :param availability: Total available hours for the resource
        """
        self.name = name
        self.cost_per_hour = cost_per_hour
        self.availability = availability

class Project:
    """Class representing a project with a budget and resources."""
    
    def __init__(self, name: str, budget: float):
        """
        Initialize a project with a name and budget.
        
        :param name: Name of the project
        :param budget: Total budget for the project
        """
        self.name = name
        self.budget = budget
        self.resources: List[Resource] = []
    
    def add_resource(self, resource: Resource):
        """
        Add a resource to the project.
        
        :param resource: Resource to be added
        """
        self.resources.append(resource)
    
    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of all resources allocated to the project.
        
        :return: Total cost of resources
        """
        total_cost = sum(resource.cost_per_hour * resource.availability for resource in self.resources)
        return total_cost
    
    def allocate_resources(self) -> Dict[str, float]:
        """
        Allocate resources based on the project budget.
        
        :return: A dictionary with resource names and their allocated hours
        """
        allocation = {}
        total_cost = self.calculate_total_cost()
        
        if total_cost > self.budget:
            raise ValueError("Total cost exceeds project budget.")
        
        for resource in self.resources:
            allocated_hours = min(resource.availability, self.budget / resource.cost_per_hour)
            allocation[resource.name] = allocated_hours
            self.budget -= allocated_hours * resource.cost_per_hour
            
            if self.budget <= 0:
                break
        
        return allocation

def main():
    """Main function to execute the budget calculation and resource allocation."""
    try:
        # Example project setup
        project = Project(name="ERP Implementation", budget=10000.0)
        
        # Adding resources
        project.add_resource(Resource(name="Developer", cost_per_hour=50.0, availability=160))
        project.add_resource(Resource(name="Designer", cost_per_hour=40.0, availability=80))
        project.add_resource(Resource(name="Project Manager", cost_per_hour=60.0, availability=100))
        
        # Calculate total cost
        total_cost = project.calculate_total_cost()
        print(f"Total cost of resources: ${total_cost:.2f}")
        
        # Allocate resources
        allocation = project.allocate_resources()
        print("Resource allocation:", json.dumps(allocation, indent=4))
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
