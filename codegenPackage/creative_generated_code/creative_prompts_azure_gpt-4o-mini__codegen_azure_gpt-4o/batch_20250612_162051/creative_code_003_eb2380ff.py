"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeco.pk
Prompt: Create a function that calculates the load capacity of different tractor attachments, using JECO's specifications for front-end loaders and backhoes.
Generated: DETERMINISTIC_eb2380ffe9b7fbad
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict, Union

# Define specifications for JECO's tractor attachments
JECO_SPECIFICATIONS = {
    "front_end_loader": {
        "capacity_kg": 1500,  # Maximum load capacity in kilograms
        "efficiency_factor": 0.85  # Efficiency factor due to design constraints
    },
    "backhoe": {
        "capacity_kg": 1200,  # Maximum load capacity in kilograms
        "efficiency_factor": 0.9  # Efficiency factor due to design constraints
    }
}

def calculate_load_capacity(attachment_type: str, load_weight_kg: Union[int, float]) -> Union[float, str]:
    """
    Calculate the available load capacity for given JECO tractor attachments.

    Parameters:
        attachment_type (str): The type of tractor attachment ('front_end_loader' or 'backhoe').
        load_weight_kg (Union[int, float]): The weight of the load in kilograms.

    Returns:
        Union[float, str]: The remaining load capacity (in kilograms) after accounting for the load weight.
                           Returns an error message if the input is invalid or exceeds capacity.
    """
    # Validate the attachment type
    if attachment_type not in JECO_SPECIFICATIONS:
        return "Error: Invalid attachment type. Valid types are 'front_end_loader' and 'backhoe'."
    
    # Validate the load weight
    if load_weight_kg <= 0:
        return "Error: Load weight must be a positive number."
    
    # Retrieve the specifications for the attachment type
    specs = JECO_SPECIFICATIONS[attachment_type]
    max_capacity = specs["capacity_kg"]
    efficiency_factor = specs["efficiency_factor"]
    
    # Calculate the effective capacity
    effective_capacity = max_capacity * efficiency_factor
    
    # Check if the load exceeds the effective capacity
    if load_weight_kg > effective_capacity:
        return f"Error: Load weight exceeds the effective capacity of {effective_capacity:.2f} kg."
    
    # Calculate the remaining capacity
    remaining_capacity = effective_capacity - load_weight_kg
    
    return remaining_capacity


# Example usage:
if __name__ == "__main__":
    # Test with valid data
    print(calculate_load_capacity("front_end_loader", 1200))  # Output: Remaining capacity
    
    # Test with load exceeding capacity
    print(calculate_load_capacity("backhoe", 1300))  # Output: Error message
    
    # Test with invalid attachment type
    print(calculate_load_capacity("invalid_attachment", 500))  # Output: Error message
    
    # Test with invalid load weight
    print(calculate_load_capacity("front_end_loader", -100))  # Output: Error message
```
