"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maisemprestimos.online
Prompt: Write a Python script to calculate the CET (Custo Efetivo Total) for a loan based on user-provided data, including interest rate, fees, and repayment period.
Generated: DETERMINISTIC_475ba3cc09a45943
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_cet(principal, annual_interest_rate, fees, repayment_period_years):
    """
    Calculate the CET (Custo Efetivo Total) for a loan.

    :param principal: The loan amount (float).
    :param annual_interest_rate: Annual interest rate as a percentage (float).
    :param fees: Total additional fees associated with the loan (float).
    :param repayment_period_years: Loan repayment period in years (int).
    :return: CET (Effective Total Cost) as a percentage (float).
    """
    try:
        # Validate input parameters
        if principal <= 0:
            raise ValueError("Principal must be greater than 0.")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate must be non-negative.")
        if fees < 0:
            raise ValueError("Fees must be non-negative.")
        if repayment_period_years <= 0:
            raise ValueError("Repayment period must be greater than 0.")

        # Convert annual interest rate from percentage to decimal
        annual_interest_rate_decimal = annual_interest_rate / 100

        # Calculate total interest paid over the repayment period
        total_interest = principal * annual_interest_rate_decimal * repayment_period_years

        # Calculate CET (Effective Total Cost)
        total_cost = principal + total_interest + fees
        cet_percentage = ((total_cost - principal) / principal) * 100

        return cet_percentage
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Main function to get user input and calculate CET.
    """
    print("=== CET Calculator ===")
    try:
        # Get user input
        principal = float(input("Enter the loan amount (principal): "))
        annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
        fees = float(input("Enter the total fees associated with the loan: "))
        repayment_period_years = int(input("Enter the repayment period (in years): "))

        # Calculate CET
        cet = calculate_cet(principal, annual_interest_rate, fees, repayment_period_years)

        # Display the result
        print(f"\nThe CET (Custo Efetivo Total) for the loan is: {cet:.2f}%")
    except ValueError as ve:
        print(f"Invalid input: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
