"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ohclift.com
Prompt: Develop a function that estimates the cost of installing a hydraulic freight elevator based on load capacity and installation location.
Generated: DETERMINISTIC_4ec421267e55fff4
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def estimate_elevator_cost(load_capacity, location):
    """
    Estimate the cost of installing a hydraulic freight elevator based on load capacity and installation location.
    
    Parameters:
        load_capacity (float): Load capacity in kilograms. Must be greater than 0.
        location (str): Installation location. Accepted values are 'urban', 'suburban', 'rural'.
        
    Returns:
        float: Estimated cost in USD.
    
    Raises:
        ValueError: If load_capacity is less than or equal to 0.
        ValueError: If location is not one of 'urban', 'suburban', or 'rural'.
    """
    # Validate input parameters
    if load_capacity <= 0:
        raise ValueError("Load capacity must be greater than 0.")
    
    valid_locations = ['urban', 'suburban', 'rural']
    if location.lower() not in valid_locations:
        raise ValueError(f"Invalid location. Accepted values are: {', '.join(valid_locations)}")
    
    # Base cost calculation based on load capacity
    # Formula: base_cost = 5000 + (load_capacity * 10)
    base_cost = 5000 + (load_capacity * 10)
    
    # Adjust cost based on the location
    location_multiplier = {
        'urban': 1.2,       # Urban areas have higher costs due to labor and permits
        'suburban': 1.0,    # Suburban areas have average costs
        'rural': 0.8        # Rural areas may have lower costs
    }
    
    adjustment_factor = location_multiplier[location.lower()]
    total_cost = base_cost * adjustment_factor
    
    # Round to two decimal places for better readability
    return round(total_cost, 2)

# Example usage:
if __name__ == "__main__":
    try:
        # Test the function with valid inputs
        load_capacity = 2000  # 2,000 kg
        location = 'urban'
        cost = estimate_elevator_cost(load_capacity, location)
        print(f"Estimated cost for installing a hydraulic freight elevator: ${cost}")
    except ValueError as e:
        # Handle invalid inputs gracefully
        print(f"Error: {e}")
```
