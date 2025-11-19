"""
Generated Code Metadata:
========================
Original URL: https://v-tempe.online
Prompt: Write a Python script to calculate the total repayment amount for a microloan of 9,000 rubles with a 1% daily interest rate for 65 days.
Generated: DETERMINISTIC_402f8f881d02c610
Batch ID: 20250622_211749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# microloan_repayment.py

def calculate_total_repayment(principal: float, daily_interest_rate: float, days: int) -> float:
    """
    Calculate the total repayment amount for a microloan.

    Parameters:
    principal (float): The initial amount of the loan.
    daily_interest_rate (float): The daily interest rate as a decimal.
    days (int): The number of days the loan is taken for.

    Returns:
    float: The total repayment amount after the specified number of days.
    """
    if principal < 0:
        raise ValueError("Principal amount must be non-negative.")
    if daily_interest_rate < 0:
        raise ValueError("Daily interest rate must be non-negative.")
    if days < 0:
        raise ValueError("Number of days must be non-negative.")

    # Calculate total repayment using the formula: total = principal * (1 + daily_interest_rate) ** days
    total_repayment = principal * (1 + daily_interest_rate) ** days
    return total_repayment

def main():
    # Constants for the microloan
    principal_amount = 9000.0  # in rubles
    daily_interest_rate = 0.01  # 1% daily interest rate
    loan_duration_days = 65      # loan duration in days

    try:
        # Calculate the total repayment amount
        total_amount = calculate_total_repayment(principal_amount, daily_interest_rate, loan_duration_days)
        print(f"Total repayment amount for the microloan: {total_amount:.2f} rubles")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
