"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Write a Python script to calculate the cost of consulting services for architectural projects, factoring in additional services beyond the initial agreement as described by TWM Associates.
Generated: DETERMINISTIC_460576b00c7d6969
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the cost of consulting services for architectural projects.
Factors include:
1. Base project cost as per the initial agreement.
2. Costs for any additional services provided by TWM Associates.

Author: [Your Name]
Date: [Date]
"""

# Import necessary libraries
import sys


def calculate_total_cost(base_cost, additional_services):
    """
    Calculate the total cost of consulting services.

    Parameters:
        base_cost (float): The base project cost agreed upon initially.
        additional_services (list of dict): A list of dictionaries where each dictionary represents
                                            an additional service with 'description' and 'cost'.

    Returns:
        float: The total cost of consulting services.
    """
    try:
        # Validate inputs
        if not isinstance(base_cost, (int, float)) or base_cost < 0:
            raise ValueError("Base cost must be a positive number.")

        if not isinstance(additional_services, list):
            raise ValueError("Additional services must be a list of dictionaries.")

        # Calculate additional service costs
        additional_cost = 0.0
        for service in additional_services:
            if not isinstance(service, dict) or 'cost' not in service:
                raise ValueError("Each additional service must be a dictionary containing a 'cost' key.")
            service_cost = service.get('cost', 0.0)
            if not isinstance(service_cost, (int, float)) or service_cost < 0:
                raise ValueError("Service cost must be a positive number.")
            additional_cost += service_cost

        # Calculate total cost
        total_cost = base_cost + additional_cost
        return total_cost

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    # Example inputs
    base_project_cost = 5000.0  # Base cost agreed upon
    additional_services_list = [
        {"description": "Site survey", "cost": 1000.0},
        {"description": "Detailed blueprints", "cost": 2500.0},
        {"description": "Environmental impact assessment", "cost": 1800.0},
    ]

    # Calculate total cost
    total_project_cost = calculate_total_cost(base_project_cost, additional_services_list)

    # Display the result
    if total_project_cost is not None:
        print(f"Total cost of consulting services: ${total_project_cost:.2f}")
    else:
        print("Failed to calculate total cost due to input errors.")
```
