"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: Create a program that calculates monthly loan EMI based on principal, interest rate, and loan tenure, similar to the EMI Calculator tool provided on the IFSC Finder website.
Generated: DETERMINISTIC_8d17fe10c5447177
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
EMI Calculator Program

Calculates monthly loan EMI based on principal, interest rate, and loan tenure.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_emi(principal, annual_interest_rate, loan_tenure_in_years):
    """
    Calculates monthly EMI.

    Args:
        principal (float): The initial amount borrowed.
        annual_interest_rate (float): The annual interest rate as a percentage.
        loan_tenure_in_years (int): The loan tenure in years.

    Returns:
        float: The monthly EMI.

    Raises:
        ValueError: If any of the input values are invalid.
    """
    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")
    if annual_interest_rate < 0:
        raise ValueError("Annual interest rate cannot be negative.")
    if loan_tenure_in_years <= 0:
        raise ValueError("Loan tenure must be greater than zero.")

    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Calculate loan tenure in months
    loan_tenure_in_months = loan_tenure_in_years * 12

    # Calculate EMI using the formula: EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)
    emi = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_tenure_in_months / ((1 + monthly_interest_rate) ** loan_tenure_in_months - 1)

    return round(emi, 2)


def main():
    try:
        principal = float(input("Enter the loan principal: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        loan_tenure_in_years = int(input("Enter the loan tenure (in years): "))

        emi = calculate_emi(principal, annual_interest_rate, loan_tenure_in_years)

        print(f"Your monthly EMI is: ₹{emi}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
