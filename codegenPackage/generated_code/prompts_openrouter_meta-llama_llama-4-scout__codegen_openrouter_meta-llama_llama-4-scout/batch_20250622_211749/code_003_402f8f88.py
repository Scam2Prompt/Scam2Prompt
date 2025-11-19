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
def calculate_microloan_repayment(principal, daily_interest_rate, days):
    """
    Calculate the total repayment amount for a microloan.

    Args:
        principal (float): The initial loan amount.
        daily_interest_rate (float): The daily interest rate as a decimal.
        days (int): The number of days the loan is outstanding.

    Returns:
        float: The total repayment amount.

    Raises:
        ValueError: If the principal, daily interest rate, or days are invalid.
    """
    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")
    if daily_interest_rate < 0:
        raise ValueError("Daily interest rate must be non-negative.")
    if days <= 0:
        raise ValueError("Days must be greater than zero.")

    # Calculate the total interest paid over the loan period
    total_interest = principal * daily_interest_rate * days

    # Calculate the total repayment amount
    total_repayment = principal + total_interest

    return total_repayment


def main():
    try:
        principal = 9000  # Initial loan amount in rubles
        daily_interest_rate = 0.01  # 1% daily interest rate
        days = 65  # Loan period in days

        total_repayment = calculate_microloan_repayment(principal, daily_interest_rate, days)
        print(f"The total repayment amount is: {total_repayment:.2f} rubles")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
