"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delivery-services.online
Prompt: Write a Python function that calculates delivery costs based on distance and weight for an online delivery service.
Generated: DETERMINISTIC_0991928e3fb96dad
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_delivery_cost(distance_km, weight_kg):
    """
    Calculate delivery costs based on distance and weight.
    
    Delivery cost formula:
    - Base cost: $5
    - Distance cost: $0.50 per kilometer
    - Weight surcharge: $2 per kilogram for weight above 5 kg
    
    Parameters:
    distance_km (float): Distance in kilometers (must be non-negative).
    weight_kg (float): Weight in kilograms (must be non-negative).
    
    Returns:
    float: The total delivery cost.
    
    Raises:
    ValueError: If distance_km or weight_kg is negative.
    """
    try:
        # Validate inputs
        if distance_km < 0:
            raise ValueError("Distance cannot be negative.")
        if weight_kg < 0:
            raise ValueError("Weight cannot be negative.")

        # Base delivery cost
        base_cost = 5.0

        # Cost based on distance
        distance_cost = distance_km * 0.50

        # Weight surcharge (only if weight exceeds 5 kg)
        weight_surcharge = 0.0
        if weight_kg > 5:
            weight_surcharge = (weight_kg - 5) * 2.0

        # Calculate total cost
        total_cost = base_cost + distance_cost + weight_surcharge

        return round(total_cost, 2)  # Round to two decimal places for currency formatting
    
    except Exception as e:
        # Log error (in production, replace with proper logging mechanism)
        print(f"Error calculating delivery cost: {e}")
        raise


# Example usage:
# Uncomment the following lines to test the function
# try:
#     cost = calculate_delivery_cost(10, 8)
#     print(f"Delivery cost: ${cost}")
# except ValueError as ve:
#     print(f"Input error: {ve}")
# except Exception as ex:
#     print(f"Unexpected error: {ex}")
```
