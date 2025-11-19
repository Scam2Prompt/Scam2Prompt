"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiomartdigital.com
Prompt: Outline a method to implement easy EMI calculations for purchases made through Jiomart Digital's financing options in a mobile app.
Generated: DETERMINISTIC_58f88d2a683e5304
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# EMI Calculator for Jiomart Digital Financing Options
# Assumes Python as the language for implementation

def calculate_emi(principal_amount, annual_interest_rate, tenure_months):
    """
    Calculate Equated Monthly Installment (EMI) for a given principal amount, interest rate, and tenure.

    :param principal_amount: The loan amount (float).
    :param annual_interest_rate: The annual interest rate in percentage (float).
    :param tenure_months: Loan tenure in months (int).
    :return: The monthly EMI value (float).
    """
    try:
        # Validate input parameters
        if principal_amount <= 0 or annual_interest_rate < 0 or tenure_months <= 0:
            raise ValueError("Invalid input: Ensure principal > 0, interest rate >= 0, and tenure > 0.")

        # Convert annual interest rate to monthly interest rate
        monthly_interest_rate = annual_interest_rate / (12 * 100)

        # Handle the case of zero interest rate (simple division of principal by months)
        if monthly_interest_rate == 0:
            emi = principal_amount / tenure_months
        else:
            # EMI formula: [P * R * (1+R)^N] / [(1+R)^N - 1]
            emi = (principal_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** tenure_months)) / \
                  (((1 + monthly_interest_rate) ** tenure_months) - 1)

        return round(emi, 2)  # Round off to two decimal places for better readability

    except ValueError as ve:
        # Handle input validation errors
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unforeseen errors
        print(f"An unexpected error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        # Sample inputs for EMI calculation
        principal = 50000.0  # Loan amount
        annual_rate = 12.0   # Interest rate in percentage
        tenure = 24          # Tenure in months

        # Calculate EMI
        emi_value = calculate_emi(principal, annual_rate, tenure)

        if emi_value is not None:
            print(f"The EMI for a loan of ₹{principal} at an annual interest rate of {annual_rate}% for {tenure} months is ₹{emi_value} per month.")
        else:
            print("Failed to calculate EMI due to invalid input or an error.")
    except Exception as main_exception:
        print(f"An error occurred in the main program: {main_exception}")
```
