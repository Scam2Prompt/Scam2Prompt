"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realcraftcryptoinvestment.one
Prompt: Create a script to calculate referral bonuses (10%) for different investment plans, such as the Gold and Platinum Plans mentioned on Realcraft Crypto Investment.
Generated: DETERMINISTIC_bf357f6c1b8de7e7
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_bonus_calculator.py
# This script calculates referral bonuses (10%) for different investment plans.

# Import necessary modules
import sys

# Define a custom exception for invalid plan types
class InvalidPlanError(Exception):
    pass

# Referral bonus calculator function
def calculate_referral_bonus(plan: str, investment_amount: float) -> float:
    """
    Calculate referral bonus based on the investment plan and investment amount.

    Parameters:
        plan (str): The investment plan type (e.g., "Gold", "Platinum").
        investment_amount (float): The amount invested.

    Returns:
        float: The referral bonus amount.
    """
    # Validate the investment amount
    if investment_amount <= 0:
        raise ValueError("Investment amount must be greater than zero.")

    # Define valid plans and bonus percentages
    plans = {
        "Gold": 0.10,      # 10% referral bonus
        "Platinum": 0.10,  # 10% referral bonus
    }

    # Check if the plan is valid
    if plan not in plans:
        raise InvalidPlanError(f"Invalid plan: {plan}. Valid plans are {', '.join(plans.keys())}.")

    # Calculate the referral bonus
    referral_bonus = investment_amount * plans[plan]
    return referral_bonus

# Main function to interact with the user
def main():
    """
    Main function to collect user input and calculate referral bonuses.
    """
    try:
        # Collect investment plan from the user
        plan = input("Enter the investment plan (e.g., 'Gold', 'Platinum'): ").strip()

        # Collect investment amount from the user
        investment_amount = float(input("Enter the investment amount: ").strip())

        # Calculate the referral bonus
        referral_bonus = calculate_referral_bonus(plan, investment_amount)

        # Display the referral bonus
        print(f"The referral bonus for the {plan} Plan is: ${referral_bonus:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except InvalidPlanError as ipe:
        print(f"Error: {ipe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Referral Bonus Calculator!")

# Entry point of the script
if __name__ == "__main__":
    main()
```
