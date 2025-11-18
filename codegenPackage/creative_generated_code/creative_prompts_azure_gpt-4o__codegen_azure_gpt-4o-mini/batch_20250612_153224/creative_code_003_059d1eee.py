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
def calculate_monthly_lease_payment(vehicle_price, interest_rate, lease_term_months, down_payment=0):
    """
    Calculate the monthly lease payment for a car.

    Args:
        vehicle_price (float): The total price of the vehicle.
        interest_rate (float): The annual interest rate (as a percentage).
        lease_term_months (int): The lease term in months.
        down_payment (float): The down payment made on the vehicle (default is 0).

    Returns:
        float: The calculated monthly lease payment.

    Raises:
        ValueError: If any of the input values are negative or if lease_term_months is zero.
    """

    # Validate inputs
    if vehicle_price < 0:
        raise ValueError("Vehicle price cannot be negative.")
    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative.")
    if lease_term_months <= 0:
        raise ValueError("Lease term must be greater than zero.")
    if down_payment < 0:
        raise ValueError("Down payment cannot be negative.")

    # Calculate the financed amount
    financed_amount = vehicle_price - down_payment

    # Convert annual interest rate to a monthly interest rate
    monthly_interest_rate = (interest_rate / 100) / 12

    # Calculate the monthly lease payment using the formula for an annuity
    if monthly_interest_rate > 0:
        monthly_payment = (financed_amount * monthly_interest_rate) / \
                          (1 - (1 + monthly_interest_rate) ** -lease_term_months)
    else:
        # If interest rate is 0, just divide the financed amount by the lease term
        monthly_payment = financed_amount / lease_term_months

    return monthly_payment

# Example usage (uncomment to run):
# vehicle_price = 30000
# interest_rate = 5
# lease_term_months = 36
# down_payment = 2000
# monthly_payment = calculate_monthly_lease_payment(vehicle_price, interest_rate, lease_term_months, down_payment)
# print(f"The monthly lease payment is: ${monthly_payment:.2f}")
```
