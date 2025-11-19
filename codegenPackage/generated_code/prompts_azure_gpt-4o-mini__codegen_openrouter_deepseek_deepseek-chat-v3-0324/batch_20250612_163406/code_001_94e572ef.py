"""
Generated Code Metadata:
========================
Original URL: https://sgfcfinance.com
Prompt: Write a Python function that calculates the total repayment amount for a group loan based on the unique terms provided by SGFC Finance, including interest rates and loan duration.
Generated: DETERMINISTIC_94e572ef077466c5
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_loan_repayment(principal_amount, annual_interest_rate, loan_duration_years, repayment_frequency='monthly'):
    """
    Calculate the total repayment amount for a group loan with SGFC Finance terms.
    
    Args:
        principal_amount (float): The initial loan amount (must be positive)
        annual_interest_rate (float): Annual interest rate in percentage (e.g., 5 for 5%)
        loan_duration_years (int): Duration of the loan in years (must be positive)
        repayment_frequency (str): Frequency of repayments ('monthly', 'quarterly', 'yearly')
        
    Returns:
        float: Total repayment amount (principal + interest)
        
    Raises:
        ValueError: If any input is invalid
    """
    # Validate input parameters
    if principal_amount <= 0:
        raise ValueError("Principal amount must be positive")
    if annual_interest_rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if loan_duration_years <= 0:
        raise ValueError("Loan duration must be positive")
    
    # Convert annual interest rate to decimal and get number of compounding periods per year
    interest_rate_decimal = annual_interest_rate / 100
    
    if repayment_frequency == 'monthly':
        periods_per_year = 12
    elif repayment_frequency == 'quarterly':
        periods_per_year = 4
    elif repayment_frequency == 'yearly':
        periods_per_year = 1
    else:
        raise ValueError("Invalid repayment frequency. Must be 'monthly', 'quarterly', or 'yearly'")
    
    total_periods = loan_duration_years * periods_per_year
    periodic_interest_rate = interest_rate_decimal / periods_per_year
    
    # Calculate total repayment using compound interest formula
    try:
        total_repayment = principal_amount * (1 + periodic_interest_rate) ** total_periods
    except OverflowError:
        raise ValueError("Calculation resulted in an overflow. Please check your input values")
    
    return round(total_repayment, 2)
```
