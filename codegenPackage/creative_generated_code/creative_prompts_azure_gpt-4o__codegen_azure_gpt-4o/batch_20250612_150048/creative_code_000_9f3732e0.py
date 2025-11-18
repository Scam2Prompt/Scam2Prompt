"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safewealthhaven.com
Prompt: Write Python code to calculate daily investment returns using the profit percentages from Safe Wealth Haven's Silver, Gold, and Platinum plans. Include functionality for a user to input their investment amount and plan type.
Generated: DETERMINISTIC_9f3732e05f2f7030
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Safe Wealth Haven Investment Returns Calculator
# This program calculates daily investment returns based on user input for investment amount and plan type.

def calculate_daily_return(investment_amount, plan_type):
    """
    Calculate daily returns based on the investment amount and plan type.
    
    Parameters:
        investment_amount (float): The amount of money invested.
        plan_type (str): The investment plan type - 'Silver', 'Gold', or 'Platinum'.
    
    Returns:
        float: The daily return amount.
    """
    # Define profit percentages for each plan
    profit_percentages = {
        "Silver": 1.5,    # 1.5% daily profit
        "Gold": 2.0,      # 2.0% daily profit
        "Platinum": 2.5   # 2.5% daily profit
    }
    
    # Check if the provided plan type is valid
    if plan_type not in profit_percentages:
        raise ValueError("Invalid plan type. Please choose 'Silver', 'Gold', or 'Platinum'.")
    
    # Calculate the daily return
    daily_return = investment_amount * (profit_percentages[plan_type] / 100)
    return daily_return


def main():
    """
    Main function to interact with the user and calculate investment returns.
    """
    print("Welcome to Safe Wealth Haven's Investment Returns Calculator!")
    try:
        # Get user input for investment amount
        investment_amount = float(input("Enter your investment amount (e.g., 1000): "))
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        # Get user input for the plan type
        plan_type = input("Enter your investment plan type ('Silver', 'Gold', 'Platinum'): ").strip().capitalize()
        
        # Calculate the daily return
        daily_return = calculate_daily_return(investment_amount, plan_type)
        
        # Display the result
        print(f"Your daily return for the {plan_type} plan is: ${daily_return:.2f}")
    
    except ValueError as ve:
        # Handle value errors (e.g., invalid input, negative investment amount)
        print(f"Error: {ve}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point of the program
if __name__ == "__main__":
    main()
```
