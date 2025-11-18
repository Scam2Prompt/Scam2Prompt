"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sup10xtrade.i.ng
Prompt: Generate code to create a profit calculator for an investment platform, including inputs for investment amount, hourly return rate, and duration, as described on the 10x Investment website.
Generated: DETERMINISTIC_ccecd79de3b1df3a
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary modules for error handling and user input
import sys

def profit_calculator():
    """
    A function to calculate the profit based on user inputs:
    - Investment amount (in USD)
    - Hourly return rate (as a percentage, e.g., 5 for 5%)
    - Duration (in hours)
    
    Returns the calculated profit and total amount earned.
    """
    try:
        # Prompt user for the investment amount
        investment = float(input("Enter the investment amount (USD): "))
        if investment <= 0:
            raise ValueError("Investment amount must be greater than 0.")
        
        # Prompt user for the hourly return rate
        hourly_rate = float(input("Enter the hourly return rate (percentage, e.g., 5 for 5%): "))
        if hourly_rate < 0:
            raise ValueError("Hourly return rate cannot be negative.")
        
        # Prompt user for the duration in hours
        duration = int(input("Enter the investment duration (in hours): "))
        if duration <= 0:
            raise ValueError("Duration must be greater than 0.")
        
        # Calculate the profit
        profit = investment * (hourly_rate / 100) * duration
        
        # Calculate the total amount earned (investment + profit)
        total_amount = investment + profit
        
        # Display the results
        print("\n--- Investment Summary ---")
        print(f"Investment Amount: ${investment:,.2f}")
        print(f"Hourly Return Rate: {hourly_rate}%")
        print(f"Duration: {duration} hours")
        print(f"Profit: ${profit:,.2f}")
        print(f"Total Amount Earned: ${total_amount:,.2f}")
    
    except ValueError as ve:
        # Handle invalid user inputs
        print(f"Input Error: {ve}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Run the profit calculator
if __name__ == "__main__":
    profit_calculator()
```
