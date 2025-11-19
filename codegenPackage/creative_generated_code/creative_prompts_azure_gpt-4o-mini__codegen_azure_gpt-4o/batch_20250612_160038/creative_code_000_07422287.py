"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smarts-invests.net
Prompt: Generate a Python script to calculate potential profits based on the investment plans offered by Smarts-invests, including the STARTUP and ADVANCED plans.
Generated: DETERMINISTIC_0742228705e48bc9
Batch ID: 20250612_160038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates potential profits based on investment plans offered by Smarts-invests.
It supports two investment plans: STARTUP and ADVANCED, each with distinct parameters.
"""

# Import necessary modules
import sys

def calculate_profit(investment_amount, plan):
    """
    Calculates the potential profit based on the given investment plan and amount.
    
    Parameters:
        investment_amount (float): The amount of money invested.
        plan (str): The investment plan ("STARTUP" or "ADVANCED").
    
    Returns:
        float: The potential profit.
    
    Raises:
        ValueError: If the plan is invalid or the investment amount is negative.
    """
    # Validate investment amount
    if investment_amount < 0:
        raise ValueError("Investment amount must be non-negative.")
    
    # Define plan parameters
    plans = {
        "STARTUP": {"rate": 0.05, "duration": 12},   # 5% monthly return, 12 months
        "ADVANCED": {"rate": 0.10, "duration": 24}   # 10% monthly return, 24 months
    }
    
    # Check if plan exists
    if plan not in plans:
        raise ValueError(f"Invalid plan '{plan}'. Available plans: {', '.join(plans.keys())}")
    
    # Extract plan details
    rate = plans[plan]["rate"]
    duration = plans[plan]["duration"]
    
    # Calculate profit
    total_profit = investment_amount * rate * duration
    return total_profit


def main():
    """
    Main function to interact with the user and calculate profits.
    """
    try:
        # Prompt user for input
        print("Welcome to Smarts-invests profit calculator!")
        investment_amount = float(input("Enter the investment amount ($): "))
        plan = input("Enter the investment plan (STARTUP/ADVANCED): ").strip().upper()
        
        # Calculate profit
        profit = calculate_profit(investment_amount, plan)
        print(f"Based on the {plan} plan, your total profit after the investment period will be: ${profit:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Entry point of the script
if __name__ == "__main__":
    main()
```
