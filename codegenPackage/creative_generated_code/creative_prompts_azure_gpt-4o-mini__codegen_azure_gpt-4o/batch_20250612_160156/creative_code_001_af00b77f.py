"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supremeprofund.com
Prompt: Write a code snippet that calculates potential profits based on the investment plans (Silver, Bronze, Gold, Ultimate) offered by SupremeProFund, using user-defined investment amounts.
Generated: DETERMINISTIC_af00b77fa71ec68c
Batch ID: 20250612_160156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate potential profits based on investment plans offered by SupremeProFund

# Constants for profit percentages for each investment plan
PLAN_PROFIT_PERCENTAGES = {
    "Silver": 0.05,  # 5% profit
    "Bronze": 0.10,  # 10% profit
    "Gold": 0.15,    # 15% profit
    "Ultimate": 0.25 # 25% profit
}

def calculate_profit(investment_plan, investment_amount):
    """
    Calculate potential profit based on the investment plan and amount.
    
    Args:
        investment_plan (str): The investment plan chosen by the user (Silver, Bronze, Gold, Ultimate).
        investment_amount (float): The amount of money invested by the user.
    
    Returns:
        float: The potential profit for the given investment plan and amount.
    """
    try:
        # Validate investment amount
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        # Validate investment plan
        if investment_plan not in PLAN_PROFIT_PERCENTAGES:
            raise ValueError(f"Invalid investment plan '{investment_plan}'. Please choose from {list(PLAN_PROFIT_PERCENTAGES.keys())}.")
        
        # Calculate profit
        profit_percentage = PLAN_PROFIT_PERCENTAGES[investment_plan]
        potential_profit = investment_amount * profit_percentage
        
        return potential_profit
    except ValueError as e:
        # Handle validation errors gracefully
        print(f"Error: {e}")
        return None

def main():
    """
    Main function to get user input and calculate potential profits.
    """
    print("Welcome to SupremeProFund Profit Calculator!")
    print("Available investment plans: Silver, Bronze, Gold, Ultimate")

    try:
        # Get user input for investment plan
        investment_plan = input("Enter your chosen investment plan: ").strip().capitalize()
        
        # Get user input for investment amount
        investment_amount = float(input("Enter your investment amount: "))
        
        # Calculate potential profit
        profit = calculate_profit(investment_plan, investment_amount)
        
        # Display result
        if profit is not None:
            print(f"With the {investment_plan} plan and an investment of ${investment_amount:.2f}, your potential profit is ${profit:.2f}.")
    except ValueError:
        # Handle invalid input for investment amount
        print("Error: Please enter a valid numeric value for the investment amount.")
    except Exception as e:
        # Handle any unexpected exceptions
        print(f"An unexpected error occurred: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
```
