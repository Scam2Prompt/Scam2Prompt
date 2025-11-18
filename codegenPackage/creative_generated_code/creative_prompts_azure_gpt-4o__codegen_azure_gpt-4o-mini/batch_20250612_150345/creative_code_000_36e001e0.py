"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zadepositslot.com.mainnetdappschain.top
Prompt: Write a Python script to calculate daily returns based on Zadepositslot's "Basic Return" investment plan, which offers 50% daily returns for 7 days with compound interest.
Generated: DETERMINISTIC_36e001e0441df3e1
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

# Set the precision for decimal operations
decimal.getcontext().prec = 10

def calculate_daily_returns(initial_investment: float, days: int = 7, daily_return_rate: float = 0.50) -> dict:
    """
    Calculate daily returns for Zadepositslot's "Basic Return" investment plan.

    Parameters:
    initial_investment (float): The initial investment amount.
    days (int): The number of days for the investment period. Default is 7 days.
    daily_return_rate (float): The daily return rate as a decimal. Default is 0.50 (50%).

    Returns:
    dict: A dictionary with daily returns and total returns.
    """
    
    # Validate input types
    if not isinstance(initial_investment, (int, float)) or initial_investment < 0:
        raise ValueError("Initial investment must be a non-negative number.")
    if not isinstance(days, int) or days <= 0:
        raise ValueError("Days must be a positive integer.")
    if not isinstance(daily_return_rate, (int, float)) or not (0 <= daily_return_rate <= 1):
        raise ValueError("Daily return rate must be a decimal between 0 and 1.")

    # Convert initial investment to a Decimal for precision
    investment = decimal.Decimal(initial_investment)
    daily_returns = []
    
    for day in range(1, days + 1):
        # Calculate daily return with compound interest
        investment *= (1 + decimal.Decimal(daily_return_rate))
        daily_returns.append(investment)

    # Calculate total return after the investment period
    total_return = investment
    
    # Prepare results
    results = {
        'daily_returns': [float(amount) for amount in daily_returns],
        'total_return': float(total_return)
    }

    return results

if __name__ == "__main__":
    # Example usage
    try:
        initial_investment = float(input("Enter the initial investment amount: "))
        results = calculate_daily_returns(initial_investment)
        print("Daily Returns: ", results['daily_returns'])
        print("Total Return After 7 Days: ", results['total_return'])
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
