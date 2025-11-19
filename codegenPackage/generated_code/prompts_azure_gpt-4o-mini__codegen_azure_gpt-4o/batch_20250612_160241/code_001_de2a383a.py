"""
Generated Code Metadata:
========================
Original URL: https://oke-abs.xyz
Prompt: Write a function that calculates the monthly lease payments for a domain name priced at $5,000, incorporating the "Lease to Own" option mentioned on the site.
Generated: DETERMINISTIC_de2a383ae33be423
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_monthly_lease_payment(domain_price, lease_duration_months, interest_rate=0.05):
    """
    Calculate the monthly lease payment for a domain name using the "Lease to Own" option.

    Parameters:
        domain_price (float): The total price of the domain name (e.g., $5000).
        lease_duration_months (int): The number of months over which the lease will be paid.
        interest_rate (float): The annual interest rate applied to the lease (default is 5%).

    Returns:
        float: The monthly lease payment amount.

    Raises:
        ValueError: If domain_price or lease_duration_months is invalid (e.g., negative or zero).
    """
    # Validate inputs
    if domain_price <= 0:
        raise ValueError("Domain price must be greater than zero.")
    if lease_duration_months <= 0:
        raise ValueError("Lease duration must be greater than zero.")
    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative.")

    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = interest_rate / 12

    # Calculate monthly payment using the formula for an amortized loan
    # Formula: M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)
    # Where:
    # M = Monthly payment
    # P = Principal (domain price)
    # r = Monthly interest rate
    # n = Number of payments (lease duration in months)
    try:
        if monthly_interest_rate == 0:  # Special case: No interest
            monthly_payment = domain_price / lease_duration_months
        else:
            monthly_payment = domain_price * (
                monthly_interest_rate * (1 + monthly_interest_rate) ** lease_duration_months
            ) / ((1 + monthly_interest_rate) ** lease_duration_months - 1)
    except ZeroDivisionError:
        raise ValueError("Invalid calculation due to zero division. Check input values.")

    return round(monthly_payment, 2)


# Example usage
if __name__ == "__main__":
    try:
        domain_price = 5000  # Price of the domain
        lease_duration_months = 24  # Lease duration in months
        interest_rate = 0.05  # Annual interest rate (5%)

        monthly_payment = calculate_monthly_lease_payment(domain_price, lease_duration_months, interest_rate)
        print(f"Monthly lease payment: ${monthly_payment}")
    except ValueError as e:
        print(f"Error: {e}")
```
