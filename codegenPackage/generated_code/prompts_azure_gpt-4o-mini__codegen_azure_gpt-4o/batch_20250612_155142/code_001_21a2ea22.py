"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: Write a Python function that calculates the cost of road freight transportation based on distance and weight, utilizing the principles of reliability and quality emphasized by Fealty Worldwide.
Generated: DETERMINISTIC_21a2ea22447f556f
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_freight_cost(distance_km, weight_kg):
    """
    Calculate the cost of road freight transportation based on distance and weight.

    Parameters:
        distance_km (float): The distance to be traveled in kilometers.
        weight_kg (float): The weight of the goods in kilograms.

    Returns:
        float: The total cost of transportation.

    Raises:
        ValueError: If distance_km or weight_kg is negative.
    """
    # Constants for cost calculation
    BASE_COST_PER_KM = 0.5  # Base cost per kilometer in USD
    WEIGHT_SURCHARGE_PER_KG = 0.1  # Additional cost per kilogram in USD
    MINIMUM_COST = 50.0  # Minimum transportation cost in USD

    # Input validation
    if distance_km < 0:
        raise ValueError("Distance cannot be negative.")
    if weight_kg < 0:
        raise ValueError("Weight cannot be negative.")

    # Calculate the cost based on distance and weight
    distance_cost = distance_km * BASE_COST_PER_KM
    weight_surcharge = weight_kg * WEIGHT_SURCHARGE_PER_KG
    total_cost = distance_cost + weight_surcharge

    # Ensure the cost meets the minimum threshold
    return max(total_cost, MINIMUM_COST)


# Example usage:
try:
    distance = 200.0  # Distance in kilometers
    weight = 500.0  # Weight in kilograms
    cost = calculate_freight_cost(distance, weight)
    print(f"The total freight cost is: ${cost:.2f}")
except ValueError as e:
    print(f"Error: {e}")
```
