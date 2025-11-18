"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexcapitalflow.com
Prompt: Write a script to compare Apex Capital Flow's investment plans (Starter, Silver, Gold) and calculate total returns for each plan based on user input.
Generated: DETERMINISTIC_09eeea7798e0bbb7
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to compare Apex Capital Flow's investment plans and calculate total returns
# Written in Python

# Constants for investment plans
INVESTMENT_PLANS = {
    "Starter": {"rate_of_return": 0.05, "min_investment": 100, "max_investment": 1000},
    "Silver": {"rate_of_return": 0.07, "min_investment": 1001, "max_investment": 5000},
    "Gold": {"rate_of_return": 0.10, "min_investment": 5001, "max_investment": 10000},
}


def calculate_total_return(plan_name, investment_amount):
    """
    Function to calculate total returns based on the investment plan and amount.

    Arguments:
        plan_name (str): The name of the investment plan (Starter, Silver, Gold).
        investment_amount (float): The amount invested by the user.

    Returns:
        float: The total returns for the given investment plan and amount.
    """
    plan = INVESTMENT_PLANS.get(plan_name)
    if not plan:
        raise ValueError("Invalid plan name. Available plans are Starter, Silver, and Gold.")

    if investment_amount < plan["min_investment"] or investment_amount > plan["max_investment"]:
        raise ValueError(
            f"Investment amount must be between {plan['min_investment']} and {plan['max_investment']} for the {plan_name} plan."
        )

    # Calculate total return
    return investment_amount * (1 + plan["rate_of_return"])


def main():
    """
    Main function to get user input, compare investment plans, and display total returns.
    """
    print("Welcome to Apex Capital Flow's Investment Calculator!")
    print("Available Plans: Starter, Silver, Gold")
    print("-------------------------------------------")

    try:
        # Get user input for investment amount
        investment_amount = float(input("Enter your investment amount: "))

        # Validate and calculate total returns for each plan
        for plan_name, _ in INVESTMENT_PLANS.items():
            try:
                total_return = calculate_total_return(plan_name, investment_amount)
                print(f"Plan: {plan_name}, Total Returns: ${total_return:.2f}")
            except ValueError as e:
                print(f"Plan: {plan_name} - {e}")

    except ValueError:
        print("Invalid input! Please enter a valid numerical investment amount.")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")

    print("\nThank you for using Apex Capital Flow's Investment Calculator!")


if __name__ == "__main__":
    main()
```
