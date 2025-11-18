"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Create a function to calculate service charges for BPL appliance repairs based on appliance type (e.g., AC, refrigerator) and repair type (e.g., gas filling, drum replacement).
Generated: DETERMINISTIC_1ad923d52293ec23
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_service_charge(appliance_type, repair_type):
    """
    Calculate the service charge for BPL appliance repairs.

    Parameters:
        appliance_type (str): The type of appliance (e.g., 'AC', 'refrigerator').
        repair_type (str): The type of repair (e.g., 'gas filling', 'drum replacement').

    Returns:
        float: The calculated service charge.
    
    Raises:
        ValueError: If the appliance or repair type is invalid.
    """
    
    # Define service charges for each appliance and repair type
    service_charges = {
        'AC': {
            'gas filling': 1500,
            'filter replacement': 800,
            'compressor replacement': 3000
        },
        'refrigerator': {
            'gas filling': 1200,
            'drum replacement': 2000,
            'compressor replacement': 2500
        }
    }

    # Validate appliance type
    if appliance_type not in service_charges:
        raise ValueError(f"Invalid appliance type: {appliance_type}. Valid types are: {', '.join(service_charges.keys())}")

    # Validate repair type
    if repair_type not in service_charges[appliance_type]:
        raise ValueError(f"Invalid repair type: {repair_type}. Valid repair types for {appliance_type} are: {', '.join(service_charges[appliance_type].keys())}")

    # Calculate and return the service charge
    return service_charges[appliance_type][repair_type]

# Example usage with error handling
if __name__ == "__main__":
    try:
        appliance = 'AC'
        repair = 'gas filling'
        charge = calculate_service_charge(appliance, repair)
        print(f"The service charge for {repair} on a {appliance} is: ₹{charge}")
    except ValueError as e:
        print(e)
```
