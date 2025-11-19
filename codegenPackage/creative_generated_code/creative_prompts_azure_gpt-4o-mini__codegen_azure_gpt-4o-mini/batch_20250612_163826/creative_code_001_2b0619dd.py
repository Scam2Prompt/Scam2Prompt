"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finflix.me
Prompt: Write a Python script that calculates monthly payments for a loan up to 7,500€ with varying terms (12 to 120 months) and an interest rate of 4.9%, as described on flix-fin.me.
Generated: DETERMINISTIC_2b0619ddefb0e279
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_monthly_payment(principal: float, annual_interest_rate: float, months: int) -> float:
    """
    Calculate the monthly payment for a loan.

    :param principal: The loan amount (in euros)
    :param annual_interest_rate: The annual interest rate (in percentage)
    :param months: The loan term in months
    :return: The monthly payment amount
    """
    # Convert annual interest rate from percentage to decimal
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Calculate monthly payment using the formula
    if monthly_interest_rate == 0:
        return principal / months  # No interest case

    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months)
    return monthly_payment

def main():
    # Constants
    MAX_LOAN_AMOUNT = 7500.0  # Maximum loan amount in euros
    ANNUAL_INTEREST_RATE = 4.9  # Fixed annual interest rate in percentage
    MIN_TERM_MONTHS = 12  # Minimum loan term in months
    MAX_TERM_MONTHS = 120  # Maximum loan term in months

    try:
        # User input for loan amount and term
        principal = float(input(f"Enter the loan amount (up to {MAX_LOAN_AMOUNT}€): "))
        if principal <= 0 or principal > MAX_LOAN_AMOUNT:
            raise ValueError(f"Loan amount must be between 0 and {MAX_LOAN_AMOUNT}€.")

        term = int(input(f"Enter the loan term in months (between {MIN_TERM_MONTHS} and {MAX_TERM_MONTHS}): "))
        if term < MIN_TERM_MONTHS or term > MAX_TERM_MONTHS:
            raise ValueError(f"Loan term must be between {MIN_TERM_MONTHS} and {MAX_TERM_MONTHS} months.")

        # Calculate monthly payment
        monthly_payment = calculate_monthly_payment(principal, ANNUAL_INTEREST_RATE, term)

        # Output result
        print(f"\nFor a loan amount of {principal:.2f}€ over {term} months at an interest rate of {ANNUAL_INTEREST_RATE}%,")
        print(f"the monthly payment will be: {monthly_payment:.2f}€.")

    except ValueError as e:
        print(f"Input error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
