"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medioswow.com
Prompt: Create a function that calculates the cost of advertising in specific locations based on the pricing structure provided by WOW MEDIA.
Generated: DETERMINISTIC_64a4582a8f97c76c
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# advertising_cost_calculator.py

def calculate_advertising_cost(location, duration_days, impressions):
    """
    Calculate the cost of advertising in specific locations based on WOW MEDIA's pricing structure.

    Parameters:
        location (str): The location where advertising will be placed (e.g., "Location A").
        duration_days (int): The number of days the advertisement will run.
        impressions (int): The number of impressions (views) the advertisement is expected to generate.

    Returns:
        float: The total cost of advertising for the given inputs.

    Raises:
        ValueError: If any input is invalid (e.g., negative duration or impressions, or unknown location).
    """
    # WOW MEDIA pricing structure (example rates; adjust as needed)
    pricing_structure = {
        "Location A": {"base_rate_per_day": 1000, "impression_rate": 0.02},
        "Location B": {"base_rate_per_day": 800, "impression_rate": 0.015},
        "Location C": {"base_rate_per_day": 500, "impression_rate": 0.01},
    }

    # Validate inputs
    if location not in pricing_structure:
        raise ValueError(f"Unknown location: {location}. Please choose a valid location.")
    if duration_days <= 0:
        raise ValueError("Duration days must be a positive integer.")
    if impressions < 0:
        raise ValueError("Impressions must be a non-negative integer.")

    # Retrieve pricing details for the specified location
    location_pricing = pricing_structure[location]
    base_rate_per_day = location_pricing["base_rate_per_day"]
    impression_rate = location_pricing["impression_rate"]

    # Calculate total cost
    total_cost = (base_rate_per_day * duration_days) + (impressions * impression_rate)
    return round(total_cost, 2)


# Example usage (Uncomment to test the function)
# try:
#     cost = calculate_advertising_cost("Location A", 10, 50000)
#     print(f"Total advertising cost: ${cost}")
# except ValueError as e:
#     print(f"Error: {e}")
```
