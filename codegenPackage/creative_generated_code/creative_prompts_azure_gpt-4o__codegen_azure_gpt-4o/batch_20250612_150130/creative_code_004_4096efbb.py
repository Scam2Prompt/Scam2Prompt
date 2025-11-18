"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeforcetd.com
Prompt: Develop a program to compare the profitability of Finance Force Ltd's "Basic Plan," "Flexible Plan," and "Advanced Plan" based on initial deposit amounts and daily returns. Use Python for the calculations and provide a summary of the best option.
Generated: DETERMINISTIC_4096efbb23defd03
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to compare profitability of Finance Force Ltd's investment plans
# Author: Expert Programmer
# Date: YYYY-MM-DD

# Import necessary libraries
import sys

# Function to calculate total returns for a given plan
def calculate_profit(initial_deposit, daily_return_rate, days):
    """
    Calculate the total return based on an initial deposit, daily return rate, and number of days.

    :param initial_deposit: Initial amount deposited (float)
    :param daily_return_rate: Daily return rate as a percentage (float)
    :param days: Number of days the investment is held (int)
    :return: Total profit (float)
    """
    try:
        # Ensure valid inputs
        if initial_deposit <= 0:
            raise ValueError("Initial deposit must be greater than 0.")
        if daily_return_rate <= 0:
            raise ValueError("Daily return rate must be greater than 0.")
        if days <= 0:
            raise ValueError("Number of days must be greater than 0.")
        
        # Convert daily return rate to decimal for calculation
        daily_rate_decimal = daily_return_rate / 100
        
        # Calculate total profit using compound interest formula
        total_profit = initial_deposit * ((1 + daily_rate_decimal) ** days - 1)
        return total_profit
    except Exception as e:
        print(f"Error calculating profit: {e}", file=sys.stderr)
        return None

# Plan configurations
plans = {
    "Basic Plan": {"daily_return_rate": 1.2, "days": 30},  # 1.2% daily return for 30 days
    "Flexible Plan": {"daily_return_rate": 1.5, "days": 25},  # 1.5% daily return for 25 days
    "Advanced Plan": {"daily_return_rate": 2.0, "days": 20},  # 2.0% daily return for 20 days
}

# Function to compare plans
def compare_plans(initial_deposit):
    """
    Compare the profitability of investment plans based on initial deposit.

    :param initial_deposit: Initial amount deposited (float)
    :return: None
    """
    try:
        # Ensure valid initial deposit input
        if initial_deposit <= 0:
            raise ValueError("Initial deposit must be greater than 0.")
        
        # Store results for comparison
        results = {}
        
        # Calculate and store profit for each plan
        for plan, config in plans.items():
            profit = calculate_profit(initial_deposit, config["daily_return_rate"], config["days"])
            if profit is not None:
                results[plan] = profit
        
        # Find the best plan
        best_plan = max(results, key=results.get)
        
        # Display results
        print("Investment Plan Comparison:")
        print(f"{'Plan':<15}{'Profit':>10}")
        print("-" * 25)
        for plan, profit in results.items():
            print(f"{plan:<15}{profit:>10.2f}")
        
        print("\nBest Option:")
        print(f"{best_plan} with a profit of {results[best_plan]:.2f}")
    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)

# Main function
def main():
    """
    Main function to drive the program.
    """
    try:
        # Prompt user for initial deposit
        initial_deposit = float(input("Enter the initial deposit amount (e.g., 1000): "))
        
        # Compare investment plans
        compare_plans(initial_deposit)
    except ValueError:
        print("Invalid input. Please enter a numeric value for the initial deposit.", file=sys.stderr)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)

# Entry point of the program
if __name__ == "__main__":
    main()
```
