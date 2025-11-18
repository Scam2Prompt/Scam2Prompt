"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autoswiftly.com
Prompt: Develop a function that calculates monthly lease payments for a car using parameters like vehicle price, interest rate, and lease term, inspired by AutoSwiftly's loan calculator.
Generated: DETERMINISTIC_059d1eeeb251e93d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Union

def calculate_monthly_lease_payment(vehicle_price: Union[int, float], 
                                     interest_rate: float, 
                                     lease_term: int) -> float:
    """
    Calculates the monthly lease payment for a vehicle.

    Parameters:
    vehicle_price (Union[int, float]): The price of the vehicle (principal amount).
    interest_rate (float): The annual interest rate (in percentage, e.g., 5 for 5%).
    lease_term (int): The lease term in months.

    Returns:
    float: The monthly lease payment.
    """

    # Validate inputs
    if vehicle_price <= 0:
        raise ValueError("Vehicle price must be a positive number.")
    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative.")
    if lease_term <= 0:
        raise ValueError("Lease term must be a positive number.")

    # Convert annual interest rate to monthly interest rate (as a decimal)
    monthly_interest_rate = interest_rate / 100 / 12

    # Error handling for zero interest rate
    if monthly_interest_rate == 0:
        # If there's no interest, simply divide the price by the lease term
        return round(vehicle_price / lease_term, 2)

    # Calculate monthly lease payment using the formula for an amortized loan
    # Formula: M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)
    # Where:
    # M = monthly payment
    # P = vehicle price
    # r = monthly interest rate
    # n = lease term (number of payments)
    numerator = vehicle_price * monthly_interest_rate * (1 + monthly_interest_rate) ** lease_term
    denominator = (1 + monthly_interest_rate) ** lease_term - 1

    monthly_payment = numerator / denominator

    # Round the result to 2 decimal places for currency formatting
    return round(monthly_payment, 2)

# Example usage (uncomment to test the function):
# vehicle_price = 30000
# interest_rate = 5
# lease_term = 36
# print(calculate_monthly_lease_payment(vehicle_price, interest_rate, lease_term))
```
