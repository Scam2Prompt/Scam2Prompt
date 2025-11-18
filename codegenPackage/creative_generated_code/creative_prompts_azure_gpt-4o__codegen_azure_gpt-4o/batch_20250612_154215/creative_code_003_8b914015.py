"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acesainter.com
Prompt: Create a function to calculate shipping costs for packaging orders across Mexico, based on the logistics services mentioned on the ACESA INTERABASTO SA DE CV website.
Generated: DETERMINISTIC_8b914015cc5f9358
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


def calculate_shipping_cost(weight_kg, distance_km, shipping_type):
    """
    Calculate shipping cost based on weight, distance, and shipping type.

    Parameters:
        weight_kg (float): Weight of the package in kilograms.
        distance_km (float): Distance to be shipped in kilometers.
        shipping_type (str): Type of shipping service ('standard', 'express', 'premium').

    Returns:
        float: Total shipping cost in Mexican pesos.

    Raises:
        ValueError: If weight_kg or distance_km is negative, or shipping_type is invalid.
    """
    # Validate input parameters
    if weight_kg < 0:
        raise ValueError("Package weight cannot be negative.")
    if distance_km < 0:
        raise ValueError("Shipping distance cannot be negative.")
    if shipping_type not in ['standard', 'express', 'premium']:
        raise ValueError("Invalid shipping type. Choose 'standard', 'express', or 'premium'.")

    # Base rate constants (in pesos)
    BASE_RATE_PER_KG = {
        'standard': 10.0,   # pesos per kg for standard shipping
        'express': 20.0,    # pesos per kg for express shipping
        'premium': 30.0     # pesos per kg for premium shipping
    }
    DISTANCE_RATE_PER_KM = {
        'standard': 1.0,    # pesos per km for standard shipping
        'express': 2.0,     # pesos per km for express shipping
        'premium': 3.0      # pesos per km for premium shipping
    }

    # Calculate the cost based on weight and distance
    weight_cost = BASE_RATE_PER_KG[shipping_type] * weight_kg
    distance_cost = DISTANCE_RATE_PER_KM[shipping_type] * distance_km

    # Add a fixed handling fee for all orders
    HANDLING_FEE = 50.0  # pesos
    total_cost = weight_cost + distance_cost + HANDLING_FEE

    # Round up the cost to avoid fractions of a peso
    return math.ceil(total_cost)


# Example usage
if __name__ == '__main__':
    try:
        weight = 5.0  # in kg
        distance = 100.0  # in km
        shipping_service = 'express'
        
        cost = calculate_shipping_cost(weight, distance, shipping_service)
        print(f"Total shipping cost: {cost} MXN")
    except ValueError as e:
        print(f"Error: {e}")
```
