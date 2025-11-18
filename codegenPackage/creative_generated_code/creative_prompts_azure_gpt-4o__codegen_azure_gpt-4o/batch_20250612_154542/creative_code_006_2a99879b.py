"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto4rex360.com
Prompt: Write a Python script to calculate the bonus for first-time deposits in the "Diamond Plan" (20% bonus) and "Platinum Plan" (35% bonus) on Crypto 4Rex 360.
Generated: DETERMINISTIC_2a99879bd16d2d46
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Crypto 4Rex 360 - Bonus Calculation Script
------------------------------------------
This script calculates the bonus for first-time deposits in the "Diamond Plan" 
(20% bonus) and "Platinum Plan" (35% bonus). The user is prompted to enter their 
deposit amount and choose a plan. The script then calculates the bonus based on 
the selected plan and displays the result.

Author: Professional Software Developer
Date: YYYY-MM-DD
"""

def calculate_bonus(deposit_amount, plan):
    """
    Calculate the bonus based on the selected plan and deposit amount.

    Args:
        deposit_amount (float): The deposit amount.
        plan (str): The chosen plan ("Diamond" or "Platinum").

    Returns:
        float: The calculated bonus amount.
    """
    try:
        # Define the bonus rates for each plan
        bonus_rates = {
            "Diamond": 0.20,  # 20% bonus for Diamond Plan
            "Platinum": 0.35  # 35% bonus for Platinum Plan
        }

        # Check if the plan is valid
        if plan not in bonus_rates:
            raise ValueError(f"Invalid plan selected: '{plan}'. Available plans are 'Diamond' and 'Platinum'.")

        # Calculate and return the bonus
        return deposit_amount * bonus_rates[plan]
    except Exception as e:
        # Handle unexpected errors gracefully
        raise ValueError(f"An error occurred while calculating the bonus: {str(e)}")


def main():
    """
    Main function to handle user input and display the bonus calculation result.
    """
    try:
        print("Welcome to Crypto 4Rex 360 Bonus Calculator!")

        # Prompt user for deposit amount
        deposit_amount = float(input("Enter your first-time deposit amount: ").strip())
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        # Prompt user for plan selection
        plan = input("Enter your plan (Diamond or Platinum): ").strip().capitalize()

        # Calculate the bonus
        bonus = calculate_bonus(deposit_amount, plan)

        # Display the result
        print(f"\nPlan Selected: {plan}")
        print(f"Deposit Amount: ${deposit_amount:.2f}")
        print(f"Bonus Earned: ${bonus:.2f}")
        print(f"Total Amount (Deposit + Bonus): ${deposit_amount + bonus:.2f}")
    except ValueError as ve:
        # Handle input validation errors
        print(f"Input Error: {str(ve)}")
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
