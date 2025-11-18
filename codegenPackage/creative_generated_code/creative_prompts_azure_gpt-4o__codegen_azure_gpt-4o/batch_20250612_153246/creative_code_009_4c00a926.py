"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refrigeratortransport.com
Prompt: Generate a Python script for calculating competitive pricing for refrigerated van rentals, factoring in vehicle type, distance, and delivery time, as outlined on RefrigeratorTransport.com.
Generated: DETERMINISTIC_4c00a9267e4f8626
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

# Define constants for base rates and surcharges
BASE_RATE_SMALL_VAN = 50.0  # Base rate for small refrigerated van per kilometer
BASE_RATE_MEDIUM_VAN = 75.0  # Base rate for medium refrigerated van per kilometer
BASE_RATE_LARGE_VAN = 100.0  # Base rate for large refrigerated van per kilometer
PEAK_HOUR_SURCHARGE = 1.25  # Multiplier for peak delivery times
NON_PEAK_HOUR_DISCOUNT = 0.90  # Multiplier for non-peak delivery times

def calculate_pricing(vehicle_type, distance_km, delivery_time):
    """
    Calculate competitive pricing for refrigerated van rentals.

    Args:
        vehicle_type (str): Type of vehicle ('small', 'medium', 'large').
        distance_km (float): Distance to be covered in kilometers.
        delivery_time (str): Delivery time as 'peak' or 'non-peak'.

    Returns:
        float: Calculated pricing for the rental.

    Raises:
        ValueError: If the vehicle type or delivery time is invalid.
        ValueError: If the distance is negative.
    """
    # Validate input
    if vehicle_type not in ['small', 'medium', 'large']:
        raise ValueError("Invalid vehicle type. Choose 'small', 'medium', or 'large'.")
    if delivery_time not in ['peak', 'non-peak']:
        raise ValueError("Invalid delivery time. Choose 'peak' or 'non-peak'.")
    if distance_km < 0:
        raise ValueError("Distance cannot be negative.")
    
    # Determine base rate based on vehicle type
    if vehicle_type == 'small':
        base_rate = BASE_RATE_SMALL_VAN
    elif vehicle_type == 'medium':
        base_rate = BASE_RATE_MEDIUM_VAN
    elif vehicle_type == 'large':
        base_rate = BASE_RATE_LARGE_VAN

    # Apply delivery time multiplier
    if delivery_time == 'peak':
        multiplier = PEAK_HOUR_SURCHARGE
    elif delivery_time == 'non-peak':
        multiplier = NON_PEAK_HOUR_DISCOUNT

    # Calculate total pricing
    total_cost = base_rate * distance_km * multiplier
    return round(total_cost, 2)

def main():
    """
    Main function to execute the pricing calculation.
    """
    print("Welcome to Refrigerated Van Rental Pricing Calculator!")
    
    try:
        # Get user input
        vehicle_type = input("Enter vehicle type ('small', 'medium', 'large'): ").strip().lower()
        distance_km = float(input("Enter distance in kilometers: "))
        delivery_time = input("Enter delivery time ('peak' or 'non-peak'): ").strip().lower()
        
        # Calculate pricing
        price = calculate_pricing(vehicle_type, distance_km, delivery_time)
        print(f"The total cost for your rental is: ${price:.2f}")
    
    except ValueError as e:
        # Handle errors gracefully
        print(f"Error: {e}")
    except Exception as e:
        # Catch any unforeseen errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
