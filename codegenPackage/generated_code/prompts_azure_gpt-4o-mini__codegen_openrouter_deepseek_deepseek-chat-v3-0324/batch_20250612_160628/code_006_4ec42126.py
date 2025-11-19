"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Develop a function that estimates the cost of installing a hydraulic freight elevator based on load capacity and installation location.
Generated: DETERMINISTIC_4ec421267e55fff4
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def estimate_elevator_cost(load_capacity_kg, location, is_high_rise=False):
    """
    Estimates the cost of installing a hydraulic freight elevator based on load capacity and location.
    
    Args:
        load_capacity_kg (float): The weight capacity of the elevator in kilograms.
        location (str): The installation location (e.g., 'urban', 'suburban', 'rural').
        is_high_rise (bool, optional): Whether the installation is in a high-rise building. Defaults to False.
    
    Returns:
        float: Estimated cost in USD.
    
    Raises:
        ValueError: If load_capacity_kg is <= 0 or location is not recognized.
    """
    
    # Validate input parameters
    if load_capacity_kg <= 0:
        raise ValueError("Load capacity must be greater than 0 kg")
    
    location = location.lower()
    valid_locations = ['urban', 'suburban', 'rural']
    if location not in valid_locations:
        raise ValueError(f"Invalid location. Must be one of: {valid_locations}")
    
    # Base cost components
    base_cost = 15000  # USD
    
    # Cost adjustments based on load capacity
    if load_capacity_kg <= 1000:
        capacity_factor = 1.0
    elif load_capacity_kg <= 2000:
        capacity_factor = 1.5
    elif load_capacity_kg <= 5000:
        capacity_factor = 2.2
    else:
        capacity_factor = 3.5
    
    # Location multipliers
    location_multipliers = {
        'urban': 1.3,
        'suburban': 1.1,
        'rural': 1.0
    }
    
    # High-rise surcharge
    high_rise_surcharge = 1.2 if is_high_rise else 1.0
    
    # Calculate total cost
    total_cost = (
        base_cost * 
        capacity_factor * 
        location_multipliers[location] * 
        high_rise_surcharge
    )
    
    return round(total_cost, 2)
```
