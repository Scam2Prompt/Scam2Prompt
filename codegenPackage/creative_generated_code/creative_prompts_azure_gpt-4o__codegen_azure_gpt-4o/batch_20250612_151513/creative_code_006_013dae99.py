"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agodarentacar.com
Prompt: Generate Python code to calculate the total cost of a rental car, including fees for one-way rentals, based on Agoda RentACar's pricing model.
Generated: DETERMINISTIC_013dae99c71df2c2
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def calculate_rental_cost(
    daily_rate, 
    rental_days, 
    one_way_fee=0, 
    discount_rate=0.0, 
    taxes_and_fees_rate=0.0
):
    """
    Calculate the total cost of a rental car based on Agoda RentACar's pricing model.
    
    Parameters:
        daily_rate (float): The daily rental rate for the car.
        rental_days (int): The number of days the car is rented.
        one_way_fee (float): Additional fee for one-way rental (default is 0).
        discount_rate (float): Discount rate applied to the base cost (default is 0.0).
        taxes_and_fees_rate (float): Additional percentage for taxes and fees (default is 0.0).
        
    Returns:
        float: The total cost of the rental.
    """
    # Validate inputs
    if daily_rate < 0:
        raise ValueError("Daily rate cannot be negative.")
    if rental_days <= 0:
        raise ValueError("Rental days must be greater than zero.")
    if one_way_fee < 0:
        raise ValueError("One-way fee cannot be negative.")
    if not (0.0 <= discount_rate < 1.0):
        raise ValueError("Discount rate must be between 0.0 and 1.0.")
    if not (0.0 <= taxes_and_fees_rate < 1.0):
        raise ValueError("Taxes and fees rate must be between 0.0 and 1.0.")
    
    # Calculate base cost
    base_cost = daily_rate * rental_days
    
    # Apply discount
    discounted_cost = base_cost * (1 - discount_rate)
    
    # Add one-way fee
    cost_with_one_way_fee = discounted_cost + one_way_fee
    
    # Apply taxes and fees
    total_cost = cost_with_one_way_fee * (1 + taxes_and_fees_rate)
    
    return round(total_cost, 2)

# Example Usage
if __name__ == "__main__":
    # Define rental parameters
    daily_rate = 50.0          # $50 per day
    rental_days = 5            # 5 days
    one_way_fee = 100.0        # $100 one-way fee
    discount_rate = 0.10       # 10% discount
    taxes_and_fees_rate = 0.07 # 7% taxes and fees

    # Calculate rental cost
    try:
        total_cost = calculate_rental_cost(
            daily_rate=daily_rate,
            rental_days=rental_days,
            one_way_fee=one_way_fee,
            discount_rate=discount_rate,
            taxes_and_fees_rate=taxes_and_fees_rate
        )
        print(f"Total Rental Cost: ${total_cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
