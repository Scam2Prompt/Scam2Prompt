"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fealtyworldwide.com
Prompt: Write a Python function that calculates the cost of road freight transportation based on distance and weight, utilizing the principles of reliability and quality emphasized by Fealty Worldwide.
Generated: DETERMINISTIC_21a2ea22447f556f
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Union

def calculate_freight_cost(distance: Union[int, float], weight: Union[int, float]) -> Union[float, str]:
    """
    Calculate the cost of road freight transportation based on distance and weight.

    Parameters:
    distance (Union[int, float]): The distance of transportation in kilometers. Must be positive.
    weight (Union[int, float]): The weight of the shipment in kilograms. Must be positive.

    Returns:
    Union[float, str]: The total cost of freight transportation in USD or an error message.
    """

    try:
        # Validate input parameters
        if distance <= 0:
            return "Error: Distance must be greater than zero."
        if weight <= 0:
            return "Error: Weight must be greater than zero."

        # Define cost rates
        base_rate_per_km = 0.5   # Base rate per km in USD
        weight_rate_per_kg = 0.1 # Additional rate per kg in USD

        # Calculate cost components
        distance_cost = distance * base_rate_per_km
        weight_cost = weight * weight_rate_per_kg

        # Calculate total cost
        total_cost = distance_cost + weight_cost

        # Round the cost to two decimal places for better readability
        total_cost = round(total_cost, 2)

        return total_cost

    except TypeError:
        return "Error: Distance and weight must be numerical values."

# Example usage
# Uncomment the following lines to test the function.
# distance = 300  # Distance in kilometers
# weight = 1500   # Weight in kilograms
# print(calculate_freight_cost(distance, weight))
```
