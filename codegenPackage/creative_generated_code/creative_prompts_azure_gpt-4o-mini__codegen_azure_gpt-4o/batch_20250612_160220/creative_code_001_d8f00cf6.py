"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://storyi.foundation
Prompt: Write a function that calculates the monthly lease payment for a domain name priced at $5,000, based on the lease-to-own model mentioned on storyi.foundation.
Generated: DETERMINISTIC_d8f00cf651cfa4a9
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary library for mathematical operations
from decimal import Decimal

def calculate_monthly_lease_payment(domain_price, lease_duration_months):
    """
    Calculate the monthly lease payment for a domain name in a lease-to-own model.

    Parameters:
        domain_price (Decimal): The total price of the domain (e.g., 5000).
        lease_duration_months (int): The number of months to lease the domain.

    Returns:
        Decimal: The monthly lease payment amount.
    """
    try:
        # Validate inputs
        if domain_price <= 0:
            raise ValueError("Domain price must be greater than zero.")
        if lease_duration_months <= 0:
            raise ValueError("Lease duration must be greater than zero.")

        # Calculate the monthly lease payment as the domain price divided by the lease duration
        monthly_payment = domain_price / lease_duration_months
        return monthly_payment
    
    except Exception as e:
        # Handle unexpected errors and provide feedback
        print(f"An error occurred: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Define constants
    DOMAIN_PRICE = Decimal("5000")  # Price of the domain in USD
    LEASE_DURATION_MONTHS = 12      # Number of months for the lease-to-own model

    # Calculate the monthly lease payment
    monthly_payment = calculate_monthly_lease_payment(DOMAIN_PRICE, LEASE_DURATION_MONTHS)

    if monthly_payment is not None:
        print(f"Monthly Lease Payment: ${monthly_payment:.2f}")
```
