"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbullminingpro.com
Prompt: Create a function to simulate profit calculations for the USDT investment plan on BitBullMiningPro, factoring in daily guaranteed returns for 30 days.
Generated: DETERMINISTIC_c4d9476568d9f08b
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_profit(initial_investment, daily_return_rate, days=30):
    """
    Simulates profit calculations for a USDT investment plan on BitBullMiningPro.
    
    Parameters:
    initial_investment (float): The amount of USDT invested.
    daily_return_rate (float): The daily guaranteed return rate (as a decimal).
    days (int): The number of days for the investment (default is 30).
    
    Returns:
    float: The total profit after the specified number of days.
    float: The total amount after profit is added to the initial investment.
    
    Raises:
    ValueError: If initial_investment or daily_return_rate is negative,
                or if days is not a positive integer.
    """
    
    # Input validation
    if initial_investment < 0:
        raise ValueError("Initial investment must be a non-negative value.")
    if daily_return_rate < 0:
        raise ValueError("Daily return rate must be a non-negative value.")
    if not isinstance(days, int) or days <= 0:
        raise ValueError("Days must be a positive integer.")
    
    # Initialize total amounts
    total_investment = initial_investment
    total_profit = 0.0
    
    # Calculate profit over the specified number of days
    for day in range(1, days + 1):
        daily_profit = total_investment * daily_return_rate
        total_profit += daily_profit
        total_investment += daily_profit  # Compounding the profit

    total_amount = initial_investment + total_profit

    return total_profit, total_amount

# Example usage
if __name__ == "__main__":
    try:
        investment = 1000.0  # Example initial investment in USDT
        daily_rate = 0.01    # Example daily return rate (1%)
        profit, total = calculate_profit(investment, daily_rate)
        print(f"Total Profit after 30 days: {profit:.2f} USDT")
        print(f"Total Amount after 30 days: {total:.2f} USDT")
    except ValueError as e:
        print(f"Error: {e}")
```
