"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oke-abs.xyz
Prompt: Write a function that calculates the monthly lease payments for a domain name priced at $5,000, incorporating the "Lease to Own" option mentioned on the site.
Generated: DETERMINISTIC_de2a383ae33be423
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_monthly_lease_payment(domain_price, lease_to_own_months=12, interest_rate=0.05):
    """
    Calculate the monthly lease payment for a domain name under a "Lease to Own" option.

    Args:
        domain_price (float): The total price of the domain name (e.g., $5000).
        lease_to_own_months (int): The number of months to pay off the domain lease. Default is 12 months.
        interest_rate (float): The annual interest rate for the lease. Default is 5% (0.05).

    Returns:
        float: The monthly lease payment amount.

    Raises:
        ValueError: If domain_price is less than or equal to zero, or lease_to_own_months is less than 1.
    """
    # Validate the inputs
    if domain_price <= 0:
        raise ValueError("Domain price must be greater than zero.")
    if lease_to_own_months < 1:
        raise ValueError("Lease-to-own months must be at least 1.")

    # Calculate the monthly interest rate
    monthly_interest_rate = interest_rate / 12

    # Monthly payment formula for lease-to-own with interest
    # Formula: P = (r * PV) / (1 - (1 + r)^(-n))
    # P = monthly payment
    # r = monthly interest rate
    # PV = present value (domain price)
    # n = number of months

    try:
        monthly_payment = (
            (monthly_interest_rate * domain_price) /
            (1 - (1 + monthly_interest_rate) ** -lease_to_own_months)
        )
    except ZeroDivisionError:
        # Handle edge case where interest rate is zero (i.e., no interest)
        monthly_payment = domain_price / lease_to_own_months

    return round(monthly_payment, 2)  # Round to 2 decimal places for currency

# Example usage
if __name__ == "__main__":
    domain_price = 5000  # Domain price in dollars
    lease_to_own_months = 12  # Lease duration in months
    interest_rate = 0.05  # Annual interest rate (5%)

    try:
        monthly_payment = calculate_monthly_lease_payment(
            domain_price, lease_to_own_months, interest_rate
        )
        print(f"Monthly Lease Payment: ${monthly_payment}")
    except ValueError as e:
        print(f"Error: {e}")
```
