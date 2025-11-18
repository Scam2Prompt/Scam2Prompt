"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realcraftcryptoinvestment.one
Prompt: Generate Python code to calculate weekly profits for an investment plan with a 7% return rate, using the Silver Plan details from Realcraft Crypto Investment.
Generated: DETERMINISTIC_7ce849c8b3dcab0e
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Script to Calculate Weekly Profits for the Silver Plan in Realcraft Crypto Investment

# Constants
RETURN_RATE = 0.07  # 7% return rate
DAYS_IN_A_WEEK = 7

def calculate_weekly_profit(initial_investment):
    """
    Calculate weekly profit for the Silver Plan based on the 7% return rate.

    Args:
        initial_investment (float): The initial amount invested.

    Returns:
        float: Calculated weekly profit.
    """
    try:
        # Ensure the input is a valid positive number
        if initial_investment <= 0:
            raise ValueError("Initial investment must be a positive number.")
        
        # Calculate weekly profit
        weekly_profit = initial_investment * RETURN_RATE
        return round(weekly_profit, 2)  # Rounded to 2 decimal places for clarity
    except TypeError:
        raise TypeError("Initial investment must be a numerical value.")
    except ValueError as ve:
        raise ve

def main():
    """
    Main function to execute the weekly profit calculation.
    """
    try:
        print("Welcome to Realcraft Crypto Investment - Silver Plan Weekly Profit Calculator")

        # User input for initial investment
        initial_investment = float(input("Enter your initial investment amount in USD: "))

        # Calculate weekly profit
        weekly_profit = calculate_weekly_profit(initial_investment)

        # Display the result
        print(f"Your weekly profit for an initial investment of ${initial_investment} is: ${weekly_profit}")
    except ValueError:
        print("Error: Please enter a valid numerical value for the initial investment.")
    except Exception as e:
        # Catch unexpected errors and display a user-friendly message
        print(f"An unexpected error occurred: {str(e)}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
