"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zenixglobaltrade.com
Prompt: Write Python code to simulate a cryptocurrency trading bot that uses the investment plans offered by ZenixGlobaltrade, such as the Starter Plan, Classic Plan, Professional Plan, and Premium Plan, to calculate potential ROI based on user input.
Generated: DETERMINISTIC_147fe0bc0af6c8de
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_roi(plan, investment_amount):
    """
    Calculate potential ROI based on chosen investment plan and amount.

    Args:
        plan (str): The investment plan chosen by the user (Starter, Classic, Professional, Premium).
        investment_amount (float): The amount of money invested.

    Returns:
        float: The calculated ROI.
    """
    # Define the ROI percentages for each plan
    roi_percentages = {
        "Starter": 0.05,    # 5% return
        "Classic": 0.10,    # 10% return
        "Professional": 0.15,  # 15% return
        "Premium": 0.20     # 20% return
    }

    if plan not in roi_percentages:
        raise ValueError(f"Invalid plan '{plan}'. Please choose one of the following: Starter, Classic, Professional, Premium.")

    # Calculate the ROI
    return investment_amount * roi_percentages[plan]


def main():
    """
    Main function to interact with the user and simulate the trading bot.
    """
    print("Welcome to the ZenixGlobaltrade Cryptocurrency Trading Bot")
    print("Investment Plans:")
    print("1. Starter Plan - 5% ROI")
    print("2. Classic Plan - 10% ROI")
    print("3. Professional Plan - 15% ROI")
    print("4. Premium Plan - 20% ROI")

    try:
        # Get user input for plan selection
        plan = input("Enter the name of your chosen plan (Starter, Classic, Professional, Premium): ").strip()

        # Get user input for investment amount
        investment_amount = float(input("Enter the amount you want to invest (in USD): "))

        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than 0.")

        # Calculate ROI
        potential_roi = calculate_roi(plan, investment_amount)

        # Display the results
        print(f"\nYou have chosen the {plan} Plan.")
        print(f"Investment Amount: ${investment_amount:.2f}")
        print(f"Potential ROI: ${potential_roi:.2f}")
        print("Thank you for using the ZenixGlobaltrade Cryptocurrency Trading Bot!")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Goodbye!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        sys.exit(0)
```
