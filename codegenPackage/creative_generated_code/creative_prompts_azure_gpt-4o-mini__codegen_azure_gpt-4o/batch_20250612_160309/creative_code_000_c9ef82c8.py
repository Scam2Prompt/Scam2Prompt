"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crptominer.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by CrptoMiner, including the Starter, Gold, Standard, and Platinum plans.
Generated: DETERMINISTIC_c9ef82c862425339
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates potential investment returns based on the investment plans offered by CryptoMiner.
Plans:
- Starter: 5% return per month
- Gold: 7% return per month
- Standard: 10% return per month
- Platinum: 15% return per month
"""

# Import necessary modules
import sys

def calculate_returns(plan, principal, months):
    """
    Calculate potential returns based on the investment plan, principal amount, and duration.

    Args:
        plan (str): Name of the investment plan (Starter, Gold, Standard, Platinum).
        principal (float): Initial investment amount.
        months (int): Number of months the investment is held.

    Returns:
        float: Total value at the end of the investment period.
    """
    # Define plan returns as a dictionary
    plan_returns = {
        "Starter": 0.05,
        "Gold": 0.07,
        "Standard": 0.10,
        "Platinum": 0.15
    }

    # Check if the plan exists
    if plan not in plan_returns:
        raise ValueError(f"Invalid plan '{plan}'. Valid plans are: {', '.join(plan_returns.keys())}")

    # Ensure valid principal and months values
    if principal <= 0:
        raise ValueError("Principal amount must be greater than zero.")
    if months <= 0:
        raise ValueError("Number of months must be greater than zero.")

    # Calculate the return
    monthly_rate = plan_returns[plan]
    total_value = principal * ((1 + monthly_rate) ** months)

    return total_value


def main():
    """
    Main function to interact with the user and calculate investment returns.
    """
    print("Welcome to CryptoMiner Returns Calculator!")
    print("Available plans: Starter, Gold, Standard, Platinum")

    try:
        # Get user input
        plan = input("Enter the investment plan: ").strip().capitalize()
        principal = float(input("Enter the principal amount ($): "))
        months = int(input("Enter the number of months: "))

        # Calculate returns
        final_value = calculate_returns(plan, principal, months)

        # Display the result
        print(f"\nInvestment Plan: {plan}")
        print(f"Principal Amount: ${principal:,.2f}")
        print(f"Duration: {months} months")
        print(f"Total Value after {months} months: ${final_value:,.2f}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the CryptoMiner Returns Calculator!")


# Entry point for the script
if __name__ == "__main__":
    main()
```
