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
class ResourceAllocationError(Exception):
    """Custom exception for Resource Allocation errors."""
    pass


def calculate_resource_allocation(total_resources, project_efficiency, sustainability_factor):
    """
    Calculate the resource allocation for engineering projects based on efficiency and sustainability principles.

    Parameters:
    total_resources (float): Total available resources for allocation.
    project_efficiency (float): Efficiency rating of the project (0 to 1).
    sustainability_factor (float): Sustainability factor affecting resource allocation (0 to 1).

    Returns:
    float: Allocated resources for the project.

    Raises:
    ResourceAllocationError: If any input parameter is not within the specified range.
    """
    
    # Validate input parameters
    if not (0 <= project_efficiency <= 1):
        raise ResourceAllocationError("Project efficiency must be between 0 and 1.")
    
    if not (0 <= sustainability_factor <= 1):
        raise ResourceAllocationError("Sustainability factor must be between 0 and 1.")
    
    if total_resources < 0:
        raise ResourceAllocationError("Total resources must be a non-negative value.")

    # Calculate the effective resources based on efficiency and sustainability
    effective_resources = total_resources * project_efficiency * sustainability_factor

    return effective_resources


if __name__ == "__main__":
    try:
        total_resources = 1000  # Total resources available
        project_efficiency = 0.85  # Efficiency of the project
        sustainability_factor = 0.75  # Sustainability impact

        allocated_resources = calculate_resource_allocation(total_resources, project_efficiency, sustainability_factor)
        print(f"Allocated Resources: {allocated_resources}")
    except ResourceAllocationError as e:
        print(f"Error in resource allocation: {e}")
```
