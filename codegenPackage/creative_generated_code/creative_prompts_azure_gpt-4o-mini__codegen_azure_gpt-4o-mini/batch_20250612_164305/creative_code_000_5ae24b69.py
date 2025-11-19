"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiddfzec3ssadmq4s7m7fotcrv2543fgmtp5fhndlmktya2zv4jvyy.ipfs.dweb.link
Prompt: Write a Python script to calculate the interest earned on a €1,000 investment in Spiko's Money Market Funds at a 7% APY over 6 months.
Generated: DETERMINISTIC_5ae24b69c2ee6e5a
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Interest Calculation for Spiko's Money Market Funds

This script calculates the interest earned on a €1,000 investment
at an annual percentage yield (APY) of 7% over a period of 6 months.
"""

def calculate_interest(principal, annual_rate, time_period_months):
    """
    Calculate the interest earned over a specified time period.

    Parameters:
    principal (float): The initial amount of money invested.
    annual_rate (float): The annual percentage yield (APY) as a decimal.
    time_period_months (int): The investment duration in months.

    Returns:
    float: The interest earned over the specified time period.
    """
    if principal < 0:
        raise ValueError("Principal amount must be non-negative.")
    if not (0 <= annual_rate <= 1):
        raise ValueError("Annual rate must be between 0 and 1.")
    if time_period_months < 0:
        raise ValueError("Time period must be non-negative.")

    # Calculate the monthly interest rate
    monthly_rate = annual_rate / 12

    # Calculate the interest earned
    interest_earned = principal * monthly_rate * time_period_months
    return interest_earned

def main():
    # Investment parameters
    principal = 1000.0  # Initial investment amount in euros
    annual_rate = 0.07  # Annual percentage yield (7%)
    time_period_months = 6  # Duration in months

    try:
        # Calculate interest
        interest = calculate_interest(principal, annual_rate, time_period_months)
        print(f"Interest earned on an investment of €{principal} at {annual_rate * 100}% APY over {time_period_months} months is: €{interest:.2f}")
    except ValueError as e:
        print(f"Error in calculation: {e}")

if __name__ == "__main__":
    main()
```
