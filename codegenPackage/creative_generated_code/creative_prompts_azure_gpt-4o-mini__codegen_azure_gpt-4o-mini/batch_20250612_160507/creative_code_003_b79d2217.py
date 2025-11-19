"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchsheelbank.com
Prompt: Develop a function that calculates the monthly payment for a housing loan based on the details provided by Panchsheel Bank.
Generated: DETERMINISTIC_b79d2217b216abec
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_monthly_payment(principal: float, annual_interest_rate: float, years: int) -> float:
    """
    Calculate the monthly payment for a housing loan.

    Parameters:
    principal (float): The total loan amount (principal).
    annual_interest_rate (float): The annual interest rate (as a percentage).
    years (int): The number of years to repay the loan.

    Returns:
    float: The monthly payment amount.

    Raises:
    ValueError: If the principal is negative, the interest rate is negative, or the years are non-positive.
    """

    # Validate input parameters
    if principal < 0:
        raise ValueError("Principal amount must be non-negative.")
    if annual_interest_rate < 0:
        raise ValueError("Annual interest rate must be non-negative.")
    if years <= 0:
        raise ValueError("Number of years must be positive.")

    # Convert annual interest rate to a monthly rate (decimal)
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Calculate the number of monthly payments
    number_of_payments = years * 12

    # Calculate the monthly payment using the formula
    if monthly_interest_rate == 0:
        # Handle case with zero interest rate
        monthly_payment = principal / number_of_payments
    else:
        monthly_payment = (
            principal * monthly_interest_rate
        ) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)

    return monthly_payment


# Example usage
if __name__ == "__main__":
    try:
        loan_amount = 250000  # Principal amount
        interest_rate = 3.5   # Annual interest rate
        loan_term = 30        # Loan term in years

        monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_term)
        print(f"The monthly payment for the loan is: ${monthly_payment:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
