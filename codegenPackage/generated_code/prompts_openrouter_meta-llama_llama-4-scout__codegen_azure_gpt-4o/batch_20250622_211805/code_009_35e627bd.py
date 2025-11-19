"""
Generated Code Metadata:
========================
Original URL: https://zyme-store.online
Prompt: Create loan calculator function considering loan amount, repayment term, interest rate of various MFOs listed on website.
Generated: DETERMINISTIC_35e627bdf7040fd6
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

def loan_calculator(loan_amount, repayment_term, mfo_interest_rates):
    """
    Calculate the monthly repayment amount for a loan from various MFOs.

    Parameters:
        loan_amount (float): The principal loan amount.
        repayment_term (int): The repayment term in months.
        mfo_interest_rates (dict): A dictionary where keys are MFO names and values are annual interest rates (in percentage).

    Returns:
        dict: A dictionary where keys are MFO names and values are the monthly repayment amounts.
    """
    if loan_amount <= 0:
        raise ValueError("Loan amount must be greater than 0.")
    if repayment_term <= 0:
        raise ValueError("Repayment term must be greater than 0.")
    if not mfo_interest_rates or not isinstance(mfo_interest_rates, dict):
        raise ValueError("MFO interest rates must be a non-empty dictionary.")

    monthly_repayments = {}

    for mfo, annual_rate in mfo_interest_rates.items():
        if annual_rate < 0:
            raise ValueError(f"Interest rate for {mfo} must be non-negative.")
        
        # Convert annual interest rate to monthly interest rate
        monthly_rate = annual_rate / 100 / 12

        # Calculate monthly repayment using the formula for an annuity loan
        if monthly_rate == 0:  # Handle zero interest rate case
            monthly_payment = loan_amount / repayment_term
        else:
            monthly_payment = loan_amount * (monthly_rate * math.pow(1 + monthly_rate, repayment_term)) / (math.pow(1 + monthly_rate, repayment_term) - 1)
        
        # Store the result in the dictionary
        monthly_repayments[mfo] = round(monthly_payment, 2)

    return monthly_repayments


# Example usage:
if __name__ == "__main__":
    try:
        loan_amount = 10000  # Example loan amount
        repayment_term = 12  # Example repayment term in months
        mfo_interest_rates = {
            "MFO1": 12.0,  # 12% annual interest rate
            "MFO2": 15.0,  # 15% annual interest rate
            "MFO3": 0.0    # 0% annual interest rate (interest-free loan)
        }

        results = loan_calculator(loan_amount, repayment_term, mfo_interest_rates)
        print("Monthly repayment amounts:")
        for mfo, payment in results.items():
            print(f"{mfo}: ${payment}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
