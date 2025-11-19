"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: Create a function that calculates the cost of advertising in specific locations based on the pricing structure provided by WOW MEDIA.
Generated: DETERMINISTIC_64a4582a8f97c76c
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List, Union

# Pricing structure for WOW MEDIA advertising
# Key: Location name
# Value: Dictionary with 'base_cost' and optional 'premium_factor' for premium locations
PRICING_STRUCTURE = {
    "New York": {"base_cost": 5000, "premium_factor": 1.5},
    "Los Angeles": {"base_cost": 4000, "premium_factor": 1.3},
    "Chicago": {"base_cost": 3000},
    "Houston": {"base_cost": 2500},
    "Miami": {"base_cost": 3500, "premium_factor": 1.2}
}

def calculate_advertising_cost(
    locations: List[str],
    days: int,
    is_premium: bool = False
) -> Union[float, None]:
    """
    Calculate the total advertising cost for given locations and duration.

    Args:
        locations: List of locations where advertising will run
        days: Number of days for advertising
        is_premium: Whether premium placement is selected (default: False)

    Returns:
        Total cost as float if calculation is successful, None if any location is invalid

    Raises:
        ValueError: If days is not a positive integer
    """
    # Validate input
    if not isinstance(days, int) or days <= 0:
        raise ValueError("Days must be a positive integer")

    total_cost = 0.0

    for location in locations:
        # Check if location exists in pricing structure
        if location not in PRICING_STRUCTURE:
            print(f"Warning: Location '{location}' not found in pricing structure")
            return None

        # Get location pricing data
        location_data = PRICING_STRUCTURE[location]
        base_cost = location_data["base_cost"]

        # Calculate daily cost
        daily_cost = base_cost
        if is_premium and "premium_factor" in location_data:
            daily_cost *= location_data["premium_factor"]

        # Add to total
        total_cost += daily_cost * days

    return total_cost


# Example usage (commented out for production)
# try:
#     cost = calculate_advertising_cost(["New York", "Chicago"], 7, True)
#     if cost is not None:
#         print(f"Total advertising cost: ${cost:,.2f}")
# except ValueError as e:
#     print(f"Error: {e}")
```
