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
def calculate_windscreen_repair_cost(vehicle_type, service_type, has_insurance=False):
    """
    Calculates the cost of windscreen repairs based on vehicle type and service type.
    
    Args:
        vehicle_type (str): Type of vehicle ('sedan', 'suv', 'ute', 'van', 'truck').
        service_type (str): Type of service ('repair', 'replacement').
        has_insurance (bool, optional): Whether the customer has insurance. Defaults to False.
    
    Returns:
        float: The total cost of the service after applying any insurance discounts.
    
    Raises:
        ValueError: If vehicle_type or service_type is invalid.
    """
    # Define base prices for different vehicle types and services
    pricing_model = {
        'sedan': {
            'repair': 100.00,
            'replacement': 300.00
        },
        'suv': {
            'repair': 120.00,
            'replacement': 350.00
        },
        'ute': {
            'repair': 110.00,
            'replacement': 330.00
        },
        'van': {
            'repair': 130.00,
            'replacement': 380.00
        },
        'truck': {
            'repair': 150.00,
            'replacement': 450.00
        }
    }
    
    # Validate input parameters
    if vehicle_type.lower() not in pricing_model:
        raise ValueError(f"Invalid vehicle type. Must be one of: {list(pricing_model.keys())}")
    
    if service_type.lower() not in ['repair', 'replacement']:
        raise ValueError("Invalid service type. Must be 'repair' or 'replacement'")
    
    # Get base price
    base_price = pricing_model[vehicle_type.lower()][service_type.lower()]
    
    # Apply insurance discount (20% off)
    if has_insurance:
        base_price *= 0.8
    
    return round(base_price, 2)
```
