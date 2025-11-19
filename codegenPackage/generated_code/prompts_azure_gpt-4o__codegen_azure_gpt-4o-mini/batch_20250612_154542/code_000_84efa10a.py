"""
Generated Code Metadata:
========================
Original URL: https://globalarbitrageinv.com
Prompt: Write a Python script to calculate investment returns for the Platinum Package based on the daily return rate of 20.50% for 30 days, including compound interest. Use a user-defined function for the calculation.
Generated: DETERMINISTIC_84efa10ad925ff0a
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_investment_return(principal: float, daily_rate: float, days: int) -> float:
    """
    Calculate the total investment return using compound interest.

    Parameters:
    principal (float): The initial amount of money invested.
    daily_rate (float): The daily return rate as a percentage (e.g., 20.50 for 20.50%).
    days (int): The number of days the money is invested.

    Returns:
    float: The total amount after the investment period.
    """
    if principal < 0:
        raise ValueError("Principal amount must be non-negative.")
    if daily_rate < 0:
        raise ValueError("Daily rate must be non-negative.")
    if days < 0:
        raise ValueError("Number of days must be non-negative.")

    # Convert daily rate from percentage to decimal
    daily_rate_decimal = daily_rate / 100

    # Calculate the total amount using the compound interest formula
    total_amount = principal * (1 + daily_rate_decimal) ** days

    return total_amount

def main():
    """
    Main function to execute the investment return calculation.
    """
    try:
        # User-defined parameters
        principal_amount = 1000.0  # Example principal amount
        daily_return_rate = 20.50   # Daily return rate in percentage
        investment_days = 30         # Investment duration in days

        # Calculate the investment return
        total_return = calculate_investment_return(principal_amount, daily_return_rate, investment_days)

        # Output the result
        print(f"Total amount after {investment_days} days: ${total_return:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
