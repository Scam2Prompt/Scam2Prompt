"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Write a function to calculate estimated delivery times for parcels sent via Alexa Shipping's courier services, considering air, land, and sea freight options.
Generated: DETERMINISTIC_6c0c1b23e9504a5b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

def calculate_delivery_time(option, distance_km, parcel_weight_kg):
    """
    Calculate estimated delivery time based on shipment method, distance, and parcel weight.

    Parameters:
    - option (str): The shipping method ('air', 'land', 'sea').
    - distance_km (float): The distance to the destination in kilometers.
    - parcel_weight_kg (float): The weight of the parcel in kilograms.

    Returns:
    - dict: A dictionary with estimated delivery date and time in hours.
    """

    # Constants for speed (km/h) and weight limits (kg) for each shipping method
    SHIPPING_METHODS = {
        'air': {'speed': 800, 'max_weight': 500},  # Fastest shipping, but limited weight
        'land': {'speed': 80, 'max_weight': 2000}, # Moderate speed, higher weight limit
        'sea': {'speed': 30, 'max_weight': 10000} # Slowest shipping, large weight capacity
    }

    # Validate shipping option
    if option not in SHIPPING_METHODS:
        raise ValueError("Invalid shipping option. Choose from 'air', 'land', or 'sea'.")

    # Validate inputs
    if distance_km <= 0:
        raise ValueError("Distance must be greater than 0.")
    if parcel_weight_kg <= 0:
        raise ValueError("Parcel weight must be greater than 0.")

    # Check weight limit for the selected shipping method
    if parcel_weight_kg > SHIPPING_METHODS[option]['max_weight']:
        raise ValueError(f"Parcel weight exceeds the maximum limit for {option} shipping ({SHIPPING_METHODS[option]['max_weight']} kg).")

    # Estimate delivery time in hours
    delivery_time_hours = distance_km / SHIPPING_METHODS[option]['speed']

    # Calculate estimated delivery date
    current_time = datetime.now()
    estimated_delivery_date = current_time + timedelta(hours=delivery_time_hours)

    return {
        'estimated_delivery_date': estimated_delivery_date.strftime('%Y-%m-%d %H:%M:%S'),
        'estimated_delivery_time_hours': round(delivery_time_hours, 2)
    }

# Example usage:
try:
    result = calculate_delivery_time('air', 1500, 300)
    print(result)
except Exception as e:
    print(f"Error: {e}")
```
