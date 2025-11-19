"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prospectlimited.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by Prospect Limited, including the Starter, Standard, Premium, Gold, and Executive plans.
Generated: DETERMINISTIC_a85d2c6b87f03357
Batch ID: 20250612_160328
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Investment Returns Calculator for Prospect Limited

This script calculates potential returns based on the investment plans offered by Prospect Limited.
Plans: Starter, Standard, Premium, Gold, and Executive.

Each plan has its own return rate and minimum investment requirement:
- Starter: 5% return, minimum $100 investment
- Standard: 7% return, minimum $500 investment
- Premium: 10% return, minimum $1000 investment
- Gold: 12% return, minimum $5000 investment
- Executive: 15% return, minimum $10000 investment

The user inputs the plan name and investment amount, and the script calculates and displays the potential return.
"""

def calculate_returns(plan: str, investment_amount: float) -> float:
    """
    Calculates the potential return based on the investment plan and amount.

    Parameters:
        plan (str): The name of the investment plan.
        investment_amount (float): The amount of money invested.

    Returns:
        float: The calculated potential return.

    Raises:
        ValueError: If the plan name is invalid or the investment amount is below the plan's minimum.
    """
    # Define the investment plans with their attributes
    investment_plans = {
        "Starter": {"rate": 0.05, "min_amount": 100},
        "Standard": {"rate": 0.07, "min_amount": 500},
        "Premium": {"rate": 0.10, "min_amount": 1000},
        "Gold": {"rate": 0.12, "min_amount": 5000},
        "Executive": {"rate": 0.15, "min_amount": 10000}
    }
    
    # Normalize the plan name to ensure case-insensitivity
    plan = plan.capitalize()

    # Check if the plan exists
    if plan not in investment_plans:
        raise ValueError(f"Invalid plan name: {plan}. Please choose from {', '.join(investment_plans.keys())}.")
    
    # Extract plan details
    plan_details = investment_plans[plan]
    rate = plan_details["rate"]
    min_amount = plan_details["min_amount"]

    # Check if the investment amount meets the minimum requirement
    if investment_amount < min_amount:
        raise ValueError(f"Investment amount must be at least ${min_amount} for the {plan} plan.")
    
    # Calculate and return the potential return
    return investment_amount * rate


def main():
    """
    Main function to interact with the user and calculate returns.
    """
    print("Welcome to Prospect Limited Investment Returns Calculator!")
    print("Available plans: Starter, Standard, Premium, Gold, Executive")

    try:
        # Get user input for the plan name
        plan_name = input("\nEnter the name of the investment plan: ").strip()

        # Get user input for the investment amount
        investment_amount = float(input("Enter the investment amount (in USD): ").strip())

        # Calculate returns
        potential_return = calculate_returns(plan_name, investment_amount)

        # Display the result
        print(f"\nThe potential return for the {plan_name.capitalize()} plan is: ${potential_return:.2f}")
    
    except ValueError as ve:
        # Handle invalid input and display an error message
        print(f"\nError: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
