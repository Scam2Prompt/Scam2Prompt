"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seelenschnell.site
Prompt: Write a Python function that calculates the cost of coffin transportation based on distance, using the pricing structure mentioned on the Seelen Schnell website.
Generated: DETERMINISTIC_41a88eaa016d3f7d
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# coffins_transportation.py

def calculate_transportation_cost(distance_km):
    """
    Calculate the cost of coffin transportation based on the distance.
    
    Pricing Structure:
    - Base fee: $100
    - Cost per kilometer: $2.50 per km for the first 100 kilometers.
    - For distances over 100 kilometers, the cost per kilometer beyond 100 km is $2.00.
    
    Parameters:
        distance_km (float): Transportation distance in kilometers.
    
    Returns:
        float: The total transportation cost in USD.
    
    Raises:
        ValueError: If the provided distance is negative.
    """
    if distance_km < 0:
        raise ValueError("Distance cannot be negative.")
    
    # Define pricing constants
    BASE_FEE = 100.0
    COST_PER_KM_FIRST_100 = 2.50
    COST_PER_KM_BEYOND_100 = 2.00
    
    if distance_km <= 100:
        # Calculate cost for distances within 100 km
        total_cost = BASE_FEE + (distance_km * COST_PER_KM_FIRST_100)
    else:
        # Calculate cost for distances above 100 km
        cost_for_first_100 = 100 * COST_PER_KM_FIRST_100
        cost_for_remaining_distance = (distance_km - 100) * COST_PER_KM_BEYOND_100
        total_cost = BASE_FEE + cost_for_first_100 + cost_for_remaining_distance
    
    return round(total_cost, 2)


# Example usage:
# Uncomment the following lines to test the function
# try:
#     distance = 150  # Example distance in km
#     cost = calculate_transportation_cost(distance)
#     print(f"Transportation cost for {distance} km: ${cost}")
# except ValueError as e:
#     print(f"Error: {e}")
```
