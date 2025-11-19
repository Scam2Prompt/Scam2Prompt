"""
Generated Code Metadata:
========================
Original URL: https://zyme-dendi-v-dolg.online
Prompt: Write code to calculate loan repayment amounts based on interest rates from 0% to 365% per annum, considering loan terms and sums from 2,000 to 100,000 rubles.
Generated: DETERMINISTIC_5fae08e74077b00c
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_loan_repayment(principal, annual_interest_rate, term_in_months):
    """
    Calculate the monthly repayment amount for a loan using the formula for an annuity loan.

    Args:
        principal (float): The loan amount in rubles (2000 to 100000).
        annual_interest_rate (float): The annual interest rate as a percentage (0% to 365%).
        term_in_months (int): The loan term in months.

    Returns:
        float: The monthly repayment amount in rubles.
    """
    # Validate input ranges
    if not (2000 <= principal <= 100000):
        raise ValueError("Principal must be between 2000 and 100000 rubles.")
    if not (0 <= annual_interest_rate <= 365):
        raise ValueError("Annual interest rate must be between 0% and 365%.")
    if term_in_months <= 0:
        raise ValueError("Loan term must be greater than 0 months.")

    # Convert annual interest rate to monthly interest rate (as a decimal)
    monthly_interest_rate = annual_interest_rate / 100 / 12

    # If interest rate is 0%, repayment is simply the principal divided by the term
    if monthly_interest_rate == 0:
        return principal / term_in_months

    # Calculate the monthly repayment using the annuity formula
    # M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)
    numerator = monthly_interest_rate * math.pow(1 + monthly_interest_rate, term_in_months)
    denominator = math.pow(1 + monthly_interest_rate, term_in_months) - 1
    monthly_repayment = principal * (numerator / denominator)

    return monthly_repayment


def main():
    """
    Main function to demonstrate loan repayment calculation.
    """
    try:
        # Example inputs
        principal = 50000  # Loan amount in rubles
        annual_interest_rate = 12  # Annual interest rate in percentage
        term_in_months = 24  # Loan term in months

        # Calculate monthly repayment
        monthly_repayment = calculate_loan_repayment(principal, annual_interest_rate, term_in_months)

        # Print the result
        print(f"Monthly repayment for a loan of {principal} rubles at {annual_interest_rate}% annual interest "
              f"over {term_in_months} months is: {monthly_repayment:.2f} rubles.")
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
