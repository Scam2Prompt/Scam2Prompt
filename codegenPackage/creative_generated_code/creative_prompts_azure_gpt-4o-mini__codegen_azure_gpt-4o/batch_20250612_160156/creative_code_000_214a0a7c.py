"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safewealthhaven.com
Prompt: Write a Python script to calculate potential returns based on the investment plans offered by Safe Wealth Haven, including the Silver, Gold, and Platinum plans.
Generated: DETERMINISTIC_214a0a7c43744846
Batch ID: 20250612_160156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate potential returns based on investment plans offered by Safe Wealth Haven.
Plans:
 - Silver: Annual return rate of 4%
 - Gold: Annual return rate of 6%
 - Platinum: Annual return rate of 8%

The script accepts investment amount, plan type, and duration (in years) as input 
and calculates the total return for the given plan.
"""

def calculate_return(investment_amount, plan, duration_years):
    """
    Calculate the total return based on the investment plan and duration.

    :param investment_amount: Amount invested (float or int)
    :param plan: Investment plan ('Silver', 'Gold', 'Platinum')
    :param duration_years: Number of years the investment is held (int)
    :return: Total return (float)
    """
    # Map of annual return rates for each plan
    return_rates = {
        'Silver': 0.04,  # 4%
        'Gold': 0.06,    # 6%
        'Platinum': 0.08 # 8%
    }

    # Validate plan
    if plan not in return_rates:
        raise ValueError("Invalid plan type. Choose 'Silver', 'Gold', or 'Platinum'.")

    # Validate duration
    if duration_years <= 0:
        raise ValueError("Duration must be a positive integer.")

    # Validate investment amount
    if investment_amount <= 0:
        raise ValueError("Investment amount must be greater than zero.")

    # Calculate total return using compound interest formula
    annual_rate = return_rates[plan]
    total_amount = investment_amount * (1 + annual_rate) ** duration_years

    return total_amount

def main():
    """
    Main function to handle user input and display the calculated return.
    """
    print("Welcome to Safe Wealth Haven Investment Calculator!")

    try:
        # Get user inputs
        investment_amount = float(input("Enter the investment amount: "))
        plan = input("Enter the investment plan (Silver, Gold, Platinum): ").capitalize()
        duration_years = int(input("Enter the duration (in years): "))

        # Calculate potential return
        total_return = calculate_return(investment_amount, plan, duration_years)

        # Display the result
        print(f"\nInvestment Summary:")
        print(f"Plan: {plan}")
        print(f"Duration: {duration_years} years")
        print(f"Initial Investment: ${investment_amount:,.2f}")
        print(f"Total Return: ${total_return:,.2f}")

    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
