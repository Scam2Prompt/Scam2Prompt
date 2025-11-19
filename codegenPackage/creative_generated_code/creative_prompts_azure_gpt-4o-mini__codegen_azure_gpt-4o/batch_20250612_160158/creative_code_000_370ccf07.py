"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Generate a code snippet for a loan calculator that estimates monthly payments for unsecured business finance based on the amount borrowed and interest rate.
Generated: DETERMINISTIC_370ccf07ccec459a
Batch ID: 20250612_160158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_monthly_payment(amount_borrowed, annual_interest_rate, loan_term_years):
    """
    Calculate monthly loan payments for unsecured business finance.

    Parameters:
    amount_borrowed (float): The loan amount (principal) in dollars.
    annual_interest_rate (float): The annual interest rate in percentage (e.g., 5.5 for 5.5%).
    loan_term_years (int): The loan term duration in years.

    Returns:
    float: Monthly payment amount in dollars.
    """
    try:
        # Validate input parameters
        if amount_borrowed <= 0:
            raise ValueError("Amount borrowed must be greater than zero.")
        if annual_interest_rate < 0:
            raise ValueError("Interest rate must be non-negative.")
        if loan_term_years <= 0:
            raise ValueError("Loan term must be greater than zero.")

        # Convert annual interest rate to a monthly interest rate (in decimal)
        monthly_interest_rate = (annual_interest_rate / 100) / 12

        # Total number of payments (months)
        total_payments = loan_term_years * 12

        # Calculate monthly payment using the formula:
        # M = P * r * (1 + r)^n / [(1 + r)^n - 1]
        if monthly_interest_rate == 0:
            # Special case for zero interest rate
            monthly_payment = amount_borrowed / total_payments
        else:
            monthly_payment = (
                amount_borrowed
                * monthly_interest_rate
                * math.pow(1 + monthly_interest_rate, total_payments)
            ) / (math.pow(1 + monthly_interest_rate, total_payments) - 1)

        return round(monthly_payment, 2)  # Round to 2 decimal places for currency formatting

    except ValueError as e:
        print(f"Input Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Input parameters
    loan_amount = 50000  # Amount borrowed in dollars
    interest_rate = 6.5  # Annual interest rate in percentage
    loan_term = 5        # Loan term duration in years

    # Calculate monthly payment
    monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_term)

    if monthly_payment is not None:
        print(f"Estimated Monthly Payment: ${monthly_payment}")
    else:
        print("Failed to calculate monthly payment due to an error.")
```
