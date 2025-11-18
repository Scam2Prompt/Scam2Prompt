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
"""
Optimal Resource Allocation for Construction Project

This script calculates the optimal allocation of resources (budget, workforce, and materials)
for a construction project based on input parameters. It uses project planning principles
and ensures efficient utilization of resources while adhering to constraints.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import json
import sys

class ResourceAllocationError(Exception):
    """Custom exception for resource allocation errors."""
    pass

def optimal_allocation(budget, workforce, materials, project_details):
    """
    Calculate optimal resource allocation for a construction project.

    Parameters:
        budget (float): The total budget available for the project.
        workforce (int): The number of workers available for the project.
        materials (dict): Dictionary of materials and their quantities/costs.
        project_details (dict): Dictionary containing project-specific data
                                like task priorities, deadlines, etc.

    Returns:
        dict: Optimal allocation of resources.

    Raises:
        ResourceAllocationError: If constraints are violated.
    """
    try:
        # Validate inputs
        if budget <= 0:
            raise ResourceAllocationError("Budget must be greater than zero.")
        if workforce <= 0:
            raise ResourceAllocationError("Workforce must be greater than zero.")
        if not isinstance(materials, dict) or not materials:
            raise ResourceAllocationError("Materials must be a non-empty dictionary.")
        if not isinstance(project_details, dict) or not project_details:
            raise ResourceAllocationError("Project details must be provided as a dictionary.")

        # Example allocation logic (simplified for demonstration purposes)
        allocation = {
            "budget_allocation": {},
            "workforce_allocation": {},
            "material_allocation": {},
        }

        # Allocate budget based on tasks and priorities
        tasks = project_details.get("tasks", [])
        total_priority = sum(task["priority"] for task in tasks)
        for task in tasks:
            priority_share = task["priority"] / total_priority
            allocation["budget_allocation"][task["name"]] = round(budget * priority_share, 2)

        # Allocate workforce equally among tasks
        workers_per_task = workforce // len(tasks)
        for task in tasks:
            allocation["workforce_allocation"][task["name"]] = workers_per_task

        # Allocate materials based on task requirements
        for task in tasks:
            required_materials = task.get("required_materials", {})
            allocation["material_allocation"][task["name"]] = {}
            for material, required_qty in required_materials.items():
                if material in materials and materials[material] >= required_qty:
                    allocation["material_allocation"][task["name"]][material] = required_qty
                else:
                    raise ResourceAllocationError(f"Not enough {material} available for {task['name']}.")

        return allocation

    except ResourceAllocationError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


def main():
    """
    Entry point of the script. Collects inputs, calculates allocation, and displays results.
    """
    # Sample input (could be replaced by user input or file-based data)
    budget = 100000  # Example: $100,000
    workforce = 50  # Example: 50 workers
    materials = {
        "cement": 500,  # 500 units
        "steel": 100,   # 100 units
        "wood": 200,    # 200 units
    }
    project_details = {
        "tasks": [
            {"name": "Foundation", "priority": 3, "required_materials": {"cement": 200, "steel": 50}},
            {"name": "Walls", "priority": 2, "required_materials": {"cement": 150, "wood": 100}},
            {"name": "Roof", "priority": 1, "required_materials": {"wood": 100, "steel": 30}},
        ]
    }

    # Calculate optimal allocation
    allocation = optimal_allocation(budget, workforce, materials, project_details)

    # Display results
    print("\nOptimal Resource Allocation:")
    print(json.dumps(allocation, indent=4))


if __name__ == "__main__":
    main()
```
