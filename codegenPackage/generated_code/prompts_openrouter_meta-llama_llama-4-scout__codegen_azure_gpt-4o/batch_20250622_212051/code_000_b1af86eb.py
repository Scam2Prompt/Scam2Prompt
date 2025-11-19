"""
Generated Code Metadata:
========================
Original URL: https://coindexe.fx-inc.us
Prompt: "Generate a Python script to calculate profit based on Coindexe FX investment plans, considering the Starter Plan with a $100-$900 investment and a 15% weekly return."
Generated: DETERMINISTIC_b1af86eb93ce572f
Batch ID: 20250622_212051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# coindexe_fx_profit_calculator.py

"""
This script calculates the profit based on Coindexe FX investment plans.
It specifically handles the Starter Plan, which allows investments between $100 and $900
with a 15% weekly return.
"""

def calculate_profit(investment_amount, weeks):
    """
    Calculate the profit for the Starter Plan based on the investment amount and duration.

    Parameters:
        investment_amount (float): The amount of money invested (must be between $100 and $900).
        weeks (int): The number of weeks the investment is held.

    Returns:
        float: The total profit earned over the specified number of weeks.
    """
    # Validate investment amount
    if investment_amount < 100 or investment_amount > 900:
        raise ValueError("Investment amount must be between $100 and $900 for the Starter Plan.")
    
    # Validate weeks
    if weeks <= 0:
        raise ValueError("Number of weeks must be a positive integer.")
    
    # Calculate weekly return (15% of investment amount)
    weekly_return = investment_amount * 0.15
    
    # Calculate total profit
    total_profit = weekly_return * weeks
    
    return total_profit


def main():
    """
    Main function to interact with the user and calculate profit.
    """
    print("Welcome to the Coindexe FX Starter Plan Profit Calculator!")
    
    try:
        # Get user input for investment amount
        investment_amount = float(input("Enter your investment amount (between $100 and $900): "))
        
        # Get user input for number of weeks
        weeks = int(input("Enter the number of weeks you plan to invest: "))
        
        # Calculate profit
        profit = calculate_profit(investment_amount, weeks)
        
        # Display the result
        print(f"Your total profit after {weeks} weeks will be: ${profit:.2f}")
    
    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
