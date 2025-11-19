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
def calculate_coffin_transport_cost(distance_km):
    """
    Calculate the cost of coffin transportation based on distance.

    Pricing Structure:
    - $100 for the first 10 km
    - $50 for each additional 10 km or part thereof

    :param distance_km: Distance in kilometers for coffin transportation
    :return: Total transportation cost in dollars
    :raises ValueError: If the distance is negative
    """

    if distance_km < 0:
        raise ValueError("Distance cannot be negative.")

    # Base cost for the first 10 km
    base_cost = 100
    additional_cost_per_10km = 50
    
    if distance_km <= 10:
        return base_cost
    else:
        # Calculate additional distance beyond the first 10 km
        additional_distance = distance_km - 10
        # Calculate number of additional segments (each 10 km or part thereof)
        additional_segments = (additional_distance + 9) // 10  # Ceiling division
        total_cost = base_cost + (additional_segments * additional_cost_per_10km)
        return total_cost

# Example of usage
if __name__ == "__main__":
    try:
        distance = 25  # Example distance in km
        cost = calculate_coffin_transport_cost(distance)
        print(f"The cost of coffin transportation for {distance} km is: ${cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
