"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.reliableridesllc.org
Prompt: Write a function that calculates the rental price per day for a vehicle based on the model and any applicable discounts, inspired by the pricing structure of Reliable Rides LLC.
Generated: DETERMINISTIC_167cf843b1e1129e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code to calculate rental price per day for a vehicle based on model and discounts.

def calculate_rental_price(vehicle_model, discount_code=None):
    """
    Calculate rental price per day for a vehicle based on the model and applicable discounts.
    
    Args:
        vehicle_model (str): The model of the vehicle.
        discount_code (str, optional): A discount code that may apply.

    Returns:
        float: The rental price per day after applying the discount.
    """
    # Base price dictionary for different vehicle models
    base_prices = {
        "sedan": 50.0,       # $50 per day
        "suv": 75.0,         # $75 per day
        "truck": 100.0,      # $100 per day
        "minivan": 60.0,     # $60 per day
        "sports_car": 150.0  # $150 per day
    }
    
    # Discount codes and their respective percentage discounts
    discount_codes = {
        "SUMMER10": 10,      # 10% discount
        "WINTER15": 15,      # 15% discount
        "LOYALTY20": 20      # 20% discount
    }

    try:
        # Retrieve the base price for the specified vehicle model
        base_price = base_prices.get(vehicle_model.lower())
        
        # Raise an exception if the vehicle model is invalid
        if base_price is None:
            raise ValueError(f"Invalid vehicle model: {vehicle_model}")
        
        # Retrieve the discount percentage based on the discount code
        discount_percentage = discount_codes.get(discount_code.upper()) if discount_code else 0
        
        # Validate discount code
        if discount_code and discount_percentage is None:
            raise ValueError(f"Invalid discount code: {discount_code}")
        
        # Apply the discount to the base price
        final_price = base_price * (1 - discount_percentage / 100)
        
        return round(final_price, 2)  # Return the final price rounded to two decimal places
    
    except ValueError as e:
        # Handle invalid inputs gracefully
        print(f"Error: {e}")
        return None

# Example usage:
# rental_price = calculate_rental_price("SUV", "SUMMER10")
# print(rental_price)
```
