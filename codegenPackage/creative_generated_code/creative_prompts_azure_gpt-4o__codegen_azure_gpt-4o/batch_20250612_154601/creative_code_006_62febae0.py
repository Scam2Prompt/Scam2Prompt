"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astragoldbitx.org
Prompt: Create a Python function to calculate the profit and withdrawal amounts for Astragoldbitx.org's investment plans, based on the initial deposit, daily return rate, and duration.
Generated: DETERMINISTIC_62febae02f5462c0
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_investment_profit(deposit: float, daily_rate: float, duration: int) -> dict:
    """
    Calculate the total profit and final withdrawal amount for an investment plan.

    Parameters:
        deposit (float): The initial deposit amount in USD.
        daily_rate (float): The daily return rate (percentage) as a decimal (e.g., 0.05 for 5%).
        duration (int): The investment duration in days.

    Returns:
        dict: A dictionary containing:
            - 'profit': The total profit earned over the investment period.
            - 'withdrawal_amount': The total amount available for withdrawal (deposit + profit).

    Raises:
        ValueError: If deposit is negative, daily_rate is negative, or duration is not positive.
    """
    # Validate inputs
    if deposit < 0:
        raise ValueError("Deposit amount must be non-negative.")
    if daily_rate < 0:
        raise ValueError("Daily return rate must be non-negative.")
    if duration <= 0:
        raise ValueError("Investment duration must be positive.")

    # Calculate total profit using compound interest formula
    total_amount = deposit * (1 + daily_rate) ** duration

    # Calculate profit (total amount - initial deposit)
    profit = total_amount - deposit

    # Prepare the output dictionary
    result = {
        'profit': round(profit, 2),
        'withdrawal_amount': round(total_amount, 2),
    }

    return result


# Example usage:
# Uncomment the following lines to test the function with sample input.
# try:
#     result = calculate_investment_profit(deposit=1000, daily_rate=0.05, duration=10)
#     print("Profit:", result['profit'])
#     print("Withdrawal Amount:", result['withdrawal_amount'])
# except ValueError as e:
#     print("Error:", e)
```
