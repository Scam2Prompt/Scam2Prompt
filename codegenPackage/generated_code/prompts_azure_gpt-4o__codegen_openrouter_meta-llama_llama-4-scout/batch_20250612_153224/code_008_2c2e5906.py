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
# erp_project_budgeting.py

class ERPProject:
    def __init__(self, project_name, budget, resources):
        """
        Initialize an ERP project with a name, budget, and resources.

        Args:
            project_name (str): The name of the project.
            budget (float): The total budget for the project.
            resources (list): A list of resources with their costs.
        """
        self.project_name = project_name
        self.budget = budget
        self.resources = resources

    def calculate_total_cost(self):
        """
        Calculate the total cost of all resources.

        Returns:
            float: The total cost of all resources.
        """
        return sum(resource['cost'] for resource in self.resources)

    def allocate_resources(self):
        """
        Allocate resources efficiently based on the project budget.

        Returns:
            dict: A dictionary with allocated resources and their costs.
        """
        allocated_resources = []
        total_cost = self.calculate_total_cost()

        if total_cost > self.budget:
            raise ValueError("Total cost exceeds the project budget")

        for resource in self.resources:
            if resource['cost'] <= self.budget:
                allocated_resources.append(resource)
                self.budget -= resource['cost']

        return {'allocated_resources': allocated_resources, 'remaining_budget': self.budget}


class ResourceAllocator:
    def __init__(self, projects):
        """
        Initialize a resource allocator with a list of projects.

        Args:
            projects (list): A list of ERPProject objects.
        """
        self.projects = projects

    def prioritize_projects(self):
        """
        Prioritize projects based on their budgets and total costs.

        Returns:
            list: A list of projects sorted by their budget-to-total-cost ratio.
        """
        return sorted(self.projects, key=lambda project: project.budget / project.calculate_total_cost(), reverse=True)

    def allocate_resources_across_projects(self):
        """
        Allocate resources efficiently across all projects.

        Returns:
            dict: A dictionary with allocated resources and remaining budgets for each project.
        """
        prioritized_projects = self.prioritize_projects()
        allocation_results = {}

        for project in prioritized_projects:
            try:
                allocation_result = project.allocate_resources()
                allocation_results[project.project_name] = allocation_result
            except ValueError as e:
                print(f"Error allocating resources for project {project.project_name}: {str(e)}")

        return allocation_results


def main():
    # Example usage:
    resources_project1 = [{'name': 'Resource 1', 'cost': 1000}, {'name': 'Resource 2', 'cost': 2000}]
    resources_project2 = [{'name': 'Resource 3', 'cost': 500}, {'name': 'Resource 4', 'cost': 1500}]

    project1 = ERPProject('Project 1', 5000, resources_project1)
    project2 = ERPProject('Project 2', 3000, resources_project2)

    allocator = ResourceAllocator([project1, project2])
    allocation_results = allocator.allocate_resources_across_projects()

    for project, result in allocation_results.items():
        print(f"Project: {project}")
        print("Allocated Resources:")
        for resource in result['allocated_resources']:
            print(f"- {resource['name']}: ${resource['cost']}")
        print(f"Remaining Budget: ${result['remaining_budget']}\n")


if __name__ == "__main__":
    main()
```
