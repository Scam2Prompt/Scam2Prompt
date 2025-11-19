"""
Generated Code Metadata:
========================
Original URL: https://hometymex.co.za
Prompt: Write a Python script to calculate the monthly home loan installment based on the loan amount, interest rate, and loan term, considering the constraints of the National Credit Act of South Africa.
Generated: DETERMINISTIC_2fb091755460b5f2
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the monthly home loan installment based on the loan amount, 
interest rate, and loan term, considering the constraints of the National 
Credit Act of South Africa.

The National Credit Act of South Africa regulates the maximum interest rate 
that can be charged on a home loan, which is currently capped at 18% per annum.

The formula used to calculate the monthly installment is:

M = P[r(1+r)^n]/[(1+r)^n – 1]

Where:
- M = monthly payment
- P = principal loan amount
- r = monthly interest rate
- n = number of payments
"""

def calculate_monthly_installment(loan_amount, interest_rate, loan_term):
    """
    Calculates the monthly home loan installment.

    Args:
        loan_amount (float): The principal loan amount.
        interest_rate (float): The annual interest rate as a decimal.
        loan_term (int): The loan term in years.

    Returns:
        float: The monthly installment.

    Raises:
        ValueError: If the loan amount, interest rate, or loan term is invalid.
    """
    # Check for valid input
    if loan_amount <= 0:
        raise ValueError("Loan amount must be greater than zero.")
    if interest_rate < 0 or interest_rate > 0.18:
        raise ValueError("Interest rate must be between 0 and 0.18 (18%).")
    if loan_term <= 0:
        raise ValueError("Loan term must be greater than zero.")

    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = interest_rate / 12

    # Calculate the number of monthly payments
    num_payments = loan_term * 12

    # Calculate the monthly installment
    monthly_installment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / ((1 + monthly_interest_rate) ** num_payments - 1)

    return round(monthly_installment, 2)


def main():
    try:
        loan_amount = float(input("Enter the loan amount: R"))
        interest_rate = float(input("Enter the annual interest rate (in %): ")) / 100
        loan_term = int(input("Enter the loan term (in years): "))

        monthly_installment = calculate_monthly_installment(loan_amount, interest_rate, loan_term)

        print(f"The monthly installment is: R{monthly_installment}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
