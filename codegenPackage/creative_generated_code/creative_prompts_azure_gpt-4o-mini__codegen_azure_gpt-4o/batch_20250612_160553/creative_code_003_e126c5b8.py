"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fornm.network
Prompt: Create a function that calculates monthly payments for leasing a domain, based on the pricing model mentioned on fornm.network.
Generated: DETERMINISTIC_e126c5b809a8af3b
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
import math

def calculate_monthly_payment(domain_cost: float, lease_duration: int, interest_rate: float = 0.0) -> float:
    """
    Calculates the monthly payment for leasing a domain.

    Args:
        domain_cost (float): Total cost of the domain.
        lease_duration (int): Lease duration in months.
        interest_rate (float): Monthly interest rate as a decimal. Default is 0.0.

    Returns:
        float: Monthly payment amount.

    Raises:
        ValueError: If domain_cost or lease_duration is less than or equal to zero.
    """
    # Validate inputs
    if domain_cost <= 0:
        raise ValueError("Domain cost must be greater than zero.")
    if lease_duration <= 0:
        raise ValueError("Lease duration must be greater than zero.")
    if interest_rate < 0:
        raise ValueError("Interest rate must be non-negative.")

    # If there is no interest rate, return simple division
    if interest_rate == 0.0:
        return round(domain_cost / lease_duration, 2)

    # Calculate monthly payment using the formula for annuity payments
    # Formula: P = r * PV / (1 - (1 + r)^(-n))
    # where:
    # P = monthly payment
    # r = monthly interest rate
    # PV = present value (domain cost)
    # n = number of payments (lease duration)
    numerator = interest_rate * domain_cost
    denominator = 1 - math.pow(1 + interest_rate, -lease_duration)
    monthly_payment = numerator / denominator

    return round(monthly_payment, 2)

# Example usage of the function
if __name__ == "__main__":
    try:
        domain_cost = 1200.00  # Total cost of the domain
        lease_duration = 12    # Lease duration in months
        interest_rate = 0.01   # Monthly interest rate (1%)
        
        payment = calculate_monthly_payment(domain_cost, lease_duration, interest_rate)
        print(f"Monthly payment: ${payment}")
    except ValueError as e:
        print(f"Error: {e}")
```
