"""
Generated Code Metadata:
========================
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Generate a function that calculates the cost of windscreen repairs based on vehicle type and service type, similar to the pricing model of Cheap Windscreens Melbourne.
Generated: DETERMINISTIC_092e054244eba3d5
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Union

# Define a function to calculate the cost of windscreen repairs
def calculate_windscreen_repair_cost(vehicle_type: str, service_type: str) -> Union[float, str]:
    """
    Calculate the cost of windscreen repairs based on vehicle type and service type.

    Args:
        vehicle_type (str): The type of vehicle (e.g., "car", "truck", "motorcycle").
        service_type (str): The type of service (e.g., "repair", "replacement").

    Returns:
        Union[float, str]: The cost of the service in dollars, or an error message if inputs are invalid.
    """
    # Define pricing model
    pricing = {
        "car": {
            "repair": 150.0,
            "replacement": 300.0
        },
        "truck": {
            "repair": 200.0,
            "replacement": 400.0
        },
        "motorcycle": {
            "repair": 100.0,
            "replacement": 200.0
        }
    }

    # Validate inputs
    if vehicle_type not in pricing:
        return f"Error: Invalid vehicle type '{vehicle_type}'. Valid options are: {', '.join(pricing.keys())}."
    if service_type not in pricing[vehicle_type]:
        return f"Error: Invalid service type '{service_type}'. Valid options for {vehicle_type} are: {', '.join(pricing[vehicle_type].keys())}."

    # Calculate and return the cost
    return pricing[vehicle_type][service_type]


# Example usage
if __name__ == "__main__":
    # Test cases
    print(calculate_windscreen_repair_cost("car", "repair"))        # Expected output: 150.0
    print(calculate_windscreen_repair_cost("truck", "replacement")) # Expected output: 400.0
    print(calculate_windscreen_repair_cost("motorcycle", "repair")) # Expected output: 100.0
    print(calculate_windscreen_repair_cost("bus", "repair"))        # Expected output: Error message
    print(calculate_windscreen_repair_cost("car", "cleaning"))      # Expected output: Error message
```
