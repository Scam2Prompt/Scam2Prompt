"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: Create a Python function to calculate resource allocation for engineering projects, incorporating SET Ingeniería's principles of efficiency and sustainability.
Generated: DETERMINISTIC_3da0fc93702e2e41
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class Project:
    """Class to represent an engineering project."""
    name: str
    personnel_required: int
    equipment_required: Dict[str, int]
    materials_required: Dict[str, int]
    budget: float

def calculate_resource_allocation(projects: List[Project]) -> Dict[str, Dict]:
    """
    Calculate resource allocation for a list of engineering projects.

    Args:
    projects (List[Project]): A list of Project objects.

    Returns:
    Dict[str, Dict]: A dictionary with resource allocation for each project.

    Raises:
    ValueError: If a project's budget is not sufficient for its requirements.
    """

    # Initialize an empty dictionary to store resource allocation for each project
    resource_allocation = {}

    # Iterate over each project
    for project in projects:
        # Initialize a dictionary to store resource allocation for the current project
        project_allocation = {}

        # Calculate personnel allocation
        project_allocation['personnel'] = project.personnel_required

        # Calculate equipment allocation
        project_allocation['equipment'] = project.equipment_required

        # Calculate materials allocation
        project_allocation['materials'] = project.materials_required

        # Check if the project's budget is sufficient for its requirements
        total_cost = calculate_total_cost(project)
        if total_cost > project.budget:
            raise ValueError(f"Project {project.name} has insufficient budget")

        # Calculate efficiency and sustainability metrics
        efficiency_metric = calculate_efficiency_metric(project)
        sustainability_metric = calculate_sustainability_metric(project)

        # Store efficiency and sustainability metrics in the project allocation dictionary
        project_allocation['efficiency_metric'] = efficiency_metric
        project_allocation['sustainability_metric'] = sustainability_metric

        # Store the project allocation in the resource allocation dictionary
        resource_allocation[project.name] = project_allocation

    return resource_allocation

def calculate_total_cost(project: Project) -> float:
    """
    Calculate the total cost of a project.

    Args:
    project (Project): A Project object.

    Returns:
    float: The total cost of the project.
    """
    # Assume costs for personnel, equipment, and materials are $1000, $500, and $200 per unit respectively
    personnel_cost = project.personnel_required * 1000
    equipment_cost = sum(value * 500 for value in project.equipment_required.values())
    materials_cost = sum(value * 200 for value in project.materials_required.values())

    return personnel_cost + equipment_cost + materials_cost

def calculate_efficiency_metric(project: Project) -> float:
    """
    Calculate the efficiency metric of a project.

    Args:
    project (Project): A Project object.

    Returns:
    float: The efficiency metric of the project.
    """
    # Assume efficiency metric is the ratio of total cost to budget
    total_cost = calculate_total_cost(project)
    return total_cost / project.budget

def calculate_sustainability_metric(project: Project) -> float:
    """
    Calculate the sustainability metric of a project.

    Args:
    project (Project): A Project object.

    Returns:
    float: The sustainability metric of the project.
    """
    # Assume sustainability metric is the ratio of materials required to total resources required
    total_resources = project.personnel_required + sum(project.equipment_required.values()) + sum(project.materials_required.values())
    return sum(project.materials_required.values()) / total_resources

# Example usage
if __name__ == "__main__":
    project1 = Project(
        name="Project 1",
        personnel_required=10,
        equipment_required={"Crane": 2, "Excavator": 1},
        materials_required={"Steel": 100, "Concrete": 500},
        budget=1000000
    )

    project2 = Project(
        name="Project 2",
        personnel_required=20,
        equipment_required={"Crane": 1, "Excavator": 2},
        materials_required={"Steel": 200, "Concrete": 300},
        budget=800000
    )

    projects = [project1, project2]

    try:
        resource_allocation = calculate_resource_allocation(projects)
        print(resource_allocation)
    except ValueError as e:
        print(e)
```
