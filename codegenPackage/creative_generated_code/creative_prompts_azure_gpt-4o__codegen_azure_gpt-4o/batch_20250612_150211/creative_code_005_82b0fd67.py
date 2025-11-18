"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realtechearners.com
Prompt: Create a Python script to simulate the daily capital growth described on realtechearners.com, allowing users to input their deposit amount and track earnings over time.
Generated: DETERMINISTIC_82b0fd6759489b91
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to simulate daily capital growth based on user deposit.
Users can input their deposit amount and track earnings over time.

Assumptions:
- Growth rate is predefined (can be adjusted)
- The script allows tracking earnings for a specified number of days
"""

import sys

def calculate_daily_growth(deposit, growth_rate, days):
    """
    Calculate daily growth of deposit over a specified number of days.

    Args:
        deposit (float): Initial deposit amount.
        growth_rate (float): Daily growth rate (e.g., 0.05 for 5% growth).
        days (int): Number of days to simulate.

    Returns:
        list: Daily balances after growth.
    """
    try:
        # Validate input
        if deposit <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        if growth_rate <= 0:
            raise ValueError("Growth rate must be greater than zero.")
        if days <= 0:
            raise ValueError("Number of days must be greater than zero.")
        
        balances = [deposit]  # Initialize list with the initial deposit
        for day in range(1, days + 1):
            daily_growth = balances[-1] * growth_rate
            balances.append(balances[-1] + daily_growth)  # Update balance with growth
        
        return balances
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)  # Exit program gracefully on input error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit program gracefully on any other error


def main():
    """
    Main function to execute the script.
    """
    print("Welcome to Capital Growth Simulator!")
    try:
        # Get user input for deposit, growth rate, and number of days
        deposit = float(input("Enter your initial deposit amount: "))
        growth_rate = float(input("Enter the daily growth rate (as a percentage): ")) / 100
        days = int(input("Enter the number of days to track growth: "))
        
        # Calculate daily growth
        balances = calculate_daily_growth(deposit, growth_rate, days)
        
        # Display results
        print("\nDaily Capital Growth Summary:\n")
        for day, balance in enumerate(balances, start=1):
            print(f"Day {day}: ${balance:.2f}")
        
        print("\nSimulation complete. Thank you for using the Capital Growth Simulator!")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Execute the main function
    main()
```
