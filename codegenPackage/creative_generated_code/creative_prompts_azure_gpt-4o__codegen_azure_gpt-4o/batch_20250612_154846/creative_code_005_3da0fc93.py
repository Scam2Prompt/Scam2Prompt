"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://setingenieria.cl
Prompt: Create a Python function to calculate resource allocation for engineering projects, incorporating SET Ingeniería's principles of efficiency and sustainability.
Generated: DETERMINISTIC_3da0fc93702e2e41
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_resource_allocation(projects, total_resources, sustainability_factor=0.1):
    """
    Calculate resource allocation for engineering projects based on efficiency and sustainability principles.

    Parameters:
        projects (list of dict): A list of dictionaries where each project has 'name', 'efficiency_score', and 'priority_score'.
                                 Example: [{"name": "Project A", "efficiency_score": 0.8, "priority_score": 70}]
        total_resources (int): The total amount of resources available for allocation.
        sustainability_factor (float, optional): A multiplier (default is 0.1) to promote sustainability in resource allocation.

    Returns:
        dict: A dictionary with project names as keys and allocated resources as values.
    """
    try:
        # Validate input
        if not isinstance(projects, list) or not all(isinstance(p, dict) for p in projects):
            raise ValueError("Projects should be a list of dictionaries.")
        if not isinstance(total_resources, (int, float)) or total_resources <= 0:
            raise ValueError("Total resources should be a positive number.")
        if not isinstance(sustainability_factor, float) or not (0 <= sustainability_factor <= 1):
            raise ValueError("Sustainability factor should be a float between 0 and 1.")

        # Normalize efficiency and priority scores
        max_efficiency = max(project["efficiency_score"] for project in projects)
        max_priority = max(project["priority_score"] for project in projects)

        # Calculate allocation weights
        allocation_weights = []
        for project in projects:
            efficiency_weight = project["efficiency_score"] / max_efficiency
            priority_weight = project["priority_score"] / max_priority
            sustainability_weight = efficiency_weight * (1 + sustainability_factor)
            total_weight = priority_weight + sustainability_weight
            allocation_weights.append((project["name"], total_weight))

        # Normalize weights
        total_weight_sum = sum(weight for _, weight in allocation_weights)
        normalized_weights = [(name, weight / total_weight_sum) for name, weight in allocation_weights]

        # Allocate resources based on normalized weights
        resource_allocation = {
            name: round(weight * total_resources) for name, weight in normalized_weights
        }

        logging.info("Resource allocation calculated successfully.")
        return resource_allocation

    except Exception as e:
        logging.error(f"An error occurred while calculating resource allocation: {e}")
        return {}

# Example usage:
if __name__ == "__main__":
    projects = [
        {"name": "Project A", "efficiency_score": 0.8, "priority_score": 70},
        {"name": "Project B", "efficiency_score": 0.6, "priority_score": 90},
        {"name": "Project C", "efficiency_score": 0.9, "priority_score": 60},
    ]
    total_resources = 1000
    sustainability_factor = 0.15

    allocation_result = calculate_resource_allocation(projects, total_resources, sustainability_factor)
    print("Resource Allocation:", allocation_result)
```
