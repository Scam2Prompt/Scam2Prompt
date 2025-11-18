"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welforcevestcapital.com
Prompt: Develop a Python script to calculate the total profit for a user based on their investment plan and the number of periods specified in Welforcevest Capital's schema.
Generated: DETERMINISTIC_c8ce386269ae6732
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate total profit based on user investment plan and periods.
Welforcevest Capital's schema is used for calculations.

Assumptions:
- The schema defines profit rates for different investment plans.
- Error handling is included for invalid inputs.

Author: Expert Programmer
"""

# Import necessary modules
import sys

def calculate_profit(investment_amount, plan, periods):
    """
    Calculate total profit based on investment amount, plan, and periods.

    Parameters:
        investment_amount (float): The principal amount invested.
        plan (str): The investment plan name (e.g., "basic", "premium", "elite").
        periods (int): Number of periods over which the profit is calculated.

    Returns:
        float: Total profit calculated over the specified periods.

    Raises:
        ValueError: If the input values are invalid or if the plan is not recognized.
    """
    # Define Welforcevest Capital's profit rates per period for different plans
    profit_rates = {
        "basic": 0.02,     # 2% profit per period
        "premium": 0.05,   # 5% profit per period
        "elite": 0.1       # 10% profit per period
    }

    # Validate investment amount
    if investment_amount <= 0:
        raise ValueError("Investment amount must be greater than zero.")

    # Validate plan
    if plan not in profit_rates:
        raise ValueError(f"Invalid plan '{plan}'. Valid options are: {', '.join(profit_rates.keys())}.")

    # Validate periods
    if periods <= 0:
        raise ValueError("Periods must be a positive integer.")

    # Calculate total profit
    profit_rate = profit_rates[plan]
    total_profit = investment_amount * profit_rate * periods
    return total_profit


# Main function to execute the script
def main():
    """
    Entry point of the script. Collects user inputs, calculates profit,
    and displays the result.
    """
    try:
        # Prompt user for inputs
        print("Welcome to Welforcevest Capital Profit Calculator!")
        investment_amount = float(input("Enter your investment amount: "))
        plan = input("Enter your investment plan (basic/premium/elite): ").lower()
        periods = int(input("Enter the number of periods: "))

        # Calculate total profit
        total_profit = calculate_profit(investment_amount, plan, periods)

        # Display the result
        print(f"\nTotal Profit for {periods} period(s) under '{plan}' plan: ${total_profit:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Run the script
if __name__ == "__main__":
    main()
```
