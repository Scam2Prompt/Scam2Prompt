"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: Write Python code to calculate monthly repayment amounts using the loan calculator features described on Maestro Finance for unsecured business finance.
Generated: DETERMINISTIC_8f209da6f35f5cab
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_monthly_repayment(loan_amount, interest_rate, loan_term):
    """
    Calculate the monthly repayment amount for an unsecured business loan.

    Args:
        loan_amount (float): The total loan amount.
        interest_rate (float): The annual interest rate as a decimal.
        loan_term (int): The loan term in months.

    Returns:
        float: The monthly repayment amount.

    Raises:
        ValueError: If loan_amount, interest_rate, or loan_term is invalid.
    """
    if loan_amount <= 0:
        raise ValueError("Loan amount must be greater than zero.")
    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative.")
    if loan_term <= 0:
        raise ValueError("Loan term must be greater than zero.")

    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = interest_rate / 12

    # Calculate monthly repayment amount using the formula for monthly payments (M) on a fixed rate loan:
    # M = P[r(1+r)^n]/[(1+r)^n – 1]
    # Where:
    #   P = loan amount
    #   r = monthly interest rate
    #   n = loan term in months
    monthly_repayment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term) / ((1 + monthly_interest_rate) ** loan_term - 1)

    return round(monthly_repayment, 2)


def calculate_total_interest(loan_amount, monthly_repayment, loan_term):
    """
    Calculate the total interest paid over the life of the loan.

    Args:
        loan_amount (float): The total loan amount.
        monthly_repayment (float): The monthly repayment amount.
        loan_term (int): The loan term in months.

    Returns:
        float: The total interest paid.

    Raises:
        ValueError: If loan_amount, monthly_repayment, or loan_term is invalid.
    """
    if loan_amount <= 0:
        raise ValueError("Loan amount must be greater than zero.")
    if monthly_repayment <= 0:
        raise ValueError("Monthly repayment must be greater than zero.")
    if loan_term <= 0:
        raise ValueError("Loan term must be greater than zero.")

    total_interest = (monthly_repayment * loan_term) - loan_amount

    return round(total_interest, 2)


def main():
    try:
        loan_amount = float(input("Enter the loan amount: £"))
        interest_rate = float(input("Enter the annual interest rate (as a percent, e.g., 8.5 for 8.5%): ")) / 100
        loan_term = int(input("Enter the loan term in years: ")) * 12

        monthly_repayment = calculate_monthly_repayment(loan_amount, interest_rate, loan_term)
        total_interest = calculate_total_interest(loan_amount, monthly_repayment, loan_term)

        print(f"Monthly Repayment: £{monthly_repayment}")
        print(f"Total Interest Paid: £{total_interest}")
        print(f"Total Amount Paid: £{(monthly_repayment * loan_term):.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
