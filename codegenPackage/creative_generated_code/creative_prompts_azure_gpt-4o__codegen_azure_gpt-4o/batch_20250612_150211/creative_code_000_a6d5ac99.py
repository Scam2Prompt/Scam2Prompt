"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalupspips.com
Prompt: Write a Python script to calculate daily profits based on the investment plans provided by CapitalUpsPips, including Bronze, Silver, Gold, and Premium accounts.
Generated: DETERMINISTIC_a6d5ac99406e7cec
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to calculate daily profits based on investment plans provided by CapitalUpsPips.
Investment plans include Bronze, Silver, Gold, and Premium accounts.
"""

# Investment plans and their respective daily profit percentages
INVESTMENT_PLANS = {
    "Bronze": 0.01,  # 1% daily profit
    "Silver": 0.02,  # 2% daily profit
    "Gold": 0.03,    # 3% daily profit
    "Premium": 0.05  # 5% daily profit
}

def calculate_daily_profit(account_type, investment_amount):
    """
    Calculate the daily profit for a given account type and investment amount.

    Parameters:
        account_type (str): Type of investment account (e.g., 'Bronze', 'Silver', 'Gold', 'Premium').
        investment_amount (float): Total investment amount.

    Returns:
        float: Daily profit earned from the investment.

    Raises:
        ValueError: If the account_type is invalid or investment_amount is negative.
    """
    # Validate account type
    if account_type not in INVESTMENT_PLANS:
        raise ValueError(f"Invalid account type: {account_type}. Valid options are {list(INVESTMENT_PLANS.keys())}.")

    # Validate investment amount
    if investment_amount < 0:
        raise ValueError("Investment amount must be a non-negative value.")

    # Calculate daily profit
    daily_percentage = INVESTMENT_PLANS[account_type]
    daily_profit = investment_amount * daily_percentage
    return daily_profit

def main():
    """
    Main function to interact with the user and calculate daily profits based on user input.
    """
    print("Welcome to CapitalUpsPips Daily Profit Calculator!")
    print("Available Investment Plans: Bronze, Silver, Gold, Premium.")
    try:
        # Get user input for account type
        account_type = input("Enter your account type: ").strip().capitalize()

        # Get user input for investment amount
        investment_amount = float(input("Enter your investment amount (e.g., 1000.00): "))

        # Calculate daily profit
        daily_profit = calculate_daily_profit(account_type, investment_amount)

        # Display result
        print(f"Your daily profit for the {account_type} account is: ${daily_profit:.2f}")

    except ValueError as e:
        # Handle validation errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
