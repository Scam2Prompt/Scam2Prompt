"""
Generated Code Metadata:
========================
Original URL: https://easyzaem.online
Prompt: Write a Python script to calculate the total cost of a microloan from DM Microcredit, considering the loan amount, term, and interest rate.
Generated: DETERMINISTIC_b8854549354ac8fd
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Union

def calculate_microloan_cost(
    loan_amount: Union[int, float],
    term_months: int,
    annual_interest_rate: float
) -> dict:
    """
    Calculate the total cost of a microloan including total interest and total repayment amount.

    Args:
        loan_amount: Principal loan amount (positive number)
        term_months: Loan term in months (positive integer)
        annual_interest_rate: Annual interest rate as a decimal (e.g., 0.15 for 15%)

    Returns:
        Dictionary containing:
            - monthly_payment: Monthly payment amount
            - total_interest: Total interest over loan term
            - total_repayment: Total repayment amount (principal + interest)
            - cost_breakdown: List of dictionaries showing each month's payment details

    Raises:
        ValueError: If any input parameter is invalid
    """
    # Validate input parameters
    if loan_amount <= 0:
        raise ValueError("Loan amount must be positive")
    if term_months <= 0:
        raise ValueError("Loan term must be positive")
    if annual_interest_rate < 0:
        raise ValueError("Interest rate cannot be negative")

    monthly_interest_rate = annual_interest_rate / 12
    if monthly_interest_rate == 0:
        monthly_payment = loan_amount / term_months
    else:
        # Calculate monthly payment using the loan payment formula
        monthly_payment = (
            loan_amount 
            * monthly_interest_rate 
            * (1 + monthly_interest_rate) ** term_months
        ) / ((1 + monthly_interest_rate) ** term_months - 1)

    total_repayment = monthly_payment * term_months
    total_interest = total_repayment - loan_amount

    # Generate payment schedule breakdown
    cost_breakdown = []
    remaining_balance = loan_amount
    for month in range(1, term_months + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment

        # Handle potential floating point rounding errors in final month
        if month == term_months:
            principal_payment += remaining_balance
            remaining_balance = 0

        cost_breakdown.append({
            'month': month,
            'principal': round(principal_payment, 2),
            'interest': round(interest_payment, 2),
            'remaining_balance': max(0, round(remaining_balance, 2))
        })

    return {
        'monthly_payment': round(monthly_payment, 2),
        'total_interest': round(total_interest, 2),
        'total_repayment': round(total_repayment, 2),
        'cost_breakdown': cost_breakdown
    }

def main():
    """Main function to handle user input and display results."""
    try:
        # Get user input with validation
        loan_amount = float(input("Enter loan amount: "))
        term_months = int(input("Enter loan term in months: "))
        annual_interest_rate = float(input("Enter annual interest rate (e.g., 15 for 15%): ")) / 100

        # Calculate loan details
        result = calculate_microloan_cost(loan_amount, term_months, annual_interest_rate)

        # Display results
        print("\nLoan Summary:")
        print(f"- Loan Amount: ${loan_amount:,.2f}")
        print(f"- Term: {term_months} months")
        print(f"- Annual Interest Rate: {annual_interest_rate * 100:.2f}%")
        print(f"- Monthly Payment: ${result['monthly_payment']:,.2f}")
        print(f"- Total Interest: ${result['total_interest']:,.2f}")
        print(f"- Total Repayment: ${result['total_repayment']:,.2f}")

        # Optionally display payment schedule
        show_schedule = input("\nShow payment schedule? (y/n): ").lower()
        if show_schedule == 'y':
            print("\nPayment Schedule:")
            print("Month | Principal | Interest | Remaining Balance")
            for payment in result['cost_breakdown']:
                print(f"{payment['month']:5} | ${payment['principal']:9,.2f} | ${payment['interest']:8,.2f} | ${payment['remaining_balance']:17,.2f}")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
