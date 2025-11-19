"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portlineshipping.com
Prompt: Write a Python function that calculates the cost of sea freight based on distance and cargo weight, referencing the services provided by Portline Shipping.
Generated: DETERMINISTIC_fd966569ace36907
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# sea_freight_calculator.py
"""
This module contains a function for calculating the cost of sea freight
based on distance and cargo weight using Portline Shipping's pricing model.

Portline Shipping Pricing:
- Base cost per kilometer: $0.05
- Cost per kilogram: $0.10
- Minimum freight charge: $50.00
"""

def calculate_sea_freight_cost(distance_km, cargo_weight_kg):
    """
    Calculates the cost of sea freight based on distance and cargo weight.

    Parameters:
        distance_km (float): The distance of the shipment in kilometers.
        cargo_weight_kg (float): The weight of the cargo in kilograms.

    Returns:
        float: The total cost of sea freight.

    Raises:
        ValueError: If distance_km or cargo_weight_kg is negative.
        TypeError: If distance_km or cargo_weight_kg is not a number.
    """
    try:
        # Validate input types
        if not isinstance(distance_km, (int, float)) or not isinstance(cargo_weight_kg, (int, float)):
            raise TypeError("Both distance_km and cargo_weight_kg must be numbers.")

        # Validate input values
        if distance_km < 0:
            raise ValueError("Distance cannot be negative.")
        if cargo_weight_kg < 0:
            raise ValueError("Cargo weight cannot be negative.")

        # Portline Shipping pricing model
        base_cost_per_km = 0.05  # USD per kilometer
        cost_per_kg = 0.10       # USD per kilogram
        minimum_charge = 50.00   # Minimum freight charge in USD

        # Calculate the freight cost
        cost = (distance_km * base_cost_per_km) + (cargo_weight_kg * cost_per_kg)

        # Ensure the minimum charge is applied
        total_cost = max(cost, minimum_charge)

        return round(total_cost, 2)  # Return cost rounded to 2 decimal places

    except Exception as e:
        # Log the error or handle it appropriately in production
        raise e  # Raise the exception to the caller for visibility

# Example usage:
# Uncomment the lines below to test the function
# freight_cost = calculate_sea_freight_cost(500, 200)
# print(f"The total cost of sea freight is: ${freight_cost}")
```
