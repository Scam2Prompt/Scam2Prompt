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
import math

def calculate_monthly_installment(loan_amount, annual_interest_rate, loan_term_years):
    """
    Calculate the monthly home loan installment using the formula for an amortizing loan.

    Parameters:
    loan_amount (float): The total amount of the loan.
    annual_interest_rate (float): The annual interest rate (as a percentage).
    loan_term_years (int): The term of the loan in years.

    Returns:
    float: The monthly installment amount.
    """
    # Validate input parameters
    if loan_amount <= 0:
        raise ValueError("Loan amount must be greater than zero.")
    if annual_interest_rate < 0:
        raise ValueError("Annual interest rate cannot be negative.")
    if loan_term_years <= 0:
        raise ValueError("Loan term must be greater than zero.")

    # Convert annual interest rate to a monthly interest rate (decimal)
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    # Total number of payments (months)
    total_payments = loan_term_years * 12

    # Calculate monthly installment using the formula
    if monthly_interest_rate == 0:  # Handle case of zero interest rate
        return loan_amount / total_payments

    monthly_installment = (loan_amount * monthly_interest_rate) / (1 - math.pow(1 + monthly_interest_rate, -total_payments))
    
    return monthly_installment

def main():
    """
    Main function to execute the loan installment calculation.
    """
    try:
        # Input values for loan calculation
        loan_amount = float(input("Enter the loan amount: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        loan_term_years = int(input("Enter the loan term (in years): "))

        # Calculate the monthly installment
        monthly_installment = calculate_monthly_installment(loan_amount, annual_interest_rate, loan_term_years)

        # Output the result
        print(f"The monthly home loan installment is: R{monthly_installment:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
