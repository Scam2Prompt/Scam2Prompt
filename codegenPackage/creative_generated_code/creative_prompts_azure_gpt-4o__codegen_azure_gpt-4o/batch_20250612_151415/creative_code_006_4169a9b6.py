"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Write a Python function to convert credit card payments into EMIs, inspired by the Credit Card EMI Converter feature on the IFSC Finder site.
Generated: DETERMINISTIC_4169a9b6a985cea1
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from math import pow


def calculate_emi(principal, annual_interest_rate, months):
    """
    Calculate the Equated Monthly Installment (EMI) for credit card payments.

    Parameters:
        principal (float): The total amount to be converted into EMI (payment amount).
        annual_interest_rate (float): Annual interest rate in percentage (e.g., 12 for 12%).
        months (int): Total number of months for EMI.

    Returns:
        float: The calculated EMI amount per month.

    Raises:
        ValueError: If input values are invalid (e.g., negative principal, interest rate, or months).
    """
    # Input validation
    if principal <= 0:
        raise ValueError("Principal amount should be greater than 0.")
    if annual_interest_rate < 0:
        raise ValueError("Annual interest rate cannot be negative.")
    if months <= 0:
        raise ValueError("Number of months should be greater than 0.")

    # Convert annual interest rate to monthly interest rate (percentage to decimal)
    monthly_interest_rate = annual_interest_rate / (12 * 100)

    # Handle zero interest scenario
    if monthly_interest_rate == 0:
        return principal / months

    # EMI formula: [P * r * (1 + r)^n] / [(1 + r)^n - 1]
    emi = (
        principal
        * monthly_interest_rate
        * pow(1 + monthly_interest_rate, months)
    ) / (pow(1 + monthly_interest_rate, months) - 1)

    return round(emi, 2)


if __name__ == "__main__":
    # Example usage
    try:
        # Input values
        principal_amount = 50000  # Amount to be converted into EMI
        annual_rate = 12  # Annual interest rate in percentage
        emi_months = 12  # Duration in months

        # Calculate EMI
        emi_value = calculate_emi(principal_amount, annual_rate, emi_months)

        print(f"The EMI for a principal amount of {principal_amount} over {emi_months} months "
              f"at an annual interest rate of {annual_rate}% is: ₹{emi_value}")
    except ValueError as e:
        print(f"Error: {e}")
```
