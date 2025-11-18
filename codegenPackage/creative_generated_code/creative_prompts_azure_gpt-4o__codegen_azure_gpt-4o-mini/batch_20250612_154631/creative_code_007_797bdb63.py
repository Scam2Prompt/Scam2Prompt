"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cointrusts-mining.com
Prompt: Write a Python function to calculate total earnings for a user investing $100 for 5 days at a 3% daily interest rate, as described in Cointrust-mining's investment plan.
Generated: DETERMINISTIC_797bdb63e49c14a3
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_earnings(investment: float, daily_interest_rate: float, days: int) -> float:
    """
    Calculate the total earnings from an investment over a given number of days.

    Parameters:
    investment (float): The initial amount of money invested.
    daily_interest_rate (float): The daily interest rate expressed as a decimal.
    days (int): The number of days the money is invested for.

    Returns:
    float: The total earnings after the specified number of days.
    
    Raises:
    ValueError: If investment is negative, daily_interest_rate is out of bounds, or days is negative.
    """
    
    # Input validation
    if investment < 0:
        raise ValueError("Investment must be a non-negative value.")
    if not (0 <= daily_interest_rate <= 1):
        raise ValueError("Daily interest rate must be between 0 and 1.")
    if days < 0:
        raise ValueError("Number of days must be a non-negative integer.")
    
    total_earnings = investment * ((1 + daily_interest_rate) ** days)
    return total_earnings

# Example usage
if __name__ == "__main__":
    try:
        initial_investment = 100.0  # Initial investment amount
        interest_rate = 0.03         # Daily interest rate (3%)
        investment_duration = 5       # Investment duration in days

        total = calculate_total_earnings(initial_investment, interest_rate, investment_duration)
        print(f"Total earnings after {investment_duration} days is: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
