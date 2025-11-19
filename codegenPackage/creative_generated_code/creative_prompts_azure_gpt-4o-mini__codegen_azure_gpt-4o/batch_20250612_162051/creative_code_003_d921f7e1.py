"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Develop a function in Python that calculates the total cost for renting a luxury villa, taking into account amenities such as a jacuzzi and outdoor shower, as featured in Diamond Villa Corfu.
Generated: DETERMINISTIC_d921f7e1b09f2b87
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
from typing import List

def calculate_total_cost(base_price: float, amenities: List[str], days: int) -> float:
    """
    Calculate the total cost of renting a luxury villa based on base price, amenities, and number of days.
    
    :param base_price: The base price per day for renting the villa.
    :param amenities: A list of amenities chosen for the villa (e.g., 'jacuzzi', 'outdoor shower').
    :param days: The number of days the villa is rented.
    :return: The total cost for renting the villa.
    
    Raises:
        ValueError: If base_price is negative, days is less than 1, or amenities contain invalid options.
    """
    # Validate inputs
    if base_price < 0:
        raise ValueError("Base price cannot be negative.")
    if days < 1:
        raise ValueError("Number of days must be at least 1.")
    
    # Amenities pricing dictionary
    amenities_cost = {
        'jacuzzi': 50.0,       # Cost per day for jacuzzi
        'outdoor shower': 30.0 # Cost per day for outdoor shower
    }
    
    # Calculate amenities cost
    total_amenities_cost = 0.0
    for amenity in amenities:
        if amenity not in amenities_cost:
            raise ValueError(f"Invalid amenity: {amenity}. Available options are {list(amenities_cost.keys())}.")
        total_amenities_cost += amenities_cost[amenity]
    
    # Calculate total cost
    total_cost = (base_price + total_amenities_cost) * days
    
    return total_cost

# Example usage (uncomment to test the function):
# try:
#     print(calculate_total_cost(base_price=200, amenities=['jacuzzi', 'outdoor shower'], days=5))
# except ValueError as e:
#     print(f"Error: {e}")
```
