"""
Generated Code Metadata:
========================
Original URL: https://maisemprestimos.online
Prompt: Write a Python script to calculate the CET (Custo Efetivo Total) for a loan based on user-provided data, including interest rate, fees, and repayment period.
Generated: DETERMINISTIC_475ba3cc09a45943
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
CET (Custo Efetivo Total) Calculator for Loans

Calculates the CET (Custo Efetivo Total) for a loan based on user-provided data.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_cet(principal, interest_rate, fees, repayment_period):
    """
    Calculates the CET (Custo Efetivo Total) for a loan.

    Args:
        principal (float): The initial loan amount.
        interest_rate (float): The annual interest rate as a decimal.
        fees (float): The total fees associated with the loan.
        repayment_period (int): The repayment period in years.

    Returns:
        float: The CET (Custo Efetivo Total) for the loan.

    Raises:
        ValueError: If any input value is invalid.
    """
    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")
    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative.")
    if fees < 0:
        raise ValueError("Fees cannot be negative.")
    if repayment_period <= 0:
        raise ValueError("Repayment period must be greater than zero.")

    # Calculate the total interest paid over the repayment period
    total_interest = principal * interest_rate * repayment_period

    # Calculate the total amount paid
    total_amount_paid = principal + total_interest + fees

    # Calculate the CET (Custo Efetivo Total) as an annual rate
    cet = (total_amount_paid / principal) ** (1 / repayment_period) - 1

    return cet


def main():
    try:
        # Get user input
        principal = float(input("Enter the loan amount: R$ "))
        interest_rate = float(input("Enter the annual interest rate (in %): ")) / 100
        fees = float(input("Enter the total fees: R$ "))
        repayment_period = int(input("Enter the repayment period (in years): "))

        # Calculate CET
        cet = calculate_cet(principal, interest_rate, fees, repayment_period)

        # Print the result
        print(f"CET (Custo Efetivo Total): {cet * 100:.2f}% per annum")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
