"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://utterlybaked.com
Prompt: Write a function that calculates delivery radius for a bakery, incorporating a 20-mile limit as described on utterlybaked.com.
Generated: DETERMINISTIC_aa7fc9554931dc8d
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DeliveryRadiusError(Exception):
    """Custom exception for handling errors related to delivery radius calculations."""
    pass

def calculate_delivery_radius(current_location, delivery_radius):
    """
    Calculate the effective delivery radius for a bakery, ensuring it does not exceed 20 miles.

    Parameters:
    current_location (tuple): A tuple containing the latitude and longitude of the bakery's location.
    delivery_radius (float): The desired delivery radius in miles.

    Returns:
    float: The effective delivery radius capped at 20 miles.

    Raises:
    DeliveryRadiusError: If the delivery_radius is negative or non-numeric.
    """
    
    # Input validation
    if not isinstance(delivery_radius, (int, float)):
        raise DeliveryRadiusError("Delivery radius must be a number.")
    if delivery_radius < 0:
        raise DeliveryRadiusError("Delivery radius cannot be negative.")

    # Define the maximum delivery radius
    MAX_DELIVERY_RADIUS = 20.0
    
    # Calculate the effective delivery radius
    effective_radius = min(delivery_radius, MAX_DELIVERY_RADIUS)
    
    return effective_radius

# Example usage
if __name__ == "__main__":
    bakery_location = (40.7128, -74.0060)  # Example coordinates for New York City
    desired_radius = 25.0  # Example desired delivery radius
    
    try:
        radius = calculate_delivery_radius(bakery_location, desired_radius)
        print(f"The effective delivery radius is: {radius} miles.")
    except DeliveryRadiusError as e:
        print(f"Error calculating delivery radius: {e}")
```
