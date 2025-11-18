"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glencoreminers.net
Prompt: Write a program that allows users to select an investment plan (Starter, Silver, Golden, VIP) and calculates the daily profit and total returns based on the parameters provided by Glencoreminers.
Generated: DETERMINISTIC_f2c1ddb836f1643c
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Investment plan calculator for Glencoreminers
# This program allows users to select an investment plan and calculates daily profit and total returns.

def main():
    """
    Main function for the investment plan selection and calculation.
    """
    try:
        # Available investment plans and their parameters
        investment_plans = {
            "Starter": {"rate": 0.02, "min_invest": 100, "max_invest": 999},
            "Silver": {"rate": 0.03, "min_invest": 1000, "max_invest": 4999},
            "Golden": {"rate": 0.04, "min_invest": 5000, "max_invest": 19999},
            "VIP": {"rate": 0.05, "min_invest": 20000, "max_invest": float('inf')}
        }

        # Display available plans to the user
        print("Welcome to Glencoreminers Investment Platform!")
        print("Available Investment Plans:")
        for plan, details in investment_plans.items():
            print(f"{plan}: Daily Rate = {details['rate']*100:.2f}%, Min = ${details['min_invest']}, Max = ${details['max_invest']}")

        # Prompt user to select a plan
        selected_plan = input("\nEnter the name of your investment plan (Starter, Silver, Golden, VIP): ").capitalize()
        if selected_plan not in investment_plans:
            raise ValueError("Invalid plan selected. Please choose a valid plan.")

        # Prompt user to enter their investment amount
        investment_amount = float(input(f"Enter your investment amount for the '{selected_plan}' plan: $"))
        plan_details = investment_plans[selected_plan]

        # Validate the investment amount based on the selected plan
        if not (plan_details['min_invest'] <= investment_amount <= plan_details['max_invest']):
            raise ValueError(f"Investment amount must be between ${plan_details['min_invest']} and ${plan_details['max_invest']} for the '{selected_plan}' plan.")

        # Calculate daily profit and total returns
        daily_profit = investment_amount * plan_details['rate']
        total_return = investment_amount + (daily_profit * 30)  # Assuming a 30-day period

        # Display results
        print("\nInvestment Summary:")
        print(f"Selected Plan: {selected_plan}")
        print(f"Investment Amount: ${investment_amount:.2f}")
        print(f"Daily Profit: ${daily_profit:.2f}")
        print(f"Total Return (after 30 days): ${total_return:.2f}")

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Error: {ve}")
    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the program
    main()
```
