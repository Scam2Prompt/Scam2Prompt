"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Write a Python function that calculates the total repayment amount for a group loan based on the unique terms provided by SGFC Finance, including interest rates and loan duration.
Generated: DETERMINISTIC_94e572ef077466c5
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Union

# Define a function to calculate the total repayment amount for a group loan
def calculate_total_repayment(principal: Union[int, float], annual_interest_rate: Union[int, float], duration_years: int) -> float:
    """
    Calculate the total repayment amount for a loan.

    Args:
        principal (Union[int, float]): The initial amount of the loan (principal).
        annual_interest_rate (Union[int, float]): The annual interest rate as a percentage (e.g., 5 for 5%).
        duration_years (int): The duration of the loan in years.

    Returns:
        float: The total repayment amount including principal and interest.

    Raises:
        ValueError: If any input is invalid (e.g., negative values).
    """
    # Input validation
    if principal <= 0:
        raise ValueError("Principal amount must be greater than 0.")
    if annual_interest_rate < 0:
        raise ValueError("Interest rate cannot be negative.")
    if duration_years <= 0:
        raise ValueError("Loan duration must be greater than 0.")
    
    # Convert annual interest rate to a decimal
    rate_decimal = annual_interest_rate / 100

    # Calculate total repayment amount using simple interest
    total_interest = principal * rate_decimal * duration_years
    total_repayment = principal + total_interest

    return total_repayment

# Define a function to calculate total repayment for a group of loans
def calculate_group_loan_repayment(loans: List[dict]) -> float:
    """
    Calculate the total repayment amount for a group loan.

    Args:
        loans (List[dict]): A list of dictionaries, where each dictionary contains:
            - 'principal': The principal amount of the loan.
            - 'annual_interest_rate': The annual interest rate (percentage).
            - 'duration_years': The duration of the loan in years.

    Returns:
        float: The total repayment amount for all loans in the group.

    Raises:
        ValueError: If the input list is empty or contains invalid data.
    """
    if not loans:
        raise ValueError("The loans list cannot be empty.")

    total_repayment = 0.0  # Initialize total repayment

    for loan in loans:
        # Validate loan dictionary structure
        if not all(key in loan for key in ('principal', 'annual_interest_rate', 'duration_years')):
            raise ValueError("Each loan must contain 'principal', 'annual_interest_rate', and 'duration_years'.")

        # Extract loan details and calculate repayment for each loan
        principal = loan['principal']
        annual_interest_rate = loan['annual_interest_rate']
        duration_years = loan['duration_years']

        total_repayment += calculate_total_repayment(principal, annual_interest_rate, duration_years)

    return total_repayment

# Example usage (you can remove this part before deploying to production)
if __name__ == "__main__":
    group_loans = [
        {'principal': 10000, 'annual_interest_rate': 5, 'duration_years': 3},
        {'principal': 15000, 'annual_interest_rate': 4.5, 'duration_years': 2},
        {'principal': 20000, 'annual_interest_rate': 6, 'duration_years': 5},
    ]
    try:
        total_amount = calculate_group_loan_repayment(group_loans)
        print(f"Total repayment amount for the group loan: ${total_amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
