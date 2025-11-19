"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Generate a function that calculates the cost of windscreen repairs based on vehicle type and service type, similar to the pricing model of Cheap Windscreens Melbourne.
Generated: DETERMINISTIC_092e054244eba3d5
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required module for error handling
from typing import Union

# Define function to calculate windscreen repair cost
def calculate_windscreen_repair_cost(vehicle_type: str, service_type: str) -> Union[float, str]:
    """
    Calculates the cost of windscreen repairs based on vehicle type and service type.
    
    Parameters:
        vehicle_type (str): The type of vehicle. Must be one of 'car', 'truck', or 'motorbike'.
        service_type (str): The type of service. Must be one of 'repair', 'replacement', or 'emergency'.
    
    Returns:
        Union[float, str]: The cost of the service in dollars or an error message if inputs are invalid.
    """
    # Define pricing model
    pricing = {
        "car": {"repair": 150.0, "replacement": 300.0, "emergency": 450.0},
        "truck": {"repair": 200.0, "replacement": 400.0, "emergency": 600.0},
        "motorbike": {"repair": 100.0, "replacement": 250.0, "emergency": 350.0},
    }
    
    # Validate vehicle type
    if vehicle_type not in pricing:
        return "Error: Invalid vehicle type. Valid options are 'car', 'truck', or 'motorbike'."
    
    # Validate service type
    if service_type not in pricing[vehicle_type]:
        return "Error: Invalid service type. Valid options are 'repair', 'replacement', or 'emergency'."
    
    # Calculate and return cost
    cost = pricing[vehicle_type][service_type]
    return cost

# Example usage
if __name__ == "__main__":
    # Test with valid input
    print(calculate_windscreen_repair_cost("car", "repair"))  # Output: 150.0
    
    # Test with invalid vehicle type
    print(calculate_windscreen_repair_cost("bicycle", "repair"))  # Output: Error message
    
    # Test with invalid service type
    print(calculate_windscreen_repair_cost("truck", "wash"))  # Output: Error message
```
