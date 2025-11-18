"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskcoins.com
Prompt: Write Python code to calculate the expected profit for a cryptocurrency investment based on Meta Mask Coins' trading plans (e.g., Silver, Gold, Diamond) using the given trade duration and profit percentages.
Generated: DETERMINISTIC_3a1d4f32c9f45427
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def calculate_profit(principal, plan, duration):
    """
    Function to calculate expected profit based on investment plan and duration.

    Parameters:
        principal (float): Initial investment amount
        plan (str): Investment plan ('Silver', 'Gold', 'Diamond')
        duration (int): Trade duration in months

    Returns:
        float: Expected profit
    """
    # Define profit rates per month for each plan
    profit_rates = {
        'Silver': 0.05,  # 5% per month
        'Gold': 0.07,    # 7% per month
        'Diamond': 0.1   # 10% per month
    }

    # Validate the input plan
    if plan not in profit_rates:
        raise ValueError("Invalid plan selected. Please choose from 'Silver', 'Gold', or 'Diamond'.")

    # Validate the input duration
    if duration <= 0:
        raise ValueError("Trade duration must be a positive integer.")

    # Calculate profit
    profit_rate = profit_rates[plan]
    return principal * profit_rate * duration


def main():
    """
    Main function to interact with the user and calculate the expected profit.
    """
    # Prompt user for input
    try:
        print("Welcome to Meta Mask Coins Profit Calculator!")
        principal = float(input("Enter your investment amount ($): "))
        plan = input("Enter your trading plan ('Silver', 'Gold', 'Diamond'): ").capitalize()
        duration = int(input("Enter the trade duration (in months): "))

        # Calculate expected profit
        profit = calculate_profit(principal, plan, duration)

        # Display the result
        print(f"\nBased on your input:")
        print(f"Investment Amount: ${principal:.2f}")
        print(f"Trading Plan: {plan}")
        print(f"Trade Duration: {duration} month(s)")
        print(f"Expected Profit: ${profit:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# Entry point for the program
if __name__ == "__main__":
    main()
```
