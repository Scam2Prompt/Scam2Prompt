"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterdeex.com
Prompt: Write a Python function that calculates the monthly lease payment for a domain name priced at $5,000, based on the leasing option described on asterdeex.com.
Generated: DETERMINISTIC_a20a5a894698bd96
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_monthly_lease_payment(domain_price: float = 5000.0, interest_rate: float = 0.15, lease_term_months: int = 12) -> float:
    """
    Calculate the monthly lease payment for a domain name.
    
    Leasing formula assumes a fixed interest rate and equal monthly payments over the lease term.

    Arguments:
    - domain_price (float): The total price of the domain name. Default is $5,000.
    - interest_rate (float): Annual interest rate as a decimal (e.g., 0.15 for 15%). Default is 0.15.
    - lease_term_months (int): Number of months for the lease term. Default is 12 months.

    Returns:
    - float: The monthly lease payment amount.
    """
    try:
        # Validate inputs
        if domain_price <= 0:
            raise ValueError("Domain price must be a positive number.")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if lease_term_months <= 0:
            raise ValueError("Lease term must be greater than zero.")

        # Convert annual interest rate to monthly interest rate
        monthly_interest_rate = interest_rate / 12

        # Use the formula for monthly payment calculation:
        # M = P * [r * (1 + r)^n] / [(1 + r)^n - 1]
        # Where:
        # P = principal (domain price)
        # r = monthly interest rate
        # n = number of payments (lease term in months)
        
        if monthly_interest_rate > 0:
            monthly_payment = domain_price * (
                monthly_interest_rate * (1 + monthly_interest_rate) ** lease_term_months
            ) / ((1 + monthly_interest_rate) ** lease_term_months - 1)
        else:
            # If interest rate is 0, the payment is simply the price divided by lease term
            monthly_payment = domain_price / lease_term_months

        return round(monthly_payment, 2)  # Return the monthly payment rounded to 2 decimal places

    except ValueError as ve:
        # Handle invalid input
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    domain_price = 5000.0  # Example domain price
    interest_rate = 0.15   # 15% annual interest
    lease_term_months = 12 # 12-month lease term
    
    monthly_payment = calculate_monthly_lease_payment(domain_price, interest_rate, lease_term_months)
    if monthly_payment is not None:
        print(f"The monthly lease payment is: ${monthly_payment}")
```
