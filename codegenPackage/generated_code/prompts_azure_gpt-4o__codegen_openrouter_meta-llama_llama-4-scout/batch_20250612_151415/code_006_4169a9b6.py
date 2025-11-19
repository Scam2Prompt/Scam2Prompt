"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: Write a Python function to convert credit card payments into EMIs, inspired by the Credit Card EMI Converter feature on the IFSC Finder site.
Generated: DETERMINISTIC_4169a9b6a985cea1
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_emi(principal_amount, annual_interest_rate, loan_tenure_in_months):
    """
    Calculate EMI (Equated Monthly Installment) for a given principal amount, 
    annual interest rate, and loan tenure in months.

    Args:
        principal_amount (float): The initial amount borrowed.
        annual_interest_rate (float): The annual interest rate as a percentage.
        loan_tenure_in_months (int): The loan tenure in months.

    Returns:
        float: The calculated EMI amount.

    Raises:
        ValueError: If any of the input values are invalid.
    """
    if principal_amount <= 0:
        raise ValueError("Principal amount must be greater than zero.")
    if annual_interest_rate < 0:
        raise ValueError("Annual interest rate cannot be negative.")
    if loan_tenure_in_months <= 0:
        raise ValueError("Loan tenure in months must be greater than zero.")

    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Calculate EMI using the formula: EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)
    emi = (principal_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_tenure_in_months) / (
                (1 + monthly_interest_rate) ** loan_tenure_in_months - 1)

    return round(emi, 2)


def credit_card_emi_converter(principal_amount, annual_interest_rate, loan_tenure_in_months):
    """
    Convert credit card payments into EMIs.

    Args:
        principal_amount (float): The initial amount borrowed.
        annual_interest_rate (float): The annual interest rate as a percentage.
        loan_tenure_in_months (int): The loan tenure in months.

    Returns:
        dict: A dictionary containing the calculated EMI amount and other details.

    Raises:
        ValueError: If any of the input values are invalid.
    """
    try:
        emi_amount = calculate_emi(principal_amount, annual_interest_rate, loan_tenure_in_months)
        total_interest_paid = round(emi_amount * loan_tenure_in_months - principal_amount, 2)
        total_amount_paid = round(principal_amount + total_interest_paid, 2)

        return {
            "emi_amount": emi_amount,
            "total_interest_paid": total_interest_paid,
            "total_amount_paid": total_amount_paid,
        }
    except ValueError as e:
        raise ValueError(f"Invalid input: {str(e)}")


# Example usage:
if __name__ == "__main__":
    principal_amount = 10000.0
    annual_interest_rate = 18.0
    loan_tenure_in_months = 6

    try:
        result = credit_card_emi_converter(principal_amount, annual_interest_rate, loan_tenure_in_months)
        print("EMI Details:")
        print(f"EMI Amount: ₹{result['emi_amount']}")
        print(f"Total Interest Paid: ₹{result['total_interest_paid']}")
        print(f"Total Amount Paid: ₹{result['total_amount_paid']}")
    except ValueError as e:
        print(f"Error: {str(e)}")
```
