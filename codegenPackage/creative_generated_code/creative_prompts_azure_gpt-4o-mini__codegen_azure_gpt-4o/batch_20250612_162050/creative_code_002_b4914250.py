"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baturjeeptour.my.id
Prompt: Write a function that calculates the total cost for a group booking of the Jeep Sunrise Tour and the ATV Quad Bike experience in Kintamani, Bali.
Generated: DETERMINISTIC_b49142508964ceb3
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Tuple

# Define constants for the tour prices
JEEP_SUNRISE_TOUR_PRICE = 75.0  # Price per person in USD
ATV_QUAD_BIKE_PRICE = 50.0      # Price per person in USD
DISCOUNT_THRESHOLD = 10         # Discount applies if group size exceeds this number
DISCOUNT_RATE = 0.10            # 10% discount

def calculate_total_cost(group_size: int, activities: List[str]) -> float:
    """
    Calculate the total cost for a group booking of the Jeep Sunrise Tour
    and/or ATV Quad Bike experience in Kintamani, Bali.

    Args:
        group_size (int): Number of people in the group.
        activities (List[str]): List of activities chosen by the group (e.g., ["jeep", "atv"]).
    
    Returns:
        float: Total cost for the group booking in USD.
    
    Raises:
        ValueError: If group_size is not a positive integer or if activities contain invalid values.
    """
    # Validate group_size
    if group_size <= 0:
        raise ValueError("Group size must be a positive integer.")
    
    # Validate activities
    valid_activities = {"jeep", "atv"}  # Allowed activities
    if not all(activity in valid_activities for activity in activities):
        raise ValueError(f"Activities must be one or more of {valid_activities}.")
    
    # Initialize total cost
    total_cost = 0.0
    
    # Calculate cost for Jeep Sunrise Tour
    if "jeep" in activities:
        total_cost += JEEP_SUNRISE_TOUR_PRICE * group_size
    
    # Calculate cost for ATV Quad Bike experience
    if "atv" in activities:
        total_cost += ATV_QUAD_BIKE_PRICE * group_size
    
    # Apply discount for large groups
    if group_size > DISCOUNT_THRESHOLD:
        total_cost *= (1 - DISCOUNT_RATE)
    
    return round(total_cost, 2)  # Return total cost rounded to 2 decimal places

# Example usage:
# Group of 12 people booking both activities
try:
    total = calculate_total_cost(12, ["jeep", "atv"])
    print(f"Total cost: ${total}")
except ValueError as e:
    print(f"Error: {e}")
```
