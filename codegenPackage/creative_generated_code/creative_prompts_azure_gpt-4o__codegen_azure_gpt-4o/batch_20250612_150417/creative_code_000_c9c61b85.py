"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longtradegroup.com
Prompt: Write Python code to calculate daily profits for a cryptocurrency staking plan based on the LongTradeGroup USD Plan, which offers 0.2% daily profit for 100 days. Include functionality to handle minimum and maximum investment limits ($25-$250).
Generated: DETERMINISTIC_c9c61b85b9f5dea1
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Cryptocurrency Staking Profit Calculator

This script calculates daily profits for the LongTradeGroup USD Plan, which offers 
0.2% daily profit for 100 days. The minimum investment is $25, and the maximum 
investment is $250.
"""

# Import necessary modules
import sys

def calculate_daily_profits(investment_amount, daily_rate=0.002, duration=100):
    """
    Calculates daily profits for a given investment amount.
    
    Parameters:
        investment_amount (float): The initial investment amount.
        daily_rate (float): The daily profit rate (default is 0.2% or 0.002).
        duration (int): The total number of days (default is 100 days).
        
    Returns:
        list: A list of daily profits for each day.
    """
    try:
        # Validate investment amount
        if investment_amount < 25 or investment_amount > 250:
            raise ValueError("Investment amount must be between $25 and $250.")
        
        # Calculate daily profits
        daily_profits = [investment_amount * daily_rate for day in range(1, duration + 1)]
        return daily_profits
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)

def display_profit_summary(investment_amount, daily_profits):
    """
    Displays the profit summary including total profits and daily breakdown.
    
    Parameters:
        investment_amount (float): The initial investment amount.
        daily_profits (list): List of daily profits over the duration.
    """
    print("\n---- Profit Summary ----")
    print(f"Initial Investment: ${investment_amount:.2f}")
    print(f"Total Profits Over {len(daily_profits)} Days: ${sum(daily_profits):.2f}")
    print("\nDaily Profits Breakdown:")
    for day, profit in enumerate(daily_profits, start=1):
        print(f"Day {day}: ${profit:.2f}")

def main():
    """
    Main function to run the staking profit calculator.
    """
    try:
        # Prompt user for investment amount
        investment_amount = float(input("Enter your investment amount ($25-$250): ").strip())
        
        # Calculate daily profits
        daily_profits = calculate_daily_profits(investment_amount)
        
        # Display the profit summary
        display_profit_summary(investment_amount, daily_profits)
    except ValueError:
        print("Error: Please enter a valid number.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

# Entry point for the script
if __name__ == "__main__":
    main()
```
