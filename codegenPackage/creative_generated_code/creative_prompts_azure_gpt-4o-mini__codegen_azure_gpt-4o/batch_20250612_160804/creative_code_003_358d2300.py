"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Develop a library function that calculates the cost of car repairs based on services like suspension repair and transmission work, similar to the pricing structure at Mechanics.ae.
Generated: DETERMINISTIC_358d2300f46d3e28
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# car_repair_cost_calculator.py
"""
Library function to calculate the cost of car repairs based on various services.
This function supports pricing similar to the structure used by Mechanics.ae.

Usage:
    from car_repair_cost_calculator import calculate_repair_cost

    selected_services = ['suspension_repair', 'transmission_work']
    total_cost = calculate_repair_cost(selected_services)
    print(f"Total repair cost: {total_cost}")
"""

# Define a dictionary to hold the service names and their respective costs
SERVICE_PRICING = {
    'oil_change': 150,               # Cost for oil change in currency units
    'brake_replacement': 300,        # Cost for brake replacement
    'suspension_repair': 500,        # Cost for suspension repair
    'transmission_work': 1200,       # Cost for transmission work
    'tire_rotation': 100,            # Cost for tire rotation
    'engine_diagnostics': 250        # Cost for engine diagnostics
}

def calculate_repair_cost(selected_services):
    """
    Calculate the total cost of car repairs based on selected services.

    Args:
        selected_services (list of str): A list of service names to be performed.

    Returns:
        float: The total cost of the selected services.

    Raises:
        ValueError: If an invalid service name is provided.
    """
    # Validate input: Ensure selected_services is a list
    if not isinstance(selected_services, list):
        raise TypeError("selected_services must be a list of strings representing service names.")

    total_cost = 0.0  # Initialize total cost

    for service in selected_services:
        # Validate if the service exists in the pricing dictionary
        if service not in SERVICE_PRICING:
            raise ValueError(f"Invalid service name: '{service}'. Please select valid services.")
        
        # Add service cost to the total
        total_cost += SERVICE_PRICING[service]

    return total_cost


# If the script is run directly, provide an example usage
if __name__ == "__main__":
    try:
        # Example: User selects services for repair
        selected_services = ['suspension_repair', 'transmission_work', 'oil_change']
        total_cost = calculate_repair_cost(selected_services)
        print(f"Total repair cost: {total_cost:.2f}")
    except (ValueError, TypeError) as e:
        # Handle errors gracefully and inform the user
        print(f"Error: {e}")
```
